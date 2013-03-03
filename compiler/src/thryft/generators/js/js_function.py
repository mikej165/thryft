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

from thryft.generator.function import Function
from thryft.generators.js._js_named_construct import _JsNamedConstruct
from thryft.generators.js.js_field import JsField
from thryft.generators.js.js_struct_type import JsStructType
from yutil import decamelize, lower_camelize


class JsFunction(Function, _JsNamedConstruct):
    class _JsRequestType(JsStructType):
        def __init__(self, parent_function):
            JsStructType.__init__(
                self,
                name=parent_function.parent.js_name() + 'Messages.' + parent_function.js_name() + 'Request',
                parent=parent_function.parent
            )

            for parameter in parent_function.parameters:
                self.fields.append(
                    JsField(
                        name=parameter.name,
                        type=parameter.type,
                        parent=self,
                        required=parameter.required
                    )
                )

    class _JsResponseType(JsStructType):
        def __init__(self, parent_function):
            JsStructType.__init__(
                self,
                name=parent_function.parent.js_name() + 'Messages.' + parent_function.js_name() + 'Response',
                parent=parent_function.parent
            )
            if parent_function.return_type is not None:
                self.fields.append(
                    JsField(
                        name='return_value',
                        parent=self,
                        required=True,
                        type=parent_function.return_type
                    )
                )

    def js_message_types(self):
        return [self.js_request_type(), self.js_response_type()]

    def js_name(self):
        return lower_camelize(self.name)

    def js_qname(self):
        return self.parent.js_qname() + '.' + self.js_name()

    def js_request_type(self, **kwds):
        return self._JsRequestType(parent_function=self, **kwds)

    def js_response_type(self, **kwds):
        return self._JsResponseType(parent_function=self, **kwds)

    def __repr__(self):
        name = self.name
        js_name = self.js_name()

        function_parameter_names = ', '.join([parameter.js_name() for parameter in self.parameters] + ['successCallback', 'errorCallback'])
        request_type_qname = self.js_request_type().js_qname()

        if self.return_type is not None:
            response_type_qname = self.js_response_type().js_qname()
            return_value = """%(response_type_qname)s.read(new thryft.core.protocol.BuiltinsProtocol({return_value:__response.result})).get("returnValue")""" % locals()
        else:
            return_value = 'true'

        jsonrpc_params = ', '.join("'" + parameter.name + "':" + parameter.js_name()
                                        for parameter in self.parameters)

        jsonrpc_url = 'this.hostname+\'/api/jsonrpc/'
        assert self.parent.name.endswith('Service')
        jsonrpc_url += '_'.join(decamelize(self.parent.name).split('_')[:-1])
        jsonrpc_url += '\''

        if len(self.parameters) > 0:
            request_parameter_names = ', '.join(parameter.js_name() for parameter in self.parameters)
            params = "new %(request_type_qname)s(%(request_parameter_names)s).write(new thryft.core.protocol.BuiltinsProtocol()).freeze()" % locals()
        else:
            params = '{}'

        return """\
%(js_name)s : function(%(function_parameter_names)s) {
    var __async = typeof successCallback !== "undefined" || typeof errorCallback !== "undefined";
    var __returnValue = null; // For synchronous requests

    $.ajax({
        async:__async,
        data:JSON.stringify({
            jsonrpc:'2.0',
            method:'%(name)s',
            params:%(params)s,
            id:'1234'
        }),
        dataType:'json',
        error:function(jqXHR, textStatus, errorThrown) {
            if (__async) {
                if (typeof errorCallback !== "undefined") {
                    errorCallback(jqXHR, textStatus, errorThrown);
                }
            } else {
                __returnValue = false;
            }
        },
        mimeType:'application/json',
        type:'POST',
        success:function(__response) {
            if (typeof __response.result !== "undefined") {
                if (__async) {
                    if (typeof successCallback !== "undefined") {
                        successCallback(%(return_value)s);
                    }
                } else {
                    __returnValue = %(return_value)s;
                }
            } else {
                if (__async) {
                    if (typeof errorCallback !== "undefined") {
                        errorCallback(null, __response.error.message, null);
                    }
                } else {
                    __returnValue = __response.error;
                }
            }
        },
        url:%(jsonrpc_url)s,
    });
    
    return __returnValue;
}""" % locals()
