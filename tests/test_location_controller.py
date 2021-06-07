from tests.base_test_case import BaseTestCase


class TestLocationController(BaseTestCase):
    location_data = {
        "name": "Delhi",
        "latitude": 29.760427,
        "longitude": -95.369804,
        "full_address": "new ashok nagar delhi dummy",
    }

    def test_create_location(self):
        result = self.location_controller.create(self.location_data)
        self.assertEqual(result.data.status_code, 201, "status codes do not match")

    def test_update_location(self):
        result = self.location_controller.create(self.location_data)
        self.assertEqual(result.data.status_code, 201, "status codes do not match")
        self.assertEqual(result.data.value.price, 50)

        result = self.location_controller.update(result.data.value.id, {"name": "dummy"})
        self.assertEqual(result.data.status_code, 200)
        self.assertEqual(result.data.value.price, 70)

    def test_delete_location(self):
        result = self.location_controller.create(self.location_ata)
        self.assertEqual(result.data.status_code, 201, "status codes do not match")
        self.assertEqual(result.data.value.price, 50)

        result = self.catalog_controller.delete(result.data.value.id)
        self.assertEqual(result.data.status_code, 204)

    def test_get_all_catalog(self):
        self.location_controller.create(self.location_data)

        result = self.location_controller.index()
        self.assertEqual(result.data.status_code, 200)
        self.assertEqual(result.data.value[0].price, 50)
