import factory
from app import Bar
from .common import Session

class BarFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Bar
        sqlalchemy_session = Session

