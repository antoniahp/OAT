from abc import ABC, abstractmethod
from typing import List

from oat.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass