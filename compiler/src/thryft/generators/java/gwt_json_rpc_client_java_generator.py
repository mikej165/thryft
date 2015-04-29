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

import os.path

from thryft.generators.java import java_generator
from yutil import indent, upper_camelize


class GwtJsonRpcClientJavaGenerator(java_generator.JavaGenerator):
    class Document(java_generator.JavaGenerator.Document):
        def java_package(self):
            try:
                return self.namespace_by_scope(('gwt_json_rpc_client_java', 'java')).name
            except KeyError:
                return None

    class Function(java_generator.JavaGenerator.Function):
        def java_repr(self):
            name = self.name
            java_name = self.java_name()
            parameters = [parameter.java_parameter(final=True) for parameter in self.parameters]
            if self.return_field is not None:
                return_type_name = self.return_field.type.java_declaration_name(boxed=True)
            else:
                return_type_name = 'Void'
            parameters.append("final com.google.gwt.user.client.rpc.AsyncCallback<%s> callback" % return_type_name)
            parameters = ', '.join(parameters)
            parameter_names = ', '.join(parameter.java_name() for parameter in self.parameters)
            request_type_name = self.java_request_type().java_name()
            response_type_name = self.java_response_type().java_name()
            service_qname = self.parent.java_qname()
            if self.return_field is not None:
                service_response_declaration = "final %(service_qname)s.Messages.%(response_type_name)s __serviceResponse;\n" % locals() + ' ' * 16
                service_response_assignment = "__serviceResponse = "
                service_response_return_value_getter_name = self.return_field.java_getter_name()
                callback = indent(' ' * 16, """
callback.onSuccess(__serviceResponse.%(service_response_return_value_getter_name)s());
""" % locals())
            else:
                service_response_declaration = service_response_assignment = ''
                callback = ''

            return """\
public final void %(java_name)s(%(parameters)s) {
    final %(service_qname)s.Messages.%(request_type_name)s __serviceRequest = new %(service_qname)s.Messages.%(request_type_name)s(%(parameter_names)s);
    final String __id = Integer.toString(System.identityHashCode(__serviceRequest));

    final String __jsonRpcOutput;
    try {
        final org.thryft.protocol.GwtJsonOutputProtocol __jsonOutputProtocol = new org.thryft.protocol.GwtJsonOutputProtocol();
        final org.thryft.protocol.JsonRpcOutputProtocol __jsonRpcOutputProtocol = new org.thryft.protocol.JsonRpcOutputProtocol(__jsonOutputProtocol);
        __jsonRpcOutputProtocol.writeMessageBegin("%(name)s", org.thryft.protocol.MessageType.CALL, __id);
        __serviceRequest.write(__jsonRpcOutputProtocol);
        __jsonRpcOutputProtocol.writeMessageEnd();
        __jsonRpcOutput = __jsonOutputProtocol.toJsonValue().toString();
    } catch (final org.thryft.protocol.OutputProtocolException e) {
        callback.onFailure(e);
        return;
    }

    final com.google.gwt.http.client.RequestBuilder __requestBuilder = new com.google.gwt.http.client.RequestBuilder(com.google.gwt.http.client.RequestBuilder.POST, jsonRpcUrl.toString());
    __requestBuilder.setHeader("Content-Type", "application/json");
    try {
        __requestBuilder.sendRequest(__jsonRpcOutput, new com.google.gwt.http.client.RequestCallback() {
            public void onError(final com.google.gwt.http.client.Request request, final Throwable exception) {
                callback.onFailure(exception);
            }

            public void onResponseReceived(final com.google.gwt.http.client.Request request, final com.google.gwt.http.client.Response response) {
                %(service_response_declaration)stry {
                    final String __responseText = response.getText();
                    final org.thryft.protocol.JsonRpcInputProtocol __iprot = new org.thryft.protocol.JsonRpcInputProtocol(new org.thryft.protocol.GwtJsonInputProtocol(__responseText));
                    final org.thryft.protocol.MessageBegin __messageBegin = __iprot.readMessageBegin();
                    if (!__messageBegin.getId().equals(__id)) {
                        throw new org.thryft.protocol.InputProtocolException("expected id in response to be " + __id + ", got " + __messageBegin.getId());
                    }
                    if (__messageBegin.getType() == org.thryft.protocol.MessageType.EXCEPTION) {
                        final org.thryft.protocol.JsonRpcErrorResponse __error = org.thryft.protocol.JsonRpcErrorResponse.read(__iprot);
                        __iprot.readMessageEnd();
                        callback.onFailure(__error);
                        return;
                    } else if (__messageBegin.getType() != org.thryft.protocol.MessageType.REPLY) {
                        throw new org.thryft.protocol.InputProtocolException("expected response message");
                    }
                    %(service_response_assignment)snew %(service_qname)s.Messages.%(response_type_name)s(__iprot);
                    __iprot.readMessageEnd();
                } catch (final Exception e) {
                    callback.onFailure(e);
                    return;
                }%(callback)s
            }
        });
    } catch (final com.google.gwt.http.client.RequestException e) {
        callback.onFailure(e);
    }
}
""" % locals()

    class Service(java_generator.JavaGenerator.Service):
        def java_name(self, boxed=False):
            return 'GwtJsonRpcClient' + java_generator.JavaGenerator.Service.java_name(self)

        def _java_constructor(self):
            name = self.java_name()
            return """\
public %(name)s(final String jsonRpcUrlPath) {
    this.jsonRpcUrl = org.thryft.native_.Url.builder()
        .setScheme(com.google.gwt.user.client.Window.Location.getProtocol())
        .setHost(com.google.gwt.user.client.Window.Location.getHost())
        .setPath(jsonRpcUrlPath)
        .build();
}
""" % locals()

        def _java_member_declarations(self):
            name = self.java_name()
            return [
                "private final org.thryft.native_.Url jsonRpcUrl;",
            ]


        def _java_methods(self):
            methods = []
            methods.append(self._java_constructor())
            # methods.append(self._java_method_do_post())
            # methods.append(self._java_method_do_post_error())
            # methods.append(self._java_method_do_post_response())
            methods.extend([function.java_repr() for function in self.functions])
            return methods

        def java_repr(self):
            name = self.java_name()
            service_qname = java_generator.JavaGenerator.Service.java_qname(self)

            sections = []
            sections.append("\n".join(self._java_methods()))
            sections.append("\n".join(self._java_member_declarations()))
            sections = "\n\n".join(indent(' ' * 4, sections))

            return """\
public final class %(name)s {
%(sections)s
}""" % locals()
