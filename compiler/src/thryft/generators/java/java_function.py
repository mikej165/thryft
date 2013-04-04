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
from thryft.generators.java.java_struct_type import \
    JavaStructType
from thryft.generators.java.java_field import JavaField
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from yutil import lower_camelize, lpad, indent


class JavaFunction(Function, _JavaNamedConstruct):
    class _JavaRequestType(JavaStructType):
        def __init__(self, parent_function, java_suppress_warnings=None, parameters=None):
            JavaStructType.__init__(
                self,
                java_class_modifiers='public final static',
                java_suppress_warnings=java_suppress_warnings,
                name=parent_function.java_name() + 'Request',
                parent=parent_function.parent
            )

            if parameters is None:
                parameters = parent_function.parameters
            for parameter in parameters:
                self.fields.append(
                    JavaField(
                        name=parameter.name,
                        type=parameter.type,
                        parent=self,
                        required=parameter.required,
                        validation=parameter.validation
                    )
                )

    class _JavaResponseType(JavaStructType):
        def __init__(self, parent_function, java_suppress_warnings=None):
            JavaStructType.__init__(
                self,
                java_class_modifiers='public final static',
                java_suppress_warnings=java_suppress_warnings,
                name=parent_function.java_name() + 'Response',
                parent=parent_function.parent
            )
            if parent_function.return_field is not None:
                self.fields.append(parent_function.return_field)

        def _java_constructor_protocol(self):
            name = self.java_name()
            if len(self.fields) > 0:
                field = self.fields[0]
                field_initializer = lpad("\n", indent(' ' * 4, field.java_protocol_initializer()))
            else:
                field_initializer = ''
            return """\
public %(name)s(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {%(field_initializer)s
}""" % locals()

    def java_declaration(self, final_parameters=False):
        name = self.java_name()
        parameters = \
            ', '.join(parameter.java_parameter(final=final_parameters) for parameter in self.parameters)
        return_type_name = \
            self.return_field is not None and \
                self.return_field.type.java_declaration_name() or \
                'void'
        throws = \
            lpad(
                ' throws ',
                ', '.join(field.type.java_declaration_name()
                           for field in self.throws)
            )
        return """\
public %(return_type_name)s %(name)s(%(parameters)s)%(throws)s;""" % locals()

    def java_message_types(self):
        return [self.java_request_type(), self.java_response_type()]

    def java_name(self, boxed=False):
        return lower_camelize(self.name)

    def java_qname(self, boxed=False):
        return self.parent.java_qname() + '.' + self.java_name()

    def java_request_type(self, **kwds):
        return self._JavaRequestType(parent_function=self, **kwds)

    def java_response_type(self, **kwds):
        return self._JavaResponseType(parent_function=self, **kwds)

    def __repr__(self):
        return self.java_declaration()
