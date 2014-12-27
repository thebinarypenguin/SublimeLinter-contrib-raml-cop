#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ethan Zimmerman,,,
# Copyright (c) 2014 Ethan Zimmerman,,,
#
# License: MIT
#

"""This module exports the RamlCop plugin class."""

from SublimeLinter.lint import NodeLinter, util


class RamlCop(NodeLinter):

    """Provides an interface to raml-cop."""

    syntax = 'raml'
    cmd = 'raml-cop --no-color'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.2.0'
    regex = (
        r'^\[.+:(?P<line>\d+):(?P<col>\d+)\] '
        r'(?:(?P<warning>WARNING)|(?P<error>ERROR)) '
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (0, 0)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
