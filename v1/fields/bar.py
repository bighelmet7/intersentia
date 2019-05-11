from flask_restful import fields

toppings_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
}

sandwich_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'toppings': fields.List(fields.Nested(toppings_fields)),
}

bar_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'sandwiches': fields.List(fields.Nested(sandwich_fields)),
}