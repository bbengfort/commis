# commis.exceptions
# Exceptions hierarchy for the commis library.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Jan 20 14:02:11 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: exceptions.py [] benjamin@bengfort.com $

"""
Exceptions hierarchy for the commis library.
"""

##########################################################################
## Exceptions
##########################################################################

class ConsoleError(Exception):
    """
    Base exception for exceptions that should be raised on the command line.
    """
    pass
