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

from yutil import indent, upper_camelize
from thryft.generators.java import _servlet_java_generator


class JsonRpcServletJavaGenerator(_servlet_java_generator._ServletJavaGenerator):
    class Document(_servlet_java_generator._ServletJavaGenerator._Document):
        def __init__(self, **kwds):
            _servlet_java_generator._ServletJavaGenerator._Document.__init__(self, servlet_type='json_rpc', **kwds)

    class Function(_servlet_java_generator._ServletJavaGenerator._Function):
        def __repr__(self):
            name = self.java_name()
            request_type_name = self.java_request_type().java_name()
            service_qname = self.parent.java_qname()
            upper_camelized_name = upper_camelize(self.name)

            if len(self.parameters) > 0:
                read_request = """
    final %(service_qname)s.Messages.%(request_type_name)s serviceRequest;
    try {
        serviceRequest = new %(service_qname)s.Messages.%(request_type_name)s(new org.thryft.protocol.JsonProtocol(jsonrpcRequestParams), jsonrpcRequestParams.isObject() ? org.thryft.protocol.TType.STRUCT : org.thryft.protocol.TType.LIST);
    } catch (final IllegalArgumentException e) {
        logger.debug("error deserializing service request: ", e);
        __doPostError(httpServletRequest, httpServletResponse, null, -32602, "invalid JSON-RPC request method parameters: " + String.valueOf(e.getMessage()), jsonrpcRequestId);
        return;
    } catch (final NullPointerException e) {
        logger.debug("error deserializing service request: ", e);
        __doPostError(httpServletRequest, httpServletResponse, null, -32602, "invalid JSON-RPC request method parameters: " + String.valueOf(e.getMessage()), jsonrpcRequestId);
        return;
    } catch (final java.io.IOException e) {
        logger.debug("error deserializing service request: ", e);
        __doPostError(httpServletRequest, httpServletResponse, null, -32602, "invalid JSON-RPC request method parameters: " + String.valueOf(e.getMessage()), jsonrpcRequestId);
        return;
    }
""" % locals()
            else:
                read_request = ''
            parameters = ', '.join(['serviceRequest.' + parameter.java_getter_name() + '()'
                                    for parameter in self.parameters])
            service_call = "service.%(name)s(%(parameters)s);" % locals()
            if self.return_field is not None:
                service_call = 'result = ' + service_call
            if len(self.throws) > 0:
                catches = ' '.join(["""\
catch (final %s e) {
    __doPostError(httpServletRequest, httpServletResponse, e, 1, e.getClass().getCanonicalName() + ": " + String.valueOf(e.getMessage()), jsonrpcRequestId);
    return;
}""" % throw.type.java_qname() for throw in self.throws])
                service_call = """\
try {
    %(service_call)s
} %(catches)s
""" % locals()
            service_call = indent(' ' * 4, service_call)

            return """\
private void __doPost%(upper_camelized_name)s(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse, final com.fasterxml.jackson.databind.JsonNode jsonrpcRequestParams, final Object jsonrpcRequestId) throws java.io.IOException {%(read_request)s
    Object result = null;
%(service_call)s

    __doPostResponse(httpServletRequest, httpServletResponse, jsonrpcRequestId, result);
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
                function_dispatches = """\
__doPostError(httpServletRequest, httpServletResponse, null, -32601, "The jsonrpcRequestMethod does not exist / is not available: " + jsonrpcRequestMethod);
return;
"""
            else:
                function_dispatches = \
                    indent(' ' * 4, ' else '.join(
                        ["""\
if (jsonrpcRequestMethod.equals("%s")) {
    __doPost%s(httpServletRequest, httpServletResponse, jsonrpcRequestParams, jsonrpcRequestId);
}""" % (function.name, upper_camelize(function.name))
                                   for function in self.functions
                        ] + ['''\
{
    __doPostError(httpServletRequest, httpServletResponse, null, -32601, "The jsonrpcRequestMethod does not exist / is not available: " + jsonrpcRequestMethod, jsonrpcRequestId);
    return;
}''']
                    ))
            return """\
protected void doPost(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse) throws java.io.IOException, javax.servlet.ServletException {
%(read_http_servlet_request_body)s

    final org.thryft.protocol.JsonRpcInputProtocol iprot = new org.thryft.protocol.JsonRpcInputProtocol(new org.thryft.protocol.JacksonJsonInputProtocol(httpServletRequestBody));
    final com.fasterxml.jackson.databind.JsonNode jsonrpcRequestNode;
    try {
        jsonrpcRequestNode = new com.fasterxml.jackson.databind.ObjectMapper().readTree(httpServletRequestBody);
    } catch (final com.fasterxml.jackson.core.JsonParseException e ){
        logger.error("error deserializing service request: ", e);
        __doPostError(httpServletRequest, httpServletResponse, null, -32700, String.valueOf(e.getMessage()), null);
        return;
    }

    final com.fasterxml.jackson.databind.JsonNode jsonrpcRequestIdNode = jsonrpcRequestNode.get("id");
    if (jsonrpcRequestIdNode == null) {
        __doPostError(httpServletRequest, httpServletResponse, null, -32600, "missing id field", null);
        return;
    }
    final Object jsonrpcRequestId;
    if (jsonrpcRequestIdNode.isTextual()) {
        jsonrpcRequestId = jsonrpcRequestIdNode.asText();
    } else if (jsonrpcRequestIdNode.isNumber()) {
        jsonrpcRequestId = jsonrpcRequestIdNode.decimalValue();
    } else if (jsonrpcRequestIdNode.isNull()) {
        jsonrpcRequestId = null;
    } else {
        __doPostError(httpServletRequest, httpServletResponse, null, -32600, "invalid id field type", null);
        return;
    }

    final com.fasterxml.jackson.databind.JsonNode jsonrpcRequestVersionNode = jsonrpcRequestNode.get("jsonrpc");
    if (jsonrpcRequestVersionNode == null || !jsonrpcRequestVersionNode.asText().equals("2.0")) {
        __doPostError(httpServletRequest, httpServletResponse, null, -32600, "invalid jsonrpc field, expected \\"2.0\\"", jsonrpcRequestId);
        return;
    }

    com.fasterxml.jackson.databind.JsonNode jsonrpcRequestMethodNode = jsonrpcRequestNode.get("method");
    if (jsonrpcRequestMethodNode == null) {
        __doPostError(httpServletRequest, httpServletResponse, null, -32600, "missing jsonrpcRequestMethod field", jsonrpcRequestId);
        return;
    }
    final String jsonrpcRequestMethod = jsonrpcRequestMethodNode.asText();

    final com.fasterxml.jackson.databind.JsonNode jsonrpcRequestParams = jsonrpcRequestNode.get("params");
    if (jsonrpcRequestParams == null) {
        __doPostError(httpServletRequest, httpServletResponse, null, -32600, "missing params field", jsonrpcRequestId);
        return;
    } else if (!jsonrpcRequestParams.isObject() && !jsonrpcRequestParams.isArray()) {
        __doPostError(httpServletRequest, httpServletResponse, null, -32600, "expected params object or array", jsonrpcRequestId);
    }

%(function_dispatches)s
}
""" % locals()

        def _java_method_do_post_error(self):
            write_http_servlet_response_body = indent(' ' * 4, self._java_write_http_servlet_response_body())
            return """\
private void __doPostError(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse, final Throwable jsonrpcErrorData, final int jsonrpcErrorCode, final String jsonrpcErrorMessage, final Object jsonrpcRequestId) throws java.io.IOException {
    final java.io.StringWriter httpServletResponseBodyWriter = new java.io.StringWriter();
    final org.thryft.protocol.JsonProtocol oprot = new org.thryft.protocol.JsonProtocol(httpServletResponseBodyWriter);

    try {
        oprot.writeStructBegin(new org.thryft.protocol.TStruct("response"));

        oprot.writeFieldBegin(new org.thryft.protocol.TField("jsonrpc", org.thryft.protocol.TType.STRING, (short)-1));
        oprot.writeString("2.0");
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.thryft.protocol.TField("id", org.thryft.protocol.TType.STRING, (short)-1));
        oprot.writeMixed(jsonrpcRequestId);
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.thryft.protocol.TField("error", org.thryft.protocol.TType.STRUCT, (short)-1));
        oprot.writeStructBegin(new org.thryft.protocol.TStruct("error"));

        oprot.writeFieldBegin(new org.thryft.protocol.TField("code", org.thryft.protocol.TType.I32, (short)-1));
        oprot.writeI32(jsonrpcErrorCode);
        oprot.writeFieldEnd();

        if (jsonrpcErrorData != null && jsonrpcErrorData instanceof org.thryft.TBase<?>) {
            oprot.writeFieldBegin(new org.thryft.protocol.TField("@class", org.thryft.protocol.TType.STRING, (short)-1));
            oprot.writeString(jsonrpcErrorData.getClass().getName());
            oprot.writeFieldEnd();
            oprot.writeFieldBegin(new org.thryft.protocol.TField("data", org.thryft.protocol.TType.STRUCT, (short)-1));
            ((org.thryft.TBase<?>)jsonrpcErrorData).write(oprot);
            oprot.writeFieldEnd();
        }

        oprot.writeFieldBegin(new org.thryft.protocol.TField("message", org.thryft.protocol.TType.STRING, (short)-1));
        oprot.writeString(jsonrpcErrorMessage);
        oprot.writeFieldEnd();

        oprot.writeFieldStop(); // error
        oprot.writeStructEnd(); // error
        oprot.writeFieldEnd(); // error

        oprot.writeFieldStop(); // httpServletResponse
        oprot.writeStructEnd(); // httpServletResponse
    } catch (final java.io.IOException e) {
        logger.error("error serializing service error response: ", e);
        throw new IllegalStateException(e);
    }

    oprot.flush();
    String httpServletResponseBody = httpServletResponseBodyWriter.toString();

%(write_http_servlet_response_body)s
}
""" % locals()

        def _java_method_do_post_response(self):
            write_http_servlet_response_body = indent(' ' * 4, self._java_write_http_servlet_response_body())
            return """\
private void __doPostResponse(final javax.servlet.http.HttpServletRequest httpServletRequest, final javax.servlet.http.HttpServletResponse httpServletResponse, final Object jsonrpcRequestId, final Object jsonrpcResult) throws java.io.IOException {
    final java.io.StringWriter httpServletResponseBodyWriter = new java.io.StringWriter();
    final org.thryft.protocol.JsonProtocol oprot = new org.thryft.protocol.JsonProtocol(httpServletResponseBodyWriter);

    try {
        oprot.writeStructBegin(new org.thryft.protocol.TStruct("response"));

        oprot.writeFieldBegin(new org.thryft.protocol.TField("jsonrpc", org.thryft.protocol.TType.STRING, (short)-1));
        oprot.writeString("2.0");
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.thryft.protocol.TField("id", org.thryft.protocol.TType.STRING, (short)-1));
        oprot.writeMixed(jsonrpcRequestId);
        oprot.writeFieldEnd();

        oprot.writeFieldBegin(new org.thryft.protocol.TField("result", org.thryft.protocol.TType.STRING, (short)-1));
        oprot.writeMixed(jsonrpcResult);
        oprot.writeFieldEnd();

        oprot.writeFieldStop(); // httpServletResponse
        oprot.writeStructEnd(); // httpServletResponse
    } catch (final java.io.IOException e) {
        logger.error("error serializing service response: ", e);
        throw new IllegalStateException(e);
    }

    oprot.flush();
    String httpServletResponseBody = httpServletResponseBodyWriter.toString();

%(write_http_servlet_response_body)s
}
""" % locals()

        def _java_methods(self):
            methods = []
            methods.append(self._java_constructor())
            methods.append(self._java_method_do_post())
            methods.append(self._java_method_do_post_error())
            methods.append(self._java_method_do_post_response())
            methods.extend([repr(function) for function in self.functions])
            return methods

        def __repr__(self):
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
