""" Creates all database objects """
from database import BASE, ENGINE
import models  # pylint: disable = unused-import

BASE.metadata.create_all(ENGINE)
