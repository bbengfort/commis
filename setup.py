#!/usr/bin/env python
# setup
# Setup script for installing commis
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Jan 20 11:48:43 2016 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Setup script for installing commis.
See https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
"""

##########################################################################
## Imports
##########################################################################

import os
import re
import codecs

from setuptools import setup
from setuptools import find_packages

##########################################################################
## Package Information
##########################################################################

## Basic information
NAME         = "commis"
DESCRIPTION  = "Create command line applications like Django management commands."
AUTHOR       = "Benjamin Bengfort"
EMAIL        = "benjamin@bengfort.com"
LICENSE      = "Apache"
REPOSITORY   = "https://github.com/bbengfort/commis"
PACKAGE      = "commis"

## Define the keywords
KEYWORDS     = (
    'commis', 'management', 'command line interface', 'argparse'
)

## Define the classifiers
## See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS  = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
)

## Important Paths
PROJECT      = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"
VERSION_PATH = os.path.join(PACKAGE, "version.py")
PKG_DESCRIBE = "DESCRIPTION.txt"

## Directories to ignore in find_packages
EXCLUDES     = (
    "tests", "bin", "docs", "fixtures", "register", "notebooks",
)

##########################################################################
## Helper Functions
##########################################################################

def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), 'rb', 'utf-8') as f:
        return f.read()


def get_version(path=VERSION_PATH):
    """
    Reads the __init__.py defined in the VERSION_PATH to find the get_version
    function, and executes it to ensure that it is loaded correctly.
    """
    namespace = {}
    exec(read(path), namespace)
    return namespace['get_version']()


def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            yield line

##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "version": get_version(),
    "description": DESCRIPTION,
    "long_description": read(PKG_DESCRIBE),
    "license": LICENSE,
    "author": AUTHOR,
    "author_email": EMAIL,
    "maintainer": AUTHOR,
    "maintainer_email": EMAIL,
    "url": REPOSITORY,
    "download_url": "{}/tarball/v{}".format(REPOSITORY, get_version()),
    "packages": find_packages(where=PROJECT, exclude=EXCLUDES),
    "install_requires": list(get_requires()),
    "classifiers": CLASSIFIERS,
    "keywords": KEYWORDS,
    "zip_safe": False,
    "scripts": [],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
