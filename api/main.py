""" This module contains the entrypoint for the Emergency Personnel Reporting API.

See README.md for details on how to run.
"""
from os import getenv
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import psycopg2

from schemas import Health


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
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@APP.get('/health')
async def health():
    """ Return 200 if site is up and healthy. At this point, we assume that being able to
    talk to the database means we're good to go. """
    # TODO: Change this to use SQLAlchemy.  # pylint: disable=fixme
    host = getenv("POSTGRES_HOST")
    dbname = getenv("POSTGRES_DATABASE")
    user = getenv("POSTGRES_USER")
    password = getenv("POSTGRES_PASSWORD")
    with psycopg2.connect(host=host, dbname=dbname, user=user, password=password) as connection:
        return Health(ok=connection is not None)
