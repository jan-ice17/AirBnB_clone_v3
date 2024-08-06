#!/usr/bin/python3
"""
This module contains the main application for the AirBnB clone RESTful API.
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv
from flask_cors import CORS
from flasgger import Swagger


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Register the blueprint that handles the API views
app.register_blueprint(app_views)
# Enable CORS to allow cross-origin requests from any IP to the API
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(obj):
    """ Close the database session when the app context is torn down """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ Return a JSON-formatted 404 error response """
    return make_response(jsonify({"error": "Not found"}), 404)


# Swagger configuration for API documentation
app.config['SWAGGER'] = {
    'title': 'AirBnB Clone - RESTful API',
    'description': 'This is the API for the AirBnB clone project.',
    'uiversion': 3
}
# Initialize Swagger for API documentation
Swagger(app)
if __name__ == "__main__":
    # Get the host and port from environment variables, with default values
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    # Run the application with the specified host and port
    app.run(host, int(port), threaded=True)
