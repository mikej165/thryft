#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------

import os.path
from thryft.generator.document import Document
from thryft.generators.js._js_named_construct import _JsNamedConstruct


class JsDocument(Document, _JsNamedConstruct):
    def js_repr(self):
        sections = []
        try:
            js_namespace = self.namespace_by_scope('js').name
        except KeyError:
            js_namespace = None
        if js_namespace is not None:
            create_namespace = []
            js_namespace_parts = js_namespace.split('.')
            for i in xrange(1, len(js_namespace_parts) + 1):
                js_namespace_prefix = '.'.join(js_namespace_parts[:i])
                create_namespace.append("""\
if (typeof %(js_namespace_prefix)s === "undefined") {
    %(js_namespace_prefix)s = new Object();
}""" % locals())
            sections.append("\n".join(create_namespace))

        sections.append(
            "\n\n".join(definition.js_repr()
                         for definition in self.definitions) + "\n"
        )

        return "\n\n".join(sections)

    def _save_to_dir(self, out_dir_path):
        try:
            out_dir_path = os.path.join(out_dir_path, self.namespace_by_scope('js').name.replace('.', os.path.sep))
        except KeyError:
            pass
        return self._save_to_file(os.path.join(out_dir_path, self.name + '.js'))

    def _save_to_file(self, out_file_path):
        return self._save_to_file_helper(self.js_repr(), out_file_path)
