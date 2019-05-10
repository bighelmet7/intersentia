from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import re
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(BASE_DIR, 'examen.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def re_compile(regex, flags=0):
    """
    Return and regex compile object with the given flags.
    """
    if not isinstance(regex, str):
        raise TypeError('Regex must be and a str instace.')
    return re.compile(regex, flags=flags)


class ValidationError(Exception):
    pass


class Bar(db.Model):
    """
    TODO: validation of the email. @validate('email').
    """

    __tablename__ = 'bars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)

    @validates('email')
    def validates_email(self, key, email):
        msg = 'Invalid email address'
        if '@' is not in email:
            raise ValidationError(msg)

        user, domain = email.split('@')
        user_regex = re_compile(
                r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z"
                r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"\Z)',
                re.IGNORECASE)
        if not user_regex.match(user):
            raise ValidationError(msg)

        domain_regex = re_compile(
                r'((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+)(?:[A-Z0-9-]{2,63}(?<!-))\Z',
                re.IGNORECASE)
        if not domain_regex.match(domain):
            raise ValidationError(msg)

        return email

    def __repr__(self):
        return '<Bar %d: %s>' % (self.id, self.name)

@app.route('/ping/')
def ping():
    return 'Pong'

@app.route('/api/v1/bars/', methods=['GET'])
def bars():
    return 'Bars'
