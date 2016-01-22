# commis.labeled
# Base class for a Label command, similar to Django's label command.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Jan 21 16:21:13 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: labeled.py [] benjamin@bengfort.com $

"""
Base class for a Label command, similar to Django's label command.
"""

##########################################################################
## Imports
##########################################################################

from .command import Command


##########################################################################
## LabelCommand
##########################################################################

class LabelCommand(Command):
    """
    A management command which takes on or more arbitrary labels and does
    something with each of them, similar to  Django's LabelCommand.

    Rather than implementing `handle()`, subclasses must implement a
    `handle_label()`, which is called once for each label.
    """

    label = 'label'

    def __init__(self, **kwargs):
        """
        Initialize the label command.
        """
        self.label    = kwargs.get('label', self.__class__.label)
        super(LabelCommand, self).__init__(**kwargs)

    def add_arguments(self):
        """
        Add the label argument by default, no need to specify it in args.
        """
        super(LabelCommand, self).add_arguments()
        self.parser.add_argument('labels', metavar=self.label, nargs="+")

    def handle(self, args):
        output = []
        for label in args.labels:
            label_output = self.handle_label(label, args)
            if label_output:
                output.append(label_output)
        return "\n".join(output)

    def handle_label(label, args):
        """
        Perform the command's actions for `label` which will be the string as
        given on the command line. All args are passed into this function.
        """
        raise NotImplementedError(
            'subclasses of LabelCommand must provide a handle_label() method'
        )
