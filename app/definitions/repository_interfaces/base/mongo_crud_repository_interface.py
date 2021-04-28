from abc import ABC

from app.definitions.repository_interfaces.base.crud_repository_interface import (
    CRUDRepository,
)


class MongoCRUDRepository(CRUDRepository, ABC):
    pass
