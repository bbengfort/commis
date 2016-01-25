# commis
# Create command line applications like Django management commands.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Jan 20 13:47:04 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Create command line applications like Django management commands.
"""

##########################################################################
## Imports
##########################################################################

from .program import ConsoleProgram
from .command import Command
from .labeled import LabelCommand
from .version import get_version
from .color   import colorize


##########################################################################
## Package Version
##########################################################################

__version__ = get_version()
