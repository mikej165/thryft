# -----------------------------------------------------------------------------
# Copyright (c) 2015, Minor Gordon
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

from thryft.generator.field import Field
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from yutil import lower_camelize, upper_camelize, indent, lpad


class JavaField(Field, _JavaNamedConstruct):
    def java_absent_value(self):
        assert not self.required
        return "com.google.common.base.Optional.<%s> absent()" % self.type.java_boxed_qname()

    def java_compare_to(self):
        name = self.java_name()
        this_value = 'this.' + name
        other_value = 'other.' + name
        if not self.required:
            this_value += '.get()'
            other_value += '.get()'
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
if (this.%(name)s.isPresent()) {
    if (other.%(name)s.isPresent()) {
%(compare_to)s
    } else {
        return 1;
    }
} else if (other.%(name)s.isPresent()) {
    return -1;
}""" % locals()
        return compare_to

    def java_default_initializer(self):
        default_value = self.java_default_value()
        name = self.java_name()
        return """\
%(name)s = %(default_value)s;""" % locals()

    def java_default_value(self):
        if self.value is not None:
            if self.required:
                return self.java_value()
            else:
                return "com.google.common.base.Optional.of(%s)" % self.java_value()
        elif not self.required:
            return 'com.google.common.base.Optional.absent()'
        else:
            return self.type.java_default_value()

    def java_equals(self, this_value, other_value, nullable=False):
        type_equals = self.type.java_equals(this_value, other_value)
        if self.required:
            return type_equals
        if nullable:
            return "((%(this_value)s != null && %(other_value)s != null) ? (%(type_equals)s) : (%(this_value)s == null && %(other_value)s == null))" % locals()
        else:
            type_equals = self.type.java_equals(this_value + '.get()', other_value + '.get()')
            return "((%(this_value)s.isPresent() && %(other_value)s.isPresent()) ? (%(type_equals)s) : (!%(this_value)s.isPresent() && !%(other_value)s.isPresent()))" % locals()

    def java_getter(self, final=True):
        final = final and 'final ' or ''
        getter_name = self.java_getter_name()
        javadoc = self.java_doc()
        name = self.java_name()
        type_name = self._java_type_name()
        return """\
%(javadoc)spublic %(final)s%(type_name)s %(getter_name)s() {
    return %(name)s;
}""" % locals()

    def java_getter_name(self):
        return JavaField.java_getter_name_static(self)

    @staticmethod
    def java_getter_name_static(field):
        return 'get' + upper_camelize(field.name)

    def java_hash_code_update(self):
        hashCode_update = \
            'hashCode = 31 * hashCode + ' + \
                self.type.java_hash_code(self.java_getter_name() + (self.required and '()' or '().get()'), already_boxed=not self.required) + \
            ';'
        if not self.required:
            hashCode_update = """\
if (%s().isPresent()) {
    %s
}""" % (self.java_getter_name(), hashCode_update)
        return hashCode_update

    def java_initializer(self, **kwds):
        return 'this.' + self.java_name() + ' = ' + self.java_validation(**kwds) + ';'

    def java_is_absent(self):
        assert not self.required
        return "!%s().isPresent()" % self.java_getter_name()

    def java_local_declaration(self, boxed=None, final=False):
        if self.value is not None:
            lhs = self.java_parameter(boxed=boxed)
            if self.required:
                rhs = self.java_value()
            else:
                rhs = "com.google.common.base.Optional.of(%s)" % self.java_value()
        elif not final:
            lhs = self.java_parameter(boxed=boxed, final=final)
            if boxed is False or self.required:
                rhs = self.type.java_default_value()
            else:
                rhs = "com.google.common.base.Optional.absent()"
        else:
            return self.java_parameter(boxed=boxed, final=final)
        return "%(lhs)s = %(rhs)s;" % locals()

    def java_member_declaration(self, assign_value=True, boxed=None, final=False):
        javadoc = self.java_doc()
        lhs = self.java_parameter(boxed=boxed, final=final)
        if self.value is not None and assign_value:
            if self.required:
                rhs = str(self.java_value())
            else:
                rhs = "com.google.common.base.Optional.of(%s);" % self.java_value()
        elif not self.required and not final and assign_value:
            rhs = 'com.google.common.base.Optional.absent()'
        else:
            rhs = ''
        rhs = lpad(' = ', rhs)
        return "%(javadoc)sprivate %(lhs)s%(rhs)s;" % locals()

    def java_name(self):
        return lower_camelize(self.name)

    def java_parameter(self, boxed=None, final=False, nullable=False):
        if boxed is None:
            boxed = not self.required
        parameter = []
        if final:
            parameter.append('final')
        parameter.append(self._java_type_name(boxed=boxed, nullable=nullable))
        parameter.append(self.java_name())
        return ' '.join(parameter)

    def java_null_initializer(self):
        null_value = self.java_default_value()
        name = self.java_name()
        return """\
%(name)s = %(null_value)s;""" % locals()

    def java_null_value(self):
        if self.value is not None:
            if self.required:
                return str(self.java_value())
            else:
                return "com.google.common.base.Optional.of(%s);" % self.java_value()
        elif not self.required:
            return 'com.google.common.base.Optional.absent()'
        else:
            return 'null'

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
 catch (final %(exception_type_name)s e) {
     throw new org.thryft.protocol.InputProtocolException(e);
}""" % locals()
                         for exception_type_name in read_protocol_throws)
            else:
                read_protocol_throws = \
                    ''.join("""\
 catch (final %(exception_type_name)s e) {
}""" % locals()
                         for exception_type_name in read_protocol_throws)
            read_protocol = indent(' ' * 4, read_protocol)
            read_protocol = """\
try {
%(read_protocol)s
}%(read_protocol_throws)s""" % locals()

        return read_protocol

    def java_repr(self):
        return self.java_parameter()

    def java_set_cases(self):
        name = self.name
        setter_name = self.java_setter_name()
        type_name = self.type.java_qname() if self.required else self.type.java_boxed_qname()
        value = 'value'
        if type_name != 'java.lang.Object':
            value = "(%(type_name)s)%(value)s" % locals()
        return ("""\
case "%(name)s": %(setter_name)s(%(value)s); return this;""" % locals(),)

    def java_set_if_present(self):
        getter_name = self.java_getter_name()
        setter_name = self.java_setter_name()
        if self.required:
            return """\
%(setter_name)s(other.%(getter_name)s());""" % locals()
        else:
            return """\
if (other.%(getter_name)s().isPresent()) {
    %(setter_name)s(other.%(getter_name)s());
}""" % locals()

    def java_set_suppress_warnings(self):
        if self.type.java_is_parameterized():
            return ('unchecked',)
        else:
            return tuple()

    def java_setters(self, return_type_name='void'):
        setter_name = self.java_setter_name()
        name = self.java_name()
        return_statement = \
            return_type_name != 'void' and "\n    return this;" or ''
        type_name = self._java_type_name()
        setters = ["""\
public %(return_type_name)s %(setter_name)s(final %(type_name)s %(name)s) {
    this.%(name)s = com.google.common.base.Preconditions.checkNotNull(%(name)s);%(return_statement)s
}""" % locals()]
        if not self.required:
            type_name = self.type.java_boxed_qname()
            setters.append("""\
public %(return_type_name)s %(setter_name)s(@javax.annotation.Nullable final %(type_name)s %(name)s) {
    this.%(name)s = com.google.common.base.Optional.fromNullable(%(name)s);%(return_statement)s
}""" % locals())
        return setters

    def java_setter_name(self):
        return 'set' + upper_camelize(self.name)

    def java_to_string_helper_add(self):
        escape = False
        for annotations in (self.annotations, self.type.annotations):
            for annotation in annotations:
                if annotation.name == 'java_exclude_from_to_string':
                    return ''
                elif annotation.name == 'java_escape_to_string':
                    escape = True
        field_value = self.java_getter_name() + '()'
        if not self.required:
            field_value += '.orNull()'
        if escape:
            field_value = "org.apache.commons.lang3.StringEscapeUtils.escapeJava(%s)" % field_value
        return """.add(\"%s\", %s)""" % (self.name, field_value)

    def _java_type_name(self, boxed=None, nullable=False):
        if self.required:
            if boxed:
                return self.type.java_boxed_qname()
            else:
                return self.type.java_qname()
        elif nullable:
            return "@javax.annotation.Nullable %s" % self.type.java_boxed_qname()
        else:
            return "com.google.common.base.Optional<%s>" % self.type.java_boxed_qname()

    def java_unsetter(self, return_type_name='void'):
        name = self.java_name()
        return_statement = \
            return_type_name != 'void' and "\n    return this;" or ''
        unsetter_name = self.java_unsetter_name()
        if self.required:
            unset = "this.%s = %s;" % (name, self.java_default_value())
        else:
            unset = "this.%s = com.google.common.base.Optional.absent();" % name
        return """\
public %(return_type_name)s %(unsetter_name)s() {
    %(unset)s%(return_statement)s
}""" % locals()

    def java_unsetter_name(self):
        return 'unset' + upper_camelize(self.name)

    def java_validation(self, boxed=False, check_optional_not_null=True, value=None, nullable=False):
        name = self.java_name()
        parent_qname = self.parent.java_qname()
        if value is None:
            value = self.java_name()

        java_validation = value
        if self.required:
            if boxed or self.type.java_is_reference():
                java_validation = """com.google.common.base.Preconditions.checkNotNull(%(java_validation)s, "%(parent_qname)s: missing %(name)s")""" % locals()
        else:
            if nullable:
                java_validation = "com.google.common.base.Optional.fromNullable(%(java_validation)s)" % locals()
            elif check_optional_not_null:
                java_validation = """com.google.common.base.Preconditions.checkNotNull(%(java_validation)s, "%(parent_qname)s: missing %(name)s")""" % locals()

        validation = {}
        for annotations in (self.annotations, self.type.annotations):
            for annotation in annotations:
                if annotation.name == 'validation':
                    validation = annotation.value.copy()
                    break
            if len(validation) > 0:
                break
        if len(validation) > 0:
            precondition_name = self.type.java_precondition_name()
            if not self.required:
                precondition_name = 'Optional' + precondition_name

            acceptance = validation.get('acceptance')
            if acceptance is not None:
                java_validation = """org.thryft.Preconditions.check%(precondition_name)sTrue(%(java_validation)s, "%(parent_qname)s: %(name)s must be true")""" % locals()

            max_length = validation.get('maxLength')
            if max_length is not None:
                java_validation = """org.thryft.Preconditions.check%(precondition_name)sMaxLength(%(java_validation)s, %(max_length)u, "%(parent_qname)s: %(name)s must have a maximum length of %(max_length)u")""" % locals()

            min_ = validation.get('min')
            if min_ is not None:
                java_validation = """org.thryft.Preconditions.check%(precondition_name)sMin(%(java_validation)s, %(min_)d, "%(parent_qname)s: %(name)s must be at least %(min_)d")""" % locals()

            min_length = validation.get('minLength')
            if min_length == 1:
                java_validation = """org.thryft.Preconditions.check%(precondition_name)sNotEmpty(%(java_validation)s, "%(parent_qname)s: %(name)s is empty")""" % locals()
            elif min_length is not None:
                java_validation = """org.thryft.Preconditions.check%(precondition_name)sMinLength(%(java_validation)s, %(min_length)u, "%(parent_qname)s: %(name)s must have a minimum length of %(min_length)u")""" % locals()

        return java_validation

    def java_value(self):
        assert self.value is not None
        return self.type.java_literal(self.value)

    def java_write_protocol(self, write_field=True, depth=0):
        id_ = self.id if self.id is not None else 0
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
oprot.writeFieldBegin("%(name)s", org.thryft.protocol.Type.%(ttype)s, (short)%(id_)d);
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
