# -----------------------------------------------------------------------------
# Copyright (c) 2015, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

import logging
import os.path

import argparse

from thryft.compiler import Compiler
from thryft.compiler.compile_exception import CompileException
from thryft.compiler.scan_exception import ScanException
from yutil import decamelize
from thryft.generator.generator import Generator


MY_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR_PATH = os.path.normpath(os.path.join(MY_DIR_PATH, '..'))


class Main(object):
    def __init__(
        self,
        clean=False,
        debug=False,
        gen=None,
        include_dir_paths=None,
        log_filename=None,
        thrift_file_paths=None
    ):
        object.__init__(self)
        self.__clean = clean
        self.__debug = debug
        if gen is None:
            gen = {}
        self.__gen = gen
        if include_dir_paths is None:
            include_dir_paths = tuple()
        else:
            include_dir_paths_dedup = []
            for include_dir_path in include_dir_paths:
                if include_dir_path not in include_dir_paths_dedup:
                    include_dir_paths_dedup.append(include_dir_path)
            include_dir_paths = tuple(include_dir_paths_dedup)
        self.__compiler = Compiler(include_dir_paths=include_dir_paths)
        self.__log_filename = log_filename
        if thrift_file_paths is None:
            thrift_file_paths = tuple()
        self.__thrift_file_paths = thrift_file_paths

    @classmethod
    def _add_arguments(cls, argument_parser):
        argument_parser.add_argument(
            '-d',
            '--debug',
            action='store_true',
            help='enable debug logging'
        )
        argument_parser.add_argument(
            '--clean',
            action='store_true',
            help="clean out generated code"
        )
        argument_parser.add_argument(
            '--dry-run',
            action='store_true',
            help="compile but don't generate code"
        )
        argument_parser.add_argument(
            '-l',
            '--log-filename',
            help='file name to log messages to'
        )
        argument_parser.add_argument(
            '--gen',
            action='append',
            help='language[:key1=val1[,key2,[key3=val3]]]'
        )
        argument_parser.add_argument(
            'thrift_file_paths',
            nargs='*'
        )

    def _main(self):
        logging_kwds = {
            'format': '%(asctime)s:%(module)s:%(lineno)s:%(name)s:%(levelname)s: %(message)s',
            'level': logging.WARN
        }  # @IgnorePep8
        if self.__debug:
            logging_kwds['level'] = logging.DEBUG
            if self.__log_filename is not None:
                logging_kwds['filename'] = self.__log_filename
        logging.basicConfig(**logging_kwds)

        if self.__clean:
            self._clean()
            return

        self._compile()

    def _clean(self):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '.clean')

    def _compile(self):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '.compile')

    def _compile_thrift_file(self, thrift_file_path, document_root_dir_path=None, generator=None, out=None):
        try:
            for i in xrange(2):
                if generator is not None:
                    gen = generator.__class__.__name__
                    gen = gen[:gen.index('Generator')]
                    gen = decamelize(gen)
                    if len(self.__gen) > 0 and gen not in self.__gen:
                        return
                else:
                    generator = Generator()

                try:
                    document = \
                        self.__compiler(
                            document_root_dir_path=document_root_dir_path,
                            generator=generator,
                            thrift_file_paths=thrift_file_path,
                        )[0]
                except (ScanException, CompileException):
                    if self.__debug:
                        raise
                    if i == 0:
                        logging.basicConfig(level=logging.DEBUG)
                        continue  # Try again with debugging on
                    else:
                        raise

                if out is not None:
                    document.save(out)
                return document
        except:
            logging.error("exception compiling %s", thrift_file_path)
            raise

    def _get_thrift_file_paths(self, thrift_dir_path):
        thrift_file_paths = self.__thrift_file_paths
        for dir_path, _, file_names in os.walk(thrift_dir_path):
            for file_name in file_names:
                if os.path.splitext(file_name)[1] != '.thrift':
                    continue

                thrift_file_name = file_name
                thrift_file_path = os.path.join(dir_path, thrift_file_name)
                if len(thrift_file_paths) > 0 and not thrift_file_path in thrift_file_paths:
                    continue

                yield thrift_file_path

    @classmethod
    def main(cls, args=None, **kwds):
        if args is None:
            argument_parser = argparse.ArgumentParser()
            cls._add_arguments(argument_parser)
            args = argument_parser.parse_args()

        parsed_gen = {}
        if args.gen is not None:
            for gen in args.gen:
                gen = gen.split(':', 1)
                if len(gen) == 1:
                    parsed_gen[gen[0]] = {}
                elif len(gen) == 2:
                    gen, gen_kwds_str = gen
                    gen_kwds = {}
                    for gen_kwd in gen_kwds_str.split(','):
                        gen_kwd_split = gen_kwd.split('=', 1)
                        if len(gen_kwd_split) == 1:
                            gen_kwds[gen_kwd_split[0]] = None
                        else:
                            gen_kwds[gen_kwd_split[0]] = gen_kwd_split[1]
                    parsed_gen[gen] = gen_kwds

        cls(
            clean=args.clean,
            debug=args.debug,
            gen=parsed_gen,
            log_filename=args.log_filename,
            thrift_file_paths=args.thrift_file_paths,
            **kwds
        )._main()
