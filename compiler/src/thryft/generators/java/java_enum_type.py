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

from thryft.generator.enum_type import EnumType
from thryft.generators.java._java_type import _JavaType
from yutil import indent, lpad


class JavaEnumType(EnumType, _JavaType):
    def java_default_value(self):
        return 'null'

    def java_from_string(self, value):
        return self.java_literal(value)

    def java_hash_code(self, value, **kwds):
        return "%(value)s.ordinal()" % locals()

    def _java_implements(self):
        implements = []
        for annotation in self.annotations:
            if annotation.name == 'java_implements':
                implements.append(annotation.value)
        return implements

    def java_is_reference(self):
        return True

    def java_literal(self, value):
        qname = self.java_qname()
        return "%(qname)s.valueOf(\"%(value)s\")" % locals()

    def java_read_protocol(self):
        qname = self.java_qname()
        return "iprot.readEnum(%(qname)s.class)" % locals()

    def java_read_protocol_throws_unchecked(self):
        return ['IllegalArgumentException']

    def java_repr(self):
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
            enumerator_deprecated = ''
            for annotation in enumerator.annotations:
                if annotation.name == 'java_deprecated':
                    enumerator_deprecated = '@Deprecated '
                    break
            enumerators.append(
                "%s%s(%u)" % (enumerator_deprecated, enumerator.name, enumerator.value)
            )
        implements = lpad(' implements ', ', '.join(self._java_implements()))
        valueOf_cases = "\n".join(indent(' ' * 8, valueOf_cases))
        enumerators = ",\n".join(indent(' ' * 4, enumerators))
        return """\
%(javadoc)spublic enum %(name)s%(implements)s {
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

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeEnum(%(value)s);" % locals()
