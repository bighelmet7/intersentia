from flask_restful import reqparse


class ParserMixin(object):

    def _parse_args(self, *args):
        # FIX: should not call this in every single request.
        parser = reqparse.RequestParser()
        for arg, _type in args:
            parser.add_argument(arg, type=_type)
        return parser.parse_args()
