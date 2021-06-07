from .endpoints.location import location
from .endpoints.zone import zone


def init_app(app):
    app.register_blueprint(location, url_prefix="/api/v1/location")
    app.register_blueprint(zone, url_prefix="/api/v1/zone")
