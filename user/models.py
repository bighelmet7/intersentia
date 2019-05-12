from passlib.apps import custom_app_context

from intersentia.database import db
from intersentia.database import Model

# TODO: validate DNI column.

class User(Model):
    """
    If not admin and manager its a normal worker.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    dni = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128))
    total_amount = db.Column(db.Float(precision=2))
    is_admin = db.Column(db.Boolean, default=False)
    is_manager = db.Column(db.Boolean, default=False)

    def hash_password(self, password):
        self.password = custom_app_context.encrypt(password)

    def verify_password(self, pwd):
        return custom_app_context.verify(pwd, self.password)
