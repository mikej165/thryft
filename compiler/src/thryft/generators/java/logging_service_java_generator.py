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
from thryft.generators.java._java_container_type import _JavaContainerType
from thryft.generators.java.java_struct_type import JavaStructType
from yutil import indent, lpad
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class LoggingServiceJavaGenerator(java_generator.JavaGenerator):
    _LOG_LEVELS = ('debug', 'error', 'info', 'trace', 'warn')

    def __init__(self, call_log_level_default='info', exception_log_level_default='error', include_current_user=True, **kwds):
        java_generator.JavaGenerator.__init__(self, **kwds)
        self._call_log_level_default = call_log_level_default.lower()
        if not self._call_log_level_default in self._LOG_LEVELS:
            raise ValueError("call log level default is not a valid log level: '%s'" % self._call_log_level_default)
        self._exception_log_level_default = exception_log_level_default.lower()
        if not self._exception_log_level_default in self._LOG_LEVELS:
            raise ValueError("exception log level default is not a valid log level: '%s'" % self._exception_log_level_default)
        self._include_current_user = include_current_user

    class Document(java_generator.JavaGenerator.Document):
        def java_package(self):
            try:
                return self.namespace_by_scope(('logging_service_java', 'java')).name
            except KeyError:
                return None

    class Function(java_generator.JavaGenerator.Function):
        def java_definition(self):
            call_log_level = self._parent_generator()._call_log_level_default
            for annotation in self.annotations:
                if annotation.name == 'java_log_level':
                    call_log_level = annotation.value
                    break
            java_name = self.java_name()
            name = self.name

            local_declarations = []
            if len(self.parameters) > 0 or self.return_field is not None:
                local_declarations.append('java.io.StringWriter __logMessageStringWriter;')
                local_declarations.append('org.thryft.protocol.LogMessageOutputProtocol __logMessageProtocol;')
            local_declarations.append('final StringBuilder __logMessageStringBuilder = new StringBuilder();')
            local_declarations = "\n".join(indent(' ' * 4, local_declarations))

            if self._parent_generator()._include_current_user:
                log_current_user = lpad("\n\n", """\
    final org.apache.shiro.subject.Subject currentUser = org.apache.shiro.SecurityUtils.getSubject();
    if (currentUser.getPrincipal() instanceof String) {
        __logMessageStringBuilder.append((String)currentUser.getPrincipal());
        __logMessageStringBuilder.append(": " );
    }""" % locals())
            else:
                log_current_user = ''

            parameters = \
                ', '.join([parameter.java_parameter(final=True)
                           for parameter in self.parameters])
            parameter_names = ', '.join([parameter.java_name()
                                         for parameter in self.parameters])

            request_type_name = self.java_request_type().java_name()
            response_type_name = self.java_response_type().java_name()

            if len(self.parameters) > 0:
                parameters_toString = indent(' ' * 4, """
try {
    __logMessageStringWriter = new java.io.StringWriter();
    __logMessageProtocol = new org.thryft.protocol.LogMessageOutputProtocol(__logMessageStringWriter);
    new Messages.%(request_type_name)s(%(parameter_names)s).writeAsStruct(__logMessageProtocol);
    __logMessageProtocol.flush();
    __logMessageStringBuilder.append(__logMessageStringWriter.toString());
} catch (final org.thryft.protocol.OutputProtocolException e) {
    __logMessageStringBuilder.append("(serialization error)");
}
""" % locals())
            else:
                parameters_toString = ''

            return_type_name = \
                self.return_field is not None and \
                    self.return_field.type.java_declaration_name() or \
                    'void'

            service_call = """\
service.%(java_name)s(%(parameter_names)s);
""" % locals()
            if self.return_field is not None:
                service_call = self.return_field.type.java_qname(boxed=False) + ' __returnValue = ' + service_call
                if isinstance(self.return_field.type, _JavaContainerType) or isinstance(self.return_field.type, JavaStructType):
                    write_response_message = """\
{
    final org.thryft.protocol.OutputProtocol oprot = __logMessageProtocol;
%s
}""" % indent(' ' * 4, self.return_field.type.java_write_protocol('__returnValue', depth=0))
                else:
                    write_response_message = "new Messages.%(response_type_name)s(__returnValue).writeAsStruct(__logMessageProtocol);" % locals()
                write_response_message = indent(' ' * 4, write_response_message)
                service_call += """
__logMessageStringBuilder.append(" -> ");
try {
    __logMessageStringWriter = new java.io.StringWriter();
    __logMessageProtocol = new org.thryft.protocol.LogMessageOutputProtocol(__logMessageStringWriter);
%(write_response_message)s
    __logMessageProtocol.flush();
    __logMessageStringBuilder.append(__logMessageStringWriter.toString());
} catch (final org.thryft.protocol.OutputProtocolException e) {
    __logMessageStringBuilder.append("(serialization error)");
}
logger.%(call_log_level)s(__logMessageStringBuilder.toString());

return __returnValue;
""" % locals()
            else:
                service_call += """
logger.%(call_log_level)s(__logMessageStringBuilder.toString());
""" % locals()
            service_call = indent(' ' * 4, service_call)
            if len(self.throws) > 0:
                catches = []
                for throw in self.throws:
                    exception_log_level = self._parent_generator()._exception_log_level_default
                    for annotation in throw.annotations:
                        if annotation.name == 'java_log_level':
                            exception_log_level = annotation.value
                            break
                    catches.append("""\
catch (final %s e) {
        __logMessageStringBuilder.append(" -> ");
        logger.%s(__logMessageStringBuilder.toString(), e);
        throw e;
    }""" % (throw.type.java_declaration_name(), exception_log_level))
                service_call = """\
    try {
%s
    } %s""" % (indent(' ' * 4, service_call), ' '.join(catches))
            throws = \
                lpad(
                    ' throws ',
                    ', '.join([field.type.java_declaration_name()
                               for field in self.throws])
                )
            return """\
public %(return_type_name)s %(java_name)s(%(parameters)s)%(throws)s {
%(local_declarations)s%(log_current_user)s

    __logMessageStringBuilder.append("%(name)s(");%(parameters_toString)s
    __logMessageStringBuilder.append(")");

%(service_call)s
}""" % locals()

    class Service(java_generator.JavaGenerator.Service):
        def java_name(self, boxed=False):
            return 'Logging' + java_generator.JavaGenerator.Service.java_name(self)

        def _java_constructor(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)
            return """\
@com.google.inject.Inject
public %(name)s(@com.google.inject.name.Named("impl") final %(service_qname)s service) {
    this.service = service;
}""" % locals()

        def _java_member_declarations(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)
            return [
                "private final static org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(%(name)s.class);" % locals(),
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

            service_qname = java_generator.JavaGenerator.Service.java_qname(self)

            return """\
@com.google.inject.Singleton
public class %(name)s implements %(service_qname)s {
%(sections)s
}""" % locals()

def __parse_java_log_level(ast_node, name, value, **kwds):
    assert isinstance(ast_node, Ast.FieldNode)

    value_lower = value.lower()
    if not value_lower in LoggingServiceJavaGenerator._LOG_LEVELS:
        raise ValueError("@%s has an invalid log level: '%s', exception: %s" % (name, value))

    ast_node.annotations.append(Ast.AnnotationNode(name=name, value=value_lower, **kwds))

Parser.register_annotation(Ast.FieldNode, 'java_log_level', __parse_java_log_level)
