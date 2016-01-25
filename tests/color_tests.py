# tests.color_tests
# Testing the color package in commis.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jan 22 16:03:34 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: color_tests.py [] benjamin@bengfort.com $

"""
Testing the color package in commis.
"""

##########################################################################
## Imports
##########################################################################

import colorama
import unittest

from commis import color

##########################################################################
## Color Fixtures
##########################################################################

colors = (
    # (commis (cm), colorama (cr)) pairs
    (color.BLACK, colorama.Fore.BLACK),
    (color.RED, colorama.Fore.RED),
    (color.GREEN, colorama.Fore.GREEN),
    (color.YELLOW, colorama.Fore.YELLOW),
    (color.BLUE, colorama.Fore.BLUE),
    (color.MAGENTA, colorama.Fore.MAGENTA),
    (color.CYAN, colorama.Fore.CYAN),
    (color.WHITE, colorama.Fore.WHITE),
    (color.RESET, colorama.Fore.RESET),
    (color.LIGHT_BLACK, colorama.Fore.LIGHTBLACK_EX),
    (color.LIGHT_RED, colorama.Fore.LIGHTRED_EX),
    (color.LIGHT_GREEN, colorama.Fore.LIGHTGREEN_EX),
    (color.LIGHT_YELLOW, colorama.Fore.LIGHTYELLOW_EX),
    (color.LIGHT_BLUE, colorama.Fore.LIGHTBLUE_EX),
    (color.LIGHT_MAGENTA, colorama.Fore.LIGHTMAGENTA_EX),
    (color.LIGHT_CYAN, colorama.Fore.LIGHTCYAN_EX),
    (color.LIGHT_WHITE, colorama.Fore.LIGHTWHITE_EX),
)

##########################################################################
## Color Tests
##########################################################################

class ColorTests(unittest.TestCase):
    """
    Tests the commis.color module as simply as possible.
    """

    def setUp(self):
        """
        Call colorama's init to setup stdout and stderr
        """
        colorama.init()

    def tearDown(self):
        """
        Tear down coloroma's stdout and sterr and go back to defaults.
        """
        colorama.deinit()

    def test_color_matches(self):
        """
        Assert color parity with colorma
        """

        for cm, cr in colors:
            self.assertEqual(
                cm, cr, "Color mismatch with colorama: {} vs {}".format(cm, cr)
            )

    def test_colorize_function(self):
        """
        Test the string format with colorize and kwargs.
        """
        templ  = "It will cost you ${amt:0.2f} to purchase the {item}."
        kwargs = {"amt": 19.993, "item": "cookie press"}
        render = templ.format(**kwargs)

        for cm, cr in colors:
            expected = cr + render + colorama.Fore.RESET
            self.assertEqual(color.colorize(templ, cm, **kwargs), expected)

    def test_colorize_alias(self):
        """
        Assert that there is a colorize alias and use args instead of kwargs.
        """
        templ  = "It will cost you ${:0.2f} to purchase the {}."
        args   = (19.993, "cookie press")
        render = templ.format(*args)

        for cm, cr in colors:
            expected = cr + render + colorama.Fore.RESET
            self.assertEqual(color.format(templ, cm, *args), expected)
