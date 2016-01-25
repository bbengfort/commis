# commis.color
# Adds color to the console utility by wrapping colorama.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Jan 21 18:33:12 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: color.py [] benjamin@bengfort.com $

"""
Adds color to the console utility by wrapping colorama.
"""

##########################################################################
## Imports
##########################################################################

import colorama


##########################################################################
## Console Colors
##########################################################################

## Helpers for Colorama foreground colors
BLACK         = colorama.Fore.BLACK
RED           = colorama.Fore.RED
GREEN         = colorama.Fore.GREEN
YELLOW        = colorama.Fore.YELLOW
BLUE          = colorama.Fore.BLUE
MAGENTA       = colorama.Fore.MAGENTA
CYAN          = colorama.Fore.CYAN
WHITE         = colorama.Fore.WHITE
RESET         = colorama.Fore.RESET

## Non standard (but well supported)
LIGHT_BLACK   = colorama.Fore.LIGHTBLACK_EX
LIGHT_RED     = colorama.Fore.LIGHTRED_EX
LIGHT_GREEN   = colorama.Fore.LIGHTGREEN_EX
LIGHT_YELLOW  = colorama.Fore.LIGHTYELLOW_EX
LIGHT_BLUE    = colorama.Fore.LIGHTBLUE_EX
LIGHT_MAGENTA = colorama.Fore.LIGHTMAGENTA_EX
LIGHT_CYAN    = colorama.Fore.LIGHTCYAN_EX
LIGHT_WHITE   = colorama.Fore.LIGHTWHITE_EX

##########################################################################
## Helper Functions
##########################################################################

def colorize(string, color, *args, **kwargs):
    """
    Implements string formatting along with color specified in colorama.Fore
    """
    string = string.format(*args, **kwargs)
    return color + string + colorama.Fore.RESET

# Alias for colorize. Expected usage:
#   >>> from commis import color
#   >>> color.format("{}", color.BLUE, "hello world!")
format   = colorize
