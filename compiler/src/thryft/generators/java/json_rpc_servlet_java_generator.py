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

from thryft.generators.java import java_generator
from yutil import indent, rpad, upper_camelize


class JsonRpcServletJavaGenerator(java_generator.JavaGenerator):
    class Document(java_generator.JavaGenerator.Document):  # @UndefinedVariable
        def java_package(self):
            try:
                return self.namespace_by_scope(('json_rpc_servlet_java', 'servlet_java')).name
            except KeyError:
                return java_generator.JavaGenerator.Document.java_package(self)

    class Function(java_generator.JavaGenerator.Function):  # @UndefinedVariable
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
        serviceRequest = %(service_qname)s.Messages.%(request_type_name)s.readAs(iprot, iprot.getCurrentFieldType(), unknownFieldCallback);
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

        def _java_read_http_servlet_request_body(self, **kwds):
            return self.parent._java_read_http_servlet_request_body(**kwds)

        def _java_write_http_servlet_response_body(self, **kwds):
            return self.parent._java_write_http_servlet_response_body(**kwds)

    class Service(java_generator.JavaGenerator.Service):  # @UndefinedVariable
        def java_name(self):
            return java_generator.JavaGenerator.Service.java_name(self) + 'JsonRpcServlet'  # @UndefinedVariable

        def _java_constructor(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)  # @UndefinedVariable
            return """\
@com.google.inject.Inject
public %(name)s(final %(service_qname)s service) {
    this.service = service;
}
""" % locals()

        def _java_member_declarations(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)  # @UndefinedVariable
            return [
                "private final static org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(%(name)s.class);" % locals(),
                "private final static com.google.common.base.Optional<org.thryft.CompoundType.UnknownFieldCallback> unknownFieldCallback = com.google.common.base.Optional.of(new org.thryft.CompoundType.UnknownFieldCallback() { public void apply(final org.thryft.protocol.FieldBegin field) throws org.thryft.protocol.InputProtocolException { throw new org.thryft.protocol.InputProtocolException(\"unknown field \" + field); } });",
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

        def _java_write_http_servlet_response_body(self, content_type='application/json; charset=utf-8', variable_name_prefix=''):
            return """\
%(variable_name_prefix)shttpServletResponse.setContentType("%(content_type)s");

if (%(variable_name_prefix)shttpServletResponseBody.length() >= 128) {
    final String %(variable_name_prefix)shttpServletRequestAcceptEncoding = %(variable_name_prefix)shttpServletRequest.getHeader("Accept-Encoding");
    if (%(variable_name_prefix)shttpServletRequestAcceptEncoding != null && !%(variable_name_prefix)shttpServletRequestAcceptEncoding.isEmpty()) {
        final String[] contentCodings = %(variable_name_prefix)shttpServletRequestAcceptEncoding.split(",");
        final java.util.TreeMap<java.math.BigDecimal, String> contentCodingsMap = new java.util.TreeMap<java.math.BigDecimal, String>();
        java.math.BigDecimal nextQvalue = new java.math.BigDecimal(Long.MAX_VALUE);
        for (final String contentCoding : contentCodings) {
            final String[] contentCodingSplit = contentCoding.split(";", 2);
            final String name = contentCodingSplit[0].trim();
            final java.math.BigDecimal qvalue;
            if (contentCodingSplit.length == 2) {
                final String[] qvalueSplit = contentCodingSplit[1].split("=", 2);
                if (qvalueSplit.length == 2) {
                    try {
                        qvalue = new java.math.BigDecimal(qvalueSplit[1].trim());
                        if (qvalue == java.math.BigDecimal.ZERO) {
                            continue;
                        }
                    } catch (final NumberFormatException e) {
                        continue;
                    }
                } else {
                    continue;
                }
            } else {
                qvalue = nextQvalue;
                nextQvalue = nextQvalue.subtract(java.math.BigDecimal.ONE);
            }
            contentCodingsMap.put(qvalue, name);
        }

        if (!contentCodingsMap.isEmpty()) {
            final String contentCoding = contentCodingsMap.lastEntry().getValue();
            if (contentCoding.equals("deflate") || contentCoding.equals("gzip")) {
                final java.io.ByteArrayOutputStream byteArrayOutputStream = new java.io.ByteArrayOutputStream();

                final java.util.zip.DeflaterOutputStream compressingOutputStream;
                if (contentCoding.equals("deflate")) {
                    compressingOutputStream = new java.util.zip.DeflaterOutputStream(byteArrayOutputStream);
                } else {
                    compressingOutputStream = new java.util.zip.GZIPOutputStream(byteArrayOutputStream);
                }

                byte[] compressedHttpServletResponseBody = null;
                try {
                    try {
                        compressingOutputStream.write(%(variable_name_prefix)shttpServletResponseBody.getBytes("UTF-8"));
                        compressingOutputStream.finish();
                        compressedHttpServletResponseBody = byteArrayOutputStream.toByteArray();
                    } finally {
                        compressingOutputStream.close();
                    }
                } catch (java.io.IOException e) {
                }

                if (compressedHttpServletResponseBody != null) {
                    %(variable_name_prefix)shttpServletResponse.setHeader("Content-Encoding", contentCoding);
                    %(variable_name_prefix)shttpServletResponse.getOutputStream().write(compressedHttpServletResponseBody);
                    return;
                }
            }
        }
    }
}

%(variable_name_prefix)shttpServletResponse.getOutputStream().write(%(variable_name_prefix)shttpServletResponseBody.getBytes("UTF-8"));""" % locals()

        def _java_read_http_servlet_request_body(self, variable_name_prefix=''):
            return """\
final String %(variable_name_prefix)shttpServletRequestContentEncoding = %(variable_name_prefix)shttpServletRequest.getHeader("Content-Encoding");
java.io.InputStream %(variable_name_prefix)shttpServletRequestInputStream = %(variable_name_prefix)shttpServletRequest.getInputStream();
if (%(variable_name_prefix)shttpServletRequestContentEncoding != null) {
    if (%(variable_name_prefix)shttpServletRequestContentEncoding.equals("deflate")) {
        %(variable_name_prefix)shttpServletRequestInputStream = new java.util.zip.InflaterInputStream(%(variable_name_prefix)shttpServletRequestInputStream);
    } else if (%(variable_name_prefix)shttpServletRequestContentEncoding.equals("gzip")) {
        %(variable_name_prefix)shttpServletRequestInputStream = new java.util.zip.GZIPInputStream(%(variable_name_prefix)shttpServletRequestInputStream);
    }
}

final String %(variable_name_prefix)shttpServletRequestBody;
{
    final java.io.InputStreamReader %(variable_name_prefix)shttpServletRequestBodyReader = new java.io.InputStreamReader(%(variable_name_prefix)shttpServletRequestInputStream);
    final java.io.StringWriter %(variable_name_prefix)shttpServletRequestBodyWriter = new java.io.StringWriter();
    final char[] %(variable_name_prefix)shttpServletRequestBodyBuffer = new char[4096];
    int %(variable_name_prefix)shttpServletRequestBodyBufferReadRet = 0;
    while ((%(variable_name_prefix)shttpServletRequestBodyBufferReadRet = %(variable_name_prefix)shttpServletRequestBodyReader.read(%(variable_name_prefix)shttpServletRequestBodyBuffer)) != -1) {
        %(variable_name_prefix)shttpServletRequestBodyWriter.write(%(variable_name_prefix)shttpServletRequestBodyBuffer, 0, %(variable_name_prefix)shttpServletRequestBodyBufferReadRet);
    }
    %(variable_name_prefix)shttpServletRequestBody = %(variable_name_prefix)shttpServletRequestBodyWriter.toString();
}
""" % locals()

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
