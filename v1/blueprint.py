from flask import Blueprint
from flask_restful import Api

from v1.resources.bars import BarDetail
from v1.resources.bars import BarList
from v1.resources.bars import SandwichList
from v1.resources.bars import SandwichDetail
from v1.resources.bars import ToppingList
from v1.resources.bars import ToppingDetail

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

#### BAR ENDPOINTS ####
api.add_resource(BarList, '/v1/bars/')
api.add_resource(BarDetail, '/v1/bars/<int:id>/')
api.add_resource(SandwichList, '/v1/bars/<int:bar_id>/sandwiches/')
api.add_resource(SandwichDetail, '/v1/bars/<int:bar_id>/sandwiches/<int:sandwich_id>/')
api.add_resource(ToppingList, '/v1/bars/<int:bar_id>/sandwiches/<int:sandwich_id>/toppings/')
api.add_resource(ToppingDetail, '/v1/bars/<int:bar_id>/sandwiches/<int:sandwich_id>/toppings/<int:topping_id>')

#### Users ENDPOINTS ####

#### Order ENDPOINTS ####
