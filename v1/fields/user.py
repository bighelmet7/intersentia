from flask_restful import fields

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'dni': fields.String,
    'total_amount': fields.Float,
    'is_manager': fields.Boolean,
    'is_admin': fields.Boolean,
}
