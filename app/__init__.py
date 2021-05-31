import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import DBAPIError
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import HTTPException
from werkzeug.utils import import_string


# load dotenv in the base root
from app.definitions.exceptions.app_exceptions import app_exception_handler

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")  # refers to application_top
dotenv_path = os.path.join(APP_ROOT, ".env")

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

# IMPORT BLUEPRINTS HERE


# SWAGGER
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Python-Flask-REST-Boilerplate"}
)

FLASK_ENV = os.getenv("FLASK_ENV") if os.getenv("FLASK_ENV") else "production"


def create_app():
    """Construct the core application"""
    app = Flask(__name__, instance_relative_config=False)
    cfg = None
    if FLASK_ENV == "development":
        cfg = import_string("config.DevelopmentConfig")()
    elif FLASK_ENV == "production":
        cfg = import_string("config.ProductionConfig")()
    elif FLASK_ENV == "testing":
        cfg = import_string("config.TestingConfig")()
    app.config.from_object(cfg)

    # add extensions
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return app_exception_handler(e)

    @app.errorhandler(DBAPIError)
    def handle_db_exception(e):
        return app_exception_handler(e)

    with app.app_context():
        db.create_all()
    return None


def register_blueprints(app):
    from .api.api_v1 import api

    """Register Flask blueprints."""
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    api.init_app(app)
    return None
