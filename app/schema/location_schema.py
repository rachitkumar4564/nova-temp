from marshmallow import Schema, fields
from .zone_schema import ZoneCreateSchema


class LocationSchema(Schema):
    id = fields.UUID()
    name = fields.Str()
    longitude = fields.Float()
    latitude = fields.Float()
    full_address = fields.Str()
    zone_id = fields.UUID()
    modified = fields.DateTime()
    created = fields.DateTime()
    zone = fields.Nested(ZoneCreateSchema)

    class Meta:
        fields = [
            "id",
            "name",
            "longitude",
            "latitude",
            "full_address",
            "zone",
            "created",
            "modified",
        ]


class LocationCreateSchema(Schema):
    name = fields.Str(required=True)
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
    full_address = fields.Str(required=True)
    zone_id = fields.UUID(required=True)

    class Meta:
        fields = ["name", "longitude", "latitude", "full_address", "zone_id"]


class LocationUpdateSchema(Schema):
    name = fields.Str()
    longitude = fields.Float()
    latitude = fields.Float()
    full_address = fields.Str()
    zone_id = fields.UUID()

    class Meta:
        fields = ["name", "longitude", "latitude", "full_address", "zone_id"]


class LocationNearSchema(Schema):
    name = fields.Str()
    longitude = fields.Float()
    latitude = fields.Float()
    full_address = fields.Str()
    # zone_id = fields.UUID()

    class Meta:
        fields = [
            "longitude",
            "latitude",
        ]
