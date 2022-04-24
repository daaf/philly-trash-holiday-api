# Third-party imports
from flask import request, jsonify

# Local imports
from . import flask_extensions, globals


app = flask_extensions.FlaskApp(__name__)


@app.route("/philly-trash-holidays")
def get_trash_holidays():
    return jsonify(globals.TRASH_HOLIDAYS_2022)


@app.route("/philly-trash-holidays", methods=["POST"])
def add_trash_holiday():
    globals.TRASH_HOLIDAYS_2022.append(request.get_json())
    return "", 204
