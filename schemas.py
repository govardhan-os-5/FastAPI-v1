from pydantic import BaseModel
from datetime import date


# profile
class ProfileCreate(BaseModel):
    id: int
    employee_name: str
    employee_dob: date
    employee_address: str
    employee_qualifications: str
    employee_designation: str
    employee_joining_date: date
    employee_salery: int
    username: str
    # password: str

    class Config:
        orm_mode = True


# leaves
# class LeavesCreate(BaseModel):
#     employee_id: str
#     allocated_leaves: int
#     utilized_leaves: int
#     left_leaves: int
#
#     class Config:
#         orm_mode = True
#
