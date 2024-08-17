from flask import Flask
from .config import Config
from .routes import register_blueprints
from .routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_bp)
    # Register Blueprints
    register_blueprints(app)

    return app
