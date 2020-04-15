""" CRUD operations for management of resources
"""
from sqlalchemy.orm import Session
from models import Employee
import schemas


def get_employee(db_session: Session, employee_idir: str):
    """ Get employee by idir """
    return db_session.query(Employee).filter(Employee.idir == employee_idir).first()


def get_employee_by_idir(db_session: Session, employee_idir: str):
    """ Get employee by idir """
    return db_session.query(Employee).filter(Employee.idir == employee_idir).first()


def get_employees(db_session: Session):
    """ Get all employees """
    list_of_emps = []
    list_of_records = db_session.query(Employee).all()
    for recd in list_of_records:
        emp = schemas.Employee(
            id=recd.id,
            idir=recd.idir,
            status=recd.status,
            location=recd.location,
            phone=recd.phone)
        list_of_emps.append(emp)
    return list_of_emps


def create_employee(db_session: Session, employee: schemas.EmployeeRequest):
    """ Create new employee """
    new_employee = Employee(
        idir=employee.idir,
        status=employee.status,
        location=employee.location,
        phone=employee.phone)
    db_session.add(new_employee)
    db_session.commit()
    db_session.refresh(new_employee)
    return db_session.query(Employee).filter(Employee.idir == employee.idir).first()


def delete_employee(db_session: Session, employee_idir: str):
    """ Delete employee by idir """
    db_session.query(Employee).filter(Employee.idir == employee_idir).delete()
    db_session.commit()
    return employee_idir


def update_employee(db_session: Session, employee: schemas.EmployeeRequest):
    """ Update employee by idir """
    db_session.query(Employee).filter(Employee.idir == employee.idir).update(
        {
            Employee.status: employee.status,
            Employee.location: employee.location,
            Employee.phone: employee.phone
        }, synchronize_session=False)
    db_session.commit()
    return db_session.query(Employee).filter(Employee.idir == employee.idir).first()
