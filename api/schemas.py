""" This module contains Pydantic models.
"""
from pydantic import BaseModel


class Health(BaseModel):
    """ A very basic health response. """
    ok: bool
