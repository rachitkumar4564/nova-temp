from app.definitions.repository_interfaces.location_repository_interface import (
    LocationRepositoryInterface,
    ZoneRepositoryInterface,
)

from app.models.location import Location, Zone
from .base import BaseRepository


class LocationRepository(BaseRepository, LocationRepositoryInterface):
    def __init__(self):
        super(LocationRepository, self).__init__(model=Location)


class ZoneRepository(BaseRepository, ZoneRepositoryInterface):
    def __init__(self):
        super(ZoneRepository, self).__init__(model=Zone)
