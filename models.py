from sqlalchemy import Column, Integer, String, Date
from database import Base


class EmployeeProfile(Base):
    __tablename__ = "employee_profile"

    id = Column(Integer, primary_key=True, unique=True)
    employee_name = Column(String)
    employee_dob = Column(Date)
    employee_address = Column(String)
    employee_qualifications = Column(String)
    employee_joining_date = Column(Date)
    employee_designation = Column(String)
    employee_salery = Column(Integer)
    username = Column(String, unique=True)

#
# class EmployeeLeaves(Base):
#     __tablename__ = "employee_leaves"
#
#     employee_id = Column(String, primary_key=True, unique=True)
#     allocated_leaves = Column(Date)
#     utilized_leaves = Column(Date)
#     left_leaves = Column(Integer)
#
#
# class Authentication(Base):
#     __tablename__ = "authentication_table"
#
#     employee_id = Column(String, primary_key=True, unique=True)
#     username = Column(String)
#     password = Column(String)
