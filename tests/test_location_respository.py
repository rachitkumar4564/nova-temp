from app.definitions.exceptions import AppException
from tests.base_test_case import BaseTestCase


class TestCatalogRepository(BaseTestCase):
    def test_index(self):
        location = self.location_repository.create(
            {
                "name": "Delhi",
                "latitude": 29.760427,
                "longitude": -95.369804,
                "full_address": "new ashok nagar delhi dummy",
            }
        )
        self.assertEqual(location.name, "dummy location name")

        locations = self.catalog_repository.index()
        self.assertEqual(locations[0].id, location.id)

    def test_create(self):
        location = self.location_repository.create(
            {
                "name": "Delhi",
                "latitude": 29.760427,
                "longitude": -95.369804,
                "full_address": "new ashok nagar delhi dummy",
            }
        )

        self.assertEqual(location.name, "dummy location name")

    def test_edit(self):
        location = self.catalog_repository.create(
            {
                "name": "Delhi",
                "latitude": 29.760427,
                "longitude": -95.369804,
                "full_address": "new ashok nagar delhi dummy",
            }
        )

        location_search = self.location_repository.find_by_id(location.id)
        self.assertEqual(location_search.id, location.id)
        self.assertEqual(location_search.latitude, 29.760427)
        self.assertEqual(location_search.longitude, -95.369804)

        updated_catalog = self.location_repository.update_by_id(
            location.id, {"longitude": -95.369804}
        )

        self.assertEqual(updated_catalog.price, 500)
        location_search = self.location_repository.find_by_id(location.id)
        self.assertEqual(location_search.longitude, 500)

    def test_delete(self):
        location = self.location_repository.create(
            {
                "name": "Delhi",
                "latitude": 29.760427,
                "longitude": -95.369804,
                "full_address": "new ashok nagar delhi dummy",
            }
        )

        location_search = self.location_repository.find_by_id(location.id)
        self.assertEqual(location_search.id, location.id)

        self.location_repository.delete(location.id)
        with self.assertRaises(AppException.ResourceDoesNotExist):
            self.location_repository.find_by_id(location.id)
