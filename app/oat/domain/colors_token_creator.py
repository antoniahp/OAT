from datetime import datetime

from oat.domain.colors_token import ColorsToken


class ColorTokenCreator:

    def create(self, user_id:int, first_color: str, second_color:str, date_start: datetime, date_end: datetime, pattern: str):
        return ColorsToken(
            user_id = user_id,
            first_color=first_color,
            second_color=second_color,
            date_start=date_start,
            date_end=date_end,
            pattern=pattern,
        )
