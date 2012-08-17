from thryft.generator.compound_types.struct_type import StructType
from thryft.generators.java.java_compound_type import JavaCompoundType
from yutil import indent, lpad, pad


class JavaStructType(StructType, JavaCompoundType):
    class _JavaBuilder(object):
        def __init__(self, java_struct_type):
            object.__init__(self)
            self.__java_struct_type = java_struct_type

        def __getattr__(self, attr):
            return getattr(self.__java_struct_type, attr)

        def _java_declarations(self):
            return [field.java_declaration(boxed=True, final=False)
                    for field in self.fields]

        def _java_method_build(self):
            constructor_parameters = \
                ', '.join([field.java_name() for field in self.fields])
            name = self.java_name()
            return {'build': """\
public %(name)s build() {
    return new %(name)s(%(constructor_parameters)s);
}""" % locals()}

        def _java_method_read_protocol(self):
            field_read_protocols = \
                lpad(' else ', indent(' ' * 8, ' else '.join(
                    [field.java_read_protocol()
                     for field in self.fields]
                )))
            name = self.java_name()
            return {'read': """\
@Override
public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    org.apache.thrift.protocol.TStruct structBegin = iprot.readStructBegin();
    if (structBegin == null) {
        return;
    }
    while (true) {
        org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
        if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
            break;
        }%(field_read_protocols)s

        iprot.readFieldEnd();
    }
    iprot.readStructEnd();
}""" % locals()}

        def _java_method_setters(self):
            return \
                dict((
                    field.java_setter_name(),
                    field.java_setter(return_type_name='Builder')
                )
                for field in self.fields)

        def _java_methods(self):
            methods = {}
            methods.update(self._java_method_build())
            methods.update(self._java_method_setters())
            methods.update(self._java_method_TBase())
            methods.update(self._java_method_read_protocol()) # Must be after TBase
            return [methods[key] for key in sorted(methods.iterkeys())]

        def __repr__(self):
            name = self.java_name()
            sections = []
            sections.append("\n\n".join(indent(' ' * 4, self._java_methods())))
            sections.append("\n".join(indent(' ' * 4, self._java_declarations())))
            sections = lpad("\n", "\n\n".join(sections))
            return """\
public static class Builder implements org.apache.thrift.TBase <%(name)s, org.apache.thrift.TFieldIdEnum> {%(sections)s
}""" % locals()

#    def _java_constructor_default(self):
#        name = self.java_name()
#
#        if len(self.fields) == 0:
#            return """\
#public %(name)s() {
#}""" % locals()
#
#        initializers = \
#            lpad("\n", "\n".join(indent(' ' * 4,
#                [field.java_default_initializer()
#                 for field in self.fields]
#            )))
#
#        for field in self.fields:
#            if field.required:
#                return """\
#protected %(name)s() {%(initializers)s
#}""" % locals()
#
#        return """\
#public %(name)s() {%(initializers)s
#}""" % locals()

    def _java_constructor_copy(self):
        name = self.java_name()
        this_call = \
            indent(' ' * 4,
                pad("\nthis(",
                    ', '.join(['other.' + field.java_getter_name() + '()'
                               for field in self.fields]),
                ");\n")
            )
        return """\
public %(name)s(final %(name)s other) {%(this_call)s
}""" % locals()

    def _java_constructor_required(self):
        fields_required = set([field.required for field in self.fields])
        if len(fields_required) <= 1:
            # All fields are optional or all fields are required
            return None # Will be covered by total constructor

        initializers = []
        name = self.java_name()
        parameters = []
        for field in self.fields:
            if field.required:
                initializers.append(field.java_initializer())
                parameters.append(field.java_parameter(final=True))
            else:
                initializers.append(field.java_default_initializer())
        initializers = \
            lpad("\n", "\n".join(indent(' ' * 4, initializers)))
        parameters = ", ".join(parameters)
        return """\
public %(name)s(%(parameters)s) {%(initializers)s
}""" % locals()

    def _java_constructor_total(self):
#        if len(self.fields) == 0:
#            return None # Will be covered by default constructor

        initializers = \
            "\n".join(indent(' ' * 4,
                [field.java_initializer()
                 for field in self.fields]
            ))
        name = self.java_name()
        parameters = ', '.join([field.java_parameter(final=True)
                                for field in self.fields])
        return """\
public %(name)s(%(parameters)s) {
%(initializers)s
}""" % locals()

    def _java_constructor_total_boxed(self):
        for field in self.fields:
            if field.required and \
               (field.type.java_name(boxed=True) != \
                field.type.java_name(boxed=False)):
                initializers = \
                    "\n".join(indent(' ' * 4,
                        [field.java_initializer()
                         for field in self.fields]
                    ))
                name = self.java_name()
                parameters = ', '.join([field.java_parameter(boxed=True, final=True)
                                        for field in self.fields])
                return """\
public %(name)s(%(parameters)s) {
%(initializers)s
}""" % locals()

    def _java_constructors(self):
        constructors = []
        for constructor in (
            # self._java_constructor_default(),
            self._java_constructor_copy(),
            self._java_constructor_required(),
            self._java_constructor_total(),
            self._java_constructor_total_boxed()
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

    def _java_method_get(self):
        fields = []
        for field in self.fields:
            field_name = field.name
            field_getter_name = field.java_getter_name()
            fields.append("""\
if (fieldName.equals("%(field_name)s")) {
    return %(field_getter_name)s();
}""" % locals())
        fields = lpad("\n", indent(' ' * 4, ' else '.join(fields)))
        return {'get': """\
public Object get(final String fieldName) {%(fields)s
    return null;
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

    def _java_method_readStatic_protocol(self):
        name = self.java_name()
        return {'readStatic': """\
public static %(name)s readStatic(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    Builder builder = new Builder();
    builder.read(iprot);
    return builder.build(); 
}""" % locals()}

    def _java_method_TBase(self):
        name = self.java_name()
        return dict((
            method_name,
            """\
@Override
public %(method_signature)s {
throw new UnsupportedOperationException();
}""" % locals())
            for method_name, method_signature in (
                ('clear', 'void clear()'),
                ('compareTo', "int compareTo(%(name)s other)" % locals()),
                ('deepCopy', "org.apache.thrift.TBase<%(name)s, org.apache.thrift.TFieldIdEnum> deepCopy()" % locals()),
                ('fieldForId', 'org.apache.thrift.TFieldIdEnum fieldForId(int fieldId)'),
                ('getFieldValue', 'Object getFieldValue(org.apache.thrift.TFieldIdEnum field)'),
                ('isSet', 'boolean isSet(org.apache.thrift.TFieldIdEnum field)'),
                ('setFieldValue', 'void setFieldValue(org.apache.thrift.TFieldIdEnum field, Object value)'),
                ('read', 'void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException'),
                ('write', 'void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException'),
            )
        )

    def _java_method_write_protocol(self):
        field_write_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                [field.java_write_protocol(depth=0)
                 for field in self.fields]
            )))
        name = self.java_name()
        return {'write': """\
@Override        
public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    oprot.writeStructBegin(new org.apache.thrift.protocol.TStruct(\"%(name)s\"));%(field_write_protocols)s

    oprot.writeFieldStop();

    oprot.writeStructEnd();
}""" % locals()}

    def _java_methods(self):
        methods = {}
        methods.update(self._java_method_equals())
        methods.update(self._java_method_get())
        methods.update(self._java_method_getters())
        methods.update(self._java_method_hash_code())
        methods.update(self._java_method_readStatic_protocol())
        methods.update(self._java_method_TBase())
        methods.update(self._java_method_write_protocol()) # Must be after TBase
        return self._java_constructors() + \
               [methods[key] for key in sorted(methods.iterkeys())]

    def java_read_protocol(self):
        name = self.java_name()
        return "%(name)s.readStatic(iprot)" % locals()

    def java_write_protocol(self, value, depth=0):
        return "%(value)s.write(oprot);" % locals()

    def __repr__(self):
        name = self.java_name()
        sections = []
        sections.append(indent(' ' * 4, repr(self._JavaBuilder(self))))
        sections.append("\n\n".join(indent(' ' * 4, self._java_methods())))
        sections.append("\n".join(indent(' ' * 4, self._java_declarations())))
        sections = lpad("\n", "\n\n".join(sections))
        return """\
@SuppressWarnings("serial")
public class %(name)s implements org.apache.thrift.TBase<%(name)s, org.apache.thrift.TFieldIdEnum> {%(sections)s
}""" % locals()
