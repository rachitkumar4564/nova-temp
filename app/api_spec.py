"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

# Create an APISpec
from app.schema import (
    LocationSchema,
    LocationUpdateSchema,
    LocationCreateSchema,
    ZoneSchema,
    ZoneUpdateSchema,
    LocationNearSchema,
)

spec = APISpec(
    title="Boilerplate project",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# register schemas with spec
spec.components.schema("Location", schema=LocationSchema)
spec.components.schema("LocationCreate", schema=LocationCreateSchema)
spec.components.schema("LocationUpdate", schema=LocationUpdateSchema)
spec.components.schema("NearByLocation", schema=LocationNearSchema)
spec.components.schema("Zone", schema=ZoneSchema)
# spec.components.schema("ZoneCreate", schema=ZoneSchema)
spec.components.schema("ZoneUpdate", schema=ZoneUpdateSchema)

# add swagger tags that are used for endpoint annotation
tags = [
    {"name": "Authentication", "description": "For user authentication."},
    {"name": "Location", "description": "Everything about Location"},
    {"name": "Zone", "description": "Everything about Zone"},
]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)
