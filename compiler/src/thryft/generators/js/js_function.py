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
from yutil import decamelize, indent, lower_camelize


class JsFunction(Function, _JsNamedConstruct):
    def js_qname(self):
        return self.parent.js_qname() + '.' + lower_camelize(self.js_name())

    def __repr__(self):
        name = self.js_name()

        if self.return_type is not None:
            ajax_callbacks = indent(' ' * 8, """\
success:function (reply) {
    result = reply.result;
}""")
        else:
            ajax_callbacks = indent(' ' * 8, """\
success:function (reply) {
    result = true;
},
error:function () {
    result = false;
}""")

        jsonrpc_params = ', '.join("'" + parameter.name + "':" + parameter.name
                                        for parameter in self.parameters)

        jsonrpc_url = self.js_qname().split('.', 1)[0] + '.hostname()+\'/api/jsonrpc/'
        assert self.parent.name.endswith('Service')
        jsonrpc_url += '_'.join(decamelize(self.parent.name).split('_')[:-1])
        jsonrpc_url += '\''

        qname = self.js_qname()

        parameter_names = ', '.join(parameter.name for parameter in self.parameters)

        return """\
%(qname)s = function(%(parameter_names)s) {
    var self = this;
    var result;

    $.ajax({
        url:%(jsonrpc_url)s,
        type:'POST',
        data:JSON.stringify({
            jsonrpc:'2.0',
            method:'%(name)s',
            params:{%(jsonrpc_params)s},
            id:'1234'
        }),
        dataType:'json',
        mimeType:'application/json',
        async:false,
%(ajax_callbacks)s
    });
    
    return result;
};
""" % locals()
