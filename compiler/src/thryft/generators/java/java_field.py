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

from thryft.generator.field import Field
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from yutil import lower_camelize, upper_camelize, indent, lpad


class JavaField(Field, _JavaNamedConstruct):
    def java_absent_value(self):
        assert not self.required
        return "com.google.common.base.Optional.<%s> absent()" % self.type.java_boxed_qname()

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
            return self.java_absent_value()
        else:
            return self.type.java_default_value()

    def java_equals(self, this_value, other_value, nullable=False):
        if self.required:
            return self.type.java_equals(this_value, other_value, boxed=False)
        elif nullable:
            type_equals = self.type.java_equals(this_value, other_value, boxed=True)
            return "((%(this_value)s != null && %(other_value)s != null) ? (%(type_equals)s) : (%(this_value)s == null && %(other_value)s == null))" % locals()
        else:
            type_equals = self.type.java_equals(this_value + '.get()', other_value + '.get()', boxed=True)
            return "((%(this_value)s.isPresent() && %(other_value)s.isPresent()) ? (%(type_equals)s) : (!%(this_value)s.isPresent() && !%(other_value)s.isPresent()))" % locals()

    def java_field_metadata_enumerator_declaration(self):
        deprecated = '@Deprecated ' if self.deprecated else ''
        enumerator_name = self.java_field_metadata_enumerator_name()
        id = self.id if self.id is not None else 0  # @ReservedAssignment
        java_name = self.java_name()
        java_type = self._java_field_metadata_java_type_qname()
        type = self.type.thrift_ttype_name()  # @ReservedAssignment
        required = 'true' if self.required else 'false'
        thrift_name = self.name
        return "%(deprecated)s%(enumerator_name)s(\"%(java_name)s\", new com.google.common.reflect.TypeToken<%(java_type)s>() {}, %(required)s, %(id)d, \"%(thrift_name)s\", org.thryft.protocol.Type.%(type)s)" % locals()

    def java_field_metadata_enumerator_name(self):
        return self.name.upper()

    def _java_field_metadata_java_type_qname(self):
        return self.type.java_boxed_qname()

    def java_field_metadata_value_of_java_name_case(self):
        enumerator_name = self.java_field_metadata_enumerator_name()
        java_name = self.java_name()
        return """case "%(java_name)s": return %(enumerator_name)s;""" % locals()

    def java_field_metadata_value_of_thrift_name_case(self):
        enumerator_name = self.java_field_metadata_enumerator_name()
        thrift_name = self.name
        return """case "%(thrift_name)s": return %(enumerator_name)s;""" % locals()

    def java_getter(self, final=True):
        deprecated = '@Deprecated\n' if self.deprecated else ''
        final = final and 'final ' or ''
        getter_name = self.java_getter_name()
        javadoc = self.java_doc()
        name = self.java_name()
        type_name = self._java_type_name()
        return """\
%(javadoc)s%(deprecated)spublic %(final)s%(type_name)s %(getter_name)s() {
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
                self.type.java_hash_code(self.java_getter_name() + (self.required and '()' or '().get()'), boxed=not self.required) + \
            ';'
        if not self.required:
            hashCode_update = """\
if (%s().isPresent()) {
    %s
}""" % (self.java_getter_name(), hashCode_update)
        return hashCode_update

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
                rhs = self.java_absent_value()
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
            rhs = self.java_absent_value()
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
            return self.java_absent_value()
        else:
            return 'null'

    def java_protocol_initializer(self):
        read_protocol_lhs = self.java_name()
        read_protocol_rhs = self.type.java_read_protocol()
        if not self.required:
            read_protocol_rhs = "com.google.common.base.Optional.of(%s)" % read_protocol_rhs
        read_protocol = read_protocol_lhs + ' = ' + read_protocol_rhs + ';'

        read_protocol_throws = \
            self.type.java_read_protocol_throws_checked() + \
            self.type.java_read_protocol_throws_unchecked()
        if len(read_protocol_throws) > 0:
            field_metadata_enumerator = 'FieldMetadata.' + self.java_field_metadata_enumerator_name()
            read_protocol_catches = []
            for exception_type_name in read_protocol_throws:
                assert exception_type_name != 'org.thryft.protocol.InputProtocolException'
                if exception_type_name == 'org.thryft.protocol.UncheckedInputProtocolException':
                    read_protocol_catches.append("""\
 catch (final %(exception_type_name)s e) {
     throw new org.thryft.protocol.InvalidFieldInputProtocolException(%(field_metadata_enumerator)s, e.getCause());
}""" % locals())
                elif self.required:
                    read_protocol_catches.append("""\
 catch (final %(exception_type_name)s e) {
     throw new org.thryft.protocol.InvalidFieldInputProtocolException(%(field_metadata_enumerator)s, e);
}""" % locals())
                else:
                    read_protocol_catches.append("""\
 catch (final %(exception_type_name)s e) {
}""" % locals())
            read_protocol = indent(' ' * 4, read_protocol)
            read_protocol_catches = ''.join(read_protocol_catches)
            read_protocol = """\
try {
%(read_protocol)s
}%(read_protocol_catches)s""" % locals()

        return read_protocol

    def java_repr(self):
        return self.java_parameter()

    def java_set_case(self):
        name_upper = self.name.upper()
        setter_name = self.java_setter_name()
        type_name = self.type.java_qname() if self.required else self.type.java_boxed_qname()
        value = 'value'
        if type_name != 'java.lang.Object':
            value = "(%(type_name)s)%(value)s" % locals()
        return """\
case %(name_upper)s: %(setter_name)s(%(value)s); return this;""" % locals(),

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
        deprecated = '@Deprecated\n' if self.deprecated else ''
        setter_name = self.java_setter_name()
        name = self.java_name()
        return_statement = \
            return_type_name != 'void' and "\n    return this;" or ''
        type_name = self._java_type_name()
        validate_method_name = self.java_validate_method_name()
        setters = ["""\
%(deprecated)spublic %(return_type_name)s %(setter_name)s(final %(type_name)s %(name)s) {
    this.%(name)s = DefaultConstructionValidator.getInstance().%(validate_method_name)s(%(name)s);%(return_statement)s
}""" % locals()]
        if not self.required:
            return_ = 'return ' if return_type_name != 'void' else ''
            type_name = self.type.java_boxed_qname()
            setters.append("""\
%(deprecated)spublic %(return_type_name)s %(setter_name)s(@javax.annotation.Nullable final %(type_name)s %(name)s) {
    %(return_)s%(setter_name)s(com.google.common.base.Optional.fromNullable(%(name)s));
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
        deprecated = '@Deprecated\n' if self.deprecated else ''
        name = self.java_name()
        return_statement = \
            return_type_name != 'void' and "\n    return this;" or ''
        unsetter_name = self.java_unsetter_name()
        if self.required:
            unset = "this.%s = %s;" % (name, self.java_default_value())
        else:
            unset = "this.%s = %s;" % (name, self.java_absent_value())
        return """\
%(deprecated)spublic %(return_type_name)s %(unsetter_name)s() {
    %(unset)s%(return_statement)s
}""" % locals()

    def java_unsetter_name(self):
        return 'unset' + upper_camelize(self.name)

    def java_validate_method_declaration(self, exception_type_name):
        name = self.java_name()
        throws = " throws %(exception_type_name)s" % locals() if exception_type_name is not None else ''
        type_name = self._java_type_name()
        validate_method_name = self.java_validate_method_name()
        return """\
public %(type_name)s %(validate_method_name)s(final %(type_name)s %(name)s)%(throws)s;""" % locals()

    def java_validate_method_implementation(self, compound_type_qname, construction=False, nop=False, read=False):
        assert construction ^ nop ^ read
        field_metadata_enumerator = 'FieldMetadata.' + self.java_field_metadata_enumerator_name()
        field_name = self.java_name()
        checks = []
        if not nop:
            if self.type.java_is_reference():
                # Null check
                message = "\"%(compound_type_qname)s: %(field_name)s is null\"" % locals()
                if construction:
                    npe = """NullPointerException(%(message)s)""" % locals()
                else:
                    npe = """org.thryft.protocol.MissingFieldInputProtocolException(%(field_metadata_enumerator)s, %(message)s)""" % locals()
                checks.append("""\
if (%(field_name)s == null) {
    throw new %(npe)s;
}""" % locals())
            if not self.required:
                # If an Optional is absent, don't do further checks
                checks.append("""\
if (!%(field_name)s.isPresent()) {
    return %(field_name)s;
}""" % locals())
            # Validation checks
            validation = {}
            for annotations in (self.annotations, self.type.annotations):
                for annotation in annotations:
                    if annotation.name == 'validation':
                        validation = annotation.value.copy()
                        break
                if len(validation) > 0:
                    break
            if len(validation) > 0:
                field_value = field_name if self.required else (field_name + '.get()')
                for validation_name, validation_value in validation.iteritems():
                    exception_prefix = "IllegalArgumentException(" if construction else ("org.thryft.protocol.InvalidFieldInputProtocolException(" + field_metadata_enumerator + ', ')
                    message_prefix = "%(compound_type_qname)s: %(field_name)s is " % locals()
                    if validation_name == 'acceptance':
                        check = ('!' + field_value) if validation_value else field_value
                        message = message_prefix + 'not ' + str(validation_value).lower()
                    elif validation_name == 'blank':
                        checks.append("""\
{
    final int __strLen = %(field_value)s.length();
    boolean __blank = true;
    for (int i = 0; i < __strLen; i++) {
        if (!Character.isWhitespace(%(field_value)s.charAt(i))) {
            __blank = false;
            break;
        }
    }
    if (__blank) {
        throw new %(exception_prefix)sString.format(\"%(message_prefix)sblank: '%%s' (length=%%d)\", %(field_value)s, __strLen));
    }
}""" % locals())
                        continue
                    elif validation_name == 'max':
                        check = self.type.java_compare(field_value, '>', self.type.java_literal(validation_value), boxed=not self.required)
                        message = message_prefix + "greater than max " + str(validation_value)
                    elif validation_name == 'maxLength':
                        check = "%s > %s" % (self.type.java_size(field_value), validation_value)
                        message = message_prefix + "greater than max length " + str(validation_value)
                    elif validation_name == 'min':
                        check = self.type.java_compare(field_value, '<', self.type.java_literal(validation_value), boxed=not self.required)
                        message = message_prefix + "less than min " + str(validation_value)
                    elif validation_name == 'minLength':
                        if validation_value == 1:
                            check = self.type.java_is_empty(field_value)
                        else:
                            check = "%s < %s" % (self.type.java_size(field_value), validation_value)
                        message = message_prefix + "less than min length " + str(validation_value)
                    else:
                        self._logger.warn('unsupported validation %s', validation_name)
                        continue
                    checks.append("""\
if (%(check)s) {
    throw new %(exception_prefix)s\"%(message)s\");
}""" % locals())

        checks = lpad("\n", "\n".join(indent(' ' * 4, checks)))
        if construction:
            exception_type_name = 'RuntimeException'
        elif nop:
            exception_type_name = None
        elif read:
            exception_type_name = 'org.thryft.protocol.InputProtocolException'
        declaration = self.java_validate_method_declaration(exception_type_name=exception_type_name).rstrip(';')
        return """\
@Override
%(declaration)s {%(checks)s
    return %(field_name)s;
}""" % locals()

    def java_validate_method_name(self):
        return 'validate' + upper_camelize(self.name)

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
