import sqlalchemy
from .common import Session

def runtests():
    engine = sqlalchemy.create_engine('sqlite://')
    Session.configure(bind=engine)
