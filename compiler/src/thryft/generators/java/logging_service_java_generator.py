from thryft.generators.java import java_generator
from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import indent, lpad


class LoggingServiceJavaGenerator(java_generator.JavaGenerator):
    class Function(JavaFunction):
        def __repr__(self):
            java_name = self.java_name()
            name = self.name

            local_declarations = []
            if len(self.parameters) > 0 or self.return_field is not None:
                local_declarations.append('java.io.StringWriter __logMessageStringWriter;')
                local_declarations.append('org.thryft.protocol.LogMessageProtocol __logMessageProtocol;')
            local_declarations.append('final StringBuilder __logMessageStringBuilder = new StringBuilder();')
            local_declarations = "\n".join(indent(' ' * 4, local_declarations))

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
    __logMessageProtocol = new org.thryft.protocol.LogMessageProtocol(__logMessageStringWriter);
    new Messages.%(request_type_name)s(%(parameter_names)s).write(__logMessageProtocol);
    __logMessageProtocol.flush();
    __logMessageStringBuilder.append(__logMessageStringWriter.toString());
} catch (final java.io.IOException e) {
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
                service_call += """
__logMessageStringBuilder.append(" -> ");
try {
    __logMessageStringWriter = new java.io.StringWriter();
    __logMessageProtocol = new org.thryft.protocol.LogMessageProtocol(__logMessageStringWriter);
    new Messages.%(response_type_name)s(__returnValue).write(__logMessageProtocol, org.thryft.protocol.TType.VOID);
    __logMessageProtocol.flush();
    __logMessageStringBuilder.append(__logMessageStringWriter.toString());
} catch (final java.io.IOException e) {
    __logMessageStringBuilder.append("(serialization error)");
}
logger.info(__logMessageStringBuilder.toString());

return __returnValue;
""" % locals()
            else:
                service_call += """
logger.info(__logMessageStringBuilder.toString());
"""
            service_call = indent(' ' * 4, service_call)
            if len(self.throws) > 0:
                catches = ' '.join(["""\
catch (final %s e) {
        __logMessageStringBuilder.append(" -> ");
        __logMessageStringBuilder.append(e.getMessage());
        logger.error(__logMessageStringBuilder.toString());
        throw e;
    }""" % throw.type.java_declaration_name() for throw in self.throws])
                service_call = """\
    try {
%s
    } %s""" % (indent(' ' * 4, service_call), catches)

            throws = \
                lpad(
                    ' throws ',
                    ', '.join([field.type.java_declaration_name()
                               for field in self.throws])
                )
            return """\
public %(return_type_name)s %(java_name)s(%(parameters)s)%(throws)s {
%(local_declarations)s

    final org.apache.shiro.subject.Subject currentUser = org.apache.shiro.SecurityUtils.getSubject();
    if (currentUser.getPrincipal() instanceof String) {
        __logMessageStringBuilder.append((String)currentUser.getPrincipal());
        __logMessageStringBuilder.append(": " );
    }

    __logMessageStringBuilder.append("%(name)s(");%(parameters_toString)s
    __logMessageStringBuilder.append(")");

%(service_call)s
}""" % locals()

    class Service(JavaService):
        def java_name(self, boxed=False):
            return 'Logging' + JavaService.java_name(self)

        def _java_constructor(self):
            name = self.java_name()
            service_qname = JavaService.java_qname(self)
            return """\
@com.google.inject.Inject
public %(name)s(@com.google.inject.name.Named("impl") final %(service_qname)s service) {
    this.service = service;
}""" % locals()

        def _java_member_declarations(self):
            name = self.java_name()
            service_qname = JavaService.java_qname(self)
            return [
                "private final static org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(%(name)s.class);" % locals(),
                "private final %(service_qname)s service;" % locals()
            ]

        def _java_methods(self):
            return [repr(function) for function in self.functions]

        def __repr__(self):
            name = self.java_name()

            sections = []
            sections.append("\n\n".join([self._java_constructor()] + self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            service_qname = JavaService.java_qname(self)

            return """\
@com.google.inject.Singleton
public class %(name)s implements %(service_qname)s {
%(sections)s
}""" % locals()
