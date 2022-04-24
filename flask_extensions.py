# Standard library imports
from datetime import date

# Third-party imports
from flask import Flask
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()


class FlaskApp(Flask):
    json_encoder = CustomJSONEncoder
