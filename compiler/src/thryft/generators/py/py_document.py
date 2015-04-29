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

from thryft.generator.document import Document
from thryft.generators.py._py_named_construct import _PyNamedConstruct
from yutil import rpad
import os.path


class PyDocument(Document, _PyNamedConstruct):
    def py_repr(self):
        imports = []
# Don't import anything that isn't required
#        for include in self.includes:
#            imports.append(str(include))
        for definition in self.definitions:
            imports.extend(definition.py_imports_definition())
        imports = "\n".join(list(sorted(set(imports))))

        definitions = \
            "\n\n".join(definition.py_repr()
                         for definition in self.definitions)
        return rpad(imports, "\n\n\n") + rpad(definitions, "\n")

    def save(self, out_path):
        out_file_path = Document.save(self, out_path)
        if out_file_path is None:
            return None
        elif not os.path.isdir(out_path):
            return out_file_path

        root_out_dir_path = out_path
        leaf_out_dir_path = os.path.split(out_file_path)[0]

        py_module_dir_path = leaf_out_dir_path
        while py_module_dir_path != root_out_dir_path:
            init_py_file_path = os.path.join(py_module_dir_path, '__init__.py')
            if not os.path.isfile(init_py_file_path):
                with open(init_py_file_path, 'wb+') as _init_py_file:
                    self._logger.info('wrote ' + init_py_file_path)
            py_module_dir_path = os.path.split(py_module_dir_path)[0]

        return out_file_path

    def _save_to_dir(self, out_dir_path):
        try:
            out_dir_path = os.path.join(out_dir_path, self.namespace_by_scope('py').name.replace('.', os.path.sep))
        except KeyError:
            pass
        return self._save_to_file(os.path.join(out_dir_path, self.name + '.py'))

    def _save_to_file(self, out_file_path):
        return self._save_to_file_helper(self.py_repr(), out_file_path)
