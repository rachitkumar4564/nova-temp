from app.definitions.repository_interfaces.zone_repository_interface import (
    ZoneRepositoryInterface,
)

from app.models import Zone
from .base import BaseRepository


class ZoneRepository(BaseRepository, ZoneRepositoryInterface):
    def __init__(self):
        super(ZoneRepository, self).__init__(model=Zone)
