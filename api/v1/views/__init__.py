#!/usr/bin/python3
"""Views module.
Contains a blueprint.
"""


from api.v1.views.index import *
from flask import Blueprint


app_views = Blueprint('app_views', url_prefix='/api/v1')
