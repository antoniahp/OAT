from datetime import datetime, timedelta
import random

from cqrs.commands.command_handler import CommandHandler
from oat.application.color_token_command import ColorTokenCommand
from oat.domain.color_choices import ColorChoices
from oat.domain.color_token_repository import ColorTokenRepository
from oat.domain.colors_token import ColorsToken
from oat.domain.colors_token_creator import ColorTokenCreator
from oat.domain.pattern_choices import PatternChoices
from oat.domain.user_repository import UserRepository


class ColorTokenCommandHandler(CommandHandler):
    def __init__(self, color_token_creator: ColorTokenCreator, color_token_repository: ColorTokenRepository, user_repository: UserRepository):
        self.__color_token_creator = color_token_creator
        self.__color_token_repository = color_token_repository
        self.__user_repository = user_repository

    def handle(self, command: ColorTokenCommand):
        now = datetime.now()
        users = self.__user_repository.get_all_users()
        for user in users:
            date_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            date_end = date_start + timedelta(minutes=1)
            for _ in range(1439):
                first_color = random.choice(ColorChoices.choices)[0]
                second_color = random.choice(ColorChoices.choices)[0]
                pattern = random.choice(PatternChoices.choices)[0]
                color_token = ColorsToken.objects.create(
                    first_color=first_color,
                    second_color=second_color,
                    pattern=pattern,
                    date_start=date_start,
                    date_end=date_end,
                    user=user
                )
                date_start = date_start + timedelta(minutes=1)
                date_end = date_end + timedelta(minutes=1)

                self.__color_token_repository.save_colors_token(color_token)




