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

from thryft.generator.service import Service
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from yutil import indent, lpad, pad


class JavaService(Service, _JavaNamedConstruct):
    def _java_annotations(self):
        return []

    def _java_extends(self):
        return self.extends

    def _java_methods(self):
        methods = []
        for function in self.functions:
            methods.extend(function.java_declarations())
        return methods

    def _java_methods_repr(self):
        return "\n\n".join(self._java_methods())

    def java_name(self, boxed=False):
        return self.name

    def _java_message_types(self):
        message_types = []
        for function in self.functions:
            message_types.extend(function.java_message_types())
        return message_types

    def _java_message_types_repr(self):
        message_types = self._java_message_types()
        if len(message_types) > 0:
            message_types = \
                "\n\n".join(indent(' ' * 4,
                    (message_type.java_repr()
                     for message_type in message_types)
                ))
            return """\
public static class Messages {
%(message_types)s
}""" % locals()

    def java_qname(self, boxed=False):
        return _JavaNamedConstruct.java_qname(self, name=self.name)

    def java_repr(self):
        annotations = pad("\n", "\n".join(self._java_annotations()), "\n")

        extends = self._java_extends()
        if extends is None:
            extends = ''
        else:
            extends = ' extends ' + extends

        javadoc = self.java_doc()
        name = self.java_name()

        sections = lpad("\n", "\n\n".join(indent(' ' * 4, self._java_repr_sections())))

        return """\
%(javadoc)s%(annotations)spublic interface %(name)s%(extends)s {%(sections)s
}""" % locals()

    def _java_repr_sections(self):
        sections = []
        for section in (
            self._java_message_types_repr(),
            self._java_methods_repr()
        ):
            if len(section) > 0:
                sections.append(section)
        return sections
