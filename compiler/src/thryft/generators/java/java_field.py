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
from yutil import lower_camelize, upper_camelize, indent, lpad


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
            return 'com.google.common.base.Optional.absent()'
        else:
            return self.type.java_default_value()

    def java_equals(self, this_value, other_value):
        if self.type.java_is_reference() or not self.required:
            return "%(this_value)s.equals(%(other_value)s)" % locals()
        else:
            return "%(this_value)s == %(other_value)s" % locals()

    def java_getter(self, final=True):
        final = final and 'final ' or ''
        getter_name = self.java_getter_name()
        javadoc = self.java_doc()
        name = self.java_name()
        type_name = self.__java_type_name()
        return """\
%(javadoc)spublic %(final)s%(type_name)s %(getter_name)s() {
    return %(name)s;
}""" % locals()

    def java_getter_name(self):
        getter_name = upper_camelize(self.name)
        if isinstance(self.type, JavaBoolType) and self.required:
            if getter_name.startswith('Is'):
                return 'is' + getter_name[2:]
            else:
                return 'is' + getter_name
        else:
            return 'get' + getter_name

    def java_hash_code_update(self):
        hashCode_update = \
            'hashCode = 31 * hashCode + ' + \
                self.type.java_hash_code(self.java_getter_name() + (self.required and '()' or '().get()')) + \
            ';'
        if not self.required:
            hashCode_update = """\
if (%s().isPresent()) {
    %s
}""" % (self.java_getter_name(), hashCode_update)
        return hashCode_update

    def java_initializer(self, check_optional_not_null=True):
        return 'this.' + self.java_name() + ' = ' + self.java_validation(check_optional_not_null=check_optional_not_null) + ';'

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
                return "%s = com.google.common.base.Optional.absent();" % \
                        self.java_parameter(boxed=boxed, final=final)
        else:
            return self.java_parameter(boxed=boxed, final=final)

    def java_member_declaration(self, boxed=None, final=False):
        javadoc = self.java_doc()
        lhs = self.java_parameter(boxed=boxed, final=final)
        if self.value is not None:
            assert not self.required
            rhs = "com.google.common.base.Optional.of(%s);" % self.java_value()
        elif not self.required and not final:
            rhs = 'com.google.common.base.Optional.absent()'
        else:
            rhs = ''
        rhs = lpad(' = ', rhs)
        return "%(javadoc)sprivate %(lhs)s%(rhs)s;" % locals()

    def java_name(self, boxed=False):
        return lower_camelize(self.name)

    def java_parameter(self, boxed=None, final=False):
        if boxed is None:
            boxed = not self.required
        parameter = []
        if final:
            parameter.append('final')
        parameter.append(self.__java_type_name(boxed=boxed))
        parameter.append(self.java_name())
        return ' '.join(parameter)

    def java_protocol_initializer(self):
        read_protocol_lhs = self.java_name()
        read_protocol_rhs = self.type.java_read_protocol()
        if not self.required:
            read_protocol_rhs = "com.google.common.base.Optional.of(%s)" % read_protocol_rhs
        read_protocol = read_protocol_lhs + ' = ' + read_protocol_rhs + ';'

        if self.required:
            read_protocol_throws = self.type.java_read_protocol_throws_checked()
        else:
            read_protocol_throws = \
                self.type.java_read_protocol_throws_checked() + \
                self.type.java_read_protocol_throws_unchecked()
        if len(read_protocol_throws) > 0:
            if self.required:
                read_protocol_throws = \
                    ''.join("""\
 catch (%(exception_type_name)s e) {
     throw new IllegalArgumentException(e);
}""" % locals()
                         for exception_type_name in read_protocol_throws)
            else:
                read_protocol_throws = \
                    ''.join("""\
 catch (%(exception_type_name)s e) {
}""" % locals()
                         for exception_type_name in read_protocol_throws)
            read_protocol = indent(' ' * 4, read_protocol)
            read_protocol = """\
try {
%(read_protocol)s
}%(read_protocol_throws)s""" % locals()

        return read_protocol

    def java_setters(self, return_type_name='void'):
        setter_name = self.java_setter_name()
        name = self.java_name()
        return_statement = \
            return_type_name != 'void' and "\n    return this;" or ''
        type_name = self.__java_type_name()
        setters = ["""\
public %(return_type_name)s %(setter_name)s(final %(type_name)s %(name)s) {
    this.%(name)s = %(name)s;%(return_statement)s
}""" % locals()]
        if not self.required:
            type_name = self.type.java_declaration_name()
            setters.append("""\
public %(return_type_name)s %(setter_name)s(final %(type_name)s %(name)s) {
    this.%(name)s = com.google.common.base.Optional.of(%(name)s);%(return_statement)s
}""" % locals())
        return setters

    def java_setter_name(self):
        return 'set' + upper_camelize(self.name)

    def __java_type_name(self, boxed=None):
        if self.required:
            return self.type.java_declaration_name(boxed=boxed)
        else:
            return "com.google.common.base.Optional<%s>" % self.type.java_declaration_name(boxed=True)

    def java_validation(self, check_optional_not_null=True, value=None):
        name = self.java_name()
        parent_qname = self.parent.java_qname()
        if value is None:
            value = self.java_name()
        java_validation = value
        if self.type.java_is_reference():
            if self.required or check_optional_not_null:
                java_validation = """com.google.common.base.Preconditions.checkNotNull(%(java_validation)s, "%(parent_qname)s: missing %(name)s")""" % locals()
        if self.type.java_has_length():
            validation = self.annotations.get('validation', {})
            min_length = validation.get('minLength')
            if min_length == 1:
                java_validation = """org.thryft.Preconditions.checkNotEmpty(%(java_validation)s, "%(parent_qname)s: %(name)s is empty")""" % locals()
            elif min_length is not None:
                java_validation = """org.thryft.Preconditions.checkMinLength(%(java_validation)s, %(min_length)u, "%(parent_qname)s: %(name)s must have a minimum length of %(min_length)u")""" % locals()
        return java_validation

    def java_value(self):
        if isinstance(self.value, str):
            return "\"%s\"" % self.value
        else:
            return self.value

    def java_write_protocol(self, write_field=True, depth=0):
        id_ = self.id
        if id_ is None:
            id_ = -1
        name = self.name
        getter_name = self.java_getter_name()
        ttype = self.type.thrift_ttype_name()
        value = getter_name + "()"
        if not self.required:
            value += '.get()'
        write_protocol = \
            self.type.java_write_protocol(value, depth=depth)
        if write_field:
            write_protocol = """\
oprot.writeFieldBegin(new org.thryft.protocol.TField("%(name)s", org.thryft.protocol.TType.%(ttype)s, (short)%(id_)d));
%(write_protocol)s
oprot.writeFieldEnd();
""" % locals()
        if not self.required:
            write_protocol = indent(' ' * 4, write_protocol)
            write_protocol = """\
if (%(getter_name)s().isPresent()) {
%(write_protocol)s
}""" % locals()
            if not write_field:
                write_protocol += """\
 else {
    oprot.writeNull();
}"""
        return write_protocol

    def __repr__(self):
        return self.java_parameter()
