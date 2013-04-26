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

from thryft.generators.java._java_container_type import _JavaContainerType
from yutil import decamelize, indent, class_qname


class _JavaSequenceType(_JavaContainerType):
    def _java_mutable_raw_qname(self):
        raise NotImplementedError(class_qname(self))

    def java_name(self, boxed=False):
        return self.java_qname(boxed=boxed)

    def java_qname(self, boxed=False):
        return "com.google.common.collect.Immutable%s<%s>" % (
                   self._java_interface_simple_name(),
                   self.element_type.java_declaration_name(boxed=True)
               )

    def _java_interface_simple_name(self):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'java'
        assert class_name_split[2] == 'type'
        return class_name_split[1].capitalize()

    def java_literal(self, value):
        return "com.google.common.collect.Immutable%s.<%s> of(%s)" % (
            self._java_interface_simple_name(),
            self.element_type.java_qname(boxed=True),
            ', '.join(self.element_type.java_literal(element_value) for element_value in value)
        )

    def java_read_protocol(self):
        element_read_protocol = self.element_type.java_read_protocol()
        add_element = "sequence.add(%(element_read_protocol)s);" % locals()
        element_read_protocol_throws = self.element_type.java_read_protocol_throws_checked()
        if len(element_read_protocol_throws) > 0:
            add_element = indent(' ' * 4, add_element)
            add_element = """\
try {
%s
}%s
""" % (add_element, ''.join("""\
 catch (%(exception_type_name)s e) {
     throw new IllegalArgumentException(e);
}""" % locals()
                     for exception_type_name in element_read_protocol_throws))
        add_element = indent(' ' * 16, add_element)

        element_type_name = self.element_type.java_declaration_name(boxed=True)
        interface_simple_name = self._java_interface_simple_name()
        mutable_raw_qname = self._java_mutable_raw_qname()

        return """\
(new com.google.common.base.Function<org.apache.thrift.protocol.TProtocol, com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s>>() {
    @Override
    public com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s> apply(final org.apache.thrift.protocol.TProtocol iprot) {
        try {
            final org.apache.thrift.protocol.T%(interface_simple_name)s sequenceBegin = iprot.read%(interface_simple_name)sBegin();
            final java.util.%(interface_simple_name)s<%(element_type_name)s> sequence = new %(mutable_raw_qname)s<%(element_type_name)s>();
            for (int elementI = 0; elementI < sequenceBegin.size; elementI++) {
%(add_element)s
            }
            iprot.read%(interface_simple_name)sEnd();
            return com.google.common.collect.Immutable%(interface_simple_name)s.copyOf(sequence);
        } catch (final org.apache.thrift.TException e) {
            return com.google.common.collect.Immutable%(interface_simple_name)s.of();
        }
    }
}).apply(iprot)""" % locals()

    def java_write_protocol(self, value, depth=0):
        element_ttype = self.element_type.thrift_ttype_name()
        element_type_name = self.element_type.java_declaration_name(boxed=True)
        element_write_protocol = \
            indent(' ' * 4,
                self.element_type.java_write_protocol(
                    "_iter%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        interface_simple_name = self._java_interface_simple_name()
        return """\
oprot.write%(interface_simple_name)sBegin(new org.apache.thrift.protocol.T%(interface_simple_name)s(org.apache.thrift.protocol.TType.%(element_ttype)s, %(value)s.size()));
for (final %(element_type_name)s _iter%(depth)u : %(value)s) {
%(element_write_protocol)s
}
oprot.write%(interface_simple_name)sEnd();""" % locals()
