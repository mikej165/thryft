from thryft.target.container_types.list_type import ListType
from thryft.targets.java.java_compound_type import JavaCompoundType
from yutil import indent


class JavaListType(ListType, JavaCompoundType):
    def java_name(self, boxed=False):
        return "com.google.common.collect.ImmutableList<%s>" % \
                self.element_type.java_name(boxed=True)

    def java_write_protocol(self, value, depth=0):
        element_ttype = self.element_type.thrift_protocol_name()
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
