from abc import ABC

from .base.crud_repository_interface import CRUDRepository


class LocationRepositoryInterface(CRUDRepository, ABC):
    pass
