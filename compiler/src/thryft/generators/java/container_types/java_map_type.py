from thryft.generator.container_types.map_type import MapType
from thryft.generators.java.java_container_type import JavaContainerType
from yutil import indent


class JavaMapType(MapType, JavaContainerType):
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
(new com.google.common.base.Function<org.apache.thrift.protocol.TProtocol, com.google.common.collect.ImmutableMap<%(key_type_name)s, %(value_type_name)s>>() {
    @Override
    public com.google.common.collect.ImmutableMap<%(key_type_name)s, %(value_type_name)s> apply(org.apache.thrift.protocol.TProtocol iprot) {
        try {
            org.apache.thrift.protocol.TMap mapBegin = iprot.readMapBegin();
            java.util.Map<%(key_type_name)s, %(value_type_name)s> map = new java.util.HashMap<%(key_type_name)s, %(value_type_name)s>();
            for (int entryI = 0; entryI < mapBegin.size; entryI++) {                    
                map.put(%(key_read_protocol)s, %(value_read_protocol)s);
            }
            iprot.readMapEnd();
            return com.google.common.collect.ImmutableMap.copyOf(map);
        } catch (org.apache.thrift.TException e) {
            return com.google.common.collect.ImmutableMap.of();
        }
    }
}).apply(iprot)""" % locals()

    def java_to_summary_string(self, value):
        key_type_qname = self.key_type.java_qname(boxed=True)
        value_type_qname = self.value_type.java_qname(boxed=True)
        return '"map<%(key_type_qname)s, %(value_type_qname)s>" + "(size=" + Integer.toString(%(value)s.size()) + ")"' % locals()

    def java_write_protocol(self, value, depth=0):
        key_ttype = self.key_type.thrift_ttype_name()
        key_type_name = self.key_type.java_declaration_name()
        key_write_protocol = \
            indent(' ' * 4,
                self.key_type.java_write_protocol(
                    "_iter%(depth)u.getKey()" % locals(),
                    depth=depth + 1
                )
            )
        value_ttype = self.value_type.thrift_ttype_name()
        value_type_name = self.value_type.java_declaration_name()
        value_write_protocol = \
            indent(' ' * 4,
                self.value_type.java_write_protocol(
                    "_iter%(depth)u.getValue()" % locals(),
                    depth=depth + 1
                )
            )
        return """\
oprot.writeMapBegin(new org.apache.thrift.protocol.TMap(org.apache.thrift.protocol.TType.%(key_ttype)s, org.apache.thrift.protocol.TType.%(value_ttype)s, %(value)s.size()));
for (com.google.common.collect.ImmutableMap.Entry<%(key_type_name)s, %(value_type_name)s> _iter%(depth)u : %(value)s.entrySet()) {
%(key_write_protocol)s
%(value_write_protocol)s
}
oprot.writeMapEnd();""" % locals()
