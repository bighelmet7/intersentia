from flask_restful import Resource, marshal_with
from flask_api import status
from user.models import User

from v1.fields.user import user_fields
from v1.resources.parser import ParserMixin


class UserList(ParserMixin, Resource):

    @marshal_with(user_fields)
    def get(self):
        results = User.query.all()
        return results, status.HTTP_200_OK

    @marshal_with(user_fields)
    def post(self):
        args = self._parse_args(('name', str), ('dni', str))
        user = User.create(**args)
        return user, status.HTTP_201_CREATED


class UserDetail(ParserMixin, Resource):

    query = lambda obj, q: User.query.filter_by(**q).first()

    @marshal_with(user_fields)
    def get(self, id):
        result = self.query({'id': id})
        return result, status.HTTP_200_OK

    @marshal_with(user_fields)
    def put(self, id):
        user = self.query({'id': id})
        if not user:
            return '', status.HTTP_404_NOT_FOUND
        args = self._parse_args(('name', str), ('is_admin', bool), ('is_manager', bool))
        user.update(**args)
        return user, status.HTTP_202_ACCEPTED

    @marshal_with(user_fields)
    def delete(self, id):
        user = self.query({'id': id})
        user.delete()
        return '', status.HTTP_200_OK
