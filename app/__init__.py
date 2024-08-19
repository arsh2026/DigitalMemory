from flask import Flask
from .config import Config
from .routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Register Blueprints
    register_blueprints(app)

    return app
