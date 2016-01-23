# example
# An example command line utility.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Jan 20 14:07:11 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: example.py [] benjamin@bengfort.com $

"""
An example command line utility.
"""

##########################################################################
## Imports
##########################################################################

import commis

from commis import Command
from commis import ConsoleProgram
from commis import color

##########################################################################
## An example Command
##########################################################################

class GreetingCommand(Command):

    name    = "greeting"
    help    = "an example command, delivers a greeting"
    args    = {
        ('-l', '--lang'): {
            'type': str,
            'default': 'english',
            'metavar': 'LANG',
            'choices': ['english', 'french', 'spanish', 'error'],
            'help': 'the language of the greeting',
        },
        'name': {
            'nargs': "+",
            'type': str,
            'help': 'the name to greet you by'
        }
    }

    def handle(self, args):
        """
        Greet each person by name.
        """
        salutation = {
            'french': 'Bonjour',
            'spanish': 'Hola',
            'english': 'Hello',
        }[args.lang.lower()]

        output = []
        for name in args.name:
            output.append("{} {}!".format(salutation, name))
        return "\n".join(output)

##########################################################################
## Utility Description
##########################################################################

DESCRIPTION = "Inspects the mimetype distribution of a directory."
EPILOG      = "Created for scientific purposes and not diagnostic ones."
COMMANDS    = [
    GreetingCommand,
]

##########################################################################
## The Example Console Utility
##########################################################################

class ExampleUtility(ConsoleProgram):

    description = color.format(DESCRIPTION, color.CYAN)
    epilog      = color.format(EPILOG, color.LIGHT_MAGENTA)
    version     = commis.__version__

    @classmethod
    def load(klass, commands=COMMANDS):
        utility = klass()
        for command in commands:
            utility.register(command)
        return utility


##########################################################################
## The Main Method
##########################################################################

if __name__ == '__main__':
    utility = ExampleUtility.load()
    utility.execute()
