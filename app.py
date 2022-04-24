"""Defines the Flask app and API endpoints."""

# Third-party imports
from flask import jsonify, Response

# Local imports
from . import flask_extensions, globals


app = flask_extensions.FlaskApp(__name__)


@app.route("/philly-trash-holidays")
def get_trash_holidays() -> Response:
    """Get the list of trash holidays.

    :return: The list of trash holidays serialized to JSON and wrapped
        in a flask.Response object.
    """
    return jsonify(globals.TRASH_HOLIDAYS_2022)
