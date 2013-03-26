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

from thryft.generators.js._js_type import _JsType
from yutil import indent, lpad


class _JsCompoundType(_JsType):
    def js_read_protocol(self):
        qname = self.js_qname()
        return "%(qname)s.read(iprot)" % locals()

    def js_write_protocol(self, value, depth=0):
        return "%(value)s.write(oprot);" % locals()

    def _js_class_methods(self):
        class_methods = {}
        class_methods.update(self._js_class_method_read())
        return [class_methods[method_name] for method_name in sorted(class_methods.iterkeys())]

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

    def _js_methods(self):
        methods = {}
        methods.update(self._js_method_write())
        methods.update(self._js_method_validate())
        return [methods[method_name] for method_name in sorted(methods.iterkeys())]

    def _js_method_validate(self):
        field_validates = lpad("\n", "\n\n".join(indent(' ' * 4,
                              [field.js_validate()
                               for field in self.fields]
                          )))
        return {'validate': """\
validate: function(attributes) {%(field_validates)s
}
""" % locals()}

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

    def js_validate(self, value, value_name, depth=0):
        qname = self.js_qname()
        return """\
if (!(%(value)s instanceof %(qname)s)) {
    return "expected %(value_name)s to be a %(qname)s";
}
var __compoundTypeValidateReturn%(depth)u = %(value)s.validate();
if (typeof __compoundTypeValidateReturn%(depth)u !== "undefined") {
    return __compoundTypeValidateReturn%(depth)u;
}""" % locals()

    def __repr__(self):
        class_properties = []
        class_properties.append("\n\n".join(indent(' ' * 8, self._js_class_methods())))
        class_properties = ",\n\n".join(class_properties)

        properties = []
        if len(self.fields) > 0:
            properties.append(
                ",\n".join(indent(' ' * 8,
                    [field.js_name() + ':undefined' for field in self.fields]
                ))
            )
        properties.append(",\n\n".join(indent(' ' * 8, self._js_methods())))
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
