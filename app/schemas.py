from pydantic import BaseModel, Field
from datetime import date


# profile
class CreateEmployee(BaseModel):
    id: str
    first_name: str
    last_name: str
    gender: str
    mobile_number: str
    email: str
    date_of_birth: date
    joining_date: date
    qualifications: str
    designation: str
    department: str
    blood_group: str
    address: str
    role: str
    password: str

    class Config:
        orm_mode = True


class CreateHR(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True


# # leaves
# class LeaveManagement(BaseModel):
#     employee_id: str
#     total: int
#     utilized: int
#     balance: int
#
#     class Config:
#         orm_mode = True
#
