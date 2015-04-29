#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------

from thryft.generator.field import Field
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct
from yutil import indent


class CppField(Field, _CppNamedConstruct):
    def cpp_default_initializer(self):
        if not self.required:
            return None
        if self.value is not None:
            value = self.cpp_value()
        else:
            value = self.type.cpp_default_value()
            if value is None:
                return None
        return "%s_(%s)" % (self.cpp_name(), value)

    def cpp_getters(self):
        member_name = self.cpp_member_name()
        name = self.cpp_name()
        type_name = self._cpp_type_qname()
        return """\
%(type_name)s& %(name)s() {
  return %(member_name)s;
}

const %(type_name)s& %(name)s() const {
  return %(member_name)s;
}""" % locals()

    def cpp_getter_name(self):
        return self.cpp_name()

    def cpp_includes_use(self):
        includes = []
        includes.extend(self.type.cpp_includes_use())
        if not self.required:
            includes.append('<thryft.hpp>')
        return includes

    def cpp_initializer(self):
        member_name = self.cpp_member_name()
        name = self.cpp_name()
        return "%(member_name)s(%(name)s)" % locals()

    def cpp_local_declaration(self):
        name = self.cpp_name()
        type_name = self._cpp_type_qname()
        return type_name + ' ' + name + ';'

    def cpp_member_declaration(self):
        return self._cpp_type_qname() + ' ' + self.cpp_member_name() + ';'

    def cpp_member_name(self):
        return self.cpp_name() + '_'

    def cpp_parameter(self):
        name = self.cpp_name()
        type_name = self._cpp_type_qname()
        return 'const ' + type_name + '& ' + name

    def cpp_read_protocol(self):
        return self.type.cpp_read_protocol(self.cpp_member_name(), optional=not self.required)

    def _cpp_type_qname(self):
        type_qname = self.type.cpp_qname()
        if not self.required:
            type_qname = "::thryft::Optional< %s >" % type_qname
        return type_qname

    def cpp_setter(self):
        member_name = self.cpp_member_name()
        name = self.cpp_name()
        parameter = self.cpp_parameter()
        parent_name = self.parent.cpp_name()
        setter_name = self.cpp_setter_name()
        type_name = self._cpp_type_qname()
        setter = """\
%(parent_name)s& %(setter_name)s(%(parameter)s) {
  this->%(member_name)s = %(name)s;
  return *this;
}""" % locals()
        if not self.required:
            type_qname = self.type.cpp_qname()
            # Setter above is for an optional parameter
            setter += """

%(parent_name)s& %(setter_name)s(const %(type_qname)s& %(name)s) {
  return %(setter_name)s(::thryft::Optional< %(type_qname)s >(%(name)s));
}""" % locals()
        return setter

    def cpp_to_string(self, depth, oss):
        if self.required:
            return self.type.cpp_to_string(depth=depth, oss=oss, value=self.cpp_member_name())
        else:
            member_name = self.cpp_member_name()
            to_string = indent(' ' * 2, self.type.cpp_to_string(depth=depth, oss=oss, value="(*%s)" % member_name))
            return """\
if (%(member_name)s.present()) {
%(to_string)s
} else {
  oss << "";
}""" % locals()

    def cpp_setter_name(self):
        return 'set_' + self.cpp_name()

    def cpp_value(self):
        return self.type.cpp_literal(self.value)

    def cpp_write_protocol(self, write_field=True):
        id_ = self.id
        if id_ is None:
            id_ = -1
        name = self.name
        getter_name = self.cpp_getter_name()
        ttype = self.type.thrift_ttype_name()
        value = getter_name + "()"
        if not self.required:
            value += '.get()'
        write_protocol = self.type.cpp_write_protocol(value)
        if write_field:
            write_protocol = """\
oprot.write_field_begin("%(name)s", ::thryft::protocol::Type::%(ttype)s, static_cast<int16_t>(%(id_)d));
%(write_protocol)s
oprot.write_field_end();
""" % locals()
        if not self.required:
            write_protocol = indent(' ' * 4, write_protocol)
            write_protocol = """\
if (%(getter_name)s().present()) {
%(write_protocol)s
}""" % locals()
            if not write_field:
                write_protocol += """\
 else {
    oprot.write_null();
}"""
        return write_protocol
