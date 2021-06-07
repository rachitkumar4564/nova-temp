from app.repositories import LocationRepository
from app.definitions.result import Result
from app.definitions.service_result import ServiceResult


class LocationController:
    def __init__(self, location_repository: LocationRepository):
        self.repository = location_repository

    def index(self):
        locations = self.repository.index()
        return ServiceResult(Result(locations, status_code=200))

    def show(self, id):
        location = self.repository.find_by_id(id)
        return ServiceResult(Result(location, status_code=200))

    def create(self, data):
        location = self.repository.create(data)
        return ServiceResult(Result(location, status_code=201))

    def update(self, obj_id, data):
        location = self.repository.update_by_id(obj_id, data)
        # publish_to_kafka("CATALOG_UPDATE", obj_id)
        return ServiceResult(Result(location, status_code=200))

    def delete(self, obj_id):
        self.repository.delete(obj_id=obj_id)
        return ServiceResult(Result({}, status_code=204))

    def dist_between_two_lat_lon(self, *args):
        from math import asin, cos, radians, sin, sqrt

        lat1, lat2, long1, long2 = map(radians, args[1:])

        dist_lats = abs(lat2 - lat1)
        dist_longs = abs(long2 - long1)

        a = sin(dist_lats / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dist_longs / 2) ** 2
        c = asin(sqrt(a)) * 2
        radius_earth = 6378
        return c * radius_earth

    def get_nearby(self, data, schema):
        locations = self.repository.index()
        try:
            nearby_location = min(
                schema(many=True).dumps(locations),
                key=lambda p: self.dist_between_two_lat_lon(
                    data["latitude"],
                    data["latitude"],
                    data["longitude"],
                    data["longitude"],
                ),
            )
            res_location = {"data": nearby_location}
        except TypeError:
            print("Not a list or not a number.")
            res_location = {"data": "Not a list or not a number"}
        return ServiceResult(Result(res_location, status_code=200))
