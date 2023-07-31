#!/usr/bin/python3
"""
Script contains index definition.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app.route('/status')
def status():
    """
    Method displays status.
    """
    return jsonify('{status': 'OK'})


@app.route('/stats')
def stats():
    """
    Method returns individual object count.
    """
    objects = {
            "amenities": storage.count.('Amenity') 
            "cities": storage.count.('City'),
            "places": storage.count.('Place'),
            "reviews": storage.count.('Review'),
            "states": storage.count.('State'),
            "users": storage.count.('User')
            }
    return jsonify(objects)
