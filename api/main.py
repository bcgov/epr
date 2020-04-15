""" This module contains the entrypoint for the Emergency Personnel Reporting API.

See README.md for details on how to run.
"""
from os import getenv
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from schemas import Employee, EmployeeRequest, EmployeeList, Health
import crud
from database import SESSION

API_INFO = '''
    Description: API for Emergency Personnel Reporting '''


APP = FastAPI(
    title="Emergency Personnel Reporting",
    description="API for Emergency Personnel Reporting",
    version="0.0.0"
)

ORIGINS = getenv('ORIGINS')

APP.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Dependency
def get_db_session():
    """ Get database session to perform transactions """
    try:
        db_session = SESSION()
        return db_session
    finally:
        db_session.close()


@APP.get('/health')
async def health(db_session: SESSION = Depends(get_db_session)):
    """ Return 200 if site is up and healthy. At this point, we assume that being able to
    talk to the database means we're good to go. """
    db_session.execute('SELECT 1')
    return Health(ok=db_session is not None)


@APP.get("/employees/{emp_idir}", response_model=Employee)
def fetch_employee(emp_idir: str, db_session: SESSION = Depends(get_db_session)):
    """ Get employee by employee idir """
    found_employee = crud.get_employee(
        db_session=db_session, employee_idir=emp_idir)
    if found_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return found_employee


@APP.get("/employees/", response_model=EmployeeList)
def fetch_employees(db_session: SESSION = Depends(get_db_session)):
    """ Get all employees """
    all_emps = crud.get_employees(db_session=db_session)
    response = EmployeeList(employee_list=all_emps)
    return response


@APP.post("/employee/", response_model=Employee)
def add_employee(emp: EmployeeRequest, db_session: SESSION = Depends(get_db_session)):
    """ Create a new employee """
    found_employee = crud.get_employee_by_idir(
        db_session=db_session, employee_idir=emp.idir)
    if found_employee is not None:
        raise HTTPException(status_code=400, detail="Employee already added")
    return crud.create_employee(db_session=db_session, employee=emp)


@APP.put("/employee/", response_model=Employee)
def modify_employee(emp: EmployeeRequest, db_session: SESSION = Depends(get_db_session)):
    """ Update employee """
    found_employee = crud.get_employee_by_idir(
        db_session=db_session, employee_idir=emp.idir)
    if found_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.update_employee(db_session=db_session, employee=emp)


@APP.delete("/employees/{emp_idir}", response_model=str)
def remove_employee(emp_idir: str, db_session: SESSION = Depends(get_db_session)):
    """ Delete employee by employee id """
    found_employee = crud.get_employee_by_idir(
        db_session=db_session, employee_idir=emp_idir)
    if found_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.delete_employee(db_session=db_session, employee_idir=emp_idir)
