import logging

from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from yutil import indent, lpad, class_qname


class BeanJavaGenerator(JavaGenerator):
    class _Type(object):
        def java_bean_boxed_name(self):
            return self.java_boxed_name()

        def java_bean_boxed_qname(self):
            return self.java_boxed_qname()

        def java_bean_name(self):
            return self.java_name()

        def java_bean_qname(self):
            return self.java_qname()

        def java_from_immutable(self, value):
            return value

    class _BaseType(_Type):
        def java_bean_boxed_name(self):
            return self.java_boxed_name()

        def java_bean_boxed_qname(self):
            return self.java_boxed_qname()

    class BinaryType(JavaGenerator.BinaryType, _BaseType):  # @UndefinedVariable
        pass

    class BoolType(JavaGenerator.BoolType, _BaseType):  # @UndefinedVariable
        pass

    class _SequenceType(_Type):
        def java_bean_qname(self):
            return self.__java_interface_qname()

        def java_from_immutable(self, value):
            mutable_implementation_qname = self._java_mutable_implementation_qname()
            element_from_immutable = self.element_type.java_from_immutable('element')
            if element_from_immutable == 'element':
                return "new %(mutable_implementation_qname)s(%(value)s)" % locals()
            element_type_name = self.element_type.java_boxed_qname()
            immutable_qname = \
                "com.google.common.collect.Immutable%s<%s>" % (
                       self._java_interface_simple_name(),
                       self.element_type.java_boxed_qname()
                   )
            interface_qname = self.__java_interface_qname()
            return """\
(new com.google.common.base.Function<%(immutable_qname)s, %(interface_qname)s>() {
    @Override
    public %(interface_qname)s apply(final %(immutable_qname)s other) {
        final %(interface_qname)s copy = new %(mutable_implementation_qname)s();
        for (final %(element_type_name)s element : other) {
            copy.add(%(element_from_immutable)s);
        }
        return copy;
    }
}).apply(%(value)s)""" % locals()

        def __java_interface_qname(self):
            return "java.util.%s<%s>" % (
                   self._java_interface_simple_name(),
                   self.element_type.java_bean_boxed_qname()
               )

        def _java_mutable_implementation_qname(self):
            raise NotImplementedError(class_qname(self))

        # Necessary for typedefs
        def java_qname(self):
            return self.__java_interface_qname()

    class Document(JavaGenerator.Document):  # @UndefinedVariable
        def _java_file_base_name(self):
            return self.definitions[0].java_bean_name()

        def java_package(self):
            try:
                return self.namespace_by_scope('bean_java').name
            except KeyError:
                return None

        def save(self, *args, **kwds):
            try:
                self.namespaces_by_scope['bean_java']
            except KeyError:
                logging.debug('no bean_java namespace set')
                return
            JavaGenerator.Document.save(self, *args, **kwds)  # @UndefinedVariable

    class DoubleType(JavaGenerator.DoubleType, _BaseType):  # @UndefinedVariable
        pass

    class EnumType(JavaGenerator.EnumType, _Type):  # @UndefinedVariable
        pass

    class Field(JavaGenerator.Field):  # @UndefinedVariable
#         def java_compare_to(self):
#             name = self.java_name()
#             this_value = 'this.' + name
#             other_value = 'other.' + name
#             type_compare_to = self.type.java_compare_to(this_value, other_value, already_boxed=not self.required)
#             if type_compare_to is None:
#                 return None
#             compare_to = """\
# result = %(type_compare_to)s;
# if (result != 0) {
#     return result;
# }""" % locals()
#             if not self.required:
#                 compare_to = indent(' ' * 8, compare_to)
#                 compare_to = """\
# if (this.%(name)s != null) {
#     if (other.%(name)s != null) {
# %(compare_to)s
#     } else {
#         return 1;
#     }
# } else if (other.%(name)s != null) {
#     return -1;
# }""" % locals()
#             return compare_to

        def java_default_value(self):
            if self.value is not None:
                return self.java_value()
            elif not self.required:
                return 'null'
            else:
                return self.type.java_default_value()

        def _java_field_metadata_java_type_qname(self):
            return self.type.java_bean_boxed_qname()

        def java_getter(self, **kwds):
            getter_name = self.java_getter_name()
            javadoc = self.java_doc()
            name = self.java_name()
            type_qname = self.type.java_bean_boxed_qname()
            return """\
%(javadoc)spublic %(type_qname)s %(getter_name)s() {
    return %(name)s;
}""" % locals()

        def java_hash_code_update(self):
            hashCode_update = \
                'hashCode = 31 * hashCode + ' + \
                    self.type.java_hash_code(self.java_getter_name() + '()', already_boxed=not self.required) + \
                ';'
            if not self.required:
                hashCode_update = """\
if (%s() != null) {
    %s
}""" % (self.java_getter_name(), hashCode_update)
            return hashCode_update

        def java_is_absent(self):
            assert not self.required
            return "%s() == null" % self.java_getter_name()

        def java_member_declaration(self, **kwds):
            javadoc = self.java_doc()
            name = self.java_name()
            type_qname = self.type.java_bean_boxed_qname()
            return "%(javadoc)sprivate %(type_qname)s %(name)s;" % locals()

        def java_setters(self, return_type_name='void'):
            name = self.java_name()
            setter_name = self.java_setter_name()
            type_qname = self.type.java_bean_boxed_qname()
            return ["""\
public void %(setter_name)s(final %(type_qname)s %(name)s) {
    this.%(name)s = %(name)s;
}""" % locals()]

        def java_to_string_helper_add(self):
            return """.add(\"%s\", %s)""" % (self.name, self.java_getter_name() + '()')

    class I32Type(JavaGenerator.I32Type, _BaseType):  # @UndefinedVariable
        pass

    class I64Type(JavaGenerator.I64Type, _BaseType):  # @UndefinedVariable
        pass

    class ListType(JavaGenerator.ListType, _SequenceType):  # @UndefinedVariable
        def _java_interface_simple_name(self):
            return 'List'

        def _java_mutable_implementation_qname(self):
            return "java.util.ArrayList<%s>" % \
                   self.element_type.java_bean_boxed_qname()

        # Necessary for typedefs
        def java_qname(self):
            return BeanJavaGenerator._SequenceType.java_qname(self)

    class MapType(JavaGenerator.MapType, _Type):  # @UndefinedVariable
        def java_bean_qname(self):
            return self.__java_interface_qname()

        def java_from_immutable(self, value):
            mutable_key_type_qname = self.key_type.java_bean_boxed_qname()
            mutable_value_type_qname = self.value_type.java_bean_boxed_qname()
            mutable_implementation_qname = "java.util.HashMap<%(mutable_key_type_qname)s, %(mutable_value_type_qname)s>" % locals()
            key_from_immutable = self.key_type.java_from_immutable('entry.getKey()')
            value_from_immutable = self.value_type.java_from_immutable('entry.getValue()')
            if key_from_immutable == 'entry.getKey()' and value_from_immutable == 'entry.getValue()':
                return "new %(mutable_implementation_qname)s(%(value)s)" % locals()
            immutable_key_type_qname = self.key_type.java_boxed_immutable_qname()
            immutable_value_type_qname = self.value_type.java_boxed_immutable_qname()
            immutable_implementation_qname = \
                "com.google.common.collect.ImmutableMap<%(immutable_key_type_qname)s, %(immutable_value_type_qname)s>" % locals()
            interface_qname = self.__java_interface_qname()
            return """\
(new com.google.common.base.Function<%(immutable_implementation_qname)s, %(interface_qname)s>() {
    @Override
    public %(interface_qname)s apply(final %(immutable_implementation_qname)s other) {
        final %(interface_qname)s copy = new %(mutable_implementation_qname)s();
        for (final java.util.Map.Entry<%(immutable_key_type_qname)s, %(immutable_value_type_qname)s> entry : other.entrySet()) {
            copy.put(%(key_from_immutable)s, %(value_from_immutable)s);
        }
        return copy;
    }
}).apply(%(value)s)""" % locals()

        def __java_interface_qname(self):
            return "java.util.Map<%s, %s>" % (
                   self.key_type.java_bean_boxed_qname(),
                   self.value_type.java_bean_boxed_qname(),
               )

        # Necessary for typedefs
        def java_qname(self):
            return self.__java_interface_qname()

    class SetType(JavaGenerator.SetType, _SequenceType):  # @UndefinedVariable
        def _java_interface_simple_name(self):
            return 'Set'

        def _java_mutable_implementation_qname(self):
            return "java.util.LinkedHashSet<%s>" % \
                   self.element_type.java_bean_boxed_qname()

        # Necessary for typedefs
        def java_qname(self):
            return BeanJavaGenerator._SequenceType.java_qname(self)

    class StringType(JavaGenerator.StringType, _BaseType):  # @UndefinedVariable
        pass

    class StructType(JavaGenerator.StructType, _Type):  # @UndefinedVariable
        def _java_constructor_default(self):
            name = self.java_bean_name()

            if len(self.fields) == 0:
                return """\
public %(name)s() {
}""" % locals()

            initializers = \
                lpad("\n", "\n".join(indent(' ' * 4,
                    (field.java_default_initializer()
                     for field in self.fields)
                )))
            return """\
public %(name)s() {%(initializers)s
}""" % locals()

        def _java_constructor_from_immutable(self):
            name = self.java_bean_name()
            immutable_name = JavaGenerator.StructType.java_qname(self)  # @UndefinedVariable
            initializers = []
            for field in self.fields:
                lhs = "this." + field.java_name()
                field_getter_call = 'other.' + field.java_getter_name() + '()'
                if field.required:
                    rhs = field.type.java_from_immutable(field_getter_call)
                else:
                    field_conversion = field.type.java_from_immutable("%(field_getter_call)s.get()" % locals())
                    rhs = "%(field_getter_call)s.isPresent() ? %(field_conversion)s : null" % locals()
                initializers.append("%(lhs)s = %(rhs)s;" % locals())
            initializers = lpad("\n", "\n".join(indent(' ' * 4, initializers)))
            return """\
public %(name)s(final %(immutable_name)s other) {%(initializers)s
}""" % locals()

        def _java_constructors(self):
            constructors = []
            for constructor in (
                self._java_constructor_default(),
                self._java_constructor_from_immutable(),
            ):
                if constructor is not None:
                    constructors.append(constructor)
            return constructors

        def java_from_immutable(self, value):
            qname = self.java_bean_qname()
            return "new %(qname)s(%(value)s)" % locals()

        def _java_methods(self):
            methods = {}
            methods.update(self._java_method_equals(name=self.java_bean_name(), nullable=True))
            methods.update(self._java_method_get())
            methods.update(self._java_method_getters())
            methods.update(self._java_method_hash_code())
            methods.update(self._java_method_is_empty())
            methods.update(self._java_method_setters())
            methods.update(self._java_method_to_string())
            return methods

        def java_bean_boxed_name(self):
            return self.java_bean_name()

        def java_bean_boxed_qname(self):
            return self.java_bean_qname()

        def java_bean_name(self):
            return _JavaNamedConstruct.java_name(self) + 'Bean'

        def java_bean_qname(self):
            return _JavaNamedConstruct.java_qname(self, java_namespace_scope='bean_java') + 'Bean'

        def java_repr(self):
            javadoc = self.java_doc()
            name = self.java_bean_name()
            methods = self._java_methods()
            sections = []
            sections.append(indent(' ' * 4, self._java_field_metadata_enum()))
            sections.append("\n\n".join(indent(' ' * 4,
                self._java_constructors() + \
                [methods[key] for key in sorted(methods.iterkeys())])))
            sections.append("\n\n".join(indent(' ' * 4, self._java_member_declarations())))
            sections = lpad("\n", "\n\n".join(section for section in sections if len(section) > 0))
            return """\
%(javadoc)spublic class %(name)s implements org.thryft.StructBean {%(sections)s
}""" % locals()

    def __init__(self, **kwds):
        JavaGenerator.__init__(self, mutable_compound_types=True, **kwds)
