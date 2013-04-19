#-------------------------------------------------------------------------------
# Copyright (c) 2013, Minor Gordon
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
#-------------------------------------------------------------------------------

from thryft.generator.field import Field
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from thryft.generators.java.java_bool_type import JavaBoolType
from yutil import lower_camelize, upper_camelize, indent


class JavaField(Field, _JavaNamedConstruct):
    def java_default_initializer(self):
        default_value = self.java_default_value()
        name = self.java_name()
        return """\
%(name)s = %(default_value)s;""" % locals()

    def java_default_value(self):
        if self.value is not None:
            return self.java_value()
        elif not self.required:
            return 'null'
        else:
            return self.type.java_default_value()

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
        getter_name = upper_camelize(self.name)
        if isinstance(self.type, JavaBoolType):
            if getter_name.startswith('Is'):
                return 'is' + getter_name[2:]
            else:
                return 'is' + getter_name
        else:
            return 'get' + getter_name

    def java_getter(self, final=True):
        final = final and 'final ' or ''
        getter_name = self.java_getter_name()
        name = self.java_name()
        type_name = self.type.java_declaration_name(boxed=not self.required)
        return """\
public %(final)s%(type_name)s %(getter_name)s() {
    return %(name)s;
}""" % locals()

    def java_initializer(self):
        return 'this.' + self.java_name() + ' = ' + self.java_validation() + ';'

    def java_local_declaration(self, boxed=None, final=False):
        if self.value is not None:
            return "%s = %s;" % \
                    (self.java_parameter(boxed=boxed), self.java_value())
        elif not final:
            if boxed is False or self.required:
                return "%s = %s;" % \
                        (self.java_parameter(boxed=boxed, final=final),
                         self.type.java_default_value())
            else:
                return "%s = null;" % \
                        self.java_parameter(boxed=boxed, final=final)
        else:
            return self.java_parameter(boxed=boxed, final=final)

    def java_member_declaration(self, boxed=None, final=False):
        if self.value is not None:
            return "private %s = %s;" % \
                    (self.java_parameter(boxed=boxed), self.java_value())
        else:
            return "private %s;" % \
                    self.java_parameter(boxed=boxed, final=final)

    def java_name(self):
        return lower_camelize(self.name)

    def java_parameter(self, boxed=None, final=False):
        if boxed is None:
            boxed = not self.required
        parameter = []
        if final:
            parameter.append('final')
        parameter.append(self.type.java_declaration_name(boxed=boxed))
        parameter.append(self.java_name())
        return ' '.join(parameter)

    def java_protocol_initializer(self):
        read_protocol = \
            self.java_name() + ' = ' + self.type.java_read_protocol() + ';'

        read_protocol_throws = self.type.java_read_protocol_throws()
        if not self.required and len(read_protocol_throws) > 0:
            read_protocol = indent(' ' * 4, read_protocol)
            read_protocol_throws = \
                ''.join("""\
 catch (%(exception_type_name)s e) {
}""" % locals()
                         for exception_type_name in read_protocol_throws)
            read_protocol = """\
try {
%(read_protocol)s
}%(read_protocol_throws)s""" % locals()

        return read_protocol

#    def java_read_protocol(self):
#        read_protocol = \
#            self.java_setter_name() + '(' + \
#                self.type.java_read_protocol() + \
#            ');'
#
#        read_protocol_throws = self.type.java_read_protocol_throws()
#        if len(read_protocol_throws) > 0:
#            read_protocol = indent(' ' * 4, read_protocol)
#            read_protocol_throws = \
#                ''.join("""\
# catch (%(exception_type_name)s e) {
# }""" % locals()
#                           for exception_type_name in read_protocol_throws)
#            read_protocol = """\
# try {
# %(read_protocol)s
# }%(read_protocol_throws)s""" % locals()
#
#        read_protocol = indent(' ' * 4, read_protocol)
#        name = self.name
#        return """\
# if (ifield.name.equals("%(name)s")) {
# %(read_protocol)s
# }""" % locals()

    def java_setter(self, return_type_name='void'):
        setter_name = self.java_setter_name()
        name = self.java_name()
        return_statement = \
            return_type_name != 'void' and "\n    return this;" or ''
        type_name = self.type.java_declaration_name(boxed=not self.required)
        return """\
public %(return_type_name)s %(setter_name)s(final %(type_name)s %(name)s) {
    this.%(name)s = %(name)s;%(return_statement)s
}""" % locals()

    def java_setter_name(self):
        return 'set' + upper_camelize(self.name)

    def java_validation(self, value=None):
        name = self.java_name()
        parent_qname = self.parent.java_qname()
        if value is None:
            java_validation = self.java_name()
        else:
            java_validation = value
        if self.type.java_is_reference():  # Only reference types like String and containers can have lengths
            validation = self.annotations.get('validation', {})
            min_length = validation.get('minLength')
            if min_length == 1:
                java_validation = """org.thryft.core.Preconditions.checkNotEmpty(%(java_validation)s, "%(parent_qname)s: %(name)s is empty")""" % locals()
                if not self.required:
                    java_validation = self.java_name() + " != null ? " + java_validation + " : null";
            elif min_length is not None:
                java_validation = """org.thryft.core.Preconditions.checkMinLength(%(java_validation)s, %(min_length)u, "%(parent_qname)s: %(name)s must have a minimum length of %(min_length)u")""" % locals()
                if not self.required:
                    java_validation = self.java_name() + " != null ? " + java_validation + " : null";
            elif self.required:
                java_validation = """com.google.common.base.Preconditions.checkNotNull(%(java_validation)s, "%(parent_qname)s: missing %(name)s")""" % locals()
        return java_validation

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
