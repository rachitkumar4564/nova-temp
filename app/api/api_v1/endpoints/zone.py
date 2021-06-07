import pinject
from flask import Blueprint, request
from app.controllers import ZoneController
from app.definitions.service_result import handle_result
from app.repositories import ZoneRepository
from app.schema import (
    ZoneSchema,
    ZoneCreateSchema,
    ZoneUpdateSchema,
)
from app.utils import validator

zone = Blueprint("zone", __name__)
obj_graph = pinject.new_object_graph(
    modules=None, classes=[ZoneController, ZoneRepository]
)
zone_controller = obj_graph.provide(ZoneController)


@zone.route("/", methods=["POST"])
@validator(schema=ZoneCreateSchema)
def create_zone_request():
    """
    ---
    post:
      description: creates a new zone
      requestBody:
        required: true
        content:
            application/json:
                schema: Zone
      responses:
        '201':
          description: returns a zone
          content:
            application/json:
              schema: Zone
      tags:
          - Zone
    """
    data = request.json
    result = zone_controller.create(data)
    return handle_result(result, schema=ZoneSchema)


@zone.route("/")
def get_all_zone():
    """
    ---
    get:
      description: returns all zones
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: Zone
      tags:
          - Zone
    """
    result = zone_controller.index()
    return handle_result(result, schema=ZoneSchema, many=True)


@zone.route("/<uuid:zone_id>", methods=["PUT"])
@validator(schema=ZoneUpdateSchema)
def update_zone(zone_id):
    """
    ---
    put:
      description: updates a catalog with id specified in path
      parameters:
        - in: path
          name: zone_id   # Note the name is the same as in the path
          required: true
          schema:
            type: string
          description: The zone ID
      requestBody:
        required: true
        content:
            application/json:
                schema: ZoneUpdate
      responses:
        '200':
          description: returns a product
          content:
            application/json:
              schema: Zone
      tags:
          - Zone
    """

    data = request.json
    result = zone_controller.update(zone_id, data)
    return handle_result(result, schema=ZoneSchema)
