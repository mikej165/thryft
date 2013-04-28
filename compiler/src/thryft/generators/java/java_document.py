#-------------------------------------------------------------------------------
# Copyright (c) 2013, Minor Gordon
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
#-------------------------------------------------------------------------------

from thryft.generator.document import Document
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
import os.path


class JavaDocument(Document, _JavaNamedConstruct):
    def _java_file_ext(self):
        return '.java'

    def java_imports(self):
        return []

    def java_package(self):
        namespaces_by_scope = self.namespaces_by_scope
        for scope in ('java', '*'):
            try:
                return namespaces_by_scope[scope].name
            except KeyError:
                pass
        return None

    def java_package_declaration(self):
        package = self.java_package()
        if package is not None:
            return 'package ' + package + ';'

    def __repr__(self):
        sections = []

        package_declaration = self.java_package_declaration()
        if package_declaration is not None:
            sections.append(package_declaration)

        imports = self.java_imports()
        if len(imports) > 0:
            sections.append("\n".join(imports))

        sections.append(
            "\n\n".join(repr(definition)
                         for definition in self.definitions)
        )

        return "\n\n".join(sections) + "\n"

    def save(self, out_path, file_ext='.java', language='java'):
        return Document.save(self, out_path=out_path, file_ext=file_ext, language=language)

    def _save(self, out_file_path):
        assert len(self.definitions) == 1, len(self.definitions)
        return \
            Document._save(
                self,
                os.path.join(
                    os.path.dirname(out_file_path),
                    self.definitions[0].java_name() + self._java_file_ext()
                )
            )
