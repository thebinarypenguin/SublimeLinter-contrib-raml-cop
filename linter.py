#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ethan Zimmerman
# Copyright (c) 2014 Ethan Zimmerman
#
# License: MIT
#

"""This module exports the RamlCop plugin class."""

from SublimeLinter.lint import NodeLinter


class RamlCop(NodeLinter):

    """Provides an interface to raml-cop."""

    syntax = 'raml'
    cmd = 'raml-cop --no-color'
    version_requirement = '>= 1.0.0'
    regex = (
        r'^\[.+:(?P<line>\d+):(?P<col>\d+)\] '
        r'(?P<message>.+)'
    )
    line_col_base = (0, 0)
