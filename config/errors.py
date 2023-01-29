from flask import jsonify


def error(place, message):
    errors = {place: [message]}

    return jsonify(errors=errors)


def set_errors(app):
    app.errorhandler(404)(url_not_found)
    app.errorhandler(405)(method_not_allowed)
    app.errorhandler(500)(internal_server_error)


def url_not_found(_):
    return error('url', "Path Not Found"), 404


def method_not_allowed(_):
    return error('request', "Method Not Allowed"), 405


def internal_server_error(_):
    return error('server', "Internal Server Error"), 500
