from flask import Flask
from config.routes import set_routes
from config.errors import set_errors

app = Flask(__name__)

set_routes(app)

set_errors(app)
