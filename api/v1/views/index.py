#!/usr/bin/python3
"""Index.
Main page for all API requests.
"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """Check if the API works."""
    return jsonify(status='ok')
