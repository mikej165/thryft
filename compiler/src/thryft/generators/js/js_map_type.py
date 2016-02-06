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

from thryft.generator.map_type import MapType
from thryft.generators.js._js_container_type import _JsContainerType
from yutil import indent


class JsMapType(MapType, _JsContainerType):
    def js_default_value(self):
        return '{}'

    def js_from_json(self, value):
        key_from_json = self.key_type.js_from_json('key')
        value_from_json = self.value_type.js_from_json('json[key]')
        return """function (json) { var map = {}; for (var key in json) { map[%(key_from_json)s] = %(value_from_json)s; } return map; }(%(value)s)""" % locals()

    def js_literal(self, value):
        return "{%s}" % ', '.join(self.key_type.js_literal(key) + ':' + self.value_type.js_literal(value_) for key, value_ in value)

    def js_name(self):
        return "Object.<%s, %s>" % (self.key_type.js_qname(), self.value_type.js_qname())

    def js_qname(self):
        return "Object.<%s, %s>" % (self.key_type.js_qname(), self.value_type.js_qname())

    def js_schema(self):
        return {'type': 'Object', 'subSchema': self.value_type.js_schema()}

    def js_validation(self, value, value_name, depth=0):
        key_type_validation = \
            indent(' ' * 4,
                self.key_type.js_validation(
                    depth=depth + 1,
                    value="__key" % locals(),
                    value_name=value_name + " key" % locals()
                )['type']
            )
        value_type_validation = \
            indent(' ' * 4,
                self.value_type.js_validation(
                    depth=depth + 1,
                    value="__value" % locals(),
                    value_name=value_name + " value" % locals()
                )['type']
            )
        return {'type': """\
if (typeof %(value)s !== "object") {
    return "expected %(value_name)s to be an object";
}
for (var __key in %(value)s) {
    var __value = %(value)s[__key];
%(key_type_validation)s
%(value_type_validation)s
}""" % locals()}

    def js_to_json(self, value):
        key_to_json = self.key_type.js_to_json('__key')
        value_to_json = self.value_type.js_to_json('value[__key]')
        return """\
function (value) { var __outObject = new Object(); for (var __key in value) { __outObject[%(key_to_json)s] = %(value_to_json)s; } return __outObject; }(%(value)s)""" % locals()
