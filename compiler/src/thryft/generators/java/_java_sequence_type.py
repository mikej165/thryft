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

from thryft.generators.java._java_container_type import _JavaContainerType
from yutil import decamelize, indent


class _JavaSequenceType(_JavaContainerType):
#     def java_compare_to(self, this_value, other_value, **kwds):
#         qname = self.java_qname()
#         element_type_qname = self.element_type.java_qname(boxed=True)
#         element_compare = indent(' ' * 16, self.element_type.java_compare_to(this_value='leftElement', other_value='rightElement', already_boxed=True))
#         return """\
# new java.util.Comparator<%(qname)s>() {
#     public int compare(final %(qname)s left, final %(qname)s right) {
#         int result = ((Integer) left.size()).compareTo(right.size());
#         if (result != 0) {
#             return result;
#         }
#
#         final java.util.List<%(element_type_qname)s> leftSortedList = com.google.common.collect.Lists
#                 .newArrayList(left);
#         java.util.Collections.sort(leftSortedList);
#         final java.util.Iterator<%(element_type_qname)s> leftI = leftSortedList.iterator();
#
#         final java.util.List<%(element_type_qname)s> rightSortedList = com.google.common.collect.Lists
#                 .newArrayList(right);
#         java.util.Collections.sort(rightSortedList);
#         final java.util.Iterator<%(element_type_qname)s> rightI = leftSortedList.iterator();
#
#         while (leftI.hasNext()) {
#             final %(element_type_qname)s leftElement = leftI.next();
#             final %(element_type_qname)s rightElement = rightI.next();
#
#             result =
# %(element_compare)s;
#             if (result != 0) {
#                 return result;
#             }
#         }
#
#         return 0;
#     }
# }.compare(%(this_value)s, %(other_value)s)""" % locals()

    def java_boxed_immutable_qname(self):
        return self.__java_qname()

    def java_from_string(self, value):
        element_from_string = self.element_type.java_from_string('elementString')
        element_type_name = self.element_type.java_boxed_qname()
        interface_simple_name = self._java_interface_simple_name()
        return """\
(new com.google.common.base.Function<String, com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s>>() {
    @Override
    public com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s> apply(final String value) {
        final com.google.common.collect.Immutable%(interface_simple_name)s.Builder<%(element_type_name)s> sequenceBuilder = com.google.common.collect.Immutable%(interface_simple_name)s.builder();
        for (final String elementString : value.split(",")) {
            sequenceBuilder.add(%(element_from_string)s);
        }
        return sequenceBuilder.build();
    }
}).apply(%(value)s.toString())""" % locals()

    def java_name(self):
        return self.java_qname()

    def __java_qname(self):
        return "com.google.common.collect.Immutable%s<%s>" % (
                   self._java_interface_simple_name(),
                   self.element_type.java_boxed_qname()
               )

    def java_qname(self):
        return self.__java_qname()

    def _java_interface_simple_name(self):
        class_name_split = decamelize(self.__class__.__name__).split('_')
        assert len(class_name_split) == 3
        assert class_name_split[0] == 'java'
        assert class_name_split[2] == 'type'
        return class_name_split[1].capitalize()

    def java_literal(self, value):
        return "com.google.common.collect.Immutable%s.<%s> of(%s)" % (
            self._java_interface_simple_name(),
            self.element_type.java_boxed_qname(),
            ', '.join(self.element_type.java_literal(element_value) for element_value in value)
        )

    def java_read_protocol(self):
        element_read_protocol = self.element_type.java_read_protocol()
        add_element = "sequenceBuilder.add(%(element_read_protocol)s);" % locals()
        element_read_protocol_throws = self.element_type.java_read_protocol_throws_checked() + self.element_type.java_read_protocol_throws_unchecked()
        if len(element_read_protocol_throws) > 0:
            add_element = indent(' ' * 4, add_element)
            add_element = """\
try {
%s
}%s
""" % (add_element, ''.join("""\
 catch (final %(exception_type_name)s e) {
     throw new org.thryft.protocol.InputProtocolException(e);
}""" % locals()
                     for exception_type_name in element_read_protocol_throws))
        add_element = indent(' ' * 16, add_element)

        element_type_name = self.element_type.java_boxed_qname()
        interface_simple_name = self._java_interface_simple_name()

        return """\
(new com.google.common.base.Function<org.thryft.protocol.InputProtocol, com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s>>() {
    @Override
    public com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s> apply(final org.thryft.protocol.InputProtocol iprot) {
        try {
            final org.thryft.protocol.%(interface_simple_name)sBegin sequenceBegin = iprot.read%(interface_simple_name)sBegin();
            final com.google.common.collect.Immutable%(interface_simple_name)s.Builder<%(element_type_name)s> sequenceBuilder = com.google.common.collect.Immutable%(interface_simple_name)s.builder();
            for (int elementI = 0; elementI < sequenceBegin.getSize(); elementI++) {
%(add_element)s
            }
            iprot.read%(interface_simple_name)sEnd();
            return sequenceBuilder.build();
        } catch (final org.thryft.protocol.InputProtocolException e) {
            throw new org.thryft.protocol.UncheckedInputProtocolException(e);
        }
    }
}).apply(iprot)""" % locals()

    def java_read_protocol_throws_unchecked(self):
        return ['org.thryft.protocol.UncheckedInputProtocolException']

    def java_write_protocol(self, value, depth=0):
        element_ttype = self.element_type.thrift_ttype_name()
        element_type_name = self.element_type.java_boxed_qname()
        element_write_protocol = \
            indent(' ' * 4,
                self.element_type.java_write_protocol(
                    "_iter%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        interface_simple_name = self._java_interface_simple_name()
        return """\
oprot.write%(interface_simple_name)sBegin(org.thryft.protocol.Type.%(element_ttype)s, %(value)s.size());
for (final %(element_type_name)s _iter%(depth)u : %(value)s) {
%(element_write_protocol)s
}
oprot.write%(interface_simple_name)sEnd();""" % locals()
