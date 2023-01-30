from marshmallow import Schema, fields, EXCLUDE
from util.validation import resource, unique
from util.functions import filename


resource_name = filename(__file__)


@resource(resource_name)
class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True, validate=unique(resource_name))
    password = fields.Str(required=True, load_only=True)
