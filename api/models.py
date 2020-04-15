""" Class models that reflect resources and map to database tables
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy import Sequence
from database import BASE


class Employee(BASE):  # pylint: disable=too-few-public-methods
    """ Employee table blueprint """
    __tablename__ = 'EMPLOYEE'

    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True, nullable=False, index=True)
    idir = Column(String, unique=True, nullable=False, index=True)
    status = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    def __init__(self, idir, status, location, phone):
        self.idir = idir
        self.status = status
        self.location = location
        self.phone = phone
