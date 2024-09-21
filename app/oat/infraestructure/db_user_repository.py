from abc import ABC, abstractmethod
from typing import List

from oat.domain.user import User
from oat.domain.user_repository import UserRepository


class DbUserRepository(UserRepository):

    def get_all_users(self) -> List[User]:
        users = User.objects.all()
        return users



    def save_user(self, user: User) -> None:
        user.save()