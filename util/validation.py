from functools import wraps
from flask import request, jsonify
from marshmallow import ValidationError
from config.errors import error
from config.schemas import app_schemas


def if_exists(func):
    def wrapper(self, id, data=None):
        index = next((i for i, item in enumerate(
            self.table) if item["id"] == id), None)

        if index == None:
            return error('url', 'Item Not Found'), 404

        if data:
            return func(self, index, data)
        else:
            return func(self, index)

    return wrapper


def validate(schema, partial=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data_input = request.get_json()
                valid_data = schema.load(data_input, partial=partial)
            except ValidationError as err:
                return jsonify(errors=err.messages), 422
            return func(*args, data=valid_data, **kwargs)
        return wrapper
    return decorator


def resource(resource_name):
    def wrapper(schema_class):
        app_schemas[resource_name] = schema_class
        return schema_class
    return wrapper


def serialize(resource, data, many=False):
    return jsonify(app_schemas[resource](many=many).dump(data))
