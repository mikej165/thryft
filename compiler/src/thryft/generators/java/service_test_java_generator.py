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

from thryft.generators.java import java_generator
from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import indent, upper_camelize


class ServiceTestJavaGenerator(java_generator.JavaGenerator):
    class Document(JavaDocument):
        def java_imports(self):
            return ['import org.junit.Test;']

        def _java_file_ext(self):
            return '.java.template'

    class Function(JavaFunction):
        def java_definition(self):
            name = self.java_name()
            return """\
@Test
public void %(name)s() {
}""" % locals()

        def java_name(self):
            return 'test' + upper_camelize(self.name)

    class Service(JavaService):
        def java_name(self, boxed=False):
            return JavaService.java_name(self) + 'Test'

        def _java_constructor(self):
            name = self.java_name()
            service_qname = JavaService.java_qname(self)
            return """\
public %(name)s(final %(service_qname)s service) {
    this.service = service;
}""" % locals()

        def _java_member_declarations(self):
            service_qname = JavaService.java_qname(self)
            return [
                "private final %(service_qname)s service;" % locals()
            ]

        def _java_methods(self):
            return [function.java_definition() for function in self.functions]

        def java_repr(self):
            name = self.java_name()

            sections = []
            sections.append("\n\n".join([self._java_constructor()] + self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            return """\
public final class %(name)s {
%(sections)s
}""" % locals()
