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

    def js_write_protocol(self, value, depth=0):
        name = self.js_qname()
        return "oprot.writeString(function(enumerator_value) { for (var enumerator_name in %(name)s) { if (%(name)s[enumerator_name] == enumerator_value) { return enumerator_name; } } }(%(value)s));" % locals()

    def __repr__(self):
        name = self.js_qname()

        enumerators = []
        if len(self.enumerators) > 0:
            enumerator_values = []
            for enumerator in self.enumerators:
                if enumerator.value is not None:
                    for enumerator in self.enumerators:
                        assert enumerator.value is not None
                        enumerator_values.append(enumerator.value)
            if len(enumerator_values) == 0:
                enumerator_values = [enumerator.id for enumerator in self.enumerators]

            for enumerator, enumerator_value in zip(self.enumerators, enumerator_values):
                enumerator_name = enumerator.name
                enumerators.append("%(enumerator_name)s: %(enumerator_value)u" % locals())
        enumerators = ', '.join(enumerators)
        return """\
%(name)s = Object.freeze({%(enumerators)s});""" % locals()
