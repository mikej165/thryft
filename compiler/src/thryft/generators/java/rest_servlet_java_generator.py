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

from thryft.generator._base_type import _BaseType
from thryft.generator.enum_type import EnumType
from thryft.generator.typedef import Typedef
from thryft.generators.java import _servlet_java_generator
from thryft.generators.java._java_base_type import _JavaBaseType
from thryft.generators.java.java_bool_type import JavaBoolType
from yutil import indent, rpad, decamelize, upper_camelize


class RestServletJavaGenerator(_servlet_java_generator._ServletJavaGenerator):
    class Document(_servlet_java_generator._ServletJavaGenerator._Document):
        def __init__(self, **kwds):
            _servlet_java_generator._ServletJavaGenerator._Document.__init__(self, servlet_type='rest', **kwds)

    class Function(_servlet_java_generator._ServletJavaGenerator._Function):
        def java_message_types(self):
            message_types = []
            request_type = self.java_request_type()
            if request_type is not None:
                message_types.append(request_type)
            return message_types

        def java_definition(self):
            annotations = self.java_annotations()
            name = '__do' + self.java_name()[0].upper() + self.java_name()[1:]

            sections = []

            variable_declarations = []
            for parameter in self.parameters:
                variable_declarations.append(parameter.java_local_declaration(final=False))
            if self.return_field is not None:
                variable_declarations.append(self.return_field.type.java_qname() + " __return_value;")
            if len(variable_declarations) > 0:
                sections.append("\n".join(indent(' ' * 4, variable_declarations)))

            read_request = []
            if len(self.parameters) > 0:
                path_parameter = self.java_rest_path_parameter()
                if path_parameter is None or len(self.parameters) > 1:
                    request_type_name = 'Messages.' + upper_camelize(self.name) + 'Request'
                else:
                    request_type_name = None
                if self.java_rest_request_method() in ('POST', 'PUT'):
                    read_http_servlet_request_body = self._java_read_http_servlet_request_body(variable_name_prefix='__')
                    read_request.append("""\
%(read_http_servlet_request_body)s
final org.thryft.protocol.InputProtocol __restRequestProtocol = new org.thryft.protocol.JacksonJsonInputProtocol(new java.io.StringReader(__httpServletRequestBody));
""" % locals())
                else:
                    if path_parameter is not None:
                        path_info_prefix = self.java_rest_path_prefix()
                        path_info_prefix_len = len(path_info_prefix)
                        path_parameter_name = path_parameter.java_name()
                        path_parameter_from_string = path_parameter.type.java_from_string("java.net.URLDecoder.decode(__httpServletRequest.getPathInfo().substring(%(path_info_prefix_len)u), \"UTF-8\")" % locals())
                        read_request.append("""\
if (__httpServletRequest.getPathInfo().length() > %(path_info_prefix_len)u) {
    %(path_parameter_name)s = %(path_parameter_from_string)s;
} else {
    __httpServletResponse.sendError(404);
    return;
}
""" % locals())
                    if path_parameter is None or len(self.parameters) > 1:
                        annotations.append('@SuppressWarnings("unchecked")')
                        read_request.append("""\
java.util.Map<String, String> __restRequestParameterStringMap = new java.util.LinkedHashMap<String, String>();
for (final java.util.Map.Entry<String, String[]> __httpServletRequestParameter : ((java.util.Map<String, String[]>)__httpServletRequest.getParameterMap()).entrySet()) {
    __restRequestParameterStringMap.put(__httpServletRequestParameter.getKey(), __httpServletRequestParameter.getValue()[0]);
}
final org.thryft.protocol.InputProtocol __restRequestProtocol = new org.thryft.protocol.StringMapInputProtocol(__restRequestParameterStringMap);
""" % locals())
                if request_type_name is not None:
                    variable_assignments = []
                    for parameter in self.parameters:
                        if parameter is path_parameter:
                            continue
                        variable_assignments.append(parameter.java_name() + ' = __serviceRequest.' + parameter.java_getter_name() + '();')
                    variable_assignments = "\n".join(indent(' ' * 4, variable_assignments))
                    read_request.append("""\
try {
    final %(request_type_name)s __serviceRequest = new %(request_type_name)s(__restRequestProtocol);
%(variable_assignments)s
} catch (final IllegalArgumentException e) {
    logger.debug("error deserializing service request: ", e);
    __httpServletResponse.sendError(400);
    return;
} catch (final NullPointerException e) {
    logger.debug("error deserializing service request: ", e);
    __httpServletResponse.sendError(400);
    return;
} catch (final org.thryft.protocol.InputProtocolException e) {
    logger.debug("error deserializing service request: ", e);
    __httpServletResponse.sendError(400);
    return;
}
""" % locals())

            if len(read_request) > 0:
                sections.append("\n".join(indent(' ' * 4, read_request)))

            service_call = \
                "service.%s(%s);" % (
                    _servlet_java_generator._ServletJavaGenerator._Function.java_name(self),
                    ', '.join([parameter.java_name() for parameter in self.parameters])
                )
            if self.return_field is not None:
                service_call = '__return_value = ' + service_call
            if len(self.throws) > 0:
                catches = ' '.join(["""\
catch (final %s e) {
    final java.io.StringWriter __httpServletResponseBodyWriter = new java.io.StringWriter();
    final org.thryft.protocol.OutputProtocol __oprot = new org.thryft.protocol.JacksonJsonOutputProtocol(__httpServletResponseBodyWriter);
    try {
        e.write(__oprot);
        __oprot.flush();
    } catch (final org.thryft.protocol.OutputProtocolException e1) {
        logger.error("error serializing service error response: ", e1);
        __httpServletResponse.sendError(500);
        return;
    }
    final String __httpServletResponseBody = __httpServletResponseBodyWriter.toString();
    __httpServletResponse.getWriter().write(__httpServletResponseBody);
    __httpServletResponse.setHeader("Content-Type", "application/json");
    __httpServletResponse.setHeader("Warning", e.getClass().getName());
    __httpServletResponse.setStatus(404);
    return;
}""" % throw.type.java_qname() for throw in self.throws])
                service_call = """\
try {
    %(service_call)s
} %(catches)s
""" % locals()
            sections.append(indent(' ' * 4, service_call))

            if self.return_field is None:
                write_response = """\
    __httpServletResponse.setStatus(204);"""
            elif isinstance(self.return_field.type, JavaBoolType):
                # assert self.java_rest_request_method() in ('DELETE', 'HEAD'), self.java_rest_request_method()
                write_response = """\
    if (__return_value) {
        __httpServletResponse.setStatus(204);
    } else {
        __httpServletResponse.setStatus(404);
    }""" % locals()
            else:
                return_write = \
                    indent(' ' * 8, self.return_field.type.java_write_protocol('__return_value'))
                if isinstance(self.return_field.type, _JavaBaseType):
                    return_ttype_id = self.return_field.type.thrift_ttype_id()
                    return_write = """\
        oprot.writeListBegin(new org.thryft.protocol.TList((byte)%(return_ttype_id)u, 1));
%(return_write)s
        oprot.writeListEnd();""" % locals()
                write_http_servlet_response_body = indent(' ' * 4, self._java_write_http_servlet_response_body(variable_name_prefix='__'))
                write_response = """\
    final java.io.StringWriter __httpServletResponseBodyWriter = new java.io.StringWriter();
    final org.thryft.protocol.OutputProtocol oprot = new org.thryft.protocol.JacksonJsonOutputProtocol(__httpServletResponseBodyWriter);
    try {
%(return_write)s
        oprot.flush();
    } catch (final org.thryft.protocol.OutputProtocolException e) {
        logger.error("error serializing service response: ", e);
        __httpServletResponse.sendError(500);
        return;
    }
    String __httpServletResponseBody = __httpServletResponseBodyWriter.toString();

    __httpServletResponse.setStatus(200);

%(write_http_servlet_response_body)s
""" % locals()
            sections.append(write_response)

            annotations = rpad("\n".join(annotations), "\n")
            sections = "\n\n".join(sections)

            return """\
%(annotations)sprivate void %(name)s(final javax.servlet.http.HttpServletRequest __httpServletRequest, final javax.servlet.http.HttpServletResponse __httpServletResponse) throws java.io.IOException, javax.servlet.ServletException {
%(sections)s
}
""" % locals()

        def java_request_type(self):
            if len(self.parameters) == 0:
                return None
            path_parameter = self.java_rest_path_parameter()
            if path_parameter is None:
                return None
            parameters = [parameter for parameter in self.parameters
                          if parameter is not path_parameter]
            if len(parameters) == 0:
                return None
            return _servlet_java_generator._ServletJavaGenerator._Function.java_request_type(self, java_suppress_warnings=tuple(), parameters=parameters)

        def java_rest_path_prefix(self):
            name_split = self.name.split('_')
            request_method = self.java_rest_request_method()
            if request_method in ('GET', 'DELETE', 'HEAD'):
                try:
                    by_i = name_split.index('by')
                except ValueError:
                    by_i = None
                if by_i is not None:
                    return '/' + '_'.join(name_split[1:by_i]) + '/'
                else:
                    return '/' + '_'.join(name_split[1:])
            elif request_method in ('POST', 'PUT'):
                return '/' + '_'.join(name_split[1:])
            else:
                raise NotImplementedError(request_method)

        def java_rest_path_parameter(self):
            parameters = self.parameters
            if len(parameters) == 0:
                return None
            if self.java_rest_request_method() not in ('GET', 'DELETE', 'HEAD'):
                return None
            if parameters[0].required:
                if len(parameters) == 1 or \
                   len([parameter for parameter in parameters[1:] if not parameter.required]) == 0:
                    parameter0_type = parameters[0].type
                    if isinstance(parameter0_type, Typedef):
                        parameter0_type = parameter0_type.type
                    if isinstance(parameter0_type, _BaseType) or isinstance(parameter0_type, EnumType):
                        return parameters[0]
            return None

        def java_rest_request_method(self):
            request_method = self.name.split('_', 1)[0].upper()
            if request_method in ('GET', 'DELETE', 'HEAD', 'POST', 'PUT'):
                return request_method
            else:
                return 'GET'

    class Service(_servlet_java_generator._ServletJavaGenerator._Service):
        def java_name(self, boxed=False):
            return _servlet_java_generator._ServletJavaGenerator._Service.java_name(self) + 'RestServlet'

        def _java_constructor(self):
            name = self.java_name()
            service_qname = _servlet_java_generator._ServletJavaGenerator._Service.java_qname(self)
            return """\
@com.google.inject.Inject
public %(name)s(final %(service_qname)s service) {
    this.service = service;
}
""" % locals()

        def _java_member_declarations(self):
            name = self.java_name()
            service_qname = _servlet_java_generator._ServletJavaGenerator._Service.java_qname(self)
            return [
                "private final static org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(%(name)s.class);" % locals(),
                "private final %(service_qname)s service;" % locals()
            ]

        def _java_methods_public(self):
            methods = []
            functions_by_request_method = {}
            for function in self.functions:
                functions_by_request_method.setdefault(function.java_rest_request_method(), {}).setdefault(function.java_rest_path_prefix(), []).append(function)
            for request_method in sorted(functions_by_request_method.iterkeys()):
                dispatches = []
                functions_by_path_info_prefix = functions_by_request_method[request_method]
                path_info_prefixes = []
                # Arrange the path_info_prefixes to do longest match first, giving alphanums precedence over /
                for path_info_prefix in sorted(functions_by_path_info_prefix.iterkeys(), lambda left, right: cmp(left.replace('/', '|'), right.replace('/', '|'))):
                    inserted_path_info_prefix = False
                    for other_path_info_prefix_i, other_path_info_prefix in enumerate(path_info_prefixes):
                        if path_info_prefix.startswith(other_path_info_prefix):
                            if len(path_info_prefix) < len(other_path_info_prefix):
                                # If this path_info_prefix starts with the other and has a shorter length,
                                # insert it after the other (shorter match)
                                path_info_prefixes.insert(other_path_info_prefix_i + 1, path_info_prefix)
                            else:
                                # If this path_info_prefix starts with the other and has a longer length,
                                # insert it before the other (longer match)
                                assert len(path_info_prefix) > len(other_path_info_prefix)
                                path_info_prefixes.insert(other_path_info_prefix_i, path_info_prefix)
                            inserted_path_info_prefix = True
                            break
                    if not inserted_path_info_prefix:
                        path_info_prefixes.append(path_info_prefix)
                have_else = False
                for path_info_prefix in path_info_prefixes:
                    functions = functions_by_path_info_prefix[path_info_prefix]
                    if len(functions) == 1:
                        function = functions[0]
                    else:
                        # Multiple functions with the same request method and path_info_prefix
                        # Pick one
                        lucky_function = None
                        for function in functions:
                            if function.name.endswith('_by_id'):
                                lucky_function = function
                                break
                        if lucky_function is not None:
                            function = lucky_function
                        else:
                            function = functions[0]
                    private_name = '__do' + function.java_name()[0].upper() + function.java_name()[1:]
                    if len(path_info_prefix) > 0:
                        dispatches.append("""\
if (request.getPathInfo().startsWith("%(path_info_prefix)s")) {
    %(private_name)s(request, response);
}""" % locals())
                    else:
                        dispatches.append("""\
{
    %(private_name)s(request, response);
}""" % locals())
                        have_else = True
                if not have_else:
                    dispatches.append('''\
{
    response.sendError(404);
}''')
                dispatches = indent(' ' * 4, ' else '.join(dispatches))
                request_method_camelized = request_method[0] + request_method[1:].lower()
                methods.append("""\
@Override
public void do%(request_method_camelized)s(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response) throws java.io.IOException, javax.servlet.ServletException {
%(dispatches)s
}
""" % locals())
            return methods

        def _java_methods_private(self):
            return [function.java_definition() for function in self.functions]

        def _java_methods(self):
            methods = []
            methods.append(self._java_constructor())
            methods.extend(self._java_methods_public())
            methods.extend(self._java_methods_private())
            return methods

        def java_repr(self):
            name = self.java_name()

            sections = []

            message_types = []
            for function in self.functions:
                message_types.extend(function.java_message_types())
            service_qname = self.java_qname()
            if len(message_types) > 0:
                message_types = \
                    "\n\n".join(indent(' ' * 4,
                        (message_type.java_repr()
                         for message_type in message_types)
                    ))
                sections.append("""\
@SuppressWarnings("unused")
private final static class Messages extends %(service_qname)s.Messages {
%(message_types)s
}""" % locals())
            else:
                sections.append("""\
private final static class Messages extends %(service_qname)s.Messages {
}""" % locals())

            sections.append("\n".join(self._java_methods()))

            sections.append("\n".join(self._java_member_declarations()))

            sections = "\n\n".join(indent(' ' * 4, sections))

            return """\
@com.google.inject.Singleton
@SuppressWarnings("serial")
public class %(name)s extends javax.servlet.http.HttpServlet {
%(sections)s
}""" % locals()

        def java_rest_path_prefix(self):
            assert self.name.endswith('Service')
            return '/' + decamelize(self.name[:-len('Service')]) + '/'
