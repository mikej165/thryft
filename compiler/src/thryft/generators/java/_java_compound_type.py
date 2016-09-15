# -----------------------------------------------------------------------------
# Copyright (c) 2016, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from thryft.generators.java._java_type import _JavaType
from yutil import lpad, indent, pad, rpad, upper_camelize


class _JavaCompoundType(_JavaType):
    class _JavaBuilder(object):
        def __init__(self, java_compound_type):
            object.__init__(self)
            self.__java_compound_type = java_compound_type

        def __getattr__(self, attr):
            return getattr(self.__java_compound_type, attr)

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
            initializers = \
                lpad("\n", "\n".join(indent(' ' * 4,
                    (field.java_null_initializer()
                     for field in self.fields)
                )))
            return """\
public Builder() {%(initializers)s
}""" % locals()

        def _java_constructors(self):
            return [
                self._java_constructor_default(),
                self._java_constructor_copy(),
            ]

        def _java_member_declarations(self):
            return [field.java_member_declaration(assign_value=False, boxed=True, final=False)
                    for field in self.fields]

        def _java_method_build(self):
            fields = []
            qname = self.java_qname()
            for field in self.fields:
                field_name = field.java_name()
                fields.append("""com.google.common.base.Preconditions.checkNotNull(%(field_name)s, "%(qname)s: missing %(field_name)s")""" % locals())
            fields = ', '.join(fields)
            name = self.java_name()
            return {'build': """\
public %(name)s build() {
    return _build(%(fields)s);
}""" % locals()}

        def _java_method__build(self):
            all_field_names = \
                ', '.join(field.java_name() for field in self.fields)
            field_parameters = \
                ', '.join(field.java_parameter(final=True) for field in self.fields)
            name = self.java_name()
            return {'_build': """\
protected %(name)s _build(%(field_parameters)s) {
    return new %(name)s(%(all_field_names)s);
}""" % locals()}

        def _java_method_read_as(self):
            return {'readAs': '''\
public Builder readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
    return readAs(iprot, type, com.google.common.base.Optional.<UnknownFieldCallback> absent());
}

public Builder readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
    switch (type) {
    case LIST:
        return readAsList(iprot);
    case STRUCT:
        return readAsStruct(iprot, unknownFieldCallback);
    default:
        throw new IllegalArgumentException("cannot read as " + type);
    }
}'''}

        def _java_method_read_as_list(self):
            body = indent(' ' * 4, self.__java_compound_type._java_method_read_as_list_body())
            return {'readAsList': """\
public Builder readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
%(body)s
    return this;
}""" % locals()}

        def _java_method_read_as_struct(self):
            body = indent(' ' * 4, self.__java_compound_type._java_method_read_as_struct_body())
            return {'readAsStruct': """\
public Builder readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
    return readAsStruct(iprot, com.google.common.base.Optional.<UnknownFieldCallback> absent());
}

public Builder readAsStruct(final org.thryft.protocol.InputProtocol iprot, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
%(body)s
    return this;
}""" % locals()}

        def _java_method_getters(self):
            return dict((field.java_getter_name(), field.java_getter())
                        for field in self.fields)

        def _java_method_set(self):
            if len(self.fields) == 0:
                return {'set': """\
public Builder set(final String fieldThriftName, @javax.annotation.Nullable final java.lang.Object value) {
    throw new IllegalArgumentException();
}

public Builder set(final org.thryft.Struct.FieldMetadata fieldMetadata, @javax.annotation.Nullable final java.lang.Object value) {
    throw new IllegalArgumentException();
}"""}

            cases = []
            suppress_warnings = []
            for field in self.fields:
                cases.extend(field.java_set_case())
                for suppress_warning in field.java_set_suppress_warnings():
                    if not suppress_warning in suppress_warnings:
                        suppress_warnings.append(suppress_warning)
            suppress_warnings = pad("@SuppressWarnings({", ', '.join('"%s"' % suppress_warning
                                                                     for suppress_warning in suppress_warnings), "})\n")
            cases = lpad("\n", "\n".join(indent(' ' * 4, cases)))
            return {'set': """\
public Builder set(final String fieldThriftName, @javax.annotation.Nullable final java.lang.Object value) {
    return set(FieldMetadata.valueOfThriftName(fieldThriftName), value);
}

public Builder set(final org.thryft.Struct.FieldMetadata fieldMetadata, @javax.annotation.Nullable final java.lang.Object value) {
    if (!(fieldMetadata instanceof FieldMetadata)) {
        throw new IllegalArgumentException();
    }
    return set((FieldMetadata)fieldMetadata, value);
}

%(suppress_warnings)spublic Builder set(final FieldMetadata fieldMetadata, @javax.annotation.Nullable final java.lang.Object value) {
    com.google.common.base.Preconditions.checkNotNull(fieldMetadata);

    switch (fieldMetadata) {%(cases)s
    default:
        throw new IllegalStateException();
    }
}""" % locals()}

        def _java_method_set_if_present(self):
            sets = []
            for field in self.fields:
                sets.append(field.java_set_if_present())
            sets = "\n".join(indent(' ' * 4, sets))
            name = self.java_name()
            return {'setIfPresent': """\
public Builder setIfPresent(final %(name)s other) {
    com.google.common.base.Preconditions.checkNotNull(other);

%(sets)s

    return this;
}""" % locals()}

        def _java_method_setters(self):
            setters = {}
            for field in self.fields:
                for field_setter_i, field_setter in enumerate(field.java_setters(return_type_name='Builder')):
                    setters[field.java_setter_name() + str(field_setter_i)] = field_setter
            return setters

        def _java_method_unset(self):
            if len(self.fields) == 0:
                return {'unset': """\
public Builder unset(final String fieldThriftName) {
    throw new IllegalArgumentException();
}

public Builder unset(final org.thryft.Struct.FieldMetadata fieldMetadata) {
    throw new IllegalArgumentException();
}"""}

            cases = []
            for field in self.fields:
                field_name_upper = field.name.upper()
                field_name_upper_camelized = upper_camelize(field.name)
                cases.append('case %(field_name_upper)s: return unset%(field_name_upper_camelized)s();' % locals())
            cases = lpad("\n", "\n".join(indent(' ' * 4, cases)))
            return {'unset': """\
public Builder unset(final String fieldThriftName) {
    return unset(FieldMetadata.valueOfThriftName(fieldThriftName));
}

public Builder unset(final org.thryft.Struct.FieldMetadata fieldMetadata) {
    if (!(fieldMetadata instanceof FieldMetadata)) {
        throw new IllegalArgumentException();
    }
    return unset((FieldMetadata)fieldMetadata);
}

public Builder unset(final FieldMetadata fieldMetadata) {
    com.google.common.base.Preconditions.checkNotNull(fieldMetadata);

    switch (fieldMetadata) {%(cases)s
    default:
        throw new IllegalStateException();
    }
}""" % locals()}

        def _java_method_unsetters(self):
            unsetters = {}
            for field in self.fields:
                unsetters[field.java_unsetter_name()] = field.java_unsetter(return_type_name='Builder')
            return unsetters

        def _java_methods(self):
            methods = {}
            methods.update(self._java_method_build())
            methods.update(self._java_method__build())
            methods.update(self._java_method_getters())
            methods.update(self._java_method_read_as())
            methods.update(self._java_method_read_as_list())
            methods.update(self._java_method_read_as_struct())
            methods.update(self._java_method_set())
            methods.update(self._java_method_set_if_present())
            methods.update(self._java_method_setters())
            methods.update(self._java_method_unset())
            methods.update(self._java_method_unsetters())
            return methods

        def java_repr(self):
            name = self.java_name()
            methods = self._java_methods()
            sections = []
            sections.append("\n\n".join(indent(' ' * 4,
                self._java_constructors() + [methods[key] for key in sorted(methods.iterkeys())]
            )))
            sections.append("\n".join(indent(' ' * 4, self._java_member_declarations())))
            sections = lpad("\n", "\n\n".join(section for section in sections if len(section) > 0))
            return """\
public static class Builder {%(sections)s
}""" % locals()

    class _JavaFactory(object):
        def __init__(self, java_compound_type):
            object.__init__(self)
            self.__java_compound_type = java_compound_type

        def java_repr(self):
            compound_type_name = self.__java_compound_type.java_name()
            return """\
public final static class Factory implements org.thryft.CompoundType.Factory<%(compound_type_name)s> {
    @Override
    public %(compound_type_name)s readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
        return %(compound_type_name)s.readAs(iprot, type);
    }

    @Override
    public %(compound_type_name)s readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type,
            final com.google.common.base.Optional<org.thryft.CompoundType.UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
        return %(compound_type_name)s.readAs(iprot, type, unknownFieldCallback);
    }

    @Override
    public %(compound_type_name)s readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        return %(compound_type_name)s.readAsList(iprot);
    }

    @Override
    public %(compound_type_name)s readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
        return %(compound_type_name)s.readAsStruct(iprot);
    }

    @Override
    public %(compound_type_name)s readAsStruct(final org.thryft.protocol.InputProtocol iprot,
            final com.google.common.base.Optional<org.thryft.CompoundType.UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
        return %(compound_type_name)s.readAsStruct(iprot, unknownFieldCallback);
    }
}""" % locals()

    class _JavaFieldMetadataEnum(object):
        def __init__(self, java_compound_type):
            object.__init__(self)
            assert len(java_compound_type.fields) > 0
            self.__java_compound_type = java_compound_type

        def java_repr(self):
            enumerators = []
            java_name_cases = []
            thrift_name_cases = []
            for field in self.__java_compound_type.fields:
                enumerators.append(field.java_field_metadata_enumerator_declaration())
                java_name_cases.append(field.java_field_metadata_value_of_java_name_case())
                thrift_name_cases.append(field.java_field_metadata_value_of_thrift_name_case())
            class_suppress_warnings = '' if 'serial' in self.__java_compound_type._suppress_warnings else "@SuppressWarnings(\"serial\")\n"
            enumerators = pad("\n", indent(' ' * 4, ",\n".join(enumerators)), ";\n")
            java_name_cases = lpad("\n", indent(' ' * 8, "\n".join(java_name_cases)))
            thrift_name_cases = lpad("\n", indent(' ' * 8, "\n".join(thrift_name_cases)))
            return """\
%(class_suppress_warnings)spublic enum FieldMetadata implements org.thryft.CompoundType.FieldMetadata {%(enumerators)s
    @Override
    public String getJavaName() {
        return javaName;
    }

    @Override
    public com.google.common.reflect.TypeToken<?> getJavaType() {
        return javaType;
    }

    @Override
    public int getThriftId() {
        return thriftId;
    }

    @Override
    public String getThriftProtocolKey() {
        return thriftProtocolKey;
    }

    @Override
    public org.thryft.protocol.Type getThriftProtocolType() {
        return thriftProtocolType;
    }

    @Override
    public String getThriftName() {
        return thriftName;
    }

    @Override
    public boolean hasThriftId() {
        return thriftId != org.thryft.protocol.FieldBegin.ABSENT_ID;
    }

    @Override
    public boolean isRequired()  {
        return required;
    }

    public static FieldMetadata valueOfJavaName(final String javaName) {
        switch (javaName) {%(java_name_cases)s
        default:
            throw new IllegalArgumentException(javaName);
        }
    }

    public static FieldMetadata valueOfThriftName(final String thriftName) {
        switch (thriftName) {%(thrift_name_cases)s
        default:
            throw new IllegalArgumentException(thriftName);
        }
    }

    private FieldMetadata(final String javaName, final com.google.common.reflect.TypeToken<?> javaType, final boolean required, final int thriftId, final String thriftName, final org.thryft.protocol.Type thriftProtocolType) {
        this.javaName = javaName;
        this.javaType = javaType;
        this.required = required;
        this.thriftId = thriftId;
        this.thriftName = thriftName;
        if (thriftId != org.thryft.protocol.FieldBegin.ABSENT_ID) {
            this.thriftProtocolKey = Integer.toString(thriftId) + ":" + thriftName;
        } else {
            this.thriftProtocolKey = thriftName;
        }
        this.thriftProtocolType = thriftProtocolType;
    }

    private final String javaName;
    private final com.google.common.reflect.TypeToken<?> javaType;
    private final boolean required;
    private final int thriftId;
    private final String thriftName;
    private final String thriftProtocolKey;
    private final org.thryft.protocol.Type thriftProtocolType;
}""" % locals()

    def __init__(
        self,
        java_class_modifiers=None,
        java_suppress_warnings=None,
        message_type=None,
        **kwds
    ):
        if java_class_modifiers is None:
            java_class_modifiers = ('public',)
        elif isinstance(java_class_modifiers, str):
            java_class_modifiers = tuple(java_class_modifiers.split())
        else:
            java_class_modifiers = tuple(java_class_modifiers)
        self.__class_modifiers = java_class_modifiers

        self.__message_type = message_type

        if java_suppress_warnings is None:
            self._suppress_warnings = tuple()
        else:
            self._suppress_warnings = tuple(java_suppress_warnings)

    def _java_constructor_default(self):
        name = self.java_name()

        if len(self.fields) == 0:
            return """\
public %(name)s() {
}""" % locals()

        for field in self.fields:
            if field.required and field.value is None:
                return None  # Will be covered by total constructor

        initializers = \
            lpad("\n", "\n".join(indent(' ' * 4,
                (field.java_default_initializer()
                 for field in self.fields)
            )))
        return """\
/**
 * Default constructor
 */
public %(name)s() {%(initializers)s
}""" % locals()

    def _java_constructor_copy(self):
        name = self.java_name()
        this_call = \
            indent(' ' * 4,
                pad("\nthis(",
                    ', '.join('other.' + field.java_getter_name() + '()'
                               for field in self.fields),
                ");\n")
            )
        return """\
/**
 * Copy constructor
 */
public %(name)s(final %(name)s other) {%(this_call)s
}""" % locals()

    def _java_constructor_protected(self):
        if len(self.fields) == 0:
            return None # Will be covered by default constructor
        name = self.java_name()
        initializers = []
        parameters = []
        for field in self.fields:
            field_name = field.java_name()
            initializers.append("this.%(field_name)s = %(field_name)s;" % locals())
            parameters.append(field.java_parameter(final=True))
        initializers = lpad("\n", "\n".join(indent(' ' * 4, initializers)))
        parameters = ", ".join(parameters)
        return """\
protected %(name)s(%(parameters)s) {%(initializers)s
}""" % locals()

    def _java_constructors(self):
        constructors = []
        for constructor in (
            self._java_constructor_default(),
            self._java_constructor_copy(),
            self._java_constructor_protected(),
        ):
            if constructor is not None:
                constructors.append(constructor)
        return constructors

    def java_default_value(self):
        return 'null'

    def java_is_reference(self):
        return True

    def _java_extends(self):
        return None

    def _java_field_metadata_enum(self):
        if len(self.fields) == 0:
            return None
        return self._JavaFieldMetadataEnum(self).java_repr()

    def _java_implements(self):
#         name = self.java_name()
#         implements = ["java.lang.Comparable<%(name)s>" % locals()
        implements = []
        for annotation in self.annotations:
            if annotation.name == 'java_implements':
                implements.append(annotation.value)
        return implements

    def _java_member_declarations(self):
        mutable = self._parent_generator().mutable_compound_types
        return [field.java_member_declaration(final=not mutable, assign_value=mutable)
                for field in self.fields]

    def _java_method_builder(self):
        name = self.java_name()
        return {'builder': """\
public static Builder builder() {
    return new Builder();
}

public static Builder builder(final %(name)s other) {
    return new Builder(other);
}

public static Builder builder(final com.google.common.base.Optional<%(name)s> other) {
    return other.isPresent() ? new Builder(other.get()) : new Builder();
}""" % locals()}

#     def _java_method_compare_to(self, name=None):
#         if name is None:
#             name = self.java_name()
#         field_compare_tos = []
#         for field in self.fields:
#             field_compare_to = field.java_compare_to()
#             if field_compare_to is not None:
#                 field_compare_tos.append(field_compare_to)
#         field_compare_tos = \
#             pad("\n\n    int result;\n", "\n\n".join(indent(' ' * 4,
#                 field_compare_tos
#             )), "\n")
#         return {'compareTo': """\
# @Override
# public int compareTo(final %(name)s other) {
#     if (other == null) {
#         throw new NullPointerException();
#     }%(field_compare_tos)s
#     return 0;
# }""" % locals()}

    def _java_method_create(self):
        overloads = []
        for overload in (
            self._java_method_create_default(),
            self._java_method_create_required(),
            self._java_method_create_total_boxed(),
            self._java_method_create_total_nullable(),
            self._java_method_create_total_optional(),
        ):
            if overload is not None:
                overloads.append(overload)
        return {'create': "\n\n".join(overloads)}

    def _java_method_create_default(self):
        name = self.java_name()
        if self._java_constructor_default() is not None:
            return """\
public static %(name)s create() {
    return new %(name)s();
}""" % locals()

    def _java_method_create_required(self):
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor
        else:
            optional_field_count = 0
            required_field_count = 0
            for field in self.fields:
                if field.required and field.value is None:
                    required_field_count += 1
                else:
                    optional_field_count += 1
            if optional_field_count == len(self.fields):
                return None  # Will be covered by total constructor
            elif required_field_count == len(self.fields):
                return None  # Will be covered by total constructor

        name = self.java_name()
        parameters = []
        parameter_delegation = []
        for field in self.fields:
            if field.required and field.value is None:
                parameters.append(field.java_parameter(final=True))
                parameter_delegation.append(field.java_preconditions_expression())
            else:
                parameter_delegation.append(field.java_default_value())
        parameters = ", ".join(parameters)
        parameter_delegation = ', '.join(parameter_delegation)
        return """\
/**
 * Required factory method
 */
public static %(name)s create(%(parameters)s) {
    return new %(name)s(%(parameter_delegation)s);
}""" % locals()

    def _java_method_create_total_boxed(self):
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor

        for field in self.fields:
            if field.required and \
               (field.type.java_boxed_qname() != \
                field.type.java_qname()):

                name = self.java_name()
                parameters = ', '.join(field.java_parameter(boxed=True)
                                        for field in self.fields)
                parameter_delegation = ', '.join(field.java_preconditions_expression(boxed=True) for field in self.fields)
                return """\
/**
 * Total boxed factory method
 */
public static %(name)s create(%(parameters)s) {
    return new %(name)s(%(parameter_delegation)s);
}""" % locals()
            # else will be covered by total_optional constructor

    def _java_method_create_total_nullable(self):
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor
        has_optional_field = False
        for field in self.fields:
            if not field.required:
                has_optional_field = True
                break
        if not has_optional_field:
            return None  # Will be covered by total_optional constructor

        name = self.java_name()
        parameters = \
            ', '.join(field.java_parameter(final=True, nullable=True)
                      for field in self.fields)
        parameter_delegation = ', '.join(field.java_preconditions_expression(nullable=True) for field in self.fields)
        return """\
/**
 * Total Nullable factory method
 */
public static %(name)s create(%(parameters)s) {
    return new %(name)s(%(parameter_delegation)s);
}""" % locals()

    def _java_method_create_total_optional(self):
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor

        name = self.java_name()
        parameters = ', '.join(field.java_parameter(final=True, nullable=False)
                                for field in self.fields)
        parameter_delegation = ', '.join(field.java_preconditions_expression(nullable=False) for field in self.fields)
        return """\
/**
 * Optional factory method
 */
public static %(name)s create(%(parameters)s) {
    return new %(name)s(%(parameter_delegation)s);
}""" % locals()

    def _java_method_equals(self, name=None, nullable=False):
        if name is None:
            name = self.java_name()

        field_equal_tests = []
        for field in self.fields:
            field_equal_tests.append(
                field.java_equals(field.java_getter_name() + '()',
                                  'other.' + field.java_getter_name() + '()', nullable=nullable)
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
public boolean equals(final java.lang.Object otherObject) {
%(struct_equal_tests)s

    %(field_equal_tests)s;
}""" % locals()}

    def _java_method_get(self):
        if len(self.fields) == 0:
            return {'get': """\
@Override
public java.lang.Object get(final String fieldThriftName) {
    throw new IllegalArgumentException(fieldThriftName);
}

@Override
public java.lang.Object get(final org.thryft.CompoundType.FieldMetadata fieldMetadata) {
    throw new IllegalArgumentException();
}"""}

        field_cases = []
        for field in self.fields:
            field_name_upper = field.name.upper()
            field_getter_name = field.java_getter_name()
            field_cases.append('case %(field_name_upper)s: return %(field_getter_name)s();' % locals())
        field_cases = lpad("\n", indent(' ' * 4, "\n".join(field_cases)))
        return {'get': """\
@Override
public java.lang.Object get(final String fieldThriftName) {
    return get(FieldMetadata.valueOfThriftName(fieldThriftName));
}

@Override
public java.lang.Object get(final org.thryft.CompoundType.FieldMetadata fieldMetadata) {
    if (!(fieldMetadata instanceof FieldMetadata)) {
        throw new IllegalArgumentException();
    }
    return get((FieldMetadata)fieldMetadata);
}

public java.lang.Object get(final FieldMetadata fieldMetadata) {
    switch (fieldMetadata) {%(field_cases)s
    default:
        throw new IllegalStateException();
    }
}""" % locals()}

    def _java_method_getters(self):
        return dict((field.java_getter_name(), field.java_getter())
                    for field in self.fields)

    def _java_method_hash_code(self):
        statements = ['int hashCode = 17;']
        statements.extend(field.java_hash_code_update() for field in self.fields)
        statements = \
            "\n".join(indent(' ' * 4, statements))
        return {'hashCode': """\
@Override
public int hashCode() {
%(statements)s
    return hashCode;
}""" % locals()}

    def _java_method_read_as(self):
        name = self.java_name()
        return {'readAs': """\
public static %(name)s readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type) throws org.thryft.protocol.InputProtocolException {
    return readAs(iprot, type, com.google.common.base.Optional.<UnknownFieldCallback> absent());
}

public static %(name)s readAs(final org.thryft.protocol.InputProtocol iprot, final org.thryft.protocol.Type type, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {
    switch (type) {
    case LIST:
        return readAsList(iprot);
    case STRUCT:
        return readAsStruct(iprot, unknownFieldCallback);
    default:
        throw new IllegalArgumentException("cannot read as " + type);
    }
}""" % locals()}

    def _java_method_read_as_list(self):
        body = indent(' ' * 4, self._java_method_read_as_list_body())
        field_declarations = \
            pad("\n", indent(' ' * 4, "\n".join(
                field.java_local_declaration(final=False)
                for field in self.fields
            )), "\n")
        field_names = ', '.join(field.java_name() for field in self.fields)
        name = self.java_name()
        return {'readAsList': """\
public static %(name)s readAsList(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {%(field_declarations)s
%(body)s
    try {
        return new %(name)s(%(field_names)s);
    } catch (final IllegalArgumentException | NullPointerException e) {
        throw new org.thryft.protocol.InputProtocolException(e);
    }
}""" % locals()}

    def _java_method_read_as_list_body(self):
        field_protocol_positional_initializers = []
        read_list = ''
        for field_i, field in enumerate(self.fields):
            field_protocol_initializer = field.java_protocol_initializer()
            if not field.required:
                field_protocol_initializer = indent(' ' * 4, field_protocol_initializer)
                field_protocol_initializer = """\
if (__list.getSize() > %(field_i)u) {
%(field_protocol_initializer)s
}""" % locals()
                read_list = "final org.thryft.protocol.ListBegin __list = "
            field_protocol_positional_initializers.append(field_protocol_initializer)
        field_protocol_positional_initializers = \
            lpad("\n", "\n".join(field_protocol_positional_initializers))
        return """\
%(read_list)siprot.readListBegin();%(field_protocol_positional_initializers)s
iprot.readListEnd();""" % locals()

    def _java_method_read_as_struct(self):
        body = indent(' ' * 4, self._java_method_read_as_struct_body())
        field_declarations = \
            pad("\n", indent(' ' * 4, "\n".join(
                field.java_local_declaration(final=False)
                for field in self.fields
            )), "\n")
        field_names = ', '.join(field.java_name() for field in self.fields)
        name = self.java_name()
        return {'readAsStruct': """\
public static %(name)s readAsStruct(final org.thryft.protocol.InputProtocol iprot) throws org.thryft.protocol.InputProtocolException {
    return readAsStruct(iprot, com.google.common.base.Optional.<UnknownFieldCallback> absent());
}

public static %(name)s readAsStruct(final org.thryft.protocol.InputProtocol iprot, final com.google.common.base.Optional<UnknownFieldCallback> unknownFieldCallback) throws org.thryft.protocol.InputProtocolException {%(field_declarations)s
%(body)s
    try {
        return new %(name)s(%(field_names)s);
    } catch (final IllegalArgumentException | NullPointerException e) {
        throw new org.thryft.protocol.InputProtocolException(e);
    }
}""" % locals()}

    def _java_method_read_as_struct_body(self):
        field_protocol_named_initializers = []
        for field in self.fields:
            field_name = field.name
            field_named_protocol_initializer = field.java_protocol_initializer()
            if field.id is not None:
                field_id = field.id
                field_named_protocol_initializer = indent(' ' * 4, field_named_protocol_initializer)
                field_named_protocol_initializer = """\
if (!ifield.hasId() || ifield.getId() == %(field_id)d) {
%(field_named_protocol_initializer)s
}""" % locals()
            field_named_protocol_initializer = indent(' ' * 4, field_named_protocol_initializer)
            field_protocol_named_initializers.append("""\
case "%(field_name)s": {
%(field_named_protocol_initializer)s
    break;
}""" % locals())
        field_protocol_named_initializers = \
            lpad("\n", indent(' ' * 4,  "\n".join(
                field_protocol_named_initializers
            )))
        return """\
iprot.readStructBegin();
while (true) {
    final org.thryft.protocol.FieldBegin ifield = iprot.readFieldBegin();
    if (ifield.getType() == org.thryft.protocol.Type.STOP) {
        break;
    }
    switch (ifield.getName()) {%(field_protocol_named_initializers)s
    default:
        if (unknownFieldCallback.isPresent()) {
            unknownFieldCallback.get().apply(ifield);
        }
        break;
    }
    iprot.readFieldEnd();
}
iprot.readStructEnd();""" % locals()

    def _java_method_replacers(self):
        methods = {}
        compound_type_name = self.java_name()
        all_field_names = [field.java_name() for field in self.fields]
        for field_i, field in enumerate(self.fields):
            field_name = field.java_name()
            field_parameter = field.java_parameter(final=True)
            all_field_names = []
            for other_field_i, other_field in enumerate(self.fields):
                if field_i == other_field_i:
                    all_field_names.append(field.java_name())
                else:
                    all_field_names.append('this.' + other_field.java_name())
            all_field_names = ', '.join(all_field_names)
            method_name = 'replace' + upper_camelize(field.name)
            methods[method_name] = """\
public %(compound_type_name)s %(method_name)s(%(field_parameter)s) {
    return new %(compound_type_name)s(%(all_field_names)s);
}""" % locals()
            if not field.required:
                field_parameter = 'final ' + field.type.java_qname() + ' ' + field.java_name()
                methods[method_name + 'Ex'] = """\
public %(compound_type_name)s %(method_name)s(%(field_parameter)s) {
    return %(method_name)s(com.google.common.base.Optional.fromNullable(%(field_name)s));
}""" % locals()

        return methods

    def _java_method_setters(self):
        if not self._parent_generator().mutable_compound_types:
            return {}
        setters = {}
        for field in self.fields:
            for field_setter_i, field_setter in enumerate(field.java_setters()):
                setters[field.java_setter_name() + str(field_setter_i)] = field_setter
        return setters

    def _java_method_to_string(self):
        add_statements = ''.join(field.java_to_string_helper_add()
                                 for field in self.fields)
        return {'toString': """\
@Override
public String toString() {
    return com.google.common.base.MoreObjects.toStringHelper(this).omitNullValues()%(add_statements)s.toString();
}""" % locals()}

    def _java_method_write_as_list(self):
        field_count = len(self.fields)
        field_value_write_protocols = \
            pad("\n\n", "\n\n".join(indent(' ' * 4,
                (field.java_write_protocol(depth=0, write_field=False)
                 for field in self.fields)
            )), "\n")
        return {'writeAsList': """\
@Override
public void writeAsList(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
    oprot.writeListBegin(org.thryft.protocol.Type.VOID_, %(field_count)u);%(field_value_write_protocols)s
    oprot.writeListEnd();
}""" % locals()}

    def _java_method_write_as_message(self):
        if self.__message_type is None:
            return {}

        field_write_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                (field.java_write_protocol(depth=0, write_field=True)
                 for field in self.fields)
            )))
        message_type = self.__message_type
        qname = self.java_qname()
        return {'writeAsMessage': """\
public void writeAsMessage(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
    oprot.writeMessageBegin(\"%(qname)s\", org.thryft.protocol.MessageType.%(message_type)s, null);%(field_write_protocols)s

    oprot.writeFieldStop();

    oprot.writeMessageEnd();
}""" % locals()}

    def _java_method_write_as_struct(self):
        field_write_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                (field.java_write_protocol(depth=0, write_field=True)
                 for field in self.fields)
            )))
        qname = self.java_qname()
        return {'writeAsStruct': """\
@Override
public void writeAsStruct(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {
    oprot.writeStructBegin("%(qname)s");
    writeFields(oprot);
    oprot.writeStructEnd();
}""" % locals()}

    def _java_method_write_fields(self):
        field_write_protocols = \
            pad("\n", "\n\n".join(indent(' ' * 4,
                (field.java_write_protocol(depth=0, write_field=True)
                 for field in self.fields)
            )), "\n")
        qname = self.java_qname()
        return {'writeFields': """\
@Override
public void writeFields(final org.thryft.protocol.OutputProtocol oprot) throws org.thryft.protocol.OutputProtocolException {%(field_write_protocols)s
    oprot.writeFieldStop();
}""" % locals()}

    def _java_methods(self):
        methods = {}
        methods.update(self._java_method_builder())
#         methods.update(self._java_method_compare_to())
        methods.update(self._java_method_create())
        methods.update(self._java_method_equals())
        methods.update(self._java_method_get())
        methods.update(self._java_method_getters())
        methods.update(self._java_method_hash_code())
        methods.update(self._java_method_read_as())
        methods.update(self._java_method_read_as_list())
        methods.update(self._java_method_read_as_struct())
        methods.update(self._java_method_replacers())
        methods.update(self._java_method_setters())
        methods.update(self._java_method_to_string())
        methods.update(self._java_method_write_as_list())
        methods.update(self._java_method_write_as_message())
        methods.update(self._java_method_write_as_struct())
        methods.update(self._java_method_write_fields())
        return methods

    def java_precondition_name(self):
        return 'CompoundType'

    def java_qname(self, **kwds):
        return _JavaNamedConstruct.java_qname(self, name=self.name, **kwds)

    def java_read_protocol(self):
        qname = self.java_qname()
        return "%(qname)s.readAsStruct(iprot)" % locals()

    def java_repr(self):
        class_annotations = []
        if len(self._suppress_warnings) > 0:
            class_annotations.append(
                "@SuppressWarnings({%s})" % \
                    ', '.join('"' + warning + '"'
                               for warning in sorted(self._suppress_warnings)))
        class_annotations = rpad("\n".join(class_annotations), "\n")
        class_modifiers = rpad(' '.join(self.__class_modifiers), ' ')
        javadoc = self.java_doc()
        name = self.java_name()
        extends = lpad(' extends ', self._java_extends())
        implements = lpad(' implements ', ', '.join(self._java_implements()))
        methods = self._java_methods()
        sections = []
        sections.append(indent(' ' * 4, self._JavaBuilder(self).java_repr()))
        sections.append(indent(' ' * 4, self._JavaFactory(self).java_repr()))
        field_metadata_enum = self._java_field_metadata_enum()
        if field_metadata_enum is not None:
            sections.append(indent(' ' * 4, field_metadata_enum))
        sections.append("\n\n".join(indent(' ' * 4,
            self._java_constructors() + \
            [methods[key] for key in sorted(methods.iterkeys())])))
        sections.append("\n\n".join(indent(' ' * 4, self._java_member_declarations())))
        sections = lpad("\n", "\n\n".join(section for section in sections if len(section) > 0))
        return """\
%(javadoc)s%(class_annotations)s%(class_modifiers)sclass %(name)s%(extends)s%(implements)s {%(sections)s
}""" % locals()

    def java_to_string(self, value):
        return "%(value)s.toString()" % locals()

    def java_write_protocol(self, value, depth=0):
        return "%(value)s.writeAsStruct(oprot);" % locals()
