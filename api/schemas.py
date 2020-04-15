'''
Pydantic models representing available resources. pydantic guarantees the types and constraints
of the output model
Note:
1. Behaviour of pydantic can be controlled via the Config class on a model
2. orm_mode = True maps to ORM model
'''
from typing import List
from pydantic import BaseModel
# pylint: disable=too-few-public-methods


class Health(BaseModel):
    """ A very basic health response. """
    ok: bool


class EmployeeRequest(BaseModel):
    """ Employee request model """
    idir: str = None
    status: str = None
    location: str = None
    phone: str = None


class Employee(EmployeeRequest):
    """ Employee model """
    id: int = None

    class Config:
        """ Configutaion """
        orm_mode = True


class EmployeeList(BaseModel):
    """ Employee list model """
    employee_list: List[Employee] = None
