# -*- coding: utf-8 -*-

from cliff.command import Command

__all__ = ['BaseCommand']


class BaseCommand(Command):
    def get_parser(self, prog_name):
        parser = super(BaseCommand, self).get_parser(prog_name)
        parser.add_argument('config')
        return parser
