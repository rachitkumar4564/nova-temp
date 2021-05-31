from marshmallow import fields
from app import ma


class LocationSchema(ma.Schema):
    name = fields.Str()
    longitude = fields.Float()
    latitude = fields.Float()
    full_address = fields.Str()
    modified = fields.DateTime()
    created = fields.DateTime()

    class Meta:
        fields = ("id", "name", "longitude", "latitude", "full_address")


class ZoneSchema(ma.Schema):
    name = fields.Str()
    wave_points = fields.Str()

    class Meta:
        fields = ("id", "name", "wave_points")


class ZoneLocationSchema(ma.Schema):
    id = fields.UUID()
    zone = fields.Nested(ZoneSchema)
    location = fields.Nested(LocationSchema)


class NestedSchema(ma.Schema):
    zone = fields.Nested(ZoneLocationSchema)
    location = fields.Nested(LocationSchema)
