from flask_marshmallow import Marshmallow
from marshmallow import fields
from app import ma


class CustomerSchema(ma.Schema):
    id = fields.UUID(required=True)
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    # sub_end = fields.Date()
    exclude = ('password', 'sub_end')
    class Meta:
        additional = ('token', )


class ResultSchema(ma.Schema):
    id = fields.Integer()
    results = fields.Raw()
    customer_id = fields.UUID()


# Init schema
customer_Schema = CustomerSchema()
customers_Schema = CustomerSchema(many=True)

resultSchema = ResultSchema()
resultsSchema = ResultSchema(many=True)