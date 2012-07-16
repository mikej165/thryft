from thryft.target.container_types.list_type import ListType
from thryft.targets.java.java_compound_type import JavaCompoundType
from yutil import indent


class JavaListType(ListType, JavaCompoundType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableList<%s>" % \
                self.element_type.java_name(boxed=True)

    def java_read_protocol(self):
        element_read_protocol = self.element_type.java_read_protocol()
        element_type_name = self.element_type.java_name()
        return """\
(new com.google.common.base.Function<org.apache.thrift.protocol.TProtocol, com.google.common.collect.ImmutableList<%(element_type_name)s>>() {
    @Override
    public com.google.common.collect.ImmutableList<%(element_type_name)s> apply(org.apache.thrift.protocol.TProtocol iprot) {
        try {
            org.apache.thrift.protocol.TList listBegin = iprot.readListBegin();
            java.util.List<%(element_type_name)s> list = com.google.common.collect.Lists.newArrayList();
            for (int elementI = 0; elementI < listBegin.size; elementI++) {
                list.add(%(element_read_protocol)s);
            }
            iprot.readListEnd();
            return com.google.common.collect.ImmutableList.copyOf(list);
        } catch (org.apache.thrift.TException e) {
            return com.google.common.collect.ImmutableList.of();
        }
    }
}).apply(iprot)""" % locals()

    def java_write_protocol(self, value, depth=0):
        element_ttype = self.element_type.thrift_ttype_name()
        element_type_name = self.element_type.java_name()
        element_write_protocol = \
            indent(' ' * 4,
                self.element_type.java_write_protocol(
                    "_iter%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        return """\
oprot.writeListBegin(new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.%(element_ttype)s, %(value)s.size()));
for (%(element_type_name)s _iter%(depth)u : %(value)s) {
%(element_write_protocol)s
}
oprot.writeListEnd();""" % locals()
