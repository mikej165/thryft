from thryft.target.field import Field
from thryft.targets.java.java_construct import JavaConstruct
from yutil import lower_camelize, upper_camelize, indent


class JavaField(Field, JavaConstruct):
    def java_declaration(self, final=False):
        if self.value is not None:
            return "private %s = %s;" % (repr(self), self.java_value())
        else:
            return "private %s;" % self.java_parameter(final=final)

    def java_default_initializer(self):
        name = self.java_name()
        if self.value is not None:
            default_value = self.java_value()
        elif not self.required:
            default_value = 'null'
        else:
            default_value = self.type.java_default_value()
        return """\
this.%(name)s = %(default_value)s;""" % locals()

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

    def java_read_protocol(self):
        read_protocol = self.type.java_read_protocol()

        setter_name = self.java_setter_name()
        read_protocol = """\
builder.%(setter_name)s(%(read_protocol)s);""" % locals()

        read_protocol_throws = self.type.java_read_protocol_throws()
        if len(read_protocol_throws) > 0:
            read_protocol = indent(' ' * 4, read_protocol)
            read_protocol_throws = \
                ''.join(["""\
 catch (%(exception_type_name)s e) {
}""" % locals()
                           for exception_type_name in read_protocol_throws])
            read_protocol = """\
try {
%(read_protocol)s
}%(read_protocol_throws)s""" % locals()

        read_protocol = indent(' ' * 4, read_protocol)
        name = self.name
        return """\
if (ifield.name.equals("%(name)s")) {
%(read_protocol)s
}""" % locals()

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

    def java_write_protocol(self, depth=0):
        id_ = self.id
        if id_ is None:
            id_ = -1
        name = self.name
        getter_name = self.java_getter_name()
        ttype = self.type.thrift_ttype_name()
        write_protocol = \
            self.type.java_write_protocol(getter_name + "()", depth=depth)
        write_protocol = """\
oprot.writeFieldBegin(new org.apache.thrift.protocol.TField("%(name)s", org.apache.thrift.protocol.TType.%(ttype)s, (short)%(id_)d));
%(write_protocol)s
oprot.writeFieldEnd();
""" % locals()
        if not self.required:
            write_protocol = indent(' ' * 4, write_protocol)
            write_protocol = """\
if (%(getter_name)s() != null) {
%(write_protocol)s
}""" % locals()
        return write_protocol

    def __repr__(self):
        return self.java_parameter()
