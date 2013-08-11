# -*- coding: utf-8 -*-

from cliff.app import App
from cliff.commandmanager import CommandManager


class CLIApp(App):
    def __init__(self):
        super(CLIApp, self).__init__(
            description="",
            version="",
            command_manager=CommandManager('pyramidbasic.scripts'),
            )


def main(argv=None):
    if argv is None:
        import sys
        argv = sys.argv[1:]
    return CLIApp().run(argv)


if __name__ == '__main__':
    sys.exit(main())
