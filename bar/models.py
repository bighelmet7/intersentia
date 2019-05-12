import re

from intersentia.database import db
from intersentia.database import Model
from intersentia.exceptions import ValidationError
from utils import re_compile
from sqlalchemy.orm import validates


bar_sandwiches = db.Table('bar_sandwiches', db.Model.metadata,
    db.Column('bar_id', db.Integer, db.ForeignKey('bars.id'), primary_key=True),
    db.Column('sandwich_id', db.Integer, db.ForeignKey('sandwiches.id'), primary_key=True),
)


class Bar(Model):

    __tablename__ = 'bars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    sandwiches = db.relationship('Sandwich', secondary=bar_sandwiches, lazy='dynamic',
        backref=db.backref('bars', lazy='dynamic'),
    )
    is_shop_day = db.Column(db.Boolean, default=False)

    @validates('email')
    def validates_email(self, key, email):
        msg = 'Invalid email address'
        if '@' not in email:
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
        return u'<Bar %d: %s>' % (self.id, self.name)


sandwiches_toppings = db.Table('sandwiches_toppings', db.Model.metadata,
    db.Column('sandwich_id', db.Integer, db.ForeignKey('sandwiches.id'), primary_key=True),
    db.Column('topping_id', db.Integer, db.ForeignKey('toppings.id'), primary_key=True),
)


class Sandwich(Model):

    __tablename__ = 'sandwiches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    toppings = db.relationship('Topping', secondary=sandwiches_toppings, 
        lazy='dynamic', backref=db.backref('sandwiches', lazy='dynamic'),
    )

    def __repr__(self):
        return u'<Sandwich %d: %s>' % (self.id, self.name)


class Topping(Model):

    __tablename__ = 'toppings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    def __repr__(self):
        return u'<Topping %d: %s>' % (self.id, self.name)
