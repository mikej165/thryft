from thryft.generator.compound_types.enum_type import EnumType
from thryft.generators.java.java_compound_type import JavaCompoundType
from yutil import indent


class JavaEnumType(EnumType, JavaCompoundType):
    def java_hash_code(self, value):
        return "%(value)s.ordinal()" % locals()

    def java_read_protocol(self):
        name = self.java_name()
        return "%(name)s.byName(iprot.readString().trim().toUpperCase())" % locals()

    def java_read_protocol_throws(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeString(%(value)s.toString());" % locals()

    def __repr__(self):
        name = self.java_name()
        if len(self.fields) == 0:
            return """\
public enum %(name)s {
}"""
        for enumerator in self.fields:
            if enumerator.value is not None:
                byValue_cases = []
                enumerators = []
                for enumerator in self.fields:
                    byValue_cases.append(
"case %u: return %s;" % (enumerator.value, enumerator.name))
                    enumerators.append(
                        "%s(%u)" % (enumerator.name, enumerator.value)
                    )
                byValue_cases = "\n".join(indent(' ' * 8, byValue_cases))
                enumerators = ",\n".join(indent(' ' * 4, enumerators))
                return """\
public enum %(name)s {
%(enumerators)s;

    private %(name)s(int value) {
        this.value = value;
    }

    public static %(name)s byName(final String name) {
        try {
            return valueOf(name);
        } catch (IllegalArgumentException e1) {
            try {
                return byValue(Integer.parseInt(name));
            } catch (NumberFormatException e2) {
                throw e1;
            }
        }
    }
    
    public static %(name)s byValue(final int value) {
        switch (value) {
%(byValue_cases)s
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
                [enumerator.name for enumerator in self.fields]
            ))
        return """public enum %(name)s {
%(enumerators)s;

    public static %(name)s byName(final String name) {
        return valueOf(name);
    }
}""" % locals()
