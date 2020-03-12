from flask_marshmallow import Marshmallow
from marshmallow import fields
from app import ma


class CustomerSchema(ma.Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    exclude = ('password')

class ResultSchema(ma.Schema):
    id = fields.Integer()
    module_id = fields.Integer()
    customer_id = fields.Integer()


# Init schema
customer_Schema = CustomerSchema()
customers_Schema = CustomerSchema(many=True)

resultSchema = ResultSchema()
resultsSchema = ResultSchema(many=True)