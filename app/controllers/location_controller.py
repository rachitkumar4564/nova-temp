import datetime
from app.definitions.repository_interfaces.location_repository_interface import (
    LocationRepositoryInterface,
    ZoneRepositoryInterface,
)
from app.definitions.result import Result
from app.definitions.service_result import ServiceResult
from loguru import logger
from app.models import Location, Zone, ZoneLocation
from app import db


class LocationController:
    def __init__(self, location_repository: LocationRepositoryInterface):
        self.location_repository = location_repository

    def create_location(self, location_data):
        location = self.location_repository.create(obj_in=location_data)
        return ServiceResult(Result(location, status_code=200))

    def update_location(self, location_id, location_data):
        location_result = self.location_repository.update_by_id(
            location_id, obj_in=location_data
        )
        logger.info(f"{location_result}| test")
        data = {"data": {"message": "updated successfully"}}
        return ServiceResult(Result(data, status_code=200))

    def delete_location(self, location_id):
        self.location_repository.delete(location_id)
        data = {"data": {"message": "deleted successfully"}}
        return ServiceResult(Result(data, status_code=200))

    def get_nearby(self, location_id):
        get_point = Location.query.get(location_id)
        return ServiceResult(Result(get_point, status_code=200))


class ZoneController:
    def __init__(self, zone_repository: ZoneRepositoryInterface):
        self.zone_repository = zone_repository

    def get_zone(self):
        # zone_location = db.session.query(Zone).join(Zone_location).filter(
        #     Zone.id == Zone_location.zone_id
        # ).all()
        # l_location = db.session.query(Location).join(Zone_location).filter(
        #     Location.id == Zone_location.location_id
        # ).all()
        # z1 = Zone_location.query.all()
        z1 = db.session.query(ZoneLocation).all()
        logger.info(f"{[i for i in z1]}")
        # data ={"zone_id": zone_location[0, "location_id": l_location[0]}
        return ServiceResult(Result(z1, status_code=200))

    def create_zone(self, zone_data):
        name = zone_data.get("name")
        wave_points = zone_data.get("wave_points")
        z_data = Zone(
            name=name,
            wave_points=wave_points,
            modified=datetime.datetime.utcnow(),
            created=datetime.datetime.utcnow(),
        )

        db.session.add(z_data)
        for location_data in zone_data.get("location"):

            l_data = Location(
                name=location_data.get("name"),
                latitude=location_data.get("latitude"),
                longitude=location_data.get("longitude"),
                full_address=location_data.get("full_address"),
                modified=datetime.datetime.utcnow(),
                created=datetime.datetime.utcnow(),
            )

        logger.info(f"{z_data, l_data}")
        db.session.add(l_data)
        db.session.commit()
        data = ZoneLocation(
            zone_id=z_data.id,
            location_id=l_data.id,
            modified=datetime.datetime.utcnow(),
            created=datetime.datetime.utcnow(),
        )
        db.session.add(data)
        db.session.commit()
        data1 = {"data": {"message": "created successfully"}}
        # location = self.zone_repository.create(obj_in=zone_data)
        return ServiceResult(Result(data1, status_code=200))

    def update_zone(self, zone_id, zone_data):
        zone_result = self.zone_repository.update_by_id(zone_id, obj_in=zone_data)
        logger.info(f"{zone_result}")
        data = {"data": {"message": "updated successfully"}}
        return ServiceResult(Result(data, status_code=200))
