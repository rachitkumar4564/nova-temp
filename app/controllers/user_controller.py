from app.definitions.result import Result
from app.definitions.service_result import ServiceResult
from app.repositories.user_repository import UserRepository


class UserController:
    def create_user(self, user_data):
        user = UserRepository().create(obj_in=user_data)
        return ServiceResult(Result(user, status_code=200))
