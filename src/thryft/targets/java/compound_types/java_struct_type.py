from thryft.target.compound_types.struct_type import StructType
from thryft.targets.java.java_compound_type import JavaCompoundType
from yutil import indent, lpad


class JavaStructType(StructType, JavaCompoundType):
    def _java_builder(self):
        constructor_parameters = \
            ', '.join([field.java_name() for field in self.fields])
        declarations = \
            lpad("\n\n", "\n".join(indent(' ' * 4,
                [field.java_declaration(final=False)
                 for field in self.fields]
            )))
        name = self.java_name()
        setters = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                [field.java_setter(return_type_name='Builder')
                 for field in self.fields]
            )))
        return """\
public static class Builder {
    public %(name)s build() {
        return new %(name)s(%(constructor_parameters)s);
    }%(setters)s%(declarations)s
}""" % locals()

    def _java_constructor_default(self):
        name = self.java_name()

        if len(self.fields) == 0:
            return """\
public %(name)s() {
}""" % locals()

        initializers = \
            lpad("\n", "\n".join(indent(' ' * 4,
                [field.java_default_initializer()
                 for field in self.fields]
            )))

        for field in self.fields:
            if field.required:
                return """\
protected %(name)s() {%(initializers)s
}""" % locals()

        return """\
public %(name)s() {%(initializers)s
}""" % locals()

    def _java_constructor_required(self):
        if len(self.fields) == 0:
            return None # Will be covered by default constructor

        for field in self.fields:
            if field.required:
                initializers = []
                name = self.java_name()
                parameters = []
                for field in self.fields:
                    field_name = field.java_name()
                    if field.required:
                        initializers.append(field.java_initializer())
                        parameters.append(field.java_parameter(final=True))
                    else:
                        initializers.append(field.java_default_initializer())
                initializers = "\n".join(indent(' ' * 4, initializers))
                parameters = ", ".join(parameters)
                return """\
public %(name)s(%(parameters)s) {
%(initializers)s
}""" % locals()

        return None # Will be covered by total constructor

    def _java_constructor_total(self):
        if len(self.fields) == 0:
            return None # Will be covered by default constructor

        initializers = []
        name = self.java_name()
        parameters = []
        for field in self.fields:
            field_name = field.java_name()
            initializers.append("this.%(field_name)s = %(field_name)s;" % locals())
            parameters.append(field.java_parameter(final=True))
        initializers = "\n".join(indent(' ' * 4, initializers))
        parameters = ", ".join(parameters)
        return """\
public %(name)s(%(parameters)s) {
%(initializers)s
}""" % locals()

    def _java_constructors(self):
        constructors = []
        for constructor in (
            self._java_constructor_default(),
            self._java_constructor_required(),
            self._java_constructor_total()
        ):
            if constructor is not None:
                constructors.append(constructor)
        return constructors

    def _java_declarations(self):
        return [field.java_declaration(final=True) for field in self.fields]

    def _java_method_equals(self):
        name = self.java_name()

        field_equal_tests = []
        for field in self.fields:
            field_equal_tests.append(
                field.java_equals(field.java_getter_name() + '()',
                                  'other.' + field.java_getter_name() + '()')
            )
        if len(field_equal_tests) > 0:
            field_equal_tests = \
                "final %(name)s other = (%(name)s)otherObject;\n" % \
                     locals() + \
                ' ' * 4 + "return\n" + \
                    indent(' ' * 8,
                           " && \n".join(field_equal_tests))
        else:
            field_equal_tests = 'return true'

        struct_equal_tests = []
        struct_equal_tests.append('''\
if (otherObject == this) {
    return true;
}''')
        struct_equal_tests.append("""\
if (!(otherObject instanceof %(name)s)) {
    return false;
}""" % locals())
        struct_equal_tests = \
            indent(' ' * 4,
                ' else '.join(struct_equal_tests)
            )

        return {'equals': """\
@Override
public boolean equals(Object otherObject) {
%(struct_equal_tests)s

    %(field_equal_tests)s;
}""" % locals()}

    def _java_method_getters(self):
        return dict((field.java_getter_name(), field.java_getter())
                    for field in self.fields)

    def _java_method_hash_code(self):
        statements = ['int hashCode = 17;']
        for field in self.fields:
            value = field.java_getter_name() + '()'
            hashCode_update = \
                'hashCode = 31 * hashCode + ' + \
                    field.type.java_hash_code(value) + \
                ';'
            if not field.required:
                hashCode_update = """\
if (%(value)s != null) {
    %(hashCode_update)s
}""" % locals()
            statements.append(hashCode_update)
        statements = \
            "\n".join(indent(' ' * 4, statements))
        return {'hashCode': """\
@Override
public int hashCode() {
%(statements)s
    return hashCode;
}""" % locals()}

    def _java_method_write_protocol(self):
        statements = []
        statements.append(
            "oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct(\"%s\"));" % \
                self.java_name()
        )
        for field in self.fields:
            statements.append(field.java_write_protocol(depth=0))
        statements.append('oprot.writeFieldStop();')
        statements.append('oprot.writeStructEnd();')
        statements = "\n\n".join(indent(' ' * 4, statements))
        return {'write': """\
public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
%(statements)s
}""" % locals()}

    def _java_methods(self):
        methods = {}
        methods.update(self._java_method_equals())
        methods.update(self._java_method_getters())
        methods.update(self._java_method_hash_code())
        methods.update(self._java_method_write_protocol())
        return self._java_constructors() + \
               [methods[key] for key in sorted(methods.iterkeys())]

    def __repr__(self):
        name = self.name

        sections = []
        sections.append(indent(' ' * 4, self._java_builder()))
        sections.append("\n\n".join(indent(' ' * 4, self._java_methods())))
        sections.append("\n".join(indent(' ' * 4, self._java_declarations())))
        sections = lpad("\n", "\n\n".join(sections))

        return """\
public class %(name)s {%(sections)s
}""" % locals()
