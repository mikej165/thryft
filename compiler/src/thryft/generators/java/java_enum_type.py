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
from thryft.generators.java._java_type import _JavaType
from yutil import indent


class JavaEnumType(EnumType, _JavaType):
    def java_default_value(self):
        return 'null'

    def java_hash_code(self, value):
        return "%(value)s.ordinal()" % locals()

    def java_is_reference(self):
        return True

    def java_read_protocol(self):
        qname = self.java_qname()
        return "(iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readEnum(%(qname)s.class) : %(qname)s.valueOf(iprot.readString().trim().toUpperCase())" % locals()

    def java_read_protocol_throws_unchecked(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeEnum(%(value)s); } else { oprot.writeString(%(value)s.toString()); }" % locals()

    def __repr__(self):
        javadoc = self.java_doc()
        name = self.java_name()
        if len(self.enumerators) == 0:
            return """\
%(javadoc)spublic enum %(qname)s {
}"""
        valueOf_cases = []
        enumerators = []
        for enumerator in self.enumerators:
            valueOf_cases.append(
"case %u: return %s;" % (enumerator.value, enumerator.name))
            enumerators.append(
                "%s(%u)" % (enumerator.name, enumerator.value)
            )
        valueOf_cases = "\n".join(indent(' ' * 8, valueOf_cases))
        enumerators = ",\n".join(indent(' ' * 4, enumerators))
        return """\
%(javadoc)spublic enum %(name)s {
%(enumerators)s;

    private %(name)s(int value) {
        this.value = value;
    }

    public static %(name)s valueOf(final int value) {
        switch (value) {
%(valueOf_cases)s
        default: throw new IllegalArgumentException();
        }
    }

    public static %(name)s valueOf(final Integer value) {
        return valueOf(value.intValue());
    }

    public final int value() {
        return value;
    }

    private final int value;
}""" % locals()

    def java_to_string(self, value):
        return "%(value)s.toString()" % locals()
