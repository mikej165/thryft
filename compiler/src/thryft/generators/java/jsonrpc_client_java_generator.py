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

import os.path

from thryft.generators.java import java_generator
from yutil import indent, upper_camelize


class JsonrpcClientJavaGenerator(java_generator.JavaGenerator):
    class Document(java_generator.JavaGenerator.Document):
        def java_package(self):
            try:
                return self.namespaces_by_scope['jsonrpc_client_java'].name
            except KeyError:
                return java_generator.JavaGenerator.Document.java_package(self)

        def _save_to_dir(self, out_dir_path):
            try:
                out_dir_path = os.path.join(out_dir_path, self.namespace_by_scope(('jsonrpc_client_java', 'java')).name.replace('.', os.path.sep))
            except KeyError:
                pass
            return self._save_to_file(os.path.join(out_dir_path, self.definitions[0].java_name() + self._java_file_ext()))


    class Function(java_generator.JavaGenerator.Function):
        def __repr__(self):
            name = self.name
            java_name = self.java_name()
            parameters = ', '.join(parameter.java_parameter(final=True) for parameter in self.parameters)
            parameter_names = ', '.join(parameter.java_name() for parameter in self.parameters)
            request_type_name = self.java_request_type().java_name()
            response_type_name = self.java_response_type().java_name()
            service_qname = self.parent.java_qname()
            if self.return_field is not None:
                service_response_assignment = "__serviceResponse = " % locals()
                service_response_declaration = "%(service_qname)s.Messages.%(response_type_name)s __serviceResponse = null;\n        " % locals()
                service_response_return_value_getter_name = self.return_field.java_getter_name()
                return_statement = indent(' ' * 8, """
if (__serviceResponse != null) {
    return __serviceResponse.%(service_response_return_value_getter_name)s();
} else {
    throw new RuntimeException("no JSON-RPC results field received from the server");
}""" % locals())
                return_type_qname = self.return_field.type.java_qname()
            else:
                service_response_assignment = ''
                service_response_declaration = ''
                return_statement = ''
                return_type_qname = 'void'

            return """\
public final %(return_type_qname)s %(java_name)s(%(parameters)s) {
    final %(service_qname)s.Messages.%(request_type_name)s __serviceRequest = new %(service_qname)s.Messages.%(request_type_name)s(%(parameter_names)s);
    final int __id = System.identityHashCode(__serviceRequest);

    try {
        final java.io.StringWriter __oStringWriter = new java.io.StringWriter();
        final org.thryft.protocol.JsonOutputProtocol __oprot = new org.thryft.protocol.JsonOutputProtocol(__oStringWriter);
        __oprot.writeStructBegin(new org.thryft.protocol.StructBegin("JSON-RPC"));
        __oprot.writeFieldBegin(new org.thryft.protocol.FieldBegin("id", org.thryft.protocol.Type.I32, (short)-1));
        __oprot.writeI32(__id);
        __oprot.writeFieldEnd();
        __oprot.writeFieldBegin(new org.thryft.protocol.FieldBegin("jsonrpc", org.thryft.protocol.Type.STRING, (short)-1));
        __oprot.writeString("2.0");
        __oprot.writeFieldEnd();
        __oprot.writeFieldBegin(new org.thryft.protocol.FieldBegin("method", org.thryft.protocol.Type.STRING, (short)-1));
        __oprot.writeString("%(name)s");
        __oprot.writeFieldEnd();
        __oprot.writeFieldBegin(new org.thryft.protocol.FieldBegin("params", org.thryft.protocol.Type.STRUCT, (short)-1));
        __serviceRequest.write(__oprot);
        __oprot.writeFieldEnd();
        __oprot.writeFieldStop();
        __oprot.writeStructEnd();
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

        %(service_response_declaration)sfinal java.io.StringReader __iStringReader = new java.io.StringReader(__iString);
        final org.thryft.protocol.JsonInputProtocol __iprot = new org.thryft.protocol.JsonInputProtocol(__iStringReader);
        __iprot.readStructBegin();
        while (true) {
            final org.thryft.protocol.FieldBegin __iFieldBegin = __iprot.readFieldBegin();
            if (__iFieldBegin.type == org.thryft.protocol.Type.STOP) {
                break;
            } else if (__iFieldBegin.name.equalsIgnoreCase("jsonrpc")) {
                final String __jsonrpc = __iprot.readString();
                if (!__jsonrpc.equals("2.0")) {
                    throw new org.thryft.protocol.OutputProtocolException("expected jsonrpc in response to be 2.0, got " + __jsonrpc);
                }
            } else if (__iFieldBegin.name.equalsIgnoreCase("id")) {
                final int __actualId = __iprot.readI32();
                if (__actualId != __id) {
                    throw new org.thryft.protocol.OutputProtocolException("expected id in response to be " + __id + ", got " + __actualId);
                }
            } else if (__iFieldBegin.name.equalsIgnoreCase("error")) {
                int __errorCode = 0;
                String __errorMessage = "";
                __iprot.readStructBegin();
                while (true) {
                    final org.thryft.protocol.FieldBegin __errorFieldBegin = __iprot.readFieldBegin();
                    if (__errorFieldBegin.type == org.thryft.protocol.Type.STOP) {
                        break;
                    } else if (__errorFieldBegin.name.equalsIgnoreCase("code")) {
                        __errorCode = __iprot.readI32();
                    } else if (__errorFieldBegin.name.equalsIgnoreCase("name")) {
                        __errorMessage = __iprot.readString();
                    }
                    __iprot.readFieldEnd();
                }
                __iprot.readStructEnd();
                throw new RuntimeException("error from server: code=" + __errorCode + ", message='" + __errorMessage + "'");
            } else if (__iFieldBegin.name.equalsIgnoreCase("results")) {
                %(service_response_assignment)snew %(service_qname)s.Messages.%(response_type_name)s(__iprot);
            }
            __iprot.readFieldEnd();
        }
        __iprot.readStructEnd();%(return_statement)s
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
            return """\
public %(name)s(final java.net.URL jsonRpcUrl) {
    this.jsonRpcUrl = com.google.common.base.Preconditions.checkNotNull(jsonRpcUrl);
}
""" % locals()

        def _java_member_declarations(self):
            name = self.java_name()
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
            methods.extend([repr(function) for function in self.functions])
            return methods

        def __repr__(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)

            sections = []
            sections.append("\n".join(self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            return """\
public final class %(name)s implements %(service_qname)s {
%(sections)s
}""" % locals()
