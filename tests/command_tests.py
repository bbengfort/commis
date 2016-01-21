# tests.command_tests
# Testing the base command package for commis.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Jan 21 17:53:18 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: command_tests.py [] benjamin@bengfort.com $

"""
Testing the base command package for commis.
"""

##########################################################################
## Imports
##########################################################################

import argparse
import unittest


from commis.command import Command
from commis.command import DefaultParser

##########################################################################
## Defaults Parser Tests
##########################################################################

class DefaultsParserTests(unittest.TestCase):
    """
    Tests the `DefaultParser` class as simply as possible.
    """

    def test_create_parser(self):
        """
        Create an argument parser with default arguments.
        """
        parser = argparse.ArgumentParser(parents=[DefaultParser()])
        args = parser.parse_args(['--traceback', '--pythonpath', '/var/lib/mypy'])

        # Ensure default arguments are present
        self.assertIn('traceback', args)
        self.assertIn('pythonpath', args)


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
            'choices': ['english', 'french', 'spanish'],
            'help': 'the language of the greeting',
        },
        'name': {
            'nargs': "+",
            'type': str,
            'help': 'the name to greet you by'
        }
    }


##########################################################################
## Command Tests
##########################################################################

class CommandTests(unittest.TestCase):
    """
    Tests the `Command` class as simply as possible.
    """

    def test_handle_interface(self):
        """
        Assert that handle raises an interface error.
        """
        with self.assertRaises(NotImplementedError):
            cmd = Command()
            cmd.handle({})

    def test_empty_create_parser(self):
        """
        Can create an empty command parser.
        """
        cmd = Command()
        self.assertIsNone(cmd.parser)

        # Create subparsers
        primary = argparse.ArgumentParser()
        subparsers = primary.add_subparsers()

        # Create the parser
        parser = cmd.create_parser(subparsers)
        self.assertIsNotNone(cmd.parser)

        args = parser.parse_args([])
        self.assertEqual(args.func, cmd.handle)

    def test_add_argument_failure(self):
        """
        Assert error on adding args without a parser.
        """
        with self.assertRaises(TypeError):
            cmd = Command()
            cmd.add_arguments()

    def test_add_arguments(self):
        """
        Testing adding arguments specified to command.
        """
        args    = {
            ('-l', '--lang'): {
                'type': str,
                'default': 'english',
                'metavar': 'LANG',
                'choices': ['english', 'french', 'spanish'],
                'help': 'the language of the greeting',
            },
            'name': {
                'nargs': "+",
                'type': str,
                'help': 'the name to greet you by'
            }
        }

        cmd = Command(args=args)

        # Create subparsers
        primary = argparse.ArgumentParser()
        subparsers = primary.add_subparsers()

        # Create the parser
        parser = cmd.create_parser(subparsers)
        args = parser.parse_args(['--lang', 'french', 'jean', 'franc'])

        self.assertEqual(args.lang, 'french')
        self.assertEqual(args.name, ['jean', 'franc'])

    def test_command_fixture(self):
        """
        Test the command fixture from the example
        """
        cmd = GreetingCommand()
        self.assertEqual(cmd.help, "an example command, delivers a greeting")
        self.assertEqual(cmd.name, "greeting")

        # Create subparsers
        primary = argparse.ArgumentParser()
        subparsers = primary.add_subparsers()

        # Create the parser
        parser = cmd.create_parser(subparsers)
        args = parser.parse_args(['--lang', 'french', 'jean', 'franc'])

        self.assertEqual(args.lang, 'french')
        self.assertEqual(args.name, ['jean', 'franc'])
