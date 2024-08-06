#!/usr/bin/python3
"""
This module contains endpoints
It checksthe status and retrieving statistics.
"""
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status of the API in JSON format
    Example response:
    {
        "status": "OK"
    }
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """
    Collects the count of each object type in the database.
    Example response:
    {
        "amenities": 10,
        "cities": 5,
        "places": 20,
        "reviews": 30,
        "states": 7,
        "users": 12
    }
    """
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
