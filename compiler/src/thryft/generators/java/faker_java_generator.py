from thryft.generators.java import java_generator
from thryft.generators.java.java_struct_type import JavaStructType
from yutil import indent, lpad


class FakerJavaGenerator(java_generator.JavaGenerator):
    class StructType(JavaStructType):
        def java_name(self):
            return JavaStructType.java_name(self) + 'Faker'

        def __repr__(self):
            name = self.java_name()
            setter_calls = \
                lpad("\n", "\n".join(indent(' ' * 8,
                    ("builder.%s(%s);" % (field.java_setter_name(), field.java_faker())
                     for field in self.fields)
                )))
            struct_type_name = JavaStructType.java_qname(self)
            return """\
public final class %(name)s {
    public static %(struct_type_name)s fake() {
        %(struct_type_name)s.Builder builder = new %(struct_type_name)s.Builder();%(setter_calls)s
        return builder.build();
    }

    private %(name)s() {
    }
}""" % locals()
