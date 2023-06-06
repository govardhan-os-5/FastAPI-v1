import models
import schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException
import bcrypt
from datetime import datetime


def employees(db: Session):
    # sorting_employees = db.query(Employee).order_by(desc(Employee.id)).all()
    return db.query(models.EmployeeDetails).all()


def employee(db: Session, email: str):
    resp = db.query(models.EmployeeDetails).filter(models.EmployeeDetails.email == email).first()
    if resp:
        return resp


def check_employee(db: Session, email: str, id: str):
    check_email = db.query(models.EmployeeDetails).filter(models.EmployeeDetails.email == email).first()
    check_id = db.query(models.EmployeeDetails).filter(models.EmployeeDetails.id == id).first()
    if check_email or check_id:
        return check_email or check_id
        # raise HTTPException(status_code=409, detail=f"Employee exists already.")
    else:
        return None
        # employee(db, email)


def create_employee(db: Session, user: schemas.CreateEmployee):
    existing_profile = employee(db, email=user.email)

    # formatting dates
    date_str = "01/01/2023"
    dob_obj = datetime.strptime(date_str, "%d/%m/%Y")
    doj_obj = datetime.strptime(date_str, "%d/%m/%Y")
    formatted_dob = dob_obj.strftime("%Y/%m/%d")
    formatted_doj = doj_obj.strftime("%Y/%m/%d")

    if existing_profile:
        raise HTTPException(status_code=409, detail=f"Employee with {user.email} email exists already.")
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    # print(hashed_password)
    db_user = models.EmployeeDetails(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender,
        mobile_number=user.mobile_number,
        email=user.email,
        date_of_birth=formatted_dob,
        joining_date=formatted_doj,
        qualifications=user.qualifications,
        designation=user.designation,
        department=user.department,
        blood_group=user.blood_group,
        address=user.address,
        role=user.role,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# converting hashed password to original
# import bcrypt
#
# # Retrieve the stored hashed password from the database
# # ... (code to retrieve the hashed password from the database)
#
# # Verify the password hash
# if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
#     # Passwords match, login successful
# else:
#     # Passwords do not match, login failed


def update_employee(db: Session, user: schemas.CreateEmployee, email: str):
    db_user = employee(db, email)
    if db_user:
        db_user.id = user.id
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.gender = user.gender
        db_user.mobile_number = user.mobile_number
        db_user.email = user.email
        db_user.date_of_birth = user.date_of_birth
        db_user.joining_date = user.joining_date
        db_user.qualifications = user.qualifications
        db_user.designation = user.designation
        db_user.department = user.department
        db_user.blood_group = user.blood_group
        db_user.address = user.address
        db_user.role = user.role
        db_user.password = user.password

        db.commit()
        db.refresh(db_user)
        return db_user
    raise HTTPException(status_code=404, detail=f"Employee with email {email} doesn't exists.")


def delete_employee(db: Session, email: str):
    db_user = employee(db, email)
    if db_user:
        db.delete(db_user)
        db.commit()
        raise HTTPException(status_code=200, detail=f"Employee {db_user.email} is deleted.")
    raise HTTPException(status_code=404, detail=f"Employee with email {email} doesn't exists.")


def get_hr_details(db: Session, email: str, password: str):
    cond_1 = models.HrDetails.email == email
    cond_2 = models.HrDetails.password == password
    resp = db.query(models.HrDetails).filter(cond_1 and cond_2).first()
    return resp


def check_hr(db: Session, user: schemas.CreateHR):
    existing_profile = get_hr_details(db, email=user.email, password=user.password)
    return existing_profile


def get_hr_by_email(db: Session, email: str):
    resp = db.query(models.HrDetails).filter(models.HrDetails.email == email).first()
    if resp:
        return resp

#
# # leaves
# def get_leaves_by_id(db: Session, employee_id: int):
#     return db.query(models.Leaves).filter(models.Leaves.employee_id == employee_id).first()
#
#
# def create_leave_by_id(db: Session, user: schemas.LeavesCreate): db_user = models.EmployeeLeaves(
# employee_id=user.employee_id, allocated_leaves=user.allocated_leaves, utilized_leaves=user.utilized_leaves,
# left_leaves=user.left_leaves) db.add(db_user) db.commit() db.refresh(db_user) return db_user


# def update_leave_info(db: Session, user: schemas.LeavesCreate, employee_id: int):
#     profile_info = get_leaves_by_username(db, employee_id)
#
#     profile_info.id = user.employee_id
#     profile_info.employee_name = user.start_date
#     profile_info.employee_dob = user.end_date
#     profile_info.employee_qualifications = user.number_of_days
#
#     db.commit()
#     db.refresh(profile_info)
#     # print(f"Profile {username} is updated.")
#     return profile_info

#
# def delete_leaves(db: Session, username: str):
#     profile_info = get_profile_by_username(db, username)
#     db.delete(profile_info)
#     db.commit()
#     return f"Profile {username} is deleted."
