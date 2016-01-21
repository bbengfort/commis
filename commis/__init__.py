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

from .command import Command
from .program import ConsoleProgram
from .version import get_version
from .labeled import LabelCommand

##########################################################################
## Package Version
##########################################################################

__version__ = get_version()
