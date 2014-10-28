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
from thryft.generators.cpp.cpp_struct_type import CppStructType
from yutil import indent, upper_camelize


class CppFunction(Function, _CppNamedConstruct):
    class _CppMessageType(CppStructType):
        pass

    class _CppRequestType(_CppMessageType):
        def __init__(self, parent_function, cpp_suppress_warnings=None, parameters=None):
            CppFunction._CppMessageType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Request',
                parent=parent_function.parent
            )
            self.__parent_function = parent_function

            if parameters is None:
                parameters = parent_function.parameters
            for parameter in parameters:
                self.fields.append(
                    parameter.__class__(
                        annotations=parameter.annotations,
                        doc=parameter.doc,
                        name=parameter.name,
                        type=parameter.type,
                        parent=self,
                        required=parameter.required,
                    )
                )

        def _cpp_extends(self):
            return self._parent_generator().cpp_service_parent_class_qname + "<%s>::Messages::Request" % self.__parent_function.parent.cpp_name()

        def cpp_forward_declaration(self):
            return 'class ' + self.cpp_name() + ';'

        def cpp_handle_declaration(self):
            return "virtual void handle(const %s&) = 0;" % self.cpp_name()

        def _cpp_method_accept(self):
            return {'accept': """\
void accept(RequestHandler& handler) const {
  handler.handle(*this);
}""" % locals()}

        def _cpp_methods_map(self):
            methods = CppStructType._cpp_methods_map(self)
            methods.update(self._cpp_method_accept())
            return methods

        def cpp_read_if(self):
            return """\
if (strcmp(function_name, "%s") == 0) {
  return new %s(iprot, as_type);
}""" % (self.__parent_function.name, self.cpp_name())

        def cpp_sync_handler(self):
            name = self.cpp_name()
            response_name = upper_camelize(self.__parent_function.cpp_name()) + 'Response'
            if self.__parent_function.return_field is not None:
                call_prefix = "request.respond(%(response_name)s(" % locals()
                call_suffix = "))"
            else:
                call_prefix = ''
                call_suffix = """;
request.respond(%(response_name)s())""" % locals()
            call_parameters = \
                ', '.join("request.%s()" % parameter.cpp_getter_name()
                           for parameter in self.fields)
            call_method_name = self.__parent_function.name
            call = "%(call_prefix)simpl_.%(call_method_name)s(%(call_parameters)s)%(call_suffix)s;" % locals()
            if len(self.__parent_function.throws) > 0:
                catches = []
                for exception in self.__parent_function.throws:
                    exception_name = exception.cpp_name()
                    exception_type_qname = exception.type.cpp_qname()
                    catches.append("""\
} catch (const %(exception_type_qname)s& %(exception_name)s) {
  request.respond(%(exception_name)s);""" % locals())
                catches = "\n".join(catches) + "\n}"
                call = indent(' ' * 2, call)
                call = """\
try {
%(call)s
%(catches)s""" % locals()
            call = indent(' ' * 2, call)
            return """\
virtual void handle(const %(name)s& request) {
%(call)s
}""" % locals()

    class _CppResponseType(_CppMessageType):
        def __init__(self, parent_function, cpp_suppress_warnings=None):
            CppFunction._CppMessageType.__init__(
                self,
                name=upper_camelize(parent_function.name) + 'Response',
                parent=parent_function.parent
            )
            self.__parent_function = parent_function
            if parent_function.return_field is not None:
                return_field = parent_function.return_field
                self.fields.append(
                    return_field.__class__(
                        annotations=return_field.annotations,
                        doc=return_field.doc,
                        name=return_field.name,
                        type=return_field.type,
                        parent=self,
                        required=True
                    )
                )

        def _cpp_extends(self):
            return self._parent_generator().cpp_service_parent_class_qname + "<%s>::Messages::Response" % self.__parent_function.parent.cpp_name()

    def cpp_declaration(self, line_ending="\n", override=False):
        override = ' override' if override else ''

        name = self.cpp_name()

        parameters = \
            ', '.join(parameter.cpp_parameter()
                      for parameter in self.parameters)

        if self.return_field is not None:
            return_type_name = self.return_field.type.cpp_qname()
        else:
            return_type_name = 'void'

        declaration = """\
%(return_type_name)s %(name)s(%(parameters)s)%(override)s""" % locals()

        if len(declaration) < 80:
            return declaration

        parameters = indent(' ' * 2,
            (',' + line_ending).join(parameter.cpp_parameter()
                      for parameter in self.parameters))

        return """\
%(return_type_name)s%(line_ending)s%(name)s(%(line_ending)s%(parameters)s%(line_ending)s)%(override)s""" % locals()

    def cpp_includes_definition(self):
        includes = []
        for exception in self.throws:
            includes.extend(exception.cpp_includes_use())
        for parameter in self.parameters:
            includes.extend(parameter.cpp_includes_use())
        if self.return_field is not None:
            includes.extend(self.return_field.cpp_includes_use())
        return includes

    def cpp_pure_virtual_declaration(self):
        return 'virtual ' + self.cpp_declaration() + ' = 0;'

    def cpp_qname(self):
        return self.name

    def cpp_repr(self):
        return self.cpp_declaration()

    def cpp_request_type(self, **kwds):
        return self._CppRequestType(parent_function=self, **kwds)

    def cpp_response_type(self, **kwds):
        return self._CppResponseType(parent_function=self, **kwds)
