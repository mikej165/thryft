# -----------------------------------------------------------------------------
# Copyright (c) 2016, Minor Gordon
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

from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from yutil import class_qname


class _JavaType(_JavaNamedConstruct):
    def java_boxed_name(self):
        return self.java_name()

    def java_boxed_immutable_qname(self):
        return self.java_qname()

    def java_boxed_qname(self):
        return self.java_qname()

    def java_default_value(self):
        raise NotImplementedError(class_qname(self) + '.java_default_value')

    def java_equals(self, this_value, other_value, boxed):
        raise NotImplementedError(class_qname(self) + '.java_equals')

    def java_from_string(self, value):
        raise NotImplementedError(class_qname(self) + '.java_from_string')

    def java_hash_code(self, value, **kwds):
        return "%(value)s.hashCode()" % locals()

    def java_is_parameterized(self):
        return False

    def java_is_reference(self):
        raise NotImplementedError(class_qname(self) + '.java_is_reference')

    def java_literal(self, value):
        raise NotImplementedError(class_qname(self) + '.java_literal')

    def java_name(self):
        return _JavaNamedConstruct.java_name(self)

    def java_read_protocol(self):
        raise NotImplementedError(class_qname(self) + '.java_read_protocol')

    def java_read_protocol_throws_checked(self):
        return []

    def java_read_protocol_throws_unchecked(self):
        return []

    def java_to_string(self, value):
        raise NotImplementedError(class_qname(self) + '.java_to_string')

    def java_write_protocol(self, value, depth=0):
        raise NotImplementedError(class_qname(self) + '.java_write_protocol')
