from app.definitions.repository_interfaces.location_repository_interface import (
    LocationRepositoryInterface,
)

from app.models import Location
from .base import BaseRepository


class LocationRepository(BaseRepository, LocationRepositoryInterface):
    def __init__(self):
        super(LocationRepository, self).__init__(model=Location)
