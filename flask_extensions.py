"""Classes to customize Flask functionality."""

# Standard library imports
from datetime import date

# Third-party imports
from flask import Flask
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    """JSONEncoder that encodes dates in ISO 8601 format.

    Encoding dates in ISO 8601 format makes them serializable to JSON.
    """

    def default(self, o) -> str:
        """If the provided object is a date, the date in ISO 8601 format."""
        if isinstance(o, date):
            return o.isoformat()


class FlaskApp(Flask):
    """Extends `Flask` by specifying a custom JSONEncoder."""

    json_encoder = CustomJSONEncoder
