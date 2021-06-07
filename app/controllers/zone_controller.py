from app.definitions import Result
from app.definitions.service_result import ServiceResult
from app.repositories import ZoneRepository

# from app.producer import publish_to_kafka


class ZoneController:
    def __init__(self, zone_repository: ZoneRepository):
        self.repository = zone_repository

    def index(self):
        zones = self.repository.index()
        return ServiceResult(Result(zones, status_code=200))

    def show(self, id):
        zone = self.repository.find_by_id(id)
        return ServiceResult(Result(zone, status_code=200))

    def create(self, data):
        zone = self.repository.create(data)
        return ServiceResult(Result(zone, status_code=201))

    def update(self, obj_id, data):
        zone = self.repository.update_by_id(obj_id, data)
        # publish_to_kafka("CATALOG_UPDATE", obj_id)
        return ServiceResult(Result(zone, status_code=200))

    def delete(self, obj_id):
        self.repository.delete(obj_id=obj_id)
        return ServiceResult(Result({}, status_code=204))
