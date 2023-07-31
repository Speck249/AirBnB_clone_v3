#!/usr/bin/python3
""" Initialization """
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url prefix ='/api/v1')
