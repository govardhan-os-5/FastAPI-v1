import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from typing import Annotated
import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/get_all_profiles")
def get_all_profiles(db: Session = Depends(get_db)):
    db_user = crud.get_profile_details(db)
    if db_user:
        print(f"Fetched all profile details.")
        return db_user
    else:
        err_msg = "There are no details in the database."
        return err_msg


@app.get("/get_profile_by_username", response_model=schemas.ProfileCreate)
def get_profile(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_profile_by_username(db, username=username)
    if db_user:
        print(f"Fetched {db_user.username} details.")
        return db_user
    elif not db_user:
        err_msg = f"User {db_user.username} not found"
        return err_msg


@app.post("/create_new_profile", response_model=schemas.ProfileCreate)
def create_new_profile(user: schemas.ProfileCreate, db: Session = Depends(get_db)):
    db_user = crud.get_profile_by_username(db, username=user.username)
    if db_user:
        err_msg = "Username is already registered."
        return err_msg
    else:
        print(f"Created profile with {db_user.username} username.")
        return crud.create_profile(db=db, user=user)


@app.put("/update_profile_by_username", response_model=schemas.ProfileCreate)
def update_profile_by_username(username: str, updated_profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    db_user = crud.get_profile_by_username(db, username=username)
    if not db_user:
        err_msg = "Profile not found."
        return err_msg
    else:
        updated_profile_data = updated_profile.dict()
        for i, j in updated_profile_data.items():
            setattr(db_user, i, j)
        db.commit()
        db.refresh(db_user)
        print(f"Updated {db_user.username} details.")
        return db_user


@app.delete("/delete_profile_by_username", response_model=schemas.ProfileCreate)
def delete_profile(username: str, db: Session = Depends(get_db)):
    db_user = crud.delete_profile(db, username=username)
    if db_user:
        db.delete(db_user)
        db.commit()
        db.refresh(db_user)
        resp = "Profile deleted successfully."
        return resp
    else:
        return f"Profile doesn't exist."


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
    uvicorn.run(app, host="127.0.0.1", port=8000)
