from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

class CustomerSchema(ma.Schema):
    id = fields.UUID(required=True)
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    sub_end = fields.Date()
    exclude = ('password')
    class Meta:
        additional = ('token', )


class AnalysisSchema(ma.Schema):
    id = fields.Integer()
    results = fields.Raw()
    customer_id = fields.UUID()
    exclude= ('customer_id')


# Init schema
customer_Schema = CustomerSchema()
customers_Schema = CustomerSchema(many=True)

analysis_Schema = AnalysisSchema()
analyses_Schema = AnalysisSchema(many=True)