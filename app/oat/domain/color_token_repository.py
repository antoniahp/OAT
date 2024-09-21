from abc import ABC, abstractmethod
from typing import List

from oat.domain.colors_token import ColorsToken


class ColorTokenRepository(ABC):
    @abstractmethod
    def get_colors_token(self) -> List[ColorsToken]:
        pass

    @abstractmethod
    def save_colors_token(self, colors_token: ColorsToken) -> None:
        pass