from marshmallow import Schema, fields


class ZoneSchema(Schema):
    id = fields.UUID()
    name = fields.Str()
    wave_points = fields.Float()
    modified = fields.DateTime()
    created = fields.DateTime()

    class Meta:
        fields = ("id", "name", "wave_points", "modified", "created")


class ZoneCreateSchema(Schema):
    id = fields.UUID()
    name = fields.Str(required=True)
    wave_points = fields.Float(required=True)

    class Meta:
        fields = ("name", "wave_points")


class ZoneUpdateSchema(Schema):
    name = fields.Str()
    wave_points = fields.Float()

    class Meta:
        fields = (
            "name",
            "wave_points",
        )
