# -----------------------------------------------------------------------------
# Copyright (c) 2016, Minor Gordon
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

from thryft.compiler.parser import Parser
from thryft.generators.java import java_generator
from thryft.generators.java.java_log_exception_stack_trace_annotation_parser import JavaLogExceptionStackTraceAnnotationParser
from thryft.generators.java.java_log_level_annotation_parser import JavaLogLevelAnnotationParser
from thryft.generators.java.java_log_levels import JAVA_LOG_LEVELS
from yutil import indent, lpad, decamelize


class LoggingServiceJavaGenerator(java_generator.JavaGenerator):
    def __init__(self, call_log_level_default='info', exception_log_level_default='error', include_current_user=False, **kwds):
        java_generator.JavaGenerator.__init__(self, **kwds)
        self._call_log_level_default = call_log_level_default.lower()
        if not self._call_log_level_default in JAVA_LOG_LEVELS:
            raise ValueError("call log level default is not a valid log level: '%s'" % self._call_log_level_default)
        self._exception_log_level_default = exception_log_level_default.lower()
        if not self._exception_log_level_default in JAVA_LOG_LEVELS:
            raise ValueError("exception log level default is not a valid log level: '%s'" % self._exception_log_level_default)
        self._include_current_user = include_current_user

    class Document(java_generator.JavaGenerator.Document):  # @UndefinedVariable
        def java_package(self):
            try:
                return self.namespace_by_scope(('logging_service_java', 'java')).name
            except KeyError:
                return None

    class Function(java_generator.JavaGenerator.Function):  # @UndefinedVariable
        def java_definitions(self):
            call_log_level = self._parent_generator()._call_log_level_default
            for annotation in self.annotations:
                if annotation.name == 'java_log_level':
                    call_log_level = annotation.value
                    break
            java_name = self.java_name()
            name = self.name

            marker = 'Markers.' + self.java_marker_variable_name()

            if self._parent_generator()._include_current_user:
                log_current_user = lpad("\n\n", """\
    final org.apache.shiro.subject.Subject currentUser = org.apache.shiro.SecurityUtils.getSubject();
    if (currentUser.getPrincipal() != null) {
        org.slf4j.MDC.put("shiro.subject.principal", currentUser.getPrincipal().toString());
    }""" % locals())
            else:
                log_current_user = ''

            parameters = \
                ', '.join([parameter.java_parameter(final=True)
                           for parameter in self.parameters])
            parameter_names = ', '.join([parameter.java_name()
                                         for parameter in self.parameters])

            request_type_name = self.java_request_type().java_name()

            if len(self.parameters) > 0:
                log_parameters = indent(' ' * 4, """
__logMessageStringBuilder.append("{}");
__logMessageArgs.add(Messages.%(request_type_name)s.create(%(parameter_names)s));
""" % locals())
            else:
                log_parameters = ''

            return_type_name = \
                self.return_field is not None and \
                    self.return_field.type.java_qname() or \
                    'void'

            service_call = """\
delegate.%(java_name)s(%(parameter_names)s);
""" % locals()
            if self.return_field is not None:
                service_call = self.return_field.type.java_qname() + ' __returnValue = ' + service_call
                service_call += """
__logMessageStringBuilder.append(" -> {}");
__logMessageArgs.add(__returnValue);

logger.%(call_log_level)s(%(marker)s, __logMessageStringBuilder.toString(), __logMessageArgs.toArray());

return __returnValue;
""" % locals()
            else:
                service_call += """
logger.%(call_log_level)s(%(marker)s, __logMessageStringBuilder.toString(), __logMessageArgs.toArray());
""" % locals()
            service_call = indent(' ' * 4, service_call)
            if len(self.throws) > 0:
                catches = []
                for throw in self.throws:
                    exception_log_level = self._parent_generator()._exception_log_level_default
                    exception_log_stack_trace = False
                    exception_type_name = throw.type.java_qname()
                    for annotations in (throw.annotations, throw.type.annotations):
                        for annotation in annotations:
                            if annotation.name == 'java_log_level':
                                exception_log_level = annotation.value
                            elif annotation.name == 'java_log_exception_stack_trace':
                                exception_log_stack_trace = annotation.value
                    exception_message = '' if exception_log_stack_trace else '{}'
                    exception_to_string = '' if exception_log_stack_trace else '.toString()'
                    catches.append("""\
catch (final %(exception_type_name)s e) {
        __logMessageStringBuilder.append(" -> %(exception_message)s");
        __logMessageArgs.add(e%(exception_to_string)s);
        logger.%(exception_log_level)s(%(marker)s, __logMessageStringBuilder.toString(), __logMessageArgs.toArray());
        throw e;
    }""" % locals())
                service_call = """\
    try {
%s
    } %s""" % (indent(' ' * 4, service_call), ' '.join(catches))
            throws = \
                lpad(
                    ' throws ',
                    ', '.join([field.type.java_qname()
                               for field in self.throws])
                )
            return self._java_delegating_definitions() + ["""\
public %(return_type_name)s %(java_name)s(%(parameters)s)%(throws)s {%(log_current_user)s
    final StringBuilder __logMessageStringBuilder = new StringBuilder();
    final java.util.List<Object> __logMessageArgs = new java.util.ArrayList<Object>();

    __logMessageStringBuilder.append("%(name)s(");%(log_parameters)s
    __logMessageStringBuilder.append(")");

%(service_call)s
}""" % locals()]

        def java_marker_name(self):
#             return decamelize(self.parent.name).upper() + '_' + self.name.upper()
            return self.name.upper()

        def java_marker_variable_name(self):
            return self.name.upper()

    class Service(java_generator.JavaGenerator.Service):  # @UndefinedVariable
        def __java_delegate_name(self):
            return "%s.%s.delegate" % (self._parent_document().java_package(), self.java_name())

        def java_name(self):
            return 'Logging' + java_generator.JavaGenerator.Service.java_name(self)  # @UndefinedVariable

        def _java_constructor(self):
            delegate_name = self.__java_delegate_name()
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)  # @UndefinedVariable
            return """\
@com.google.inject.Inject
public %(name)s(@com.google.inject.name.Named("%(delegate_name)s") final %(service_qname)s delegate) {
    this.delegate = com.google.common.base.Preconditions.checkNotNull(delegate);
}""" % locals()

        def __java_markers(self):
            service_marker_variable_name = service_marker_name = decamelize(self.name).upper()
            add_function_markers = []
            function_markers = []
            for function in self.functions:
                function_marker_variable_name = function.java_marker_variable_name()
                function_markers.append(
                    "public final static org.slf4j.Marker %s = org.slf4j.MarkerFactory.getMarker(\"%s\");" % (
                        function_marker_variable_name,
                        function.java_marker_name()
                ))
                add_function_markers.append("%(service_marker_variable_name)s.add(%(function_marker_variable_name)s);" % locals())
            add_function_markers = "\n".join(indent(' ' * 8, add_function_markers))
            function_markers = "\n".join(indent(' ' * 4, function_markers))
            return """\
public static class Markers {
%(function_markers)s

    public final static org.slf4j.Marker %(service_marker_variable_name)s = org.slf4j.MarkerFactory.getMarker("%(service_marker_name)s");
    static {
%(add_function_markers)s
    }
}""" % locals()

        def _java_member_declarations(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)  # @UndefinedVariable
            return [
                "private final static org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(%(name)s.class);" % locals(),
                "private final %(service_qname)s delegate;" % locals()
            ]

        def _java_methods(self):
            methods = []
            for function in self.functions:
                methods.extend(function.java_definitions())
            return methods

        def java_repr(self):
            delegate_name = self.__java_delegate_name()
            name = self.java_name()

            sections = []
            sections.append(self.__java_markers())
            sections.append("""public final static com.google.inject.name.Named DELEGATE_NAME = com.google.inject.name.Names.named("%(delegate_name)s");""" % locals())
            sections.append("\n\n".join([self._java_constructor()] + self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            service_qname = java_generator.JavaGenerator.Service.java_qname(self)  # @UndefinedVariable

            return """\
@com.google.inject.Singleton
public class %(name)s implements %(service_qname)s {
%(sections)s
}""" % locals()


Parser.register_annotation_parser(JavaLogExceptionStackTraceAnnotationParser())
Parser.register_annotation_parser(JavaLogLevelAnnotationParser())
