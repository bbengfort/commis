# Commis

**Create command line applications like Django management commands.**

[![Build Status](https://travis-ci.org/bbengfort/commis.svg?branch=master)](https://travis-ci.org/bbengfort/commis)
[![Coverage Status](https://coveralls.io/repos/github/bbengfort/commis/badge.svg?branch=master)](https://coveralls.io/github/bbengfort/commis?branch=master)
[![PyPI version](https://badge.fury.io/py/commis.svg)](https://badge.fury.io/py/commis)
[![Documentation Status](https://readthedocs.org/projects/commis/badge/?version=latest)](http://commis.readthedocs.org/en/latest/?badge=latest)
[![Stories in Ready](https://badge.waffle.io/bbengfort/commis.png?label=ready&title=Ready)](https://waffle.io/bbengfort/commis)

[![Pâte de fruit (gominolas) de laranxa sanguina][gominolas.jpg]][gominolas_flickr]

Read the full documentation at [http://commis.readthedocs.org/](http://commis.readthedocs.org/).

## Getting Started

To install the Commis library, the simplest thing to do is use `pip` as follows:

    $ pip install commis

Alternatively, you can download the latest (development) version or clone directly from Github and install it using the `setup.py` script:

    $ git clone https://github.com/bbengfort/commis.git
    $ cd commis
    $ python setup.py install

### Writing Commands

There is a bit more detail in the full documentation, but basically the way you create commands is to subclass the `Command` class, define its `name`, `help`, and `args` attributes, then implement a `handle` method. This more or less looks as follows:

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

### Writing a Console Program

Once you have your commands, you need to create and define a console utility to execute them. Simply subclass `ConsoleProgram` with your definition as follows:

```python
DESCRIPTION = "Inspects the mimetype distribution of a directory."
EPILOG      = "Created for scientific purposes and not diagnostic ones."
COMMANDS    = [
    GreetingCommand,
]

class ExampleUtility(ConsoleProgram):

    description = DESCRIPTION
    epilog      = EPILOG
    version     = commis.__version__

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

For more on writing console utilities and programs, check out the documentation at [http://commis.readthedocs.org/](http://commis.readthedocs.org/).

## About

I'm not sure why this doesn't exist yet, but I needed a library for creating command line utilities that wrapped the `argparse` library. Most of the ones I found used a decorator based syntax; but I really do like the Django management commands style of creating applications. Therefore, this library serves to give you the ability to do so!

### Contributing

Commis is open source, and I would be happy to have you contribute! You can contribute in the following ways:

1. Create a pull request in Github: [https://github.com/bbengfort/commis](https://github.com/bbengfort/commis)
2. Add issues or bugs on the bug tracker: [https://github.com/bbengfort/commis/issues](https://github.com/bbengfort/commis/issues)
3. Checkout the current dev board on waffle.io: [https://waffle.io/bbengfort/commis](https://waffle.io/bbengfort/commis)

Note that labels in the Github issues are defined in the blog post: [How we use labels on GitHub Issues at Mediocre Laboratories](https://mediocre.com/forum/topics/how-we-use-labels-on-github-issues-at-mediocre-laboratories).

If you've contributed a fair amount, I'll give you direct access to the repository, which is set up in a typical production/release/development cycle as described in _[A Successful Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/)_. A typical workflow is as follows:

1. Select a card from the [dev board](https://waffle.io/bbengfort/commis) - preferably one that is "ready" then move it to "in-progress".

2. Create a branch off of develop called "feature-[feature name]", work and commit into that branch.

        ~$ git checkout -b feature-myfeature develop

3. Once you are done working (and everything is tested) merge your feature into develop.

        ~$ git checkout develop
        ~$ git merge --no-ff feature-myfeature
        ~$ git branch -d feature-myfeature
        ~$ git push origin develop

4. Repeat. Releases will be routinely pushed into master via release branches, then deployed to the server.

Note that pull requests will be reviewed when the Travis-CI tests pass, so including tests with your pull request is ideal!

You can contact me on Twitter if needed: [@bbengfort](https://twitter.com/bbengfort)

### Name Origin
<big>com &middot; mis</big><br />
/ˈkämē,kô-/<br/>
*noun* a junior chef.

Origin<br />
[Latin] *committere*: 1930s: from French, 'deputy, clerk', past participle of commettre 'entrust', from Latin.<br \>

A commis is a basic chef in larger kitchens who works under a chef de partie to learn the station's or range's responsibilities and operation.[3] This may be a chef who has recently completed formal culinary training or is still undergoing training. &mdash; [Wikipedia](https://en.wikipedia.org/wiki/Chef#Commis_.28Chef.29_.2F_Range_chef)

This package is closely related to the [Confire](https://github.com/bbengfort/confire) configuration tool, hence the name in the same vein &mdash; French cooking words. In this case, a commis is someone to whom orders are given (commands) and seemed an appropriate term for a package whose function is accept and execute commands.

### Attribution

The photo used in this README, &ldquo;[Pâte de fruit (gominolas) de laranxa sanguina][gominolas_flickr]&rdquo; by [Receitasparatodososdias](https://www.flickr.com/photos/100127130@N05/) is used under a [CC BY-NC-ND 2.0](https://creativecommons.org/licenses/by-nc-nd/2.0/) creative commons license.

### Throughput

[![Throughput Graph](https://graphs.waffle.io/bbengfort/commis/throughput.svg)](https://waffle.io/bbengfort/commis/metrics)

## Changelog

The release versions that are sent to the Python package index are also tagged in Github. You can see the tags through the Github web application and download the tarball of the version you'd like. Additionally PyPI will host the various releases of commis.

The versioning uses a three part version system, "a.b.c" - "a" represents a major release that may not be backwards compatible. "b" is incremented on minor releases that may contain extra features, but are backwards compatible. "c" releases are bug fixes or other micro changes that developers should feel free to immediately update to.

### Milestone 0.3

This milestone will add Python 3 compatibility as well as new features like Confire integration and progress bars. Work for this milestone hasn't been set yet, so please feel to contribute issues and ideas!

### Version 0.2

* **tag**: v0.2
* **deployment**: January 25, 2016
* **commit**: [90e2275](https://github.com/bbengfort/commis/commit/90e2275214f23d9da4e9e632df88c052bb890389)

Solidified the Commis library by improving the test suite and the documentation. I've also included a couple of modules that were big helps in the past: a color library that wraps colorama, and a LabelCommand. This is really the official "first" version that I feel is production ready.

### Version 0.1

* **tag**: v0.1
* **deployment**: January 20, 2016
* **commit**: [35ca6df](https://github.com/bbengfort/commis/commit/35ca6df11a51503b50466c7ec2b0c44103778802)

This is the initial release, which will simply bring over all the code and features that have previously been implemented in other locations. This release has also been published to PyPI and has some initial documentation.

<!-- References -->
[gominolas.jpg]: docs/img/gominolas.jpg
[gominolas_flickr]: https://flic.kr/p/mcSxAK
