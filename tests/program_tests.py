# tests.program_tests
# Testing the primary console utility for commis.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jan 22 17:24:41 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: program_tests.py [] benjamin@bengfort.com $

"""
Testing the primary console utility for commis.
"""

##########################################################################
## Imports
##########################################################################

import sys
import six
import argparse
import unittest

from commis.command import Command
from commis.command import DefaultParser
from commis.program import handle_default_args
from commis.program import ConsoleProgram
from commis.exceptions import ConsoleError

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from unittest import mock
except ImportError:
    import mock

##########################################################################
## Helper Function Tests
##########################################################################

class HelperFunctionTests(unittest.TestCase):
    """
    Tests the `commis.program` functions library
    """

    def test_handle_default_args(self):
        """
        Assert that the --pythonpath argument changes sys.path
        """
        parser = argparse.ArgumentParser(parents=[DefaultParser()])
        args = parser.parse_args(['--traceback', '--pythonpath', '/tmp/lib/mypy'])

        # Handle the default arguments
        handle_default_args(args)

        # Ensure that the path is modified.
        self.assertIn('/tmp/lib/mypy', sys.path)

    def test_no_path_modification(self):
        """
        Ensure that sys.path remains unchanged after defaults.
        """
        parser = argparse.ArgumentParser(parents=[DefaultParser()])
        args = parser.parse_args([])

        oldpath = list(sys.path)

        # Handle the default arguments
        handle_default_args(args)

        # Ensure that the path is unmodified.
        self.assertEqual(oldpath, sys.path)

##########################################################################
## An example utility with a single command
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

class ExampleUtility(ConsoleProgram):

    description = "example utility"
    epilog      = "the ending"
    version     = "1.0"

    @classmethod
    def load(klass, commands=[GreetingCommand]):
        utility = klass()
        for command in commands:
            utility.register(command)
        return utility

##########################################################################
## ConsoleProgram Tests
##########################################################################

class ConsoleProgramTests(unittest.TestCase):
    """
    Tests the `ConsoleProgram` class as simply as possible.
    """

    def setUp(self):
        """
        Redirect stdout and stderr to a StringIO
        """
        self.out, sys.stdout = sys.stdout, StringIO()
        self.err, sys.stderr = sys.stderr, StringIO()

    def tearDown(self):
        """
        Replace stdout and stderr with original streams
        """
        sys.stdout = self.out
        sys.stderr = self.err

    def read(self, stream):
        """
        Returns the contents of the StringIO specified.
        """
        if isinstance(stream, six.string_types):
            stream = {
                'stdout': sys.stdout,
                'stderr': sys.stderr,
            }[stream]

        stream.seek(0)
        return stream.read()

    def test_command_registration(self):
        """
        Ensure that a command can be added to a program correctly.
        """
        utility = ConsoleProgram()
        utility.register(GreetingCommand)

        self.assertIn(GreetingCommand.name, utility.commands)
        self.assertIsNotNone(utility.commands[GreetingCommand.name].parser)

    def test_duplicate_command_registration(self):
        """
        Ensure a command cannot be registered twice.
        """
        utility = ConsoleProgram()
        utility.register(GreetingCommand)

        with self.assertRaises(ConsoleError):
            utility.register(GreetingCommand)

    def test_good_exit_without_parser(self):
        """
        Test the exit of the process without a parser.
        """
        utility = ConsoleProgram()

        with self.assertRaises(SystemExit) as cm:
            utility.exit(0)

        self.assertEqual(cm.exception.code, 0)

    def test_bad_exit_without_parser(self):
        """
        Test the error exit of the process without a parser.
        """
        utility = ConsoleProgram()

        with self.assertRaises(SystemExit) as cm:
            utility.exit(1)

        self.assertEqual(cm.exception.code, 1)

    def test_good_exit_message_without_parser(self):
        """
        Check stdout, stderr value on a good exit
        """
        utility = ConsoleProgram()

        with self.assertRaises(SystemExit) as cm:
            utility.exit(0, "good")

        self.assertEqual("good", self.read('stdout'))
        self.assertEqual("", self.read('stderr'))

    def test_bad_exit_message_without_parser(self):
        """
        Check stdout, stderr value on a error exit
        """
        utility = ConsoleProgram()

        with self.assertRaises(SystemExit) as cm:
            utility.exit(1, "brimstone!")

        self.assertEqual("", self.read('stdout'))
        self.assertEqual("brimstone!", self.read('stderr'))

    def test_good_exit_with_parser(self):
        """
        Check that good exit is passed to the parser
        """
        # Setup the utility and register a command (forces parser creation)
        utility = ConsoleProgram()
        utility.register(GreetingCommand)

        # Mock the parser exit/error functions
        utility.parser.error = mock.MagicMock()
        utility.parser.error.side_effect = lambda m: sys.exit(1)
        utility.parser.exit = mock.MagicMock()
        utility.parser.exit.side_effect = lambda c,m: sys.exit(0)

        # Perform a good exit
        with self.assertRaises(SystemExit) as cm:
            utility.exit(0, "good")

        # Check the exit status
        self.assertEqual(cm.exception.code, 0)
        utility.parser.error.assert_not_called()
        utility.parser.exit.assert_called_once_with(0, "good")


    def test_bad_exit_with_parser(self):
        """
        Check that a bad exit is passed to the parser
        """
        # Setup the utility and register a command (forces parser creation)
        utility = ConsoleProgram()
        utility.register(GreetingCommand)

        # Mock the parser exit/error functions
        utility.parser.error = mock.MagicMock()
        utility.parser.error.side_effect = lambda m: sys.exit(1)
        utility.parser.exit = mock.MagicMock()
        utility.parser.exit.side_effect = lambda c,m: sys.exit(0)

        # Perform a bad exit
        with self.assertRaises(SystemExit) as cm:
            utility.exit(1, "brimstone!")

        # Check the exit status
        self.assertEqual(cm.exception.code, 1)
        utility.parser.error.assert_called_once_with("brimstone!")
        utility.parser.exit.assert_not_called()

    def test_execution_no_commands(self):
        """
        Assert a utility requires commands on execution
        """
        # Create the utility and mock the exit
        utility = ConsoleProgram()

        # Execute the utility without registering commands
        with self.assertRaises(NotImplementedError):
            utility.execute()

    def test_handle_defaults_on_execution(self):
        """
        Assert handle default args is called on execute
        """
        # Create the utility and register a command
        utility = ConsoleProgram()
        utility.register(GreetingCommand)

        # Create fake arguments for the parser
        args = utility.parser.parse_args(["greeting", "bob", '--pythonpath', '/tmp/var/mypy'])

        # Mock the exit, handler and parser
        utility.exit = mock.MagicMock()
        utility.parser.parse_args = mock.MagicMock(return_value=args)

        # Execute the command
        utility.execute()

        # Check the execution status
        self.assertIn('/tmp/var/mypy', sys.path)

    def test_good_execution(self):
        """
        Assert a utility requires commands on execution
        """
        # Create the utility and register a command
        utility = ConsoleProgram()
        GreetingCommand.handle = mock.MagicMock(return_value="Hello Bob!")
        utility.register(GreetingCommand)

        # Create fake arguments for the parser
        args = utility.parser.parse_args(["greeting", "bob"])

        # Mock the exit, handler and parser
        utility.exit = mock.MagicMock()
        utility.parser.parse_args = mock.MagicMock(return_value=args)

        # Execute the command
        utility.execute()

        # Check the execution status
        utility.commands['greeting'].handle.assert_called_once_with(args)
        utility.exit.assert_called_once_with(0, "Hello Bob!\n")

    def test_error_execution(self):
        """
        Assert a utility requires commands on execution
        """
        # Create the utility and register a command
        utility = ConsoleProgram()
        GreetingCommand.handle = mock.MagicMock(side_effect=ValueError("bad"))
        utility.register(GreetingCommand)

        # Create fake arguments for the parser
        args = utility.parser.parse_args(["greeting", "bob"])

        # Mock the exit and parser
        utility.exit = mock.MagicMock()
        utility.parser.parse_args = mock.MagicMock(return_value=args)

        # Execute the utility
        utility.execute()

        # Check the execution status
        utility.exit.assert_called_once_with(1, '\x1b[31mbad\x1b[39m')
        self.assertEqual("", self.read("stdout"))
        self.assertEqual("", self.read("stderr"))

    def test_traceback_execution(self):
        """
        Assert a utility requires commands on execution
        """
        # Create the utility and register a command
        utility = ConsoleProgram()
        GreetingCommand.handle = mock.MagicMock(side_effect=ValueError("bad"))
        utility.register(GreetingCommand)

        # Create fake arguments for the parser
        args = utility.parser.parse_args(["greeting", "bob", '--traceback'])

        # Mock the exit and parser
        utility.exit = mock.MagicMock()
        utility.parser.parse_args = mock.MagicMock(return_value=args)

        # Execute the utility
        utility.execute()

        # Check the execution status
        utility.exit.assert_called_once_with(1, '\x1b[31mbad\x1b[39m')
        self.assertEqual("", self.read("stdout"))
        self.assertIn("ValueError", self.read("stderr"))
