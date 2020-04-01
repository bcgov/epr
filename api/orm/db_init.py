""" Setup database to perform CRUD transactions
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_STRING = 'postgres://{}:{}@{}:{}/{}'.format(getenv('POSTGRES_USER'),
                                               getenv('POSTGRES_PASSWORD'),
                                               getenv('POSTGRES_HOST'),
                                               getenv('POSTGRES_PORT'),
                                               getenv('POSTGRES_DATABASE'))
# connect to database
ENGINE = create_engine(DB_STRING)

# bind session to database
SESSION = sessionmaker(bind=ENGINE)

# constructing a base class for declarative class definitions
BASE = declarative_base()
