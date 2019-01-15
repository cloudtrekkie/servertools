#!/usr/bin/env python
# @formatter:off
#
#                                             ,,
#                                             db
#     \
#     _\,,          `7MM  `7MM  `7MMpMMMb.  `7MM  ,p6"bo   ,pW"Wq.`7Mb,od8 `7MMpMMMb.
#    "-=\~     _      MM    MM    MM    MM    MM 6M'  OO  6W'   `Wb MM' "'   MM    MM
#       \\~___( ~     MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#      _|/---\\_      MM    MM    MM    MM    MM 8M       8M     M8 MM       MM    MM
#     \        \      MM    MM    MM    MM    MM YM.    , YA.   ,A9 MM       MM    MM
#                     `Mbod"YML..JMML  JMML..JMML.YMbmd'   `Ybmd9'.JMML.   .JMML  JMML.
#
#                     <> with ❤ by Micha Grandel (talk@michagrandel.de)
#
#                     Project:         https://github.com/michagrandel/servertools
#                     Report a bug:    https://github.com/michagrandel/servertools/issues
#                     Contribute:      https://github.com/michagrandel/servertools/wiki/Contribute
#
#                     -----------------------------------------------------------------
#
#                     Copyright 2019 Micha Grandel
#
#                     Licensed under the Apache License, Version 2.0 (the 'License');
#                     you may not use this file except in compliance with the License.
#                     You may obtain a copy of the License at
#
#                     http://www.apache.org/licenses/LICENSE-2.0
#
#                     Unless required by applicable law or agreed to in writing,
#                     software distributed under the License is distributed on an
#                     'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
#                     either express or implied. See the License for the specific
#                     language governing permissions and limitations under the License.
#
#                     -----------------------------------------------------------------
#                     @formatter:on


from __future__ import print_function, division, unicode_literals
import sys
import platform
import os
import locale
import logging
import gettext
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from argparse import ArgumentParser
import pkg_resources

from typing import AnyStr, List


sys.path.append('../servertools')

from servertools import MittwaldServer, Uberspace
from servertools.appdirs import user_log_dir, user_config_dir


""" test the server environment and apply fixes """

__status__ = 'development'
__author__ = 'Micha Grandel'
__version__ = '1.0'
__copyright__ = '<> with ❤ by Micha Grandel'
__license__ = 'Apache License, Version 2.0'
__contact__ = 'michagrandel@googlemail.com'


def _log_default_handler(proc: AnyStr, log_dir: AnyStr = '.'):
    """
    provides a default handler for a Logger

    :param proc: name of the script
    :param log_dir: directory in which the log file will be saved; default: '.'
    """
    
    log_dir = os.path.abspath(log_dir)
    try:
        # create directory if it does not exist yet
        os.makedirs(log_dir)
    except IOError:
        pass
    
    # create Logger Objects
    filename = os.path.join(log_dir, '{}.log'.format(os.path.splitext(proc)[0]))  # type: AnyStr
    handlers = [
        TimedRotatingFileHandler(filename, when='midnight', backupCount=10, encoding='utf-8')
    ]  # type: List[TimedRotatingFileHandler]
    
    # add formatter and set level for the Logger Objects
    message_format = '%(asctime)s [%(levelname)s] %(message)s'  # type: AnyStr
    level = logging.DEBUG if __status__ == 'development' else logging.INFO  # type: int
    
    if __status__ == 'development':
        message_format += ' (in %(name)s.%(filename)s)'
    for i in range(len(handlers)):
        handlers[i].setLevel(level)
        handlers[i].setFormatter(logging.Formatter(message_format, datefmt='%x %X'))
    
    return handlers


def main(args: List[AnyStr] = None) -> None:
    """
    prepare and start application

    the main method is responsible for setting up the environment,
    i.e. to load translations, set a logger, parse the command line arguments,
    load configuration files and start the application.

    :param args: command line arguments; default: None
    :type args: List of strings
    """
    if not args:
        args = sys.argv
    
    script_name = os.path.basename(sys.argv[0])
    logging_path = user_log_dir(os.path.splitext(script_name)[0], __author__, __version__)
    config_path = user_config_dir(os.path.splitext(script_name)[0], __author__, __version__)
    
    # set locale
    locale.setlocale(locale.LC_ALL, '')
    _locale = locale.getlocale(locale.LC_ALL)[0]
    locale_path = pkg_resources.resource_filename("servertools", "data/i18n".format(_locale))
    
    translate = gettext.translation("servertools", localedir=locale_path, languages=[locale.getlocale()[0], 'en'])
    translate.install()
    if '_' not in globals():
        try:
            _ = unicode
        except NameError:
            _ = str
    
    # setup logging
    handlers = _log_default_handler(proc=script_name, log_dir=logging_path)
    logging.basicConfig(level=4, format="%(message)s", handlers=handlers)
    
    logger = logging.getLogger("{}_logger".format(os.path.splitext(script_name)[0]))
    logger.setLevel(logging.DEBUG)
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(stream_handler)
    
    # setup argument parser
    parser = ArgumentParser(prog=script_name)
    verbosity_parsergroup = parser.add_mutually_exclusive_group()
    verbosity_parsergroup.add_argument("-v", dest='verbosity', action="count", help=_("increase verbosity"), default=0)
    verbosity_parsergroup.add_argument("--silent", action="store_true", help=_("silent (no output to terminal)"))
    parser.add_argument("--version", action="version", help=_("print version and exit"))
    parser.add_argument("--log-file", metavar='FILEPATH', action="store", help=_("overwrite path to log file"))
    
    command_parsers = parser.add_subparsers(help="commands")
    identify_parser = command_parsers.add_parser("identify", add_help=False, parents=[parser])
    
    # todo: valid values for --look-for should come from installed plugins
    identify_parser.add_argument("--look-for", metavar="SERVER", dest="look_for", help=_("look for a specific server"),
                                 choices=["mittwald", "uberspace"], default='')
    identify_parser.set_defaults(name="identify")
    
    # todo: add feature to fix server-specific problems
    # fix_parser = command_parsers.add_parser('fix', help=_('apply fixes for a server'))
    
    # parse arguments
    args = parser.parse_args(args[1:])
    
    # handle verbosity
    verbosity = max(0, min(3, args.verbosity))
    if args.silent:
        verbosity = -1
    
    logging_level = {
        -1: logging.CRITICAL,  # 50
        0: logging.WARNING,  # 30
        1: logging.INFO,  # 20
        2: logging.INFO,  # 20
        3: logging.DEBUG  # 10
    }.get(verbosity, logging.WARNING)
    stream_handler.setLevel(logging_level)
    
    # start application
    logger.debug(_("{0} started at {1:%X} on Python {2} ({3})").format(
        script_name, datetime.now(), platform.python_version(), platform.architecture()[0]
    ))
    logger.debug(_("Save logs to {}").format(logging_path))
    logger.debug(_("Load configurations from {}").format(config_path))
    logger.debug(_("Verbosity Level at {}").format(verbosity))
    
    mw = MittwaldServer(logger=logger, verbose=verbosity)
    uberspace = Uberspace(logger=logger, verbose=verbosity)
    
    # todo: make server identification extendable through plugins for identification
    try:
        # handle command line subparser "identify"
        if args.look_for == "mittwald":
            mw.identify()
        if args.look_for == "uberspace":
            uberspace.identify()
    except AttributeError:
        # handle default behaviour
        if not mw.identify() and not uberspace.identify():
            logger.info(_("unknown platform"))
    logger.debug("-" * 80)


if __name__ == "__main__":
    main(sys.argv)
