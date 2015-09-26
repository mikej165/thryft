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

from thryft.generators.java._java_base_type import _JavaBaseType


class _JavaNumericType(_JavaBaseType):
    def java_compare_to(self, this_value, other_value, **kwds):
        boxed_name = self.java_name(boxed=True)
        return "%(boxed_name)s.compare(%(this_value)s, %(other_value)s)" % locals()

    def java_default_value(self):
        return "((%s)0)" % self.java_name(boxed=False)

    def java_from_string(self, value):
        boxed_name = self.java_name(boxed=True)
        return "%(boxed_name)s.parse%(boxed_name)s(%(value)s)" % locals()

    def java_hash_code(self, value, already_boxed):
        if already_boxed:
            return "%(value)s.hashCode()" % locals()
        else:
            return value

    def java_literal(self, value):
        return "((%s)%s)" % (self.java_name(boxed=False), value)

    def java_read_protocol_throws_unchecked(self):
        return ['NumberFormatException']

    def java_to_string(self, value):
        return "%s.toString(%(value)s)" % (self.java_name(boxed=True), value)
