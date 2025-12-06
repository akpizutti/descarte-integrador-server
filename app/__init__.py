from flask import Flask
from .routes.api import api_bp

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.config.Config')

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app