#!/usr/bin/python3
"""AirBnB clone RESTful API.
RESTful API of the AirBnB clone project.
"""


from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
api_host = getenv("HBNB_API_HOST", default="0.0.0.0")
api_port = getenv("HBNB_API_PORT", default="5000")


@app.errorhandler(404)
def not_found(error):
    """Special HTTP 404 handler."""
    return make_response(jsonify(error="Not found"), 404)


@app.teardown_appcontext
def close_session(e):
    """Close the SQLAlchemy session after the request."""
    storage.close


if __name__ == "__main__":
    app.run(host=api_host, port=api_port, threaded=True)
