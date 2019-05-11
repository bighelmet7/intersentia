from flask_api import status
from flask_restful import Resource, marshal_with, reqparse

from bar.models import Bar
from bar.models import Sandwich
from v1.fields.bar import bar_fields
from v1.fields.bar import sandwich_fields

# TODO: 
# same standarize the parser pattern. https://flask-restful.readthedocs.io/en/latest/reqparse.html#parser-inheritance

class BarParserMixin(object):

    def _parse_args(self):
        # FIX: should not call this in every single request.
        parser = reqparse.RequestParser()
        parser.add_argument('email')
        parser.add_argument('name')
        return parser.parse_args()


class BarList(BarParserMixin, Resource):

    @marshal_with(bar_fields)
    def get(self):
        results = Bar.query.all()
        return results, status.HTTP_200_OK

    @marshal_with(bar_fields)
    def post(self):
        args = self._parse_args()
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
        args = self._parse_args()
        bar = self.query({'id': id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        bar.update(**args)
        return bar, status.HTTP_202_ACCEPTED

    @marshal_with(bar_fields)
    def delete(self, id):
        bar = self.query({'id': id})
        bar.delete()
        return '', status.HTTP_200_OK


class SandwichParserMixin(object):

    def _parse_args(self):
        # FIX: creates a new parser for every new request.
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('price')
        return parser.parse_args()


class SandwichList(SandwichParserMixin, Resource):

    query = lambda obj, q: Bar.query.filter_by(**q).first()

    @marshal_with(sandwich_fields)
    def get(self, bar_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        return bar.sandwiches, status.HTTP_200_OK

    @marshal_with(sandwich_fields)
    def post(self, bar_id):
        bar = self.query({'id': bar_id})
        if not bar:
            return '', status.HTTP_404_NOT_FOUND
        args = self._parse_args()
        sandwich = Sandwich.create(**args)
        bar.sandwiches.append(sandwich)
        # FIX: this is not atomic. ACID issues could appear.
        bar.save()
        return sandwich, status.HTTP_201_CREATED
        

