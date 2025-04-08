# Import the Flask class from the flask package
from flask import Flask

# Import the Config class from the config module
from config import Config

def create_app():
    # Create a Flask app instance
    app = Flask(__name__)

    # Load configuration settings from the Config class
    app.config.from_object(Config)

    # Return the Flask app instance
    return app
