import logging

from thryft.generators.java.java_generator import JavaGenerator
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from yutil import indent, lpad


class BeanJavaGenerator(JavaGenerator):
    def __init__(self, **kwds):
        JavaGenerator.__init__(self, mutable_compound_types=True, **kwds)

    class Document(JavaGenerator.Document):  # @UndefinedVariable
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

    class Field(JavaGenerator.Field):  # @UndefinedVariable
        def java_compare_to(self):
            name = self.java_name()
            this_value = 'this.' + name
            other_value = 'other.' + name
            type_compare_to = self.type.java_compare_to(this_value, other_value, already_boxed=not self.required)
            if type_compare_to is None:
                return None
            compare_to = """\
result = %(type_compare_to)s;
if (result != 0) {
    return result;
}""" % locals()
            if not self.required:
                compare_to = indent(' ' * 8, compare_to)
                compare_to = """\
if (this.%(name)s != null) {
    if (other.%(name)s != null) {
%(compare_to)s
    } else {
        return 1;
    }
} else if (other.%(name)s != null) {
    return -1;
}""" % locals()
            return compare_to

        def java_default_value(self):
            if self.value is not None:
                return self.java_value()
            elif not self.required:
                return 'null'
            else:
                return self.type.java_default_value()

        def java_getter(self, final=True):
            final = final and 'final ' or ''
            getter_name = self.java_getter_name()
            javadoc = self.java_doc()
            name = self.java_name()
            type_name = self._java_type_name(nullable=True)
            return """\
%(javadoc)spublic %(final)s%(type_name)s %(getter_name)s() {
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

        def java_member_declaration(self, **kwds):
            javadoc = self.java_doc()
            lhs = self.java_parameter(nullable=True)
            return "%(javadoc)sprivate %(lhs)s;" % locals()

        def java_setters(self, return_type_name='void'):
            name = self.java_name()
            setter_name = self.java_setter_name()
            type_name = self._java_type_name(nullable=True)
            return ["""\
public void %(setter_name)s(final %(type_name)s %(name)s) {
    this.%(name)s = %(name)s;
}""" % locals()]

        def java_to_string_helper_add(self):
            return """.add(\"%s\", %s)""" % (self.name, self.java_getter_name() + '()')

    class StructType(JavaGenerator.StructType):  # @UndefinedVariable
        def _java_constructor_default(self):
            name = self.java_name()

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

        def _java_constructors(self):
            constructors = []
            for constructor in (
                self._java_constructor_default(),
#                 self._java_constructor_total_nullable()
            ):
                if constructor is not None:
                    constructors.append(constructor)
            return constructors

#         def _java_constructor_total_nullable(self):
#             if len(self.fields) == 0:
#                 return None  # Will be covered by default constructor
#             initializers = \
#                 "\n".join(indent(' ' * 4,
#                     (field.java_initializer(nullable=True)
#                      for field in self.fields)
#                 ))
#             name = self.java_name()
#             parameters = \
#                 ', '.join(field.java_parameter(final=True, nullable=True)
#                           for field in self.fields)
#             return """\
# public %(name)s(%(parameters)s) {
# %(initializers)s
# }""" % locals()

        def _java_methods(self):
            methods = {}
            methods.update(self._java_method_compare_to())
            methods.update(self._java_method_equals())
            methods.update(self._java_method_getters())
            methods.update(self._java_method_hash_code())
            methods.update(self._java_method_setters())
            methods.update(self._java_method_to_string())
            return methods

        def java_name(self, **kwds):
            return _JavaNamedConstruct.java_name(self, **kwds) + 'Bean'

        def java_qname(self, **kwds):
            return _JavaNamedConstruct.java_qname(self, java_namespace_scope='bean_java', **kwds)

        def java_repr(self):
            javadoc = self.java_doc()
            name = self.java_name()
            methods = self._java_methods()
            sections = []
            sections.append("\n\n".join(indent(' ' * 4,
                self._java_constructors() + \
                [methods[key] for key in sorted(methods.iterkeys())])))
            sections.append("\n\n".join(indent(' ' * 4, self._java_member_declarations())))
            sections = lpad("\n", "\n\n".join(section for section in sections if len(section) > 0))
            return """\
%(javadoc)spublic class %(name)s implements Comparable<%(name)s> {%(sections)s
}""" % locals()
