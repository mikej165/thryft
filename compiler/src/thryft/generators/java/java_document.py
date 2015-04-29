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
from thryft.generator.typedef import Typedef
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
import os.path


class JavaDocument(Document, _JavaNamedConstruct):
    def _java_file_ext(self):
        return '.java'

    def java_imports(self):
        return []

    def java_package(self):
        try:
            return self.namespace_by_scope('java').name
        except KeyError:
            return None

    def java_package_declaration(self):
        package = self.java_package()
        if package is not None:
            return 'package ' + package + ';'

    def java_repr(self):
        sections = []

        package_declaration = self.java_package_declaration()
        if package_declaration is not None:
            sections.append(package_declaration)

        imports = self.java_imports()
        if len(imports) > 0:
            sections.append("\n".join(imports))

        sections.append(
            "\n\n".join(definition.java_repr()
                         for definition in self.definitions)
        )

        return "\n\n".join(sections) + "\n"

    def save(self, *args, **kwds):
        if len(self.definitions) == 0:
            return
        assert len(self.definitions) == 1, len(self.definitions)
        if isinstance(self.definitions[0], Typedef):
            return
        return Document.save(self, *args, **kwds)

    def _save_to_dir(self, out_dir_path):
        java_package = self.java_package()
        if java_package is not None:
            try:
                out_dir_path = os.path.join(out_dir_path, java_package.replace('.', os.path.sep))
            except KeyError:
                pass
        return self._save_to_file(os.path.join(out_dir_path, self.definitions[0].java_name() + self._java_file_ext()))

    def _save_to_file(self, out_file_path):
        return self._save_to_file_helper(self.java_repr(), out_file_path)
