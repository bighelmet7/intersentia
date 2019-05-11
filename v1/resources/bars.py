from flask_api import status
from flask_restful import Resource, marshal_with, reqparse
from sqlalchemy.orm.exc import NoResultFound

from bar.models import Bar
from bar.models import Sandwich
from bar.models import Topping
from v1.fields.bar import bar_fields
from v1.fields.bar import sandwich_fields
from v1.fields.bar import toppings_fields

# INFO: only one sandwiches per employee.

# TODO: 
# standarize the parser pattern. https://flask-restful.readthedocs.io/en/latest/reqparse.html#parser-inheritance
# add_argument accepts a parameter append, that concates the url-x-form values
# in the same key {'key': ['v1', 'v2', 'v3']}.
# slipt these doc into 3 files: bar, sandwich and topping.
# Create a QueryManager object to handle all the Queries.

class BarParserMixin(object):

    def _parse_args(self, *args):
        # FIX: should not call this in every single request.
        parser = reqparse.RequestParser()
        for arg in args:
            parser.add_argument(arg)
        return parser.parse_args()


class BarList(BarParserMixin, Resource):

    @marshal_with(bar_fields)
    def get(self):
        results = Bar.query.all()
        return results, status.HTTP_200_OK

    @marshal_with(bar_fields)
    def post(self):
        args = self._parse_args('name', 'email')
        bar_result = Bar.create(**args)
        return bar_result, status.HTTP_201_CREATED


class BarDetail(BarParserMixin, Resource):

    query = lambda obj, q: Bar.query.filter_by(**q).first()

    @marshal_with(bar_fields)
    def get(self, id):
        result = self.query({'id': id})
        return result, status.HTTP_200_OK

    @marshal_with(bar_fields)
    def put(self, id):
        bar = self.query({'id': id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        # INFO: name its not editable.
        args = self._parse_args('email')
        bar.update(**args)
        return bar, status.HTTP_202_ACCEPTED

    @marshal_with(bar_fields)
    def delete(self, id):
        bar = self.query({'id': id})
        bar.delete()
        return '', status.HTTP_200_OK


class SandwichParserMixin(object):

    def _parse_args(self, *args):
        # FIX: creates a new parser for every new request.
        parser = reqparse.RequestParser()
        for arg in args:
            parser.add_argument(arg)
        return parser.parse_args()


class SandwichList(SandwichParserMixin, Resource):

    query = lambda obj, q: Bar.query.filter_by(**q).first()

    @marshal_with(sandwich_fields)
    def get(self, bar_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        return bar.sandwiches.all(), status.HTTP_200_OK

    @marshal_with(sandwich_fields)
    def post(self, bar_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        args = self._parse_args('name', 'price')
        sandwich = Sandwich.create(**args)
        bar.sandwiches.append(sandwich)
        # FIX: this is not atomic. ACID issues could appear.
        bar.save()
        return sandwich, status.HTTP_201_CREATED
        

class SandwichDetail(SandwichParserMixin, Resource):

    query = lambda obj, q: Bar.query.filter_by(**q).first()

    @marshal_with(sandwich_fields)
    def get(self, bar_id, sandwich_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        try:
            sandwich = bar.sandwiches.filter(Sandwich.id==sandwich_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        return sandwich, status.HTTP_200_OK

    @marshal_with(sandwich_fields)
    def put(self, bar_id, sandwich_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        try:
            sandwich = bar.sandwiches.filter(Sandwich.id==sandwich_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        args = self._parse_args('price')
        # INFO: only the price is editable.
        sandwich.update(**args)
        return sandwich, status.HTTP_202_ACCEPTED

    @marshal_with(sandwich_fields)
    def delete(self, bar_id, sandwich_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        try:
            sandwich = bar.sandwiches.filter(Sandwich.id==sandwich_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        sandwich.delete()
        return '', status.HTTP_200_OK


class ToppingParserMixin(object):

    def _parse_args(self, *args):
        # FIX: creates a new parser for every new request.
        parser = reqparse.RequestParser()
        for arg in args:
            parser.add_argument(arg)
        return parser.parse_args()


class ToppingList(ToppingParserMixin, Resource):

    query = lambda obj, q: Bar.query.filter_by(**q).first()

    @marshal_with(toppings_fields)
    def get(self, bar_id, sandwich_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        try:
            sandwich = bar.sandwiches.filter(Sandwich.id==sandwich_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        return sandwich.toppings.all(), status.HTTP_200_OK

    @marshal_with(toppings_fields)
    def post(self, bar_id, sandwich_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        args = self._parse_args('name', 'price')
        try:
            sandwich = bar.sandwiches.filter(Sandwich.id==sandwich_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        topping = Topping.create(**args)
        sandwich.toppings.append(topping)
        # FIX: this is not atomic. ACID issues could appear.
        sandwich.save()
        return topping, status.HTTP_201_CREATED
        

class ToppingDetail(ToppingParserMixin, Resource):

    query = lambda obj, q: Bar.query.filter_by(**q).first()


    @marshal_with(toppings_fields)
    def put(self, bar_id, sandwich_id, topping_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        try:
            sandwich = bar.sandwiches.filter(Sandwich.id==sandwich_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        args = self._parse_args('price')
        try:
            topping = sandwich.toppings.filter(Topping.id==topping_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        # INFO: only the price is editable.
        topping.update(**args)
        return topping, status.HTTP_202_ACCEPTED

    @marshal_with(toppings_fields)
    def delete(self, bar_id, sandwich_id, topping_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        try:
            sandwich = bar.sandwiches.filter(Sandwich.id==sandwich_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        try:
            topping = sandwich.toppings.filter(Topping.id==topping_id).one()
        except NoResultFound:
            return '', status.HTTP_404_NOT_FOUND
        topping.delete()
        return '', status.HTTP_200_OK
