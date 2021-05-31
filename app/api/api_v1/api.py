from .endpoints.location import location


def init_app(app):
    app.register_blueprint(location, url_prefix="/api")
