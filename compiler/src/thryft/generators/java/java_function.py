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

from thryft.generator.function import Function
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from thryft.generators.java.java_struct_type import JavaStructType
from yutil import lower_camelize, lpad, indent, upper_camelize


class JavaFunction(Function, _JavaNamedConstruct):
    class _JavaMessageType(JavaStructType):
        pass

    class _JavaRequestType(_JavaMessageType):
        def __init__(self, parent_function, java_suppress_warnings=None, parameters=None):
            JavaFunction._JavaMessageType.__init__(
                self,
                java_class_modifiers='public final static',
                java_suppress_warnings=java_suppress_warnings,
                name=upper_camelize(parent_function.name) + 'Request',
                parent=parent_function.parent
            )

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

    class _JavaResponseType(_JavaMessageType):
        def __init__(self, parent_function, java_suppress_warnings=None):
            JavaFunction._JavaMessageType.__init__(
                self,
                java_class_modifiers='public final static',
                java_suppress_warnings=java_suppress_warnings,
                name=upper_camelize(parent_function.name) + 'Response',
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
public %(name)s(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {%(field_initializer)s
}""" % locals()

    def java_annotations(self):
        annotations = []
        for requires_x in ('authentication', 'guest', 'user'):
            for annotation in self.annotations:
                if annotation.name == 'requires_' + requires_x:
                    annotations.append('@org.apache.shiro.authz.annotation.Requires' + requires_x.capitalize())
                    break
        for requires_x in ('permissions', 'roles'):
            for annotation in self.annotations:
                if annotation.name == 'requires_' + requires_x:
                    annotations.append("@org.apache.shiro.authz.annotation.Requires%s({ %s })" % (
                        requires_x.capitalize(),
                        ', '.join('"%s"' % x for x in annotation.value)
                    ))
                    break
        return annotations

    def java_declaration(self):
        javadoc = self.java_doc()

        name = self.java_name()

        parameters = \
            ', '.join(parameter.java_parameter(final=True) for parameter in self.parameters)

        if self.return_field is not None:
            return_type_name = self.return_field.type.java_declaration_name()
        else:
            return_type_name = 'void'

        throws = \
            lpad(
                ' throws ',
                ', '.join(field.type.java_declaration_name()
                           for field in self.throws)
            )

        return """\
%(javadoc)spublic %(return_type_name)s %(name)s(%(parameters)s)%(throws)s;""" % locals()

    def java_doc(self):
        javadoc_lines = []
        if self.doc is not None:
            javadoc_lines.extend(line.strip() for line in self.doc.splitlines())
            javadoc_lines.append('')

        name = self.java_name()

        for parameter in self.parameters:
            if parameter.doc is not None:
                javadoc_lines.append("@param %s %s" % (parameter.name, parameter.doc))

        if self.return_field is not None and self.return_field.doc is not None:
            javadoc_lines.append('@return ' + self.return_field.doc)

        for field in self.throws:
            if field.doc is not None:
                javadoc_lines.append("@throws %s %s" % (field.type.java_qname(), field.doc))

        if len(javadoc_lines) > 0:
            javadoc_lines = "\n".join(' * ' + javadoc_line for javadoc_line in javadoc_lines)
            return """\
/**
%(javadoc_lines)s
 */
""" % locals()
        else:
            return ''

    def java_message_types(self):
        message_types = [self.java_request_type()]
        if not self.oneway:
            message_types.append(self.java_response_type())
        return message_types

    def java_name(self, boxed=False):
        return lower_camelize(self.name)

    def java_qname(self, boxed=False):
        return self.parent.java_qname() + '.' + self.java_name()

    def java_request_type(self, **kwds):
        return self._JavaRequestType(parent_function=self, **kwds)

    def java_repr(self):
        return self.java_declaration()

    def java_response_type(self, **kwds):
        return self._JavaResponseType(parent_function=self, **kwds)
