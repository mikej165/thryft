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

from thryft.generator.map_type import MapType
from thryft.generators.java._java_container_type import _JavaContainerType
from yutil import indent


class JavaMapType(MapType, _JavaContainerType):
    def java_compare_to(self, this_value, other_value, **kwds):
        qname = self.java_qname()
        key_type_qname = self.key_type.java_declaration_name(boxed=True)
        value_type_qname = self.value_type.java_declaration_name(boxed=True)
        value_compare = indent(' ' * 16, self.value_type.java_compare_to(this_value='leftValue', other_value='rightValue', already_boxed=True))
        return """\
new java.util.Comparator<%(qname)s>() {
    public int compare(final %(qname)s left, final %(qname)s right) {
        int result = ((Integer) left.size()).compareTo(right.size());
        if (result != 0) {
            return result;
        }

        // Compare keys
        final java.util.List<%(key_type_qname)s> leftSortedKeySet = com.google.common.collect.Lists
                .newArrayList(left.keySet());
        java.util.Collections.sort(leftSortedKeySet);
        final java.util.Iterator<%(key_type_qname)s> leftKeyI = leftSortedKeySet.iterator();

        final java.util.List<%(key_type_qname)s> rightSortedKeySet = com.google.common.collect.Lists
                .newArrayList(right.keySet());
        java.util.Collections.sort(rightSortedKeySet);
        final java.util.Iterator<%(key_type_qname)s> rightKeyI = leftSortedKeySet.iterator();

        while (leftKeyI.hasNext()) {
            final %(key_type_qname)s leftKey = leftKeyI.next();
            final %(key_type_qname)s rightKey = rightKeyI.next();

            result = leftKey.compareTo(rightKey);
            if (result != 0) {
                return result;
            }
        }

        // Compare values
        for (final java.util.Map.Entry<%(key_type_qname)s, %(value_type_qname)s> leftEntry : left.entrySet()) {
            final %(value_type_qname)s leftValue = leftEntry.getValue();
            final %(value_type_qname)s rightValue = right.get(leftEntry.getKey());

            result =
%(value_compare)s;
            if (result != 0) {
                return result;
            }
        }

        return 0;
    }
}.compare(%(this_value)s, %(other_value)s)""" % locals()

    def java_literal(self, value):
        return "com.google.common.collect.ImmutableMap.<%s, %s> of(%s)" % (
            self.key_type.java_qname(boxed=True),
            self.value_type.java_qname(boxed=True),
            ', '.join(self.key_type.java_literal(key) + ', ' + self.value_type.java_literal(value_) for key, value_ in value.iteritems())
        )

    def java_name(self, boxed=False):
        return self.java_qname(boxed=boxed)

    def java_qname(self, boxed=False):
        return "com.google.common.collect.ImmutableMap<%s, %s>" % (
                   self.key_type.java_declaration_name(boxed=True),
                   self.value_type.java_declaration_name(boxed=True)
               )

    def java_read_protocol(self):
        key_read_protocol = self.key_type.java_read_protocol()
        key_type_name = self.key_type.java_declaration_name(boxed=True)
        value_read_protocol = self.value_type.java_read_protocol()
        value_type_name = self.value_type.java_declaration_name(boxed=True)
        return """\
(new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.ImmutableMap<%(key_type_name)s, %(value_type_name)s>>() {
    @Override
    public com.google.common.collect.ImmutableMap<%(key_type_name)s, %(value_type_name)s> apply(final org.thryft.protocol.InputProtocol iprot) {
        try {
            final org.thryft.protocol.MapBegin mapBegin = iprot.readMapBegin();
            final com.google.common.collect.ImmutableMap.Builder<%(key_type_name)s, %(value_type_name)s> map = com.google.common.collect.ImmutableMap.builder();
            for (int entryI = 0; entryI < mapBegin.getSize(); entryI++) {
                map.put(%(key_read_protocol)s, %(value_read_protocol)s);
            }
            iprot.readMapEnd();
            return map.build();
        } catch (final org.thryft.protocol.InputProtocolException e) {
            return com.google.common.collect.ImmutableMap.of();
        }
    }
}).apply(iprot)""" % locals()

    def java_write_protocol(self, value, depth=0):
        key_ttype = self.key_type.thrift_ttype_name()
        key_type_name = self.key_type.java_declaration_name(boxed=True)
        key_write_protocol = \
            indent(' ' * 4,
                self.key_type.java_write_protocol(
                    "_iter%(depth)u.getKey()" % locals(),
                    depth=depth + 1
                )
            )
        value_ttype = self.value_type.thrift_ttype_name()
        value_type_name = self.value_type.java_declaration_name(boxed=True)
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
