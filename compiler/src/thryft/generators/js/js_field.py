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

from thryft.generator.field import Field
from thryft.generators.js._js_named_construct import _JsNamedConstruct
from yutil import indent
import json


class JsField(Field, _JsNamedConstruct):
    def js_declaration(self):
        return \
            "/** @type %s */\n" % self.type.js_qname() + \
            self.js_name() + ':undefined'  # + self.type.js_default_value()

    def js_from_json(self):
        from_json = self.type.js_from_json('json[fieldName]')
        name = self.name
        js_name = self.js_name()
        field_name_tests = ["fieldName == \"%(name)s\"" % locals()]
        if self.id is not None:
            id_ = self.id
            field_name_tests.append("fieldName == \"%(id_)d:%(name)s\"" % locals())
        field_name_tests = ' || '.join(field_name_tests)
        return """\
if (%(field_name_tests)s) {
    fields["%(js_name)s"] = %(from_json)s;
}""" % locals()

    def js_name(self):
#         return lower_camelize(self.name)
        # Per MJ's decision 20151014, use Thrift-style underscore_separated names
        return self.name

    def js_name_constant(self):
        return '%s: "%s"' % (self.name.upper(), self.name)

    def js_qname(self):
        return self.parent.js_qname() + '.' + self.js_name()

    def js_schema(self):
        schema = self.type.js_schema()
        if self.required:
            schema = schema.copy()
            schema.setdefault('validators', []).append('required')
        return {self.js_name(): schema}

    def js_to_json(self):
        js_name = self.js_name()
        json_name = self.name
        if self.id is not None:
            json_name = str(self.id) + ':' + json_name
        to_json = """json["%(json_name)s"] = """ % locals() + self.type.js_to_json("this.get(\"%(js_name)s\")" % locals()) + ';'
        if not self.required:
            to_json = indent(' ' * 4, to_json)
            to_json = """\
if (this.has("%(js_name)s")) {
%(to_json)s
}""" % locals()
        return to_json

    def js_validation(self):
        validation = {}
        for annotation in self.annotations:
            if annotation.name == 'validation':
                validation = annotation.value.copy()
                break
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
