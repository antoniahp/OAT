from abc import ABC, abstractmethod
from typing import List

from oat.domain.color_token_repository import ColorTokenRepository
from oat.domain.colors_token import ColorsToken


class DbColorTokenRepository(ColorTokenRepository):

    def get_colors_token(self) -> List[ColorsToken]:
        colors_token = ColorsToken.objects.all()
        return colors_token


    def save_colors_token(self, colors_token: ColorsToken) -> None:
        colors_token.save()