
from sqlalchemy.orm import Session

import models
import schemas


# profile
def get_profile_details(db: Session):
    return db.query(models.EmployeeProfile).all()


def get_profile_by_username(db: Session, username: str):
    return db.query(models.EmployeeProfile).filter(models.EmployeeProfile.username == username).first()


def create_profile(db: Session, user: schemas.ProfileCreate):
    # db_user = db.query(models.EmployeeProfile).filter(models.EmployeeProfile.username == user.username).first()
    db_user = models.EmployeeProfile(id=user.id, employee_name=user.employee_name, employee_dob=user.employee_dob, employee_address=user.employee_address, employee_qualifications=user.employee_qualifications, employee_joining_date=user.employee_joining_date, employee_designation=user.employee_designation, employee_salery=user.employee_salery, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_profile(db: Session, user: schemas.ProfileCreate, username: str):
    profile_info = get_profile_by_username(db, username)

    profile_info.id = user.id
    profile_info.employee_name = user.employee_name
    profile_info.employee_dob = user.employee_dob
    profile_info.employee_address = user.employee_address
    profile_info.employee_qualifications = user.employee_qualifications
    profile_info.employee_designation = user.employee_designation
    profile_info.employee_joining_date = user.employee_joining_date
    profile_info.employee_salery = user.employee_salery
    profile_info.username = user.username
    # profile_info.password = user.password

    db.commit()
    db.refresh(profile_info)
    return profile_info


def delete_profile(db: Session, username: str):
    profile_info = get_profile_by_username(db, username)
    db.delete(profile_info)
    db.commit()
    return f"Profile {username} is deleted."

#
# # leaves
# def get_leaves_by_username(db: Session, employee_id: int):
#     return db.query(models.EmployeeLeaves).filter(models.EmployeeLeaves.employee_id == employee_id).first()
#
#
# def create_leave_by_username(db: Session, user: schemas.LeavesCreate):
#     db_user = models.EmployeeLeaves(employee_id=user.employee_id, allocated_leaves=user.allocated_leaves, utilized_leaves=user.utilized_leaves, left_leaves=user.left_leaves)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
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

