# tests
# Testing for the Commis library
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Jan 20 13:47:12 2016 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the Mosaic file system usage analysis utility
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Module Constants
##########################################################################

TEST_VERSION = "0.5" ## Also the expected version onf the package

##########################################################################
## Test Cases
##########################################################################

class InitializationTest(unittest.TestCase):

    def test_initialization(self):
        """
        Tests a simple world fact by asserting that 10**2 is 100.
        """
        self.assertEqual(10**2, 100)

    def test_import(self):
        """
        Can import commis
        """
        try:
            import commis
        except ImportError:
            self.fail("Unable to import the commis module!")

    def test_version(self):
        """
        Assert that the version is sane
        """
        import commis
        self.assertEqual(TEST_VERSION, commis.__version__)
