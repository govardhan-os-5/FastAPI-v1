from sqlalchemy import Column, String, Date
from app.database import Base


class EmployeeDetails(Base):
    __tablename__ = "employee_details"

    id = Column(String, primary_key=True, unique=True, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    mobile_number = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    joining_date = Column(Date, nullable=True)
    qualifications = Column(String, nullable=True)
    designation = Column(String, nullable=True)
    department = Column(String, nullable=True)
    blood_group = Column(String, nullable=True)
    address = Column(String, nullable=True)
    role = Column(String, nullable=True)
    password = Column(String, nullable=True)

    __table_args__ = {"extend_existing": True}


# class EmployeeLeaves(Base):
#     __tablename__ = "employee_leaves"
#
#     employee_id = Column(String, primary_key=True, unique=True)
#     allocated_leaves = Column(Date)
#     utilized_leaves = Column(Date)
#     left_leaves = Column(Integer)


class HrDetails(Base):
    __tablename__ = "authentication_table"

    email = Column(String, primary_key=True, unique=True, nullable=True)
    password = Column(String, unique=True, nullable=True)

    __table_args__ = {"extend_existing": True}


class Leaves(Base):
    __tablename__ = "leave_management"

    employee_id = Column(String, primary_key=True, unique=True, nullable=True)
    total = Column(String, nullable=True)
    utilized = Column(String, nullable=True)
    balance = Column(String, nullable=True)

    __table_args__ = {"extend_existing": True}
