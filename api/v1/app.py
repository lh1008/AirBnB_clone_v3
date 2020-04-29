#!/usr/bin/python3
"""AirBnB clone RESTful API.
RESTful implementation of the AirBnB clone project.
"""


from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
api_host = getenv("HBNB_API_HOST", default="0.0.0.0")
api_port = getenv("HBNB_API_PORT", default="5000")


@app.teardown_appcontext
def close_session():
    """Close the SQLAlchemy session after the request."""
    storage.close


if __name__ == "__main__":
    app.run(host=api_host, port=api_port, threaded=True)
