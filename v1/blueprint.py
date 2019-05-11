from flask import Blueprint
from flask_restful import Api

from v1.views.bars import BarDetail
from v1.views.bars import BarList
from v1.views.bars import SandwichList
from v1.views.bars import SandwichDetail

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(BarList, '/v1/bars/')
api.add_resource(BarDetail, '/v1/bars/<int:id>/')
api.add_resource(SandwichList, '/v1/bars/<int:bar_id>/sandwiches/')
api.add_resource(SandwichDetail, '/v1/bars/<int:bar_id>/sandwiches/<int:sandwich_id>/')
