""" Test to connect to database and execute transaction

TODO: remove this file!
"""

from db_init import SESSION, BASE, ENGINE
from models.employee import Employee

BASE.metadata.create_all(ENGINE)
CURRENT_SESSION = SESSION()

EMPLOYEE = Employee(idir="nkuruba",
                    status="online",
                    location="victoria",
                    phone="123-456-7890")
# create
CURRENT_SESSION.add(EMPLOYEE)
CURRENT_SESSION.commit()

# Read
EMPLOYEES = CURRENT_SESSION.query(Employee)
for EMPLOYEE in EMPLOYEES:
    print(EMPLOYEE.idir)

# Delete
CURRENT_SESSION.delete(EMPLOYEE)
CURRENT_SESSION.commit()
CURRENT_SESSION.close()
