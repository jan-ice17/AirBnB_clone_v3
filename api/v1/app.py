#!/usr/bin/python3
"""
A script that create a variable
app_views which is an instance of Blueprint"
"""
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """This will close the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    from os import getenv
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
