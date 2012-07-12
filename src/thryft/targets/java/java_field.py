from thryft.target.field import Field
from yutil import lower_camelize, upper_camelize


class JavaField(Field):
    def java_declaration(self, final=False):
        if self.value is not None:
            return "private %s = %s;" % (repr(self), self.java_value())
        else:
            return "private %s;" % self.java_parameter(final=final)

    def java_default_initializer(self):
        name = self.java_name()
        if self.value is not None:
            value = self.java_value()
            return """\
this.%(name)s = %(value)s;""" % locals()
        else:
            return """\
this.%(name)s = null;""" % locals()

    def java_equals(self, this_value, other_value):
        if not self.required:
            return """\
((%(this_value)s == null && %(other_value)s == null) ||
(%(this_value)s != null && %(other_value)s != null &&
%(this_value)s.equals(%(other_value)s)))""" % locals()
        elif self.type.java_is_reference():
            return "%(this_value)s.equals(%(other_value)s)" % locals()
        else:
            return "%(this_value)s == %(other_value)s" % locals()

    def java_getter_name(self):
        return 'get' + upper_camelize(self.name)

    def java_getter(self, final=True):
        final = final and 'final ' or ''
        getter_name = self.java_getter_name()
        name = self.java_name()
        type_name = self.type.java_name(boxed=not self.required)
        return """\
public %(final)s%(type_name)s %(getter_name)s() {
    return %(name)s;
}""" % locals()

    def java_initializer(self):
        lhs = 'this.' + self.java_name()
        rhs = self.java_name()
        if self.required and self.type.java_is_reference():
            rhs = "com.google.common.base.Preconditions.checkNotNull(%(rhs)s)" % locals()
        return """\
%(lhs)s = %(rhs)s;""" % locals()

    def java_name(self):
        return lower_camelize(self.name)

    def java_parameter(self, final=False):
        parameter = []
        if final:
            parameter.append('final')
        parameter.append(self.type.java_name(boxed=not self.required))
        parameter.append(self.java_name())
        return ' '.join(parameter)

    def java_setter(self, return_type_name='void'):
        setter_name = self.java_setter_name()
        name = self.java_name()
        return_statement = \
            return_type_name != 'void' and "\n    return this;" or ''
        type_name = self.type.java_name(boxed=not self.required)
        return """\
public %(return_type_name)s %(setter_name)s(final %(type_name)s %(name)s) {
    this.%(name)s = %(name)s;%(return_statement)s
}""" % locals()

    def java_setter_name(self):
        return 'set' + upper_camelize(self.name)

    def java_value(self):
        if isinstance(self.value, str):
            return "\"%s\"" % self.value
        else:
            return self.value

    def __repr__(self):
        return self.java_parameter()
