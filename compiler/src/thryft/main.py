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
from yutil import camelize, decamelize


MY_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR_PATH = os.path.normpath(os.path.join(MY_DIR_PATH, '..'))


class Main(object):
    class _CompileTask(object):
        def __init__(self, generator, out, thrift_file_path, document_root_dir_path=None):
            object.__init__(self)
            self.__document_root_dir_path = document_root_dir_path
            self.__generator = generator
            self.__out = out
            self.__thrift_file_path = thrift_file_path

        @property
        def document_root_dir_path(self):
            return self.__document_root_dir_path

        @property
        def generator(self):
            return self.__generator

        @property
        def out(self):
            return self.__out

        @property
        def thrift_file_path(self):
            return self.__thrift_file_path

    def __init__(
        self,
        clean=False,
        debug=False,
        dry_run=False,
        gen=None,
        include_dir_paths=None,
        log_filename=None,
        out=None,
        thrift_file_paths=None
    ):
        object.__init__(self)
        self.__clean = clean
        self.__debug = debug
        self.__dry_run = dry_run
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
        self.__include_dir_paths = include_dir_paths
        self.__log_filename = log_filename
        self.__out = out
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
            '-I',
            action='append',
            dest='include_dir_paths',
            help='include directory paths'
        )
        argument_parser.add_argument(
            '-out',
            help='output directory path'
        )
        argument_parser.add_argument(
            'thrift_file_paths',
            nargs='*'
        )

    def __call__(self):
        logging_kwds = {
            'format': '%(asctime)s:%(module)s:%(lineno)s:%(name)s:%(levelname)s: %(message)s',
            'level': logging.WARN
        }  # @IgnorePep8
        if self._debug:
            logging_kwds['level'] = logging.DEBUG
            if self.__log_filename is not None:
                logging_kwds['filename'] = self.__log_filename
        logging.basicConfig(**logging_kwds)

        if self.__clean:
            self._clean()
            return

        compiler = Compiler(include_dir_paths=self._include_dir_paths)
        for compile_task in self._get_compile_tasks():
            if compile_task.generator is None and not self.__dry_run:
                continue

            for i in xrange(2):
                gen = compile_task.generator.__class__.__name__
                gen = gen[:gen.index('Generator')]
                gen = decamelize(gen)
                if len(self.__gen) > 0 and gen not in self.__gen:
                    continue

                try:
                    documents = \
                        compiler(
                            document_root_dir_path=compile_task.document_root_dir_path,
                            generator=compile_task.generator,
                            thrift_file_paths=compile_task.thrift_file_path,
                        )
                except (ScanException, CompileException):
                    if self._debug:
                        raise
                    if i == 0:
                        logging.basicConfig(level=logging.DEBUG)
                        continue  # Try again with debugging on
                    else:
                        raise

                if compile_task.generator is not None:
                    for document in documents:
                        document.save(compile_task.out)
                break

    @property
    def _debug(self):
        return self.__debug

    @property
    def _dry_run(self):
        return self.__dry_run

    @property
    def _gen(self):
        return self.__gen

    def _clean(self):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '.clean')

    def _get_compile_tasks(self):
        generators = []
        if not self._dry_run:
            for gen, kwds in self._gen.iteritems():
                generator_module_name = "thryft.generators.%s.%s_generator" % (gen.rsplit('_', 1)[-1], gen)
                generator_module = __import__(generator_module_name)
                for module_name in generator_module_name.split('.')[1:]:
                    generator_module = getattr(generator_module, module_name)
                generator_class_name = camelize(gen) + 'Generator'
                generator_class = getattr(generator_module, generator_class_name)
                generator = generator_class(**kwds)
                generators.append(generator)

        for thrift_file_path in self._thrift_file_paths:
            compile_task_kwds = {'out':self._out, 'thrift_file_path':thrift_file_path}
            if len(generators) == 0:
                yield self._CompileTask(generator=None, **compile_task_kwds)
            else:
                for generator in generators:
                    yield self._CompileTask(generator=generator, **compile_task_kwds)

    def _get_thrift_file_paths(self, thrift_dir_path):
        thrift_file_paths = self._thrift_file_paths
        for dir_path, _, file_names in os.walk(thrift_dir_path):
            for file_name in file_names:
                if os.path.splitext(file_name)[1] != '.thrift':
                    continue

                thrift_file_name = file_name
                thrift_file_path = os.path.join(dir_path, thrift_file_name)
                if len(thrift_file_paths) > 0 and not thrift_file_path in thrift_file_paths:
                    continue

                yield thrift_file_path

    @property
    def _include_dir_paths(self):
        return self.__include_dir_paths

    @classmethod
    def main(cls):
        argument_parser = argparse.ArgumentParser()
        cls._add_arguments(argument_parser)
        args = argument_parser.parse_args()
        cls._main(args)

    @classmethod
    def _main(cls, args, **kwds):
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

        return \
            cls(
                clean=args.clean,
                debug=args.debug,
                dry_run=args.dry_run,
                include_dir_paths=args.include_dir_paths,
                gen=parsed_gen,
                out=args.out,
                thrift_file_paths=args.thrift_file_paths,
                **kwds
            )()

    @property
    def _out(self):
        return self.__out

    @property
    def _thrift_file_paths(self):
        return self.__thrift_file_paths

if __name__ == '__main__':
    Main.main()
