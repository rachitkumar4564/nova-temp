import pinject
from flask import Blueprint, jsonify, request
from app.controllers.location_controller import LocationController, ZoneController
from app.definitions.service_result import handle_result
from app.models.location import Location, ZoneLocation
from app.repositories.location_repository import LocationRepository, ZoneRepository
from app.schema.location_schema import (
    LocationSchema,
    ZoneLocationSchema,
)
from loguru import logger
from http import HTTPStatus

location = Blueprint("location", __name__)


@location.route("/location")
def index():
    locations = Location.query.all()
    logger.error(locations)
    schema = LocationSchema(many=True).dump(locations)
    return jsonify(
        {"data": schema, "status": HTTPStatus.OK, "message": "locations retrieved"}
    )


@location.route("/location", methods=["POST"])
def create():
    data = request.json
    name = data["name"]
    longitude = data["longitude"]
    latitude = data["latitude"]
    full_address = data["full_address"]
    obj_graph = pinject.new_object_graph(
        modules=None, classes=[LocationController, LocationRepository]
    )

    location_controller = obj_graph.provide(LocationController)
    result = location_controller.create_location(
        {
            "name": name,
            "longitude": longitude,
            "latitude": latitude,
            "full_address": full_address,
        }
    )
    return handle_result(result, schema=LocationSchema())


@location.route("location/<uuid:location_id>", methods=["PUT", "DELETE"])
def update(location_id):
    logger.info(f"{request.method}")
    data = request.json
    logger.info(f"{data}")
    obj_graph = pinject.new_object_graph(
        modules=None, classes=[LocationController, LocationRepository]
    )
    location_controller = obj_graph.provide(LocationController)
    if request.method == "PUT":
        result = location_controller.update_location(location_id, data)
    elif request.method == "DELETE":
        result = location_controller.delete_location(location_id)

    return handle_result(result)


@location.route("/zone", methods=["GET", "POST"])
def create_zone_request():
    data = request.json
    logger.info(f"{data}")
    obj_graph = pinject.new_object_graph(
        modules=None, classes=[ZoneController, ZoneRepository]
    )
    logger.info(f"{data}")
    zone_controller = obj_graph.provide(ZoneController)
    if request.method == "POST":
        result = zone_controller.create_zone(data)
        return handle_result(result)
    else:
        data = ZoneLocation.query.all()
        # logger.info(f'{data}')
        schema = ZoneLocationSchema(many=True).dump(data)
        return jsonify(
            {"data": schema, "status": HTTPStatus.OK, "message": "locations retrieved"}
        )


@location.route("/zone/<uuid:zone_id>", methods=["PUT"])
def update_zone_request(zone_id):
    data = request.json
    obj_graph = pinject.new_object_graph(
        modules=None, classes=[ZoneController, ZoneRepository]
    )
    zone_controller = obj_graph.provide(ZoneController)
    result = zone_controller.update_zone(zone_id, data)
    # logger.info(f'{result}')
    return handle_result(result)


def dist_between_two_lat_lon(*args):
    from math import asin, cos, radians, sin, sqrt

    lat1, lat2, long1, long2 = map(radians, args)

    dist_lats = abs(lat2 - lat1)
    dist_longs = abs(long2 - long1)
    a = sin(dist_lats / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dist_longs / 2) ** 2
    c = asin(sqrt(a)) * 2
    radius_earth = 6378
    return c * radius_earth


@location.route("/getNearbyLocation/<uuid:location_id>", methods=["POST"])
def get_nearby_Location(location_id):
    obj_graph = pinject.new_object_graph(
        modules=None, classes=[LocationController, LocationRepository]
    )
    location_controller = obj_graph.provide(LocationController)
    result = location_controller.get_nearby(location_id)
    data = Location.query.all()
    logger.info(f"{result}| {data}")
    logger.info(f"{LocationSchema().dumps(data)}")

    try:
        nearby_location = min(
            LocationSchema().dump(data),
            key=lambda p: dist_between_two_lat_lon(
                result["latitude"],
                result["latitude"],
                result["longitude"],
                result["longitude"],
            ),
        )
        result = {"data": {"locations": nearby_location}}
    except Exception as e:
        result = {"data": {"msg": "not found in db", "error": str(e)}}
    logger.info(f"{LocationSchema().dump(data)}")
    return handle_result(result)
