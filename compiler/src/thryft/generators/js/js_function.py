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
            if parent_function.return_field is not None:
                self.fields.append(parent_function.return_field)

    def js_message_types(self):
        return [self.js_request_type(), self.js_response_type()]

    def js_name(self):
        return lower_camelize(self.name)

    def js_qname(self):
        return self.parent.js_qname() + '.' + self.js_name()

    def js_request_type(self, **kwds):
        return self._JsRequestType(parent_function=self, **kwds)

    def js_repr(self):
        for parameter in self.parameters:
            assert parameter.name != 'error', self.parent.name
            assert parameter.name != 'success', self.parent.name

        name = self.name
        js_name = self.js_name()
        service_js_qname = self.parent.js_qname()

        jsdoc_lines = []
        if self.doc is not None:
            jsdoc_lines.extend(line.strip() for line in self.doc.splitlines())
        else:
            jsdoc_lines.append(js_name)
        jsdoc_lines.append('')
        jsdoc_lines.append("@this {%(service_js_qname)s}" % locals())

        function_parameter_names = ', '.join([parameter.js_name() for parameter in self.parameters] + ['successCallback', 'errorCallback'])
        request_type_qname = self.js_request_type().js_qname()

        if len(self.parameters) > 0:
            request = """

    var request = new %(request_type_qname)s(params);
    if (!request.isValid(true)) {
        if (async) {
            if (typeof errorCallback !== "undefined") {
                errorCallback(null, request.validationError, null);
            }
            return;
        } else {
            throw new TypeError(request.validationError);
        }
    }""" % locals()
            jsonrpc_params = "request.write(new thryft.protocol.BuiltinsProtocol()).freeze()" % locals()
        else:
            jsonrpc_params = '{}'
            request = ''

        jsdoc_lines.extend(
           "@param {%s} %s%s" % (
                parameter.type.js_qname(), parameter.name,
                parameter.doc is not None and (' ' + parameter.doc) or ''
            )
            for parameter in self.parameters
        )

        jsonrpc_url = 'this.hostname+\'/api/jsonrpc/'
        if self.parent.name.endswith('Service'):
            jsonrpc_url += '_'.join(decamelize(self.parent.name).split('_')[:-1])
        else:
            jsonrpc_url += decamelize(self.parent.name)
        jsonrpc_url += '\''

        if self.return_field is not None:
            jsdoc_lines.append(
                "@returns {%s}%s" % (
                    self.return_field.type.js_qname(),
                    self.return_field.doc is not None and (' ' + self.return_field.doc) or '')
            )
            response_type_qname = self.js_response_type().js_qname()
            return_value = """%(response_type_qname)s.read(new thryft.protocol.BuiltinsProtocol({return_value:__response.result})).get("returnValue")""" % locals()
        else:
            return_value = 'true'

        if len(self.throws) > 0:
            jsdoc_lines.extend(
                "@throws {%s}%s" % (
                    exception.type.js_qname(),
                    exception.doc is not None and (' ' + exception.doc) or ''
                )
                for exception in self.throws
            )

        jsdoc_lines = "\n".join(' * ' + jsdoc_line for jsdoc_line in jsdoc_lines)

        return """\
/**
%(jsdoc_lines)s
 */
%(js_name)s : function(kwds) {
    var async = false;
    var errorCallback = undefined;
    var params = jQuery.extend({}, kwds);
    var returnValue = null; // For synchronous requests
    var successCallback = undefined;

    for (var key in kwds) {
        if (key === "error") {
            async = true;
            errorCallback = kwds[key];
            delete params[key];
        } else if (key === "success") {
            async = true;
            successCallback = kwds[key];
            delete params[key];
        }
    }%(request)s

    $.ajax({
        async:async,
        data:JSON.stringify({
            jsonrpc:'2.0',
            method:'%(name)s',
            params:%(jsonrpc_params)s,
            id:'1234'
        }),
        dataType:'json',
        error:function(jqXHR, textStatus, errorThrown) {
            if (async) {
                if (typeof errorCallback !== "undefined") {
                    errorCallback(jqXHR, textStatus, errorThrown);
                }
            } else {
                returnValue = false;
            }
        },
        mimeType:'application/json',
        type:'POST',
        success:function(__response) {
            if (typeof __response.result !== "undefined") {
                if (async) {
                    if (typeof successCallback !== "undefined") {
                        successCallback(%(return_value)s);
                    }
                } else {
                    returnValue = %(return_value)s;
                }
            } else {
                if (async) {
                    if (typeof errorCallback !== "undefined") {
                        errorCallback(null, __response.error.message, null);
                    }
                } else {
                    throw new Error(__response.error);
                }
            }
        },
        url:%(jsonrpc_url)s,
    });

    return returnValue;
}""" % locals()

    def js_response_type(self, **kwds):
        return self._JsResponseType(parent_function=self, **kwds)
