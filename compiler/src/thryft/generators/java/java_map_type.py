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

from thryft.generator.map_type import MapType
from thryft.generators.java._java_container_type import _JavaContainerType
from yutil import indent


class JavaMapType(MapType, _JavaContainerType):
    def java_boxed_immutable_qname(self):
        return self.__java_qname()

    def java_literal(self, value):
        return "com.google.common.collect.ImmutableMap.<%s, %s> of(%s)" % (
            self.key_type.java_boxed_qname(),
            self.value_type.java_boxed_qname(),
            ', '.join(self.key_type.java_literal(key) + ', ' + self.value_type.java_literal(value_) for key, value_ in value)
        )

    def java_name(self):
        return self.java_qname()

    def __java_qname(self):
        return "com.google.common.collect.ImmutableMap<%s, %s>" % (
                   self.key_type.java_boxed_qname(),
                   self.value_type.java_boxed_qname()
               )

    def java_qname(self):
        return self.__java_qname()

    def java_read_protocol(self):
        def try_catch(statement, throws):
            if len(throws) == 0:
                return statement
            statement = indent(' ' * 4, statement)
            return """\
try {
%s
}%s
""" % (statement, ''.join("""\
 catch (final %(exception_type_name)s e) {
     throw new org.thryft.protocol.InputProtocolException(e);
}""" % locals()
                     for exception_type_name in throws))

        key_read_protocol = \
            indent(' ' * 16, try_catch(
                'key = ' + self.key_type.java_read_protocol() + ';',
                self.key_type.java_read_protocol_throws_checked() + self.key_type.java_read_protocol_throws_unchecked()
            ))
        key_type_name = self.key_type.java_boxed_qname()

        value_read_protocol = \
            indent(' ' * 16, try_catch(
                'value = ' + self.value_type.java_read_protocol() + ';',
                self.value_type.java_read_protocol_throws_checked() + self.value_type.java_read_protocol_throws_unchecked()
            ))

        value_type_name = self.value_type.java_boxed_qname()
        return """\
(new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<%(key_type_name)s, %(value_type_name)s>>() {
    @Override
    public com.google.common.collect.ImmutableMap<%(key_type_name)s, %(value_type_name)s> apply(final org.thryft.protocol.InputProtocol iprot) {
        try {
            final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
            final com.google.common.collect.ImmutableMap.Builder<%(key_type_name)s, %(value_type_name)s> map = com.google.common.collect.ImmutableMap.builder();
            for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                final %(key_type_name)s key;
%(key_read_protocol)s
                final %(value_type_name)s value;
%(value_read_protocol)s
                map.put(key, value);
            }
            iprot.readMapEnd();
            return map.build();
        } catch (final org.thryft.protocol.InputProtocolException e) {
            throw new org.thryft.protocol.UncheckedInputProtocolException(e);
        }
    }
}).apply(iprot)""" % locals()

    def java_read_protocol_throws_unchecked(self):
        return ['org.thryft.protocol.UncheckedInputProtocolException']

    def java_write_protocol(self, value, depth=0):
        key_ttype = self.key_type.thrift_ttype_name()
        key_type_name = self.key_type.java_boxed_qname()
        key_write_protocol = \
            indent(' ' * 4,
                self.key_type.java_write_protocol(
                    "_iter%(depth)u.getKey()" % locals(),
                    depth=depth + 1
                )
            )
        value_ttype = self.value_type.thrift_ttype_name()
        value_type_name = self.value_type.java_boxed_qname()
        value_write_protocol = \
            indent(' ' * 4,
                self.value_type.java_write_protocol(
                    "_iter%(depth)u.getValue()" % locals(),
                    depth=depth + 1
                )
            )
        return """\
oprot.writeMapBegin(org.thryft.protocol.Type.%(key_ttype)s, org.thryft.protocol.Type.%(value_ttype)s, %(value)s.size());
for (com.google.common.collect.ImmutableMap.Entry<%(key_type_name)s, %(value_type_name)s> _iter%(depth)u : %(value)s.entrySet()) {
%(key_write_protocol)s
%(value_write_protocol)s
}
oprot.writeMapEnd();""" % locals()
