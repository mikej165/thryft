from thryft.generator.compound_types.enum_type import EnumType
from thryft.generators.java.java_type import JavaType
from yutil import indent


class JavaEnumType(EnumType, JavaType):
    def java_default_value(self):
        return 'null'

    def java_hash_code(self, value):
        return "%(value)s.ordinal()" % locals()

    def java_is_reference(self):
        return True

    def java_read_protocol(self):
        qname = self.java_qname()
        return "(iprot instanceof org.thryft.protocol.Protocol) ? ((org.thryft.protocol.Protocol)iprot).readEnum(%(qname)s.class) : %(qname)s.valueOf(iprot.readString().trim().toUpperCase())" % locals()

    def java_read_protocol_throws(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "if (oprot instanceof org.thryft.protocol.Protocol) { ((org.thryft.protocol.Protocol)oprot).writeEnum(%(value)s); } else { oprot.writeString(%(value)s.toString()); }" % locals()

    def __repr__(self):
        name = self.java_name()
        if len(self.enumerators) == 0:
            return """\
public enum %(qname)s {
}"""
        for enumerator in self.enumerators:
            if enumerator.value is not None:
                valueOfInt_cases = []
                enumerators = []
                for enumerator in self.enumerators:
                    valueOfInt_cases.append(
"case %u: return %s;" % (enumerator.value, enumerator.name))
                    enumerators.append(
                        "%s(%u)" % (enumerator.name, enumerator.value)
                    )
                valueOfInt_cases = "\n".join(indent(' ' * 8, valueOfInt_cases))
                enumerators = ",\n".join(indent(' ' * 4, enumerators))
                return """\
public enum %(name)s {
%(enumerators)s;

    private %(name)s(int value) {
        this.value = value;
    }
    
    public static %(name)s valueOfInt(final int value) {
        switch (value) {
%(valueOfInt_cases)s
        default: throw new IllegalArgumentException();
        }
    }

    public final int value() {
        return value;
    }
        
    private final int value;
}""" % locals()

        enumerators = \
            ",\n".join(indent(' ' * 4,
                [enumerator.name for enumerator in self.enumerators]
            ))
        return """public enum %(name)s {
%(enumerators)s;
}""" % locals()

    def java_to_string(self, value):
        return "%(value)s.toString()" % locals()
