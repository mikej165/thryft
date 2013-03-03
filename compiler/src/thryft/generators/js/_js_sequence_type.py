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

from thryft.generators.js._js_container_type import _JsContainerType
from yutil import decamelize, indent


class _JsSequenceType(_JsContainerType):
    def js_name(self):
        return "Array.<%s>" % self.element_type.js_qname()

    def js_qname(self):
        return "Array.<%s>" % self.element_type.js_qname()

    def js_read_protocol(self):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'js'
        assert class_name_split[2] == 'type'

        element_ttype_id = self.element_type.thrift_ttype_id()
        element_read_protocol = self.element_type.js_read_protocol()
        type_name = class_name_split[1].capitalize()
        return """function(iprot) { var sequenceBegin = iprot.read%(type_name)sBegin(); var sequence = new Array(); for (var i = 0; i < sequenceBegin.size; i++) { sequence.push(%(element_read_protocol)s); } iprot.read%(type_name)sEnd(); return sequence; }(iprot)""" % locals()

    def js_write_protocol(self, value, depth=0):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'js'
        assert class_name_split[2] == 'type'

        element_ttype_id = self.element_type.thrift_ttype_id()
        element_write_protocol = \
            indent(' ' * 4, self.element_type.js_write_protocol("__sequence%(depth)u[__i%(depth)u]" % locals(), depth=depth + 1))
        type_name = class_name_split[1].capitalize()
        return """\
var __sequence%(depth)u = %(value)s;
oprot.write%(type_name)sBegin(%(element_ttype_id)u, __sequence%(depth)u.length);
for (var __i%(depth)u = 0; __i%(depth)u < __sequence%(depth)u.length; __i%(depth)u++) {
%(element_write_protocol)s
}
oprot.write%(type_name)sEnd();""" % locals()
