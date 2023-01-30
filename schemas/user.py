from marshmallow import Schema, fields, EXCLUDE
from util.validation import resource, unique


@resource('users')
class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True, validate=unique(resource_name='users'))
    password = fields.Str(required=True, load_only=True)
