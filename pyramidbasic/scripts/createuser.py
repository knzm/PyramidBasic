# -*- coding: utf-8 -*-

from getpass import getpass

import transaction

from .base import BaseCommand

from pyramid.paster import (
    bootstrap,
    setup_logging,
    )

from pyramidbasic.models import DBSession, UserModel

__all__ = ['CreateUserCommand']


class CreateUserCommand(BaseCommand):
    """Create user"""

    def take_action(self, parsed):
        env = bootstrap(parsed.config)
        setup_logging(parsed.config)

        username = raw_input('user_name: ')
        password = getpass('password: ')
        password2 = getpass('confirm password: ')
        if password != password2:
            raise RuntimeError("not match")

        with transaction.manager:
            user = UserModel(username=username)
            user.password = password
            DBSession.add(user)

        print("Successfully created.")
