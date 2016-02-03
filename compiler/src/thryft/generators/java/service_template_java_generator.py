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
from yutil import indent, lpad


class ServiceTemplateJavaGenerator(java_generator.JavaGenerator):
    class Document(JavaDocument):
        def _java_file_ext(self):
            return '.java.template'

    class Function(JavaFunction):
        def java_definition(self):
            name = self.java_name()
            parameters = [parameter.java_parameter(final=True)
                          for parameter in self.parameters]
            parameters = ', '.join(parameters)
            if self.return_field is not None:
                return_statement = lpad("\n", "    return %s;" % self.return_field.type.java_default_value())
                return_type_name = self.return_field.type.java_qname()
            else:
                return_statement = ''
                return_type_name = 'void'
            throws = \
                lpad(
                    ' throws ',
                    ', '.join(field.type.java_qname()
                               for field in self.throws)
                )

            return """\
@Override
protected %(return_type_name)s _%(name)s(%(parameters)s)%(throws)s {%(return_statement)s
}""" % locals()

    class Service(JavaService):
        def java_name(self):
            return JavaService.java_name(self) + 'Impl'

        def _java_methods(self):
            return [function.java_definition() for function in self.functions]

        def java_repr(self):
            name = self.java_name()
            sections = []
            sections.append("\n\n".join(self._java_methods()))
            sections = "\n\n".join(indent(' ' * 4, sections))
            service_name = JavaService.java_name(self)
            service_package = self._parent_document().java_package()
            return """\
public class %(name)s extends %(service_package)s.Abstract%(service_name)s {
%(sections)s
}""" % locals()
