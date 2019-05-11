import factory
from bar.models import Bar
from intersentia.common import Session

class BarFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Bar
        sqlalchemy_session = Session

