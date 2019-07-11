# Welcome to Commis

Commis is a library to create command line utilities like `git` or `django-admin` where there is a single command that implements many subcommands. Internally, Commis uses the [argparse](https://docs.python.org/2.7/library/argparse.html) module to create subparsers and parse command line options. However, much like the [Django management utility](https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/), it exposes an API that allows you to write command classes and create very simple console programs.

## Getting Started

To install the Commis library, the simplest thing to do is use `pip` as follows:

    $ pip install commis

Alternatively, you can download the latest (development) version or clone directly from Github and install it using the `setup.py` script:

    $ git clone https://github.com/bbengfort/commis.git
    $ cd commis
    $ python setup.py install

## Writing Commands

Basically the way you create commands is to subclass the `Command` class, define its `name`, `help`, and `args` attributes, then implement a `handle` method. This more or less looks as follows:

```python
class GreetingCommand(Command):

    name    = "greeting"
    help    = "an example command, delivers a greeting"

    args    = {
        # Language selection option
        ('-l', '--lang'): {
            'type': str,
            'default': 'english',
            'metavar': 'LANG',
            'choices': ['english', 'french', 'spanish'],
            'help': 'the language of the greeting',
        },

        # List of one or more name arguments
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
```

The `args` is a Python dictionary of keyword arguments to be passed to `argparse.add_argument` and uses the same syntax. See [the add_argument method](https://argparse.googlecode.com/svn/trunk/doc/add_argument.html) for more details.

The `handle` method should accept args as its only argument, and should return a string to be printed to the command line.

## Writing a Console Program

Once you have your commands, you need to create and define a console utility to execute them. Simply subclass `ConsoleProgram` with your definition as follows:

```python
VERSION     = "1.0"
DESCRIPTION = "Inspects the mimetype distribution of a directory."
EPILOG      = "Created for scientific purposes and not diagnostic ones."
COMMANDS    = [
    GreetingCommand,
]

class ExampleUtility(ConsoleProgram):

    description = DESCRIPTION
    epilog      = EPILOG
    version     = VERSION

    @classmethod
    def load(klass, commands=COMMANDS):
        utility = klass()
        for command in commands:
            utility.register(command)
        return utility
```

The `ConsoleProgram` has a `register` method which allows you to register various commands. You can do this at run time, creating dynamic utilities with different commands, or you can explore a directory and load all commands from it. Here I just simply add a simple `load` static method to load the commands and instantiate the utility. Using the utility is then as simple as creating a script as follows:

```python
from example import ExampleUtility

if __name__ == '__main__':
    utility = ExampleUtility.load()
    utility.execute()
```

For more on writing console utilities and programs, check out the tutorial which follows.
