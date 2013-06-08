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

from thryft.generator.field import Field
from thryft.generators.js._js_named_construct import _JsNamedConstruct
from yutil import indent, lower_camelize
import json


class JsField(Field, _JsNamedConstruct):
    def js_declaration(self):
        return \
            "/** @type %s */\n" % self.type.js_qname() + \
            self.js_name() + ':undefined'  # + self.type.js_default_value()

    def js_name(self):
        return lower_camelize(self.name)

    def js_qname(self):
        return self.parent.js_qname() + '.' + self.js_name()

    def js_read_protocol(self):
        name = self.name
        js_name = self.js_name()
        read_protocol = self.type.js_read_protocol()
        return """\
if (field.fname == "%(name)s") {
    fields["%(js_name)s"] = %(read_protocol)s;
}""" % locals()

    def js_schema(self):
        schema = self.type.js_schema()
        if self.required:
            schema = schema.copy()
            schema.setdefault('validators', []).append('required')
        return {self.js_name(): schema}

    def js_validation(self):
        try:
            validation = self.annotations['validation'].copy()
        except KeyError:
            validation = {}
        validation['required'] = self.required
        name = self.js_name()
        qname = self.js_qname()
        validation.update(self.type.js_validation(depth=0, value='value', value_name=qname))
        type_validation = validation.pop('type')
        if not self.required:
            type_validation = indent(' ' * 4, type_validation)
            type_validation = """\
if (typeof attr !== "undefined" && attr !== "null") {
%(type_validation)s
}
""" % locals()
        type_validation = indent(' ' * 8, type_validation)
        validation = json.dumps(validation).lstrip('{').rstrip('}')
        return """\
%(name)s: {
    "fn": function(value, attr, computedState) {
%(type_validation)s
    },
    %(validation)s
}""" % locals()

    def js_write_protocol(self):
        name = self.name
        js_name = self.js_name()
        write_protocol = self.type.js_write_protocol("this.get(\"" + self.js_name() + "\")")
        write_protocol = """\
oprot.writeFieldBegin("%(name)s");
%(write_protocol)s
oprot.writeFieldEnd();""" % locals()
        if not self.required:
            write_protocol = indent(' ' * 4, write_protocol)
            write_protocol = """\
if (this.has("%(js_name)s")) {
%(write_protocol)s
}""" % locals()
        return write_protocol
