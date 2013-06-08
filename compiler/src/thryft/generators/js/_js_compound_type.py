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

from thryft.generators.js._js_type import _JsType
from yutil import indent, lpad
import json
import re


class _JsCompoundType(_JsType):
    def js_is_model(self):
        return True

    def js_read_protocol(self):
        qname = self.js_qname()
        return "%(qname)s.read(iprot)" % locals()

    def js_write_protocol(self, value, depth=0):
        return "%(value)s.write(oprot);" % locals()

    def _js_class_properties(self):
        class_properties = {}
        class_properties.update(self._js_class_method_read())
        return [class_properties[method_name] for method_name in sorted(class_properties.iterkeys())]

    def _js_class_method_read(self):
        field_reads = \
            lpad(' else ', indent(' ' * 8, ' else '.join(
                field.js_read_protocol() for field in self.fields
            )))
        name = self.js_qname()
        return {'read': """\
read: function(iprot) {
    var fields = {};
    iprot.readStructBegin();
    while (true) {
        var field = iprot.readFieldBegin();
        if (field.fname.length == 0) {
            break;
        }%(field_reads)s
        iprot.readFieldEnd();
    }
    iprot.readStructEnd();
    return new %(name)s(fields);
}""" % locals()}

    def js_default_value(self):
        return 'null'

    def _js_method_write(self):
        field_writes = indent(' ' * 4, "\n".join(field.js_write_protocol() for field in self.fields))
        name = self.js_name()
        return {'write': """\
write: function(oprot) {
    oprot.writeStructBegin("%(name)s");
%(field_writes)s
    oprot.writeStructEnd();
    return oprot;
}""" % locals()}

    def _js_properties(self):
        properties = {}
        # properties.update(self._js_property_defaults())
        properties.update(self._js_property_schema())
        properties.update(self._js_property_validation())
        properties.update(self._js_property_view_metadata())
        properties.update(self._js_method_write())
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
            field_view_metadata = field.annotations.get('js_view_metadata', None)
            if field_view_metadata is not None:
                view_metadata[field.js_name()] = field_view_metadata
        if len(view_metadata) == 0:
            return {}
        view_metadata = json.dumps(view_metadata, indent=4)
        return {'viewMetadata': """\
viewMetadata: %s
""" % view_metadata}

    def js_schema(self):
        return {'type': 'NestedModel', 'model': self.js_qname()}

    def js_validation(self, value, value_name, **kwds):
        qname = self.js_qname()
        return {'type': """\
if (!(%(value)s instanceof %(qname)s)) {
    return "expected %(value_name)s to be a %(qname)s";
}
if (!%(value)s.isValid(true)) {
    return %(value)s.validationError;
}""" % locals()}

    def __repr__(self):
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
