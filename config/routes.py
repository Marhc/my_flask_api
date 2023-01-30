
from flask import Blueprint
from config.api import base_url
from routers.users import user_router


def set_routes(app):
    app.register_blueprint(app_router)


app_router = Blueprint('root', __name__, url_prefix=base_url)

app_router.register_blueprint(user_router)
