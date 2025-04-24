from .models import User
from .dto import UserDTO


class UserRepository:
    @staticmethod
    def get_user_by_id(user_id: int) -> UserDTO:
        try:
            user = User.objects.get(pk=user_id)
            return UserDTO(id=user.id, name=user.name, email=user.email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_all_users() -> list[UserDTO]:
        users = User.objects.all()
        return [UserDTO(id=user.id, name=user.name, email=user.email) for user in users]
