"""Defines the Flask app and API endpoints."""

# Third-party imports
from flask import jsonify, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Local imports
from . import flask_extensions, constants


app = flask_extensions.FlaskApp(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour", "10 per minute"],
)


@app.route("/philly-trash-holidays")
def get_trash_holidays() -> Response:
    """Get the list of trash holidays.

    :return: The list of trash holidays serialized to JSON and wrapped
        in a flask.Response object.
    """
    return jsonify(constants.TRASH_HOLIDAYS_2022)
