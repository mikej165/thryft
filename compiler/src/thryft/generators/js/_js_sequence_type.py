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

from thryft.generators.js._js_compound_type import _JsCompoundType
from thryft.generators.js._js_container_type import _JsContainerType
from yutil import decamelize, indent


class _JsSequenceType(_JsContainerType):
    def js_default_value(self):
        return '[]'

    def js_from_json(self, value):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'js'
        assert class_name_split[2] == 'type'

        element_from_json = self.element_type.js_from_json('json[i]')
        if isinstance(self.element_type, _JsCompoundType):
            element_type_qname = self.element_type.js_qname()
            return_value = "new Backbone.Collection(sequence, {model: %(element_type_qname)s})" % locals()
        else:
            return_value = 'sequence'
        type_name = class_name_split[1].capitalize()
        return """function(json) { var sequence = new Array(); for (var i = 0; i < json.length; i++) { sequence.push(%(element_from_json)s); } return %(return_value)s; }(%(value)s)""" % locals()

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

    def js_schema(self):
        element_schema = self.element_type.js_schema()
        schema = {'type': 'List', 'itemType': element_schema['type']}
        for key, value in element_schema.iteritems():
            if key != 'type':
                schema[key] = value
        return schema

    def js_to_json(self, value):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'js'
        assert class_name_split[2] == 'type'

        if self.element_type.js_is_model():
            elements_property = '.models'
        else:
            elements_property = ''
        element_to_json = self.element_type.js_to_json("__inArray[__i]" % locals())
        type_name = class_name_split[1].capitalize()
        return """\
function (__inArray) { var __outArray = new Array(); for (var __i = 0; __i < __inArray.length; __i++) { __outArray.push(%(element_to_json)s); } return __outArray; }(%(value)s%(elements_property)s)""" % locals()

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
