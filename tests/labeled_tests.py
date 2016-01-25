# tests.labeled_tests
# Testing the labeled command package for commis.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jan 22 16:33:51 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: labeled_tests.py [] benjamin@bengfort.com $

"""
Testing the labeled command package for commis.
"""

##########################################################################
## Imports
##########################################################################

import argparse
import unittest

from commis.labeled import LabelCommand

try:
    from unittest import mock
except ImportError:
    import mock

##########################################################################
## An example Command
##########################################################################

class GreetingCommand(LabelCommand):

    name    = "greeting"
    help    = "an example command, delivers a greeting"
    label   = "name"
    args    = {
        ('-l', '--lang'): {
            'type': str,
            'default': 'english',
            'metavar': 'LANG',
            'choices': ['english', 'french', 'spanish'],
            'help': 'the language of the greeting',
        },
    }

    def handle_label(self, name, args):
        return "{}-{}".format(name.lower(), args.lang[:2])


##########################################################################
## Command Tests
##########################################################################

class LabelCommandTests(unittest.TestCase):
    """
    Tests the `LabelCommand` class as simply as possible.
    """

    def test_handle_interface(self):
        """
        Assert that handle_label raises an interface error.
        """
        with self.assertRaises(NotImplementedError):
            cmd = LabelCommand()
            cmd.handle_label({})

    def test_add_label_argument(self):
        """
        Test the default addition of the label.
        """
        cmd = LabelCommand(label="foo")

        # Create subparsers
        primary = argparse.ArgumentParser()
        subparsers = primary.add_subparsers()

        # Create the parser
        parser = cmd.create_parser(subparsers)
        args = parser.parse_args(['baz', 'bar', 'biz', 'byr'])

        self.assertEqual(args.labels, ['baz', 'bar', 'biz', 'byr'])

    def test_handle_label_calls(self):
        """
        Assert handle_label is called for every argument.
        """
        cmd = LabelCommand(label="foo")

        # Mock the laberl command
        cmd.handle_label = mock.MagicMock(return_value="b")

        # Create subparsers
        primary = argparse.ArgumentParser()
        subparsers = primary.add_subparsers()

        # Create the parser
        parser = cmd.create_parser(subparsers)
        labels = ['baz', 'bar', 'biz', 'byr']
        args   = parser.parse_args(labels)

        # Call the handle method with the args
        output = cmd.handle(args)

        # Assert the mock method was called
        self.assertEqual(cmd.handle_label.call_count, len(labels))

        # Assert the mock was called with each label and args
        cmd.handle_label.assert_has_calls([
            mock.call(label, args)
            for label in labels
        ])

        # Check output is the newline joined string values
        self.assertEqual(output, "b\nb\nb\nb")

    def test_label_command_fixture(self):
        """
        Test the label command fixture
        """
        cmd = GreetingCommand()

        # Create subparsers
        primary = argparse.ArgumentParser()
        subparsers = primary.add_subparsers()

        # Create the parser
        parser = cmd.create_parser(subparsers)
        args = parser.parse_args(['--lang', 'french', 'jean', 'franc'])

        self.assertEqual(args.lang, 'french')
        self.assertEqual(args.labels, ['jean', 'franc'])

        output = cmd.handle(args)
        self.assertEqual(output, "jean-fr\nfranc-fr")
