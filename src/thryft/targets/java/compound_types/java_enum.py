from thryft.target.compound_type import CompoundType
from yutil import indent


class JavaEnum(CompoundType):
    def java_is_reference(self):
        return True

    def java_name(self, boxed=False):
        return self.name

    def __repr__(self):
        name = self.java_name()
        if len(self.fields) == 0:
            return """\
public enum %(name)s {
}"""
        for enumerator in self.fields:
            if enumerator.value is not None:
                enumerators = []
                for enumerator in self.fields:
                    enumerators.append(
                        "%s(%u)" % (enumerator.name, enumerator.value)
                    )
                enumerators = ",\n".join(indent(' ' * 4, enumerators))
                return """\
public enum %(name)s {
%(enumerators)s;

    private %(name)s(int value) {
        this.value = value;
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
%(enumerators)s
}""" % locals()
