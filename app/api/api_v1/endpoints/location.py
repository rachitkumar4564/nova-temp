import pinject
from flask import Blueprint, request
from app.controllers import LocationController
from app.definitions.service_result import handle_result
from app.repositories import LocationRepository
from app.schema.location_schema import (
    LocationSchema,
    LocationCreateSchema,
    LocationUpdateSchema,
    LocationNearSchema,
)
from app.utils import validator

location = Blueprint("location", __name__)

obj_graph = pinject.new_object_graph(
    modules=None, classes=[LocationController, LocationRepository]
)

location_controller = obj_graph.provide(LocationController)


@location.route("/", methods=["POST"])
@validator(schema=LocationCreateSchema)
def create():
    """
    ---
    post:
      description: creates a new Location
      requestBody:
        required: true
        content:
            application/json:
                schema: LocationCreate
      responses:
        '201':
          description: returns a location
          content:
            application/json:
              schema: Location
      tags:
          - Location
    """
    data = request.json
    result = location_controller.create(data)
    return handle_result(result, schema=LocationSchema)


@location.route("/")
def get_all_location():
    """
    ---
    get:
      description: returns all locations
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: Location
      tags:
          - Location
    """
    result = location_controller.index()
    return handle_result(result, schema=LocationSchema, many=True)


@location.route("/<string:location_id>", methods=["PUT"])
@validator(schema=LocationUpdateSchema)
def update_location(location_id):
    """
    ---
    put:
      description: updates a location with id specified in path
      parameters:
        - in: path
          name: location_id   # Note the name is the same as in the path
          required: true
          schema:
            type: string
          description: The Location ID
      requestBody:
        required: true
        content:
            application/json:
                schema: LocationUpdate
      responses:
        '200':
          description: returns a location
          content:
            application/json:
              schema: location
      tags:
          - Location
    """

    data = request.json
    result = location_controller.update(location_id, data)
    return handle_result(result, schema=LocationUpdateSchema)


@location.route("/<string:location_id>", methods=["DELETE"])
def delete_location(location_id):
    """
    ---
    put:
      description: delete a location with id specified in path
      parameters:
        - in: path
          name: location_id   # Note the name is the same as in the path
          required: true
          schema:
            type: string
          description: The Location ID
      requestBody:
        required: true
        content:
            application/json:
                schema: LocationUpdate
      responses:
        '200':
          description: returns a location
          content:
            application/json:
              schema: location
      tags:
          - Location
    """

    # data = request.json
    result = location_controller.delete(location_id)

    return handle_result(result, schema=LocationSchema)


@location.route("/get_nearby_location", methods=["POST"])
def nearby_location():
    """
    ---
    post:
      description: find nearby location with id specified in path
      parameters:
        - in: path
          name: location_id   # Note the name is the same as in the path
          required: true
          schema:
            type: string
          description: The Location ID
      requestBody:
        required: true
        content:
            application/json:
                schema: LocationNearSchema
      responses:
        '200':
          description: returns a location
          content:
            application/json:
              schema: LocationNearSchema
      tags:
          - Location
    """
    data = request.json
    result = location_controller.get_nearby(data, schema=LocationSchema)

    return handle_result(result, schema=LocationNearSchema)
