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

from thryft.generators.java import _servlet_java_generator
from yutil import indent, rpad, upper_camelize


class JsonRpcServletJavaGenerator(_servlet_java_generator._ServletJavaGenerator):
    class Document(_servlet_java_generator._ServletJavaGenerator._Document):
        def __init__(self, **kwds):
            _servlet_java_generator._ServletJavaGenerator._Document.__init__(self, servlet_type='json_rpc', **kwds)

    class Function(_servlet_java_generator._ServletJavaGenerator._Function):
        def java_definition(self):
            annotations = rpad("\n".join(self.java_annotations()), "\n")
            name = self.java_name()
            request_type_name = self.java_request_type().java_name()
            service_qname = self.parent.java_qname()
            upper_camelized_name = upper_camelize(self.name)

            if len(self.parameters) > 0:
                read_request = """
    final %(service_qname)s.Messages.%(request_type_name)s serviceRequest;
    try {
        serviceRequest = %(service_qname)s.Messages.%(request_type_name)s.readAs(iprot, iprot.getCurrentFieldType());
    } catch (final IllegalArgumentException | org.thryft.protocol.InputProtocolException | NullPointerException e) {
        logger.debug("error deserializing service request: ", e);
        __doPostError(httpServletRequest, httpServletResponse, new org.thryft.protocol.JsonRpcErrorResponse(e, -32602, "invalid JSON-RPC request method parameters: " + String.valueOf(e.getMessage())), jsonRpcRequestId);
        return;
    }
""" % locals()
            else:
                read_request = ''
            parameters = ', '.join(['serviceRequest.' + parameter.java_getter_name() + '()'
                                    for parameter in self.parameters])
            service_call = "service.%(name)s(%(parameters)s);" % locals()
            if self.return_field is not None:
                result_declaration = "    final %s result;\n" % self.return_field.type.java_qname()
                service_call = 'result = ' + service_call
                write_result = self.return_field.type.java_write_protocol(value='result')
            else:
                result_declaration = ''
                write_result = '''\
oprot.writeStructBegin("response");
oprot.writeStructEnd();
'''
            write_result = indent(' ' * 12, write_result)
            if len(self.throws) > 0:
                catches = ' '.join(["""\
catch (final %s e) {
    __doPostError(httpServletRequest, httpServletResponse, new org.thryft.protocol.JsonRpcErrorResponse(e, 1, e.getClass().getCanonicalName() + ": " + String.valueOf(e.getMessage())), jsonRpcRequestId);
    return;
}""" % throw.type.java_qname() for throw in self.throws])
                service_call = """\
try {
    %(service_call)s
} %(catches)s
""" % locals()
            service_call = indent(' ' * 4, service_call)

            return """\
%(annotations)spublic void doPost%(upper_camelized_name)s(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse, final org.thryft.protocol.JsonRpcInputProtocol iprot, final Object jsonRpcRequestId) throws java.io.IOException {%(read_request)s
%(result_declaration)s%(service_call)s

    final String httpServletResponseBody;
    {
        final java.io.StringWriter httpServletResponseBodyWriter = new java.io.StringWriter();
        try {
            final org.thryft.protocol.JsonRpcOutputProtocol oprot = new org.thryft.protocol.JsonRpcOutputProtocol(new org.thryft.protocol.JacksonJsonOutputProtocol(httpServletResponseBodyWriter));
            oprot.writeMessageBegin("", org.thryft.protocol.MessageType.REPLY, jsonRpcRequestId);
%(write_result)s
            oprot.writeMessageEnd();
            oprot.flush();
        } catch (final org.thryft.protocol.OutputProtocolException e) {
            logger.error("error serializing service error response: ", e);
            throw new IllegalStateException(e);
        }
        httpServletResponseBody = httpServletResponseBodyWriter.toString();
    }
    __doPostResponse(httpServletRequest, httpServletResponse, httpServletResponseBody);
}
""" % locals()

    class Service(_servlet_java_generator._ServletJavaGenerator._Service):
        def java_name(self, boxed=False):
            return _servlet_java_generator._ServletJavaGenerator._Service.java_name(self) + 'JsonRpcServlet'

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

        def _java_method_do_post(self):
            read_http_servlet_request_body = indent(' ' * 4, self._java_read_http_servlet_request_body())
            function_dispatches = []
            if len(self.functions) == 0:
                function_dispatches = indent(' ' * 8, """\
__doPostError(httpServletRequest, httpServletResponse, new org.thryft.protocol.JsonRpcErrorResponse(-32601, String.format("the method '%s' does not exist / is not available", messageBegin.getName())), messageBegin.getId());
return;
""")
            else:
                function_dispatches = \
                    indent(' ' * 8, ' else '.join(
                        ["""\
if (messageBegin.getName().equals("%s")) {
    doPost%s(httpServletRequest, httpServletResponse, iprot, messageBegin.getId());
}""" % (function.name, upper_camelize(function.name))
                                   for function in self.functions
                        ] + ['''\
{
    __doPostError(httpServletRequest, httpServletResponse, new org.thryft.protocol.JsonRpcErrorResponse(-32601, String.format("the method '%s' does not exist / is not available", messageBegin.getName())), messageBegin.getId());
    return;
}''']
                    ))
            return """\
@Override
protected void doPost(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse) throws java.io.IOException, javax.servlet.ServletException {
%(read_http_servlet_request_body)s

    org.thryft.protocol.MessageBegin messageBegin = null;
    try {
        final org.thryft.protocol.JsonRpcInputProtocol iprot;
        try {
            iprot = new org.thryft.protocol.JsonRpcInputProtocol(new org.thryft.protocol.JacksonJsonInputProtocol(httpServletRequestBody));
            messageBegin = iprot.readMessageBegin();
        } catch (final org.thryft.protocol.JsonRpcInputProtocolException e) {
            throw e;
        } catch (final org.thryft.protocol.InputProtocolException e) {
            throw new org.thryft.protocol.JsonRpcInputProtocolException(e, -32600);
        }
        if (messageBegin.getType() != org.thryft.protocol.MessageType.CALL) {
            throw new org.thryft.protocol.JsonRpcInputProtocolException(-32600, "expected request");
        }
%(function_dispatches)s
    } catch (final org.thryft.protocol.JsonRpcInputProtocolException e) {
        __doPostError(httpServletRequest, httpServletResponse, new org.thryft.protocol.JsonRpcErrorResponse(e), messageBegin != null ? messageBegin.getId() : null);
        return;
    }
}
""" % locals()

        def _java_method_do_post_error(self):
            write_http_servlet_response_body = indent(' ' * 4, self._java_write_http_servlet_response_body())
            return """\
private void __doPostError(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse, final org.thryft.protocol.JsonRpcErrorResponse jsonRpcErrorResponse, @javax.annotation.Nullable final Object jsonRpcRequestId) throws java.io.IOException {
    final java.io.StringWriter httpServletResponseBodyWriter = new java.io.StringWriter();
    try {
        final org.thryft.protocol.JsonRpcOutputProtocol oprot = new org.thryft.protocol.JsonRpcOutputProtocol(new org.thryft.protocol.JacksonJsonOutputProtocol(httpServletResponseBodyWriter));
        oprot.writeMessageBegin("", org.thryft.protocol.MessageType.EXCEPTION, jsonRpcRequestId);
        jsonRpcErrorResponse.writeAsStruct(oprot);
        oprot.writeMessageEnd();
        oprot.flush();
    } catch (final org.thryft.protocol.OutputProtocolException e) {
        logger.error("error serializing service error response: ", e);
        throw new IllegalStateException(e);
    }
    __doPostResponse(httpServletRequest, httpServletResponse, httpServletResponseBodyWriter.toString());
}
""" % locals()

        def _java_method_do_post_response(self):
            write_http_servlet_response_body = indent(' ' * 4, self._java_write_http_servlet_response_body())
            return """\
private void __doPostResponse(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse, final String httpServletResponseBody) throws java.io.IOException {
%(write_http_servlet_response_body)s
}
""" % locals()

        def _java_methods(self):
            methods = []
            methods.append(self._java_constructor())
            methods.append(self._java_method_do_post())
            methods.append(self._java_method_do_post_error())
            methods.append(self._java_method_do_post_response())
            methods.extend(function.java_definition() for function in self.functions)
            return methods

        def java_repr(self):
            name = self.java_name()

            sections = []
            sections.append("\n".join(self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            return """\
@com.google.inject.Singleton
@SuppressWarnings("serial")
public class %(name)s extends javax.servlet.http.HttpServlet {
%(sections)s
}""" % locals()
