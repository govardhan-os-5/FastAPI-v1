import os

import jwt
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

import crud
import models
import schemas
from app.database import engine, SessionLocal

load_dotenv("../env.env")


app = FastAPI()
metadata = MetaData()
security = HTTPBearer()
models.Base.metadata.create_all(bind=engine)
secret_key = os.environ.get("JWT_SECRET_KEY")
algorithm = os.environ.get("JWT_ALGORITHM")


def generate_token(email: str) -> str:
    payload = {"email": email}
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/employee/{email}", tags=["Employee Details"], response_model=schemas.CreateEmployee)
def employee(email: str = Path(..., description="email of the employee"), db: Session = Depends(get_db),
             token: str = Depends(security)):
    try:
        payload = jwt.decode(token.credentials, secret_key, algorithms=[algorithm])
        if payload["email"] != email:
            raise HTTPException(status_code=403, detail="You are not authorized to access this employee data.")
        db_user = crud.employee(db, email=email)
        if db_user:
            print(f"Fetched employee with email {db_user.email} details.")
            return db_user
        else:
            print(f"Employee with email {email} doesn't exists.")
            raise HTTPException(status_code=404, detail=f"Employee with email {email} doesn't exists.")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/employees", tags=["Employee Details"])
def employees(db: Session = Depends(get_db)):
    db_user = crud.employees(db)
    if db_user:
        print(f"Fetched all employees.")
        return db_user


@app.post("/create_employee", tags=["Employee Details"], response_model=schemas.CreateEmployee)
def create_employee(user: schemas.CreateEmployee, db: Session = Depends(get_db)):
    db_user = crud.check_employee(db, email=user.email, id=user.id)
    if db_user:
        if db_user.email == user.email or db_user.id == user.id:
            print(f"Employee with ID or Email already exists.")
            raise HTTPException(status_code=409, detail=f"Employee with ID or Email already exists.")

    print(f"Created employee with {user.email} email.")
    return crud.create_employee(db=db, user=user)


@app.put("/update_employee/{email}", tags=["Employee Details"], response_model=schemas.CreateEmployee)
def update_employee(email: str, updated_employee: schemas.CreateEmployee, db: Session = Depends(get_db)):
    db_user = crud.employee(db, email=email)
    updated_employee_data = updated_employee.dict()
    if db_user:
        for i, j in updated_employee_data.items():
            setattr(db_user, i, j)
        db.commit()
        db.refresh(db_user)
        print(f"Updated {db_user.email} details.")
        return db_user
    else:
        print(f"Employee with email {email} doesn't exists.")


@app.delete("/delete_employee/{email}", tags=["Employee Details"], response_model=schemas.CreateEmployee)
def delete_employee(email: str, db: Session = Depends(get_db)):
    employee_to_delete = crud.employee(db, email=email)
    if employee_to_delete:
        db_user = crud.delete_employee(db, email=email)
        db.commit()
        db.refresh(db_user)
        print(f"Employee with email {email} deleted successfully.")
        raise HTTPException(status_code=200, detail=f"Profile with email {db_user.email} is deleted.")
    else:
        print(f"Profile with email {email} doesn't exist.")
        raise HTTPException(status_code=404, detail=f"Profile with email {email} doesn't exists.")


def get_role(email):
    with SessionLocal as db:
        query = text("SELECT role FROM employee_details WHERE email = :email")
        result = db.execute(query, {"email": email})
        role = result.scalar()
        print(role)
    if role is not None:
        return role
    else:
        raise HTTPException(status_code=404, detail="Role not found")


@app.post("/authentication", tags=["HR Details"], response_model=schemas.CreateHR)
def authenticating_hr(hr: schemas.CreateHR, db: Session = Depends(get_db)):
    db_hr = crud.check_hr(db, user=hr)
    if not db_hr or db_hr.email != hr.email or db_hr.password != hr.password:
        print("Invalid credentials")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    elif db_hr and db_hr.email == hr.email and db_hr.password == hr.password:
        role = get_role(hr.email)
        token = generate_token(hr.email)
        print(f"HR with {hr.email} email credentials are matched.")
        result = {"role": role, "jwt_token": token}
        raise HTTPException(status_code=200, detail=result)


# creating a new hr account
# @app.post("/create_hr", tags=["HR Details"], response_model=schemas.CreateHR)
# def create_new_hr(user: schemas.CreateHR, db: Session = Depends(get_db)):
#     db_user = crud.get_hr_by_email(db, email=email.id)
#     if db_user:
#         print(f"HR with email {db_user.email} is already registered.")
#         raise HTTPException(status_code=409, detail=f"HR with email {db_user.email} is already registered.")
#     print(f"Created HR with {user.id} id.")
#     return crud.create_hr(db=db, user=user)

# get hr details by email
# @app.get("/hr_details", tags=["HR Details"], response_model=schemas.CreateHR)
# def get_hr_by_email(id: str, db: Session = Depends(get_db)):
#     db_user = crud.get_hr_by_email(db, id=id)
#     if db_user:
#         print(f"Fetched HR with email {db_user.email}.")
#         return db_user
#     else:
#         print(f"HR with email {email} doesn't exists.")
#         raise HTTPException(status_code=404, detail=f"HR with email {email} doesn't exists.")


# leaves CRUD operations
# @app.get("/get_leaves", response_model=schemas.LeavesCreate)
# def get_profile(username: str, db: Session = Depends(get_db)):
#     db_user = crud.get_leaves_by_username(db, employee_id=employee_id)
#     print(f"Fetched {employee_id} details.")
#     if db_user:
#         return db_user
#     else:
#         raise HTTPException(status_code=404, detail="User profile not found")
#
#
# @app.post("/post_leaves", response_model=schemas.LeavesCreate)
# def create_profile(user: schemas.LeavesCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_profile_by_username(db, employee_id=user.employee_id)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered.")
#     print(f"Applied Leave.")
#     return crud.create_leave_by_username(db=db, employee_id=employee_id)
#
#
# @app.put("/update_profile", response_model=schemas.ProfileCreate)
# def update_profile(username: str, updated_profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_profile_by_username(db, username=username)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="Profile not found.")
#     updated_profile_data = updated_profile.dict()
#     for i, j in updated_profile_data.items():
#         setattr(db_user, i, j)
#     db.commit()
#     db.refresh(db_user)
#     print(f"Updated {db_user.username} details.")
#     return db_user
#
#
# @app.delete("/delete_profile", response_model=schemas.ProfileCreate)
# def delete_profile(username: str, db: Session = Depends(get_db)):
#     db_user = crud.delete_profile(db, username=username)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="Profile not found")
#     db.delete(db_user)
#     db.commit()
#     db.refresh(db_user)
#     print(f"Profile deleted successfully.")
#     return db_user


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
