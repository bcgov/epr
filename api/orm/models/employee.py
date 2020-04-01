from sqlalchemy import Column, String, Integer
from sqlalchemy import Sequence
from db_init import BASE


class Employee(BASE):
    __tablename__ = 'EMPLOYEE'

    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True, nullable=False)
    idir = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    def __init__(self, idir, status, location, phone):
        self.idir = idir
        self.status = status
        self.location = location
        self.phone = phone
