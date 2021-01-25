from flask import jsonify
from flask import Blueprint

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(400)
def error_400(error):
    return jsonify(message="Bad request", status=400), 400


@errors.app_errorhandler(404)
def error_404(error):
    return jsonify(message="Page does not exist", status=404), 404


@errors.app_errorhandler(500)
def error_500(error):
    return jsonify(message="Something went wrong", status=500), 500
