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

    def java_read_protocol(self):
        element_read_protocol = self.element_type.java_read_protocol()
        element_type_name = self.element_type.java_declaration_name(boxed=True)
        interface_simple_name = self._java_interface_simple_name()
        mutable_raw_qname = self._java_mutable_raw_qname()
        return """\
(new com.google.common.base.Function<org.apache.thrift.protocol.TProtocol, com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s>>() {
    @Override
    public com.google.common.collect.Immutable%(interface_simple_name)s<%(element_type_name)s> apply(org.apache.thrift.protocol.TProtocol iprot) {
        try {
            org.apache.thrift.protocol.T%(interface_simple_name)s sequenceBegin = iprot.read%(interface_simple_name)sBegin();
            java.util.%(interface_simple_name)s<%(element_type_name)s> sequence = new %(mutable_raw_qname)s<%(element_type_name)s>();
            for (int elementI = 0; elementI < sequenceBegin.size; elementI++) {
                sequence.add(%(element_read_protocol)s);
            }
            iprot.read%(interface_simple_name)sEnd();
            return com.google.common.collect.Immutable%(interface_simple_name)s.copyOf(sequence);
        } catch (org.apache.thrift.TException e) {
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
for (%(element_type_name)s _iter%(depth)u : %(value)s) {
%(element_write_protocol)s
}
oprot.write%(interface_simple_name)sEnd();""" % locals()
