#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------

from thryft.generators.java import java_generator
from yutil import indent, lower_camelize


class JsonRpcClientJavaGenerator(java_generator.JavaGenerator):
    class Document(java_generator.JavaGenerator.Document):
        def java_package(self):
            try:
                return self.namespace_by_scope(('json_rpc_client_java', 'java')).name
            except KeyError:
                return None

    class Function(java_generator.JavaGenerator.Function):
        def java_repr(self):
            name = self.name
            java_name = self.java_name()
            parameters = ', '.join(parameter.java_parameter(final=True) for parameter in self.parameters)
            parameter_names = ', '.join(parameter.java_name() for parameter in self.parameters)
            request_type_name = self.java_request_type().java_name()
            response_type_name = self.java_response_type().java_name()
            service_qname = self.parent.java_qname()
            if self.return_field is not None:
                service_response_assignment = "%(service_qname)s.Messages.%(response_type_name)s __serviceResponse = " % locals()
                service_response_return_value_getter_name = self.return_field.java_getter_name()
                return_statement = indent(' ' * 8, """
return __serviceResponse.%(service_response_return_value_getter_name)s();
""" % locals())
                return_type_qname = self.return_field.type.java_qname()
            else:
                service_response_assignment = ''
                return_statement = ''
                return_type_qname = 'void'

            return """\
public final %(return_type_qname)s %(java_name)s(%(parameters)s) {
    final %(service_qname)s.Messages.%(request_type_name)s __serviceRequest = new %(service_qname)s.Messages.%(request_type_name)s(%(parameter_names)s);
    final String __id = Integer.toString(System.identityHashCode(__serviceRequest));

    try {
        final java.io.StringWriter __oStringWriter = new java.io.StringWriter();
        final org.thryft.protocol.JsonRpcOutputProtocol __oprot = new org.thryft.protocol.JsonRpcOutputProtocol(new org.thryft.protocol.JacksonJsonOutputProtocol(__oStringWriter));
        __oprot.writeMessageBegin("%(name)s", org.thryft.protocol.MessageType.CALL, __id);
        __serviceRequest.write(__oprot);
        __oprot.writeMessageEnd();
        __oprot.flush();
        final String __oString = __oStringWriter.toString();

        final java.net.HttpURLConnection __connection = (java.net.HttpURLConnection)jsonRpcUrl.openConnection();
        __connection.setRequestMethod("POST");
        __connection.setRequestProperty("Content-Type", "application/json");
        __connection.setUseCaches(false);
        __connection.setDoInput(true);
        __connection.setDoOutput(true);
        try (final java.io.OutputStream __connectionOutputStream = __connection.getOutputStream()) {
            __connectionOutputStream.write(__oString.getBytes("UTF-8"));
            __connectionOutputStream.flush();
        }

        final String __iString;
        try (final java.io.InputStream __connectionInputStream = __connection.getInputStream()) {
            try (final java.util.Scanner __connectionInputScanner = new java.util.Scanner(__connectionInputStream).useDelimiter("\\\\A")) {
                __iString = __connectionInputScanner.hasNext() ? __connectionInputScanner.next() : "";
            }
        }
        final org.thryft.protocol.JsonRpcInputProtocol __iprot = new org.thryft.protocol.JsonRpcInputProtocol(new org.thryft.protocol.JacksonJsonInputProtocol(new java.io.StringReader(__iString)));
        final org.thryft.protocol.MessageBegin __messageBegin = __iprot.readMessageBegin();
        if (!__messageBegin.getId().equals(__id)) {
            throw new org.thryft.protocol.InputProtocolException(String.format("expected id in response to be %%s, got %%s", __id, __messageBegin.getId()));
        }
        if (__messageBegin.getType() == org.thryft.protocol.MessageType.EXCEPTION) {
            final org.thryft.protocol.JsonRpcErrorResponse __error = org.thryft.protocol.JsonRpcErrorResponse.read(__iprot);
            __iprot.readMessageEnd();
            throw __error;
        } else if (__messageBegin.getType() != org.thryft.protocol.MessageType.REPLY) {
            throw new org.thryft.protocol.InputProtocolException("expected response message");
        }
        %(service_response_assignment)snew %(service_qname)s.Messages.%(response_type_name)s(__iprot);
        __iprot.readMessageEnd();%(return_statement)s
    } catch (final java.io.IOException e) {
        throw new RuntimeException(e);
    } catch (final org.thryft.protocol.ProtocolException e) {
        throw new RuntimeException(e);
    }
}
""" % locals()

    class Service(java_generator.JavaGenerator.Service):
        def java_name(self, boxed=False):
            return 'JsonRpcClient' + java_generator.JavaGenerator.Service.java_name(self)

        def _java_constructor(self):
            name = self.java_name()
            name_lower_camelized = lower_camelize(name)
            return """\
@com.google.inject.Inject
public %(name)s(@com.google.inject.name.Named("%(name_lower_camelized)sUrl") final java.net.URL jsonRpcUrl) {
    this.jsonRpcUrl = com.google.common.base.Preconditions.checkNotNull(jsonRpcUrl);
}
""" % locals()

        def _java_member_declarations(self):
            return [
                "private final java.net.URL jsonRpcUrl;",
                # "private final static org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(%(name)s.class);" % locals(),
            ]


        def _java_methods(self):
            methods = []
            methods.append(self._java_constructor())
            # methods.append(self._java_method_do_post())
            # methods.append(self._java_method_do_post_error())
            # methods.append(self._java_method_do_post_response())
            methods.extend(function.java_repr() for function in self.functions)
            return methods

        def java_repr(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)

            sections = []
            sections.append("\n".join(self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            return """\
public class %(name)s implements %(service_qname)s {
%(sections)s
}""" % locals()
