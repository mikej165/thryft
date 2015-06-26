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

import os.path
from shutil import copyfile

THRYFT_ROOT_DIR_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', '..'))

try:
    import thryft
except ImportError:
    import sys
    sys.path.append(os.path.join(THRYFT_ROOT_DIR_PATH, 'compiler', 'src'))
from thryft.compiler import Compiler
from thryft.generators.cpp.cpp_generator import CppGenerator
from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.js.js_generator import JsGenerator
from thryft.generators.py.py_generator import PyGenerator
import thryft.main
from yutil import camelize


class Main(thryft.main.Main):
    def _get_compile_tasks(self):
        gen = self._gen

        generators = {
            'cpp': (CppGenerator(),),
            'java': (JavaGenerator(),),
            'js': (JsGenerator(),),
            'py': (PyGenerator(),),
        }

        for in_dir_path, out_dir_paths in (
              (
                  os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'thrift', 'src', 'thryft', 'native'),
                  {
                      'cpp': (os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'cpp', 'include'),)
                  }
              ),
              (
                  os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'thrift', 'test'),
                  {
                      'cpp': (os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'cpp', 'test'),),
                      'java': (
                          os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'java', 'src', 'test', 'java'),
                       ),
                      'js': (os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'js', 'test'),),
                      'py': (os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'py', 'test'),),
                  },
             ),
              (
                  os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'thrift', 'src', 'thryft', 'protocol'),
                  {
                      'cpp': (os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'cpp', 'include'),),
                      'java': (
                          os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'java', 'src', 'main', 'java'),
                       ),
                      'py': (os.path.join(THRYFT_ROOT_DIR_PATH, 'lib', 'py', 'src'),),
                  },
             ),
        ):
            gen = self._gen
            for thrift_file_path in self._get_thrift_file_paths(in_dir_path):
                if os.path.splitext(os.path.split(thrift_file_path)[1])[0] in ('float', 'i8', 'u32', 'u64', 'variant'):
                    continue

                compile_task_kwds = {
                    'document_root_dir_path': in_dir_path,
                    'thrift_file_path': thrift_file_path
                }

                yield self._CompileTask(generator=None, out=None, **compile_task_kwds)

                for gen_name in generators.keys() if len(gen) == 0 else gen.keys():
                    for generator in generators[gen_name]:
                        for out_dir_path in out_dir_paths.get(gen_name, []):
                            yield \
                                self._CompileTask(
                                    generator=generator,
                                    out=out_dir_path,
                                    **compile_task_kwds
                                )


assert __name__ == '__main__'
Main.main()
