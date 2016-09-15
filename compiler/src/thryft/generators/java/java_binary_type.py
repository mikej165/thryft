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

from thryft.generator.binary_type import BinaryType
from thryft.generators.java._java_base_type import _JavaBaseType


class JavaBinaryType(BinaryType, _JavaBaseType):
    def java_boxed_name(self):
        return self.java_name()

    def java_compare_to(self, this_value, other_value, **kwds):
        return "com.google.common.primitives.SignedBytes.lexicographicalComparator().compare(%(this_value)s, %(other_value)s)" % locals()

    def java_default_value(self):
        return 'null'

    def java_equals(self, this_value, other_value):
        return "java.util.Arrays.equals(%(this_value)s, %(other_value)s)" % locals()

    def java_from_string(self, value):
        return "%(value)s.getBytes()" % locals()

    def java_hash_code(self, value, **kwds):
        return "java.util.Arrays.hashCode(%(value)s)" % locals()

    def java_is_empty(self, value):
        return value + '.length == 0'

    def java_is_reference(self):
        return True

    def java_name(self):
        return 'byte[]'

    def java_size(self, value):
        return value + '.length'

    def java_to_string(self, value):
        return "java.util.Arrays.toString(%(value)s)" % locals()
