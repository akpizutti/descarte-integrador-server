from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')

    from app.routes.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app