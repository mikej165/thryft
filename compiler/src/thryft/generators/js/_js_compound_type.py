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

from thryft.generators.js._js_type import _JsType
from yutil import indent, lpad
import json
import re


class _JsCompoundType(_JsType):
    def js_is_model(self):
        return True

    def _js_class_properties(self):
        class_properties = {}
        class_properties.update(self._js_class_method_from_thryft_json())
        return [class_properties[method_name] for method_name in sorted(class_properties.iterkeys())]

    def _js_class_method_from_thryft_json(self):
        qname = self.js_qname()
        if len(self.fields) == 0:
            return {'fromThryftJSON': """\
fromThryftJSON: function(json) {
    return new %(qname)s({});
}""" % locals()}

        fields_from_json = \
            lpad("\n", indent(' ' * 8, ' else '.join(
                field.js_from_json() for field in self.fields
            )))
        return {'fromThryftJSON': """\
fromThryftJSON: function(json) {
    var fields = {};
    for (var fieldName in json) {%(fields_from_json)s
    }
    return new %(qname)s(fields);
}""" % locals()}

    def js_default_value(self):
        return 'null'

    def js_from_json(self, value):
        qname = self.js_qname()
        return "%(qname)s.fromThryftJSON(%(value)s)" % locals()

    def _js_method_to_thryft_json(self):
        if len(self.fields) == 0:
            return {'toThryftJSON': """\
toThryftJSON: function() {
    return {};
}""" % locals()}

        fields_to_json = indent(' ' * 4, "\n".join(field.js_to_json() for field in self.fields))
        return {'toThryftJSON': """\
toThryftJSON: function() {
    var json = {};
%(fields_to_json)s
    return json;
}""" % locals()}

    def _js_properties(self):
        properties = {}
        # properties.update(self._js_property_defaults())
        properties.update(self._js_method_to_thryft_json())
        properties.update(self._js_property_schema())
        properties.update(self._js_property_validation())
        properties.update(self._js_property_view_metadata())
        return [properties[method_name] for method_name in sorted(properties.iterkeys())]

#     def _js_property_defaults(self):
#         return {'defaults': """\
# defaults: function() {
#     return {
# %s
#     };
# }""" % (",\n".join(indent(' ' * 8,
#             [field.js_declaration() for field in self.fields]
#         )))}

    def _js_property_schema(self):
        schema = {}
        for field in self.fields:
            schema.update(field.js_schema())
        schema = json.dumps(schema, indent=4)
        schema = re.sub('\"model\"\: \"([\w\.]+)"', '"model": \\1', schema)
        return {'schema': """\
schema: %s
""" % schema}

    def _js_property_validation(self):
        return {'validation': """\
validation: {%s
}
""" % lpad("\n", ",\n\n".join(indent(' ' * 4,
          (field.js_validation()
           for field in self.fields)
      )))}

    def _js_property_view_metadata(self):
        view_metadata = {}
        for field in self.fields:
            for annotation in field.annotations:
                if annotation.name == 'js_view_metadata':
                    view_metadata[field.js_name()] = annotation.value
                    break
        if len(view_metadata) == 0:
            return {}
        view_metadata = json.dumps(view_metadata, indent=4)
        return {'viewMetadata': """\
viewMetadata: %s
""" % view_metadata}

    def js_repr(self):
        class_properties = []
        class_properties.append("\n\n".join(indent(' ' * 8, self._js_class_properties())))
        class_properties = ",\n\n".join(class_properties)

        properties = []
        properties.append(",\n\n".join(indent(' ' * 8, self._js_properties())))
        properties = ",\n\n".join(properties)

        qname = self.js_qname()

        return """\
%(qname)s = Backbone.Model.extend(
    {
%(properties)s
    },
    {
%(class_properties)s
    }
);""" % locals()

    def js_schema(self):
        return {'type': 'NestedModel', 'model': self.js_qname()}

    def js_to_json(self, value, depth=0):
        return "%(value)s.toThryftJSON()" % locals()

    def js_validation(self, value, value_name, **kwds):
        qname = self.js_qname()
        return {'type': """\
if (!(%(value)s instanceof %(qname)s)) {
    return "expected %(value_name)s to be a %(qname)s";
}
if (!%(value)s.isValid(true)) {
    return %(value)s.validationError;
}""" % locals()}
