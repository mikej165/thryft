from thryft.target.compound_types.struct import Struct
from yutil import indent, lpad


class JavaStruct(Struct):
    def java_builder(self):
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

    def java_constructors(self):
        constructors = []
        for constructor in (
            self._java_required_constructor(),
            self._java_total_constructor()
        ):
            if constructor is not None:
                constructors.append(constructor)
        return constructors

    def java_declarations(self):
        return [field.java_declaration(final=True) for field in self.fields]

    def java_is_reference(self):
        return True

    def java_getters(self):
        return [field.java_getter() for field in self.fields]

    def java_name(self, boxed=False):
        qname = self.qname
        if qname == 'date.Date' or qname == 'date_time.DateTime':
            return 'org.joda.time.DateTime'
        elif qname == 'decimal.Decimal':
            return 'java.math.BigDecimal'
        else:
            return self.name

    def _java_required_constructor(self):
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

    def _java_total_constructor(self):
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

    def __repr__(self):
        name = self.name

        sections = []
        sections.append(indent(' ' * 4, self.java_builder()))
        sections.append("\n\n".join(indent(' ' * 4, self.java_constructors())))
        sections.append("\n\n".join(indent(' ' * 4, self.java_getters())))
        sections.append("\n".join(indent(' ' * 4, self.java_declarations())))
        sections = lpad("\n", "\n\n".join(sections))

        return """\
public class %(name)s {%(sections)s
}""" % locals()
