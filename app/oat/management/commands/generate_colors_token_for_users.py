import random
from datetime import datetime, timedelta

from django.core.management import BaseCommand

from oat.application.color_token_command import ColorTokenCommand
from oat.application.color_token_command_handler import ColorTokenCommandHandler
from oat.domain.color_choices import ColorChoices
from oat.domain.colors_token import ColorsToken
from oat.domain.colors_token_creator import ColorTokenCreator
from oat.domain.pattern_choices import PatternChoices
from oat.domain.user import User
from oat.infraestructure.db_color_token_repository import DbColorTokenRepository
from oat.infraestructure.db_user_repository import DbUserRepository


class Command(BaseCommand):
    help = 'Generate colors token for users'
    def __init__(self):
        super().__init__()
        self.__color_token_creator = ColorTokenCreator()
        self.__db_token_repository = DbColorTokenRepository()
        self.__db_user_repository = DbUserRepository()
        self.__color_token_command_handler = ColorTokenCommandHandler(color_token_creator=self.__color_token_creator,
                                                                      color_token_repository=self.__db_token_repository,
                                                                      user_repository=self.__db_user_repository)



    def handle(self, *args, **options):
        command = ColorTokenCommand()
        self.__color_token_command_handler.handle(command)

