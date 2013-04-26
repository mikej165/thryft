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

from thryft.generators.js._js_compound_type import _JsCompoundType
from thryft.generators.js._js_container_type import _JsContainerType
from yutil import decamelize, indent


class _JsSequenceType(_JsContainerType):
    def js_literal(self, value):
        if isinstance(self.element_type, _JsCompoundType):
            return \
                "new Backbone.Collection([%s], {model: %s})" % (
                    ', '.join(self.element_type.js_literal(element_value)
                              for element_value in value),
                    self.element_type.js_qname()
                )
        else:
            return "[%s]" % ', '.join(self.element_type.js_literal(element_value) for element_value in value)

    def js_name(self):
        if isinstance(self.element_type, _JsCompoundType):
            return 'Backbone.Collection'
        else:
            return "Array.<%s>" % self.element_type.js_qname()

    def js_qname(self):
        if isinstance(self.element_type, _JsCompoundType):
            return 'Backbone.Collection'
        else:
            return "Array.<%s>" % self.element_type.js_qname()

    def js_read_protocol(self):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'js'
        assert class_name_split[2] == 'type'

        element_ttype_id = self.element_type.thrift_ttype_id()
        element_read_protocol = self.element_type.js_read_protocol()
        if isinstance(self.element_type, _JsCompoundType):
            element_type_qname = self.element_type.js_qname()
            return_value = "new Backbone.Collection(sequence, {model: %(element_type_qname)s})" % locals()
        else:
            return_value = 'sequence'
        type_name = class_name_split[1].capitalize()
        return """function(iprot) { var sequenceBegin = iprot.read%(type_name)sBegin(); var sequence = new Array(); for (var i = 0; i < sequenceBegin.size; i++) { sequence.push(%(element_read_protocol)s); } iprot.read%(type_name)sEnd(); return %(return_value)s; }(iprot)""" % locals()

    def js_schema(self):
        element_schema = self.element_type.js_schema()
        schema = {'type': 'List', 'itemType': element_schema['type']}
        for key, value in element_schema.iteritems():
            if key != 'type':
                schema[key] = value
        return schema

    def js_validation(self, value, value_name, depth=0):
        if isinstance(self.element_type, _JsCompoundType):
            element_type_qname = self.element_type.js_qname()
            return {'type': """\
if (!(%(value)s instanceof Backbone.Collection)) {
    return "expected %(value_name)s to be a Backbone.Collection";
}
if (%(value)s.model !== %(element_type_qname)s) {
    return "expected %(value_name)s to be a Backbone.Collection with model=%(element_type_qname)s";
}
if (!%(value)s.isValid(true)) {
    return %(value)s.validationError;
}""" % locals()}
        else:
            element_validate = \
                indent(' ' * 4,
                    self.element_type.js_validation(
                        depth=depth + 1,
                        value=value + "[__i%(depth)u]" % locals(),
                        value_name=value_name + "[i]" % locals()
                    )['type']
                )
            return {'type': """\
if (!Array.isArray(%(value)s)) {
    return "expected %(value_name)s to be an Array";
}
for (var __i%(depth)u = 0; __i%(depth)u < %(value)s.length; __i%(depth)u++) {
%(element_validate)s
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'js'
        assert class_name_split[2] == 'type'

        element_ttype_id = self.element_type.thrift_ttype_id()
        if isinstance(self.element_type, _JsCompoundType):
            elements_property = '.models'
        else:
            elements_property = ''
        element_write_protocol = \
            indent(' ' * 4, self.element_type.js_write_protocol("__sequence%(depth)u%(elements_property)s[__i%(depth)u]" % locals(), depth=depth + 1))
        type_name = class_name_split[1].capitalize()
        return """\
var __sequence%(depth)u = %(value)s;
oprot.write%(type_name)sBegin(%(element_ttype_id)u, __sequence%(depth)u%(elements_property)s.length);
for (var __i%(depth)u = 0; __i%(depth)u < __sequence%(depth)u%(elements_property)s.length; __i%(depth)u++) {
%(element_write_protocol)s
}
oprot.write%(type_name)sEnd();""" % locals()
