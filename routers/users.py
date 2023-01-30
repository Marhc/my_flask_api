from flask import Blueprint

from controllers.users import UserController
from schemas.users import UserSchema
from util.validation import validate
from util.functions import filename


resource_name = filename(__file__)

item_url = '/<int:id>'

user_controller = UserController()

user_schema = UserSchema()

user_router = Blueprint(resource_name, __name__, url_prefix=resource_name)


@user_router.route('', methods=['GET'])
def index():
    return user_controller.list()


@user_router.route('', methods=['POST'])
@validate(user_schema)
def store(data):
    return user_controller.create(data)


@user_router.route(item_url, methods=['GET'])
def show(id):
    return user_controller.read(id)


@user_router.route(item_url, methods=['PUT', 'PATCH'])
@validate(user_schema, partial=True)
def save(id, data):
    return user_controller.update(id, data)


@user_router.route(item_url, methods=['DELETE'])
def remove(id):
    return user_controller.delete(id)
