from thryft.generators.java.java_type import JavaType
from yutil import lpad, indent, pad, rpad


class JavaCompoundType(JavaType):
    class _JavaBuilder(object):
        def __init__(self, java_struct_type):
            object.__init__(self)
            self.__java_struct_type = java_struct_type

        def __getattr__(self, attr):
            return getattr(self.__java_struct_type, attr)

        def _java_constructor_copy(self):
            initializers = []
            for field in self.fields:
                getter_name = field.java_getter_name()  # IGNORE:W0612
                variable_name = field.java_name()  # IGNORE:W0612
                initializers.append(
                    "this.%(variable_name)s = other.%(getter_name)s();" % \
                        locals()
                )
            initializers = \
                lpad("\n", "\n".join(indent(' ' * 4,
                    initializers
                )))
            name = self.java_name()
            return """\
public Builder(final %(name)s other) {%(initializers)s
}""" % locals()

        def _java_constructor_default(self):
            return """\
public Builder() {
}""" % locals()

        def _java_constructors(self):
            return [
                self._java_constructor_default(),
                self._java_constructor_copy()
            ]

        def _java_member_declarations(self):
            return [field.java_member_declaration(boxed=True, final=False)
                    for field in self.fields]

        def _java_method_build(self):
            field_names = \
                ', '.join([field.java_name() for field in self.fields])
            name = self.java_name()
            return {'build': """\
public %(name)s build() {
    return _build(%(field_names)s);
}""" % locals()}

        def _java_method__build(self):
            field_names = \
                ', '.join([field.java_name() for field in self.fields])
            field_parameters = \
                ', '.join([field.java_parameter(final=True) for field in self.fields])
            name = self.java_name()
            return {'_build': """\
protected %(name)s _build(%(field_parameters)s) {
    return new %(name)s(%(field_names)s);
}""" % locals()}

#        def _java_method_read_protocol(self):
#            field_read_protocols = \
#                lpad(' else ', indent(' ' * 8, ' else '.join(
#                    [field.java_read_protocol()
#                     for field in self.fields]
#                )))
#            name = self.java_name()
#            readStructBegin = lpad("\n", indent(' ' * 4, 'iprot.readStructBegin();'))
#            readStructEnd = lpad("\n", indent(' ' * 4, 'iprot.readStructEnd();'))
#            return {'read': """\
# @Override
# public void read(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {%(readStructBegin)s
#    while (true) {
#        org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
#        if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
#            break;
#        }%(field_read_protocols)s
#        iprot.readFieldEnd();
#    }%(readStructEnd)s
# }""" % locals()}

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
            methods.update(self._java_method__build())
            methods.update(self._java_method_setters())
            # methods.update(self._java_method_read_protocol()) # Must be after TBase
            return methods

        def __repr__(self):
            name = self.java_name()
            methods = self._java_methods()
            sections = []
            sections.append("\n\n".join(indent(' ' * 4,
                self._java_constructors() + [methods[key] for key in sorted(methods.iterkeys())]
            )))
            sections.append("\n".join(indent(' ' * 4, self._java_member_declarations())))
            sections = lpad("\n", "\n\n".join(sections))
            return """\
public static class Builder {%(sections)s
}""" % locals()

    def __init__(self, java_class_modifiers=None, java_suppress_warnings=None, **kwds):
        if java_class_modifiers is None:
            java_class_modifiers = ('public',)
        elif isinstance(java_class_modifiers, str):
            java_class_modifiers = tuple(java_class_modifiers.split())
        else:
            java_class_modifiers = tuple(java_class_modifiers)
        self.__class_modifiers = java_class_modifiers

        if java_suppress_warnings is None:
            self.__suppress_warnings = ('serial',)
        else:
            self.__suppress_warnings = tuple(java_suppress_warnings)

    def _java_constructor_default(self):
        name = self.java_name()

        if len(self.fields) == 0:
            return """\
public %(name)s() {
}""" % locals()

        for field in self.fields:
            if field.required:
                return None  # Will be covered by total constructor

        initializers = \
            lpad("\n", "\n".join(indent(' ' * 4,
                [field.java_default_initializer()
                 for field in self.fields]
            )))
        return """\
public %(name)s() {%(initializers)s
}""" % locals()

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

    def _java_constructor_protocol(self):
        field_declarations = \
            pad("\n", indent(' ' * 4, "\n".join(
                [field.java_local_declaration(final=False)
                 for field in self.fields]
            )), "\n")
        field_initializers = \
            lpad("\n\n", "\n".join(indent(' ' * 4,
                [field.java_initializer()
                 for field in self.fields]
            )))
        field_protocol_named_initializers = \
            lpad(' else ', indent(' ' * 16, ' else '.join(
                ["""\
if (ifield.name.equals("%s")) {
%s
}""" % (field.name, indent(' ' * 4, field.java_protocol_initializer()))
                 for field in self.fields]
            )))
        field_protocol_positional_initializers = \
            lpad("\n", indent(' ' * 12, "\n".join([
                field.java_protocol_initializer()
                for field in self.fields
            ])))
        name = self.java_name()
        return """\
public %(name)s(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    this(iprot, org.apache.thrift.protocol.TType.STRUCT);
}
        
public %(name)s(final org.apache.thrift.protocol.TProtocol iprot, final byte readAsTType) throws org.apache.thrift.TException {%(field_declarations)s
    switch (readAsTType) {
        case org.apache.thrift.protocol.TType.LIST:
            iprot.readListBegin();%(field_protocol_positional_initializers)s           
            iprot.readListEnd();
            break;
    
        case org.apache.thrift.protocol.TType.STRUCT:
            iprot.readStructBegin();
            while (true) {
                org.apache.thrift.protocol.TField ifield = iprot.readFieldBegin();
                if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
                    break;
                }%(field_protocol_named_initializers)s
                iprot.readFieldEnd();
            }
            iprot.readStructEnd();
            break;
        
        default: 
            throw new org.apache.thrift.TException("unknown readAsType");
    }%(field_initializers)s    
}""" % locals()

    def _java_constructor_required(self):
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor
        elif len(set([field.required for field in self.fields])) <= 1:
            # All fields are optional or all fields are required
            return None  # Will be covered by total constructor

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
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor

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
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor

        for field in self.fields:
            if field.required and \
               (field.type.java_declaration_name(boxed=True) != \
                field.type.java_declaration_name(boxed=False)):
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
            self._java_constructor_default(),
            self._java_constructor_copy(),
            self._java_constructor_protocol(),
            self._java_constructor_required(),
            self._java_constructor_total(),
            self._java_constructor_total_boxed()
        ):
            if constructor is not None:
                constructors.append(constructor)
        return constructors

    def java_default_value(self):
        return 'null'

    def java_hash_code(self, value):
        return "%(value)s.hashCode()" % locals()

    def java_is_reference(self):
        return True

    def _java_extends(self):
        return None

    def _java_implements(self):
        name = self.java_name()
        return ["org.apache.thrift.TBase<%(name)s, org.apache.thrift.TFieldIdEnum>" % locals()]

    def _java_member_declarations(self):
        return [field.java_member_declaration(final=True)
                for field in self.fields]

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
public boolean equals(final Object otherObject) {
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
                ('compareTo', "int compareTo(final %(name)s other)" % locals()),
                ('deepCopy', "org.apache.thrift.TBase<%(name)s, org.apache.thrift.TFieldIdEnum> deepCopy()" % locals()),
                ('fieldForId', 'org.apache.thrift.TFieldIdEnum fieldForId(final int fieldId)'),
                ('getFieldValue', 'Object getFieldValue(final org.apache.thrift.TFieldIdEnum field)'),
                ('isSet', 'boolean isSet(final org.apache.thrift.TFieldIdEnum field)'),
                ('setFieldValue', 'void setFieldValue(final org.apache.thrift.TFieldIdEnum field, Object value)'),
                ('read', 'void read(final org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException'),
                ('write', 'void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException'),
            )
        )

    def _java_method_to_string(self):
        add_statements = []
        for field in self.fields:
            add_statement = \
                """helper.add(\"%s\", %s());""" % (field.name, field.java_getter_name())
            if not field.required:
                add_statement = """\
if (%s() != null) {
    %s
}""" % (field.java_getter_name(), add_statement)
            add_statements.append(add_statement)
        add_statements = lpad("\n", "\n".join(indent(' ' * 4, add_statements)))
        return {'toString': """\
@Override
public String toString() {
    final com.google.common.base.Objects.ToStringHelper helper = com.google.common.base.Objects.toStringHelper(this);%(add_statements)s
    return helper.toString();
}""" % locals()}

    def _java_method_write_protocol(self):
        field_write_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                [field.java_write_protocol(depth=0)
                 for field in self.fields]
            )))
        name = self.java_name()
        return {'write': """\
@Override        
public void write(final org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
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
        methods.update(self._java_method_TBase())
        methods.update(self._java_method_to_string())
        methods.update(self._java_method_write_protocol())  # Must be after TBase
        return methods

    def java_read_protocol(self):
        qname = self.java_qname()
        return "new %(qname)s(iprot)" % locals()

    def java_to_string(self, value):
        return "%(value)s.toString()" % locals()

    def java_write_protocol(self, value, depth=0):
        return "%(value)s.write(oprot);" % locals()

    def __repr__(self):
        class_annotations = []
        if len(self.__suppress_warnings) > 0:
            class_annotations.append(
                "@SuppressWarnings({%s})" % \
                    ', '.join(['"' + warning + '"'
                               for warning in sorted(self.__suppress_warnings)]))
        class_annotations = rpad("\n".join(class_annotations), "\n")
        class_modifiers = rpad(' '.join(self.__class_modifiers), ' ')
        name = self.java_name()
        extends = lpad(' extends ', self._java_extends())
        implements = lpad(' implements ', ', '.join(self._java_implements()))
        methods = self._java_methods()
        sections = []
        sections.append(indent(' ' * 4, repr(self._JavaBuilder(self))))
        sections.append("\n\n".join(indent(' ' * 4,
            self._java_constructors() + \
            [methods[key] for key in sorted(methods.iterkeys())])))
        sections.append("\n".join(indent(' ' * 4, self._java_member_declarations())))
        sections = lpad("\n", "\n\n".join(sections))
        return """\
%(class_annotations)s%(class_modifiers)sclass %(name)s%(extends)s%(implements)s {%(sections)s
}""" % locals()
