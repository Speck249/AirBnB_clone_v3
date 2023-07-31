#!/usr/bin/python3
"""
Script runs flask.
"""
from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """
    Remove current SQLAlchemy Session.
    """
    storage.close()


@app_views.app_errorhandler(404)
def not_found(error):
    """
    Method handles error page.
    """
    return jsonify({'error': 'not found'}), 404


if __name__ == '__main__':
    """ Start Flask dev server. """
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
