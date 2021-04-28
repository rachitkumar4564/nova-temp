from app.definitions.repository_interfaces.user_repository_interface import (
    UserRepositoryInterface,
)
from app.models.user import User
from .base import BaseRepository


class UserRepository(BaseRepository, UserRepositoryInterface):
    def __init__(self):
        super(UserRepository, self).__init__(model=User)
