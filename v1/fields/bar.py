from flask_restful import fields

sandwich_fields = {
    'name': fields.String,
    'price': fields.Float,
}

bar_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'sandwiches': fields.List(fields.Nested(sandwich_fields)),
}