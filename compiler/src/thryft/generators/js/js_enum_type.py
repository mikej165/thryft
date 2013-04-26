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

from thryft.generator.enum_type import EnumType
from thryft.generators.js._js_type import _JsType


class JsEnumType(EnumType, _JsType):
    def js_read_protocol(self):
        name = self.js_qname()
        return "%(name)s[iprot.readString()]" % locals()

    def js_schema(self):
        return {'type': 'Select', 'options': [enumerator.name for enumerator in self.enumerators]}

    def js_validate(self, value, value_name, **kwds):
        if len(self.enumerators) > 0:
            qname = self.js_qname()
            enumerator_comparisons = ' && '.join("%s !== %s" % (value, enumerator.value)
                                                 for enumerator in self.enumerators)
            enumerator_comparisons = """
if (%(enumerator_comparisons)s) {
    return "%(value_name)s is not a valid enumerator of %(qname)s";
}""" % locals()
        else:
            enumerator_comparisons = ''
        return """\
if (typeof %(value)s !== "number") {
    return "expected %(value_name)s to be a number";
}%(enumerator_comparisons)s
""" % locals()

    def js_write_protocol(self, value, depth=0):
        name = self.js_qname()
        return "oprot.writeString(function(enumerator_value) { for (var enumerator_name in %(name)s) { if (%(name)s[enumerator_name] == enumerator_value) { return enumerator_name; } } }(%(value)s));" % locals()

    def __repr__(self):
        enumerators = ', '.join("%s: %u" % (enumerator.name, enumerator.value)
                                for enumerator in self.enumerators)
        name = self.js_qname()
        return """\
%(name)s = Object.freeze({%(enumerators)s});""" % locals()
