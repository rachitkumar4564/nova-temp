from flask_testing import TestCase
from app import create_app
from app.models import Location, Zone
from app.controllers import LocationController, ZoneController
from app.repositories import LocationRepository, ZoneRepository

# from tests.redis_mock import RedisMock


class BaseTestCase(TestCase):
    data = {}

    def create_app(self):
        app = create_app("config.TestingConfig")
        self.location_repository = LocationRepository()
        self.zone_repository = ZoneRepository()
        self.location_controller = LocationController(ZoneRepository())
        self.zone_controller = ZoneController()
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        Location.drop_collection()
        Zone.drop_collection()

    def tearDown(self):
        """
        Will be called after every test
        """
        Zone.drop_collection()
        Location.drop_collection()
        # self.redis_mock.redis_mock = {}
