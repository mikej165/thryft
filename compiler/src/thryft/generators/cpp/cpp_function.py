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

from thryft.generator.function import Function
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct
from thryft.generators.cpp.cpp_field import CppField
from thryft.generators.cpp.cpp_struct_type import CppStructType
from yutil import lower_camelize, lpad, indent, upper_camelize


class CppFunction(Function, _CppNamedConstruct):
    class _CppRequestType(CppStructType):
        def __init__(self, parent_function, cpp_suppress_warnings=None, parameters=None):
            CppStructType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Request',
                parent=parent_function.parent
            )
            self.__parent_function_name = parent_function.name

            if parameters is None:
                parameters = parent_function.parameters
            for parameter in parameters:
                self.fields.append(
                    CppField(
                        annotations=parameter.annotations,
                        doc=parameter.doc,
                        name=parameter.name,
                        type=parameter.type,
                        parent=self,
                        required=parameter.required,
                    )
                )

        def _cpp_extends(self):
            return 'Request'

        def cpp_forward_declaration(self):
            return 'class ' + self.cpp_name() + ';'

        def _cpp_method_accept(self):
            return """\
void accept(RequestHandler& handler) const {
  handler.handle(*this);
}"""

        def _cpp_methods(self):
            methods = CppStructType._cpp_methods(self)
            methods.append(self._cpp_method_accept())
            return methods

        def cpp_read_if(self):
            return """\
if (strcmp(function_name, "%s") == 0) {
  return new %s(iprot, as_type);
}""" % (self.__parent_function_name, self.cpp_name())

        def cpp_handle_declaration(self):
            return "virtual void handle(const %s&) = 0;" % self.cpp_name()

    class _CppResponseType(CppStructType):
        def __init__(self, parent_function, cpp_suppress_warnings=None):
            CppStructType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Response',
                parent=parent_function.parent
            )
            if parent_function.return_field is not None:
                return_field = parent_function.return_field
                self.fields.append(
                    CppField(
                        annotations=return_field.annotations,
                        doc=return_field.doc,
                        name=return_field.name,
                        type=return_field.type,
                        parent=self,
                        required=return_field.required,
                    )
                )

        def _cpp_extends(self):
            return 'Response'

    def _cpp_declaration(self):
        name = self.cpp_name()

        parameters = \
            ', '.join(parameter.cpp_parameter() for parameter in self.parameters)

        if self.return_field is not None:
            return_type_name = self.return_field.type.cpp_name()
        else:
            return_type_name = 'void'

        return """\
%(return_type_name)s %(name)s(%(parameters)s)""" % locals()

    def cpp_includes_definition(self):
        includes = []
        for parameter in self.parameters:
            includes.extend(parameter.cpp_includes_use())
        if self.return_field is not None:
            includes.extend(self.return_field.cpp_includes_use())
        return includes

    def cpp_name(self):
        return self.name

    def cpp_pure_virtual_declaration(self):
        return 'virtual ' + self._cpp_declaration() + ' = 0;'

    def cpp_request_type(self, **kwds):
        return self._CppRequestType(parent_function=self, **kwds)

    def cpp_response_type(self, **kwds):
        return self._CppResponseType(parent_function=self, **kwds)

    def __repr__(self):
        return self.cpp_declaration()
