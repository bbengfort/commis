# `commis`

The `commis` module aggregates Commis' most used comonents into a single namespace for convenience. You can of course also access everything via their actual submodules. However, for the most part, submodules are just code organizational guidelines.

## Components

The following tables outline a rough sketch of the components involved in Commis. Use this guide to plan development or to find tools that are not explicitly referenced in the documentation.

### Color

The color module wraps [colorama](https://pypi.python.org/pypi/colorama) to provide cross-platform colored terminal text. While not strictly necessary, we have decided to integrate it into `commis` to set this CLI library apart from others. Plus we routinely integrate colors into our console utilities.

Component  | Description
---------- | -------------------------------------------------------------
`colorize` | Implements string formatting and colors the string with specified ANSI color.
`format`   | Alias for `colorize`. Expected usage is to import the color module (`color.format`)
`BLACK`/`LIGHT_BLACK` | Alias for `colorama.Fore.BLACK` and `colorama.Fore.LIGHTBLACK_EX`
`RED`/`LIGHT_RED` | Alias for `colorama.Fore.RED` and `colorama.Fore.LIGHTRED_EX`
`GREEN`/`LIGHT_GREEN` | Alias for `colorama.Fore.GREEN` and `colorama.Fore.LIGHTGREEN_EX`
`YELLOW`/`LIGHT_YELLOW` | Alias for `colorama.Fore.YELLOW` and `colorama.Fore.LIGHTYELLOW_EX`
`BLUE`/`LIGHT_BLUE` | Alias for `colorama.Fore.BLUE` and `colorama.Fore.LIGHTBLUE_EX`
`MAGENTA`/`LIGHT_MAGENTA` | Alias for `colorama.Fore.MAGENTA` and `colorama.Fore.LIGHTMAGENTA_EX`
`CYAN`/`LIGHT_CYAN` | Alias for `colorama.Fore.CYAN` and `colorama.Fore.LIGHTCYAN_EX`
`WHITE`/`LIGHT_WHITE` | Alias for `colorama.Fore.WHITE` and `colorama.Fore.LIGHTWHITE_EX`
`RESET` | Alias for `colorama.Fore.RESET`

### Command

The command module contains the default parsing and command behavior. `Command` subclasses are the primary interface for using Commis.

Component       | Description
--------------- | -------------------------------------------------------------
`DefaultParser` | Provides default arguments to all commands (like `--traceback`)
`Command`       | Provides the base functionality for all commands in a console utility.

### Exceptions

Provides an exception hierarchy for capturing Commis-related errors, or so that users can raise them to handle different execution environments.

Component       | Description
--------------- | -------------------------------------------------------------
`ConsoleError`  | Base exception for exceptions that should be raised on the command line.

### Labeled

Provides specialized iterator commands, where the same function is applied to a list of arguments (labels). This was inspired by Django's `LabelCommand`.

Component       | Description
--------------- | -------------------------------------------------------------
`LabelCommand`  | A command which takes on or more arbitrary labels and does something with each of them.


### Program

Implements the complete console utility. Programs and utilities defined in this module are subclassed and given specific commands. They can then easily be loaded and executed in a small Python script.

Component       | Description
--------------- | -------------------------------------------------------------
`handle_default_args`  | Include handling of any default arguments that all commands should implement.
`ConsoleProgram` | The base program from which all console commands are executed.

### Version

The version module handles meta information about the package. It must be in its own separate file thanks to the packaging methodology found in `setup.py`. The version is bumped on each new release.

Component       | Description
--------------- | -------------------------------------------------------------
`get_version`   | Computes a string representation of the version from `__version_info__`.
