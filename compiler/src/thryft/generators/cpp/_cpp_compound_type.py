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

from thryft.generator.document import Document
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct
from thryft.generators.cpp._cpp_type import _CppType
from yutil import lpad, indent, pad, rpad, upper_camelize


class _CppCompoundType(_CppType):
    def _cpp_constructor_default(self):
        name = self.cpp_name()

        if len(self.fields) == 0:
            return """\
%(name)s() {
}""" % locals()

        initializers = []
        for field in self.fields:
            default_initializer = field.cpp_default_initializer()
            if default_initializer is not None:
                initializers.append(default_initializer)
        initializers = lpad("\n  : ", ', '.join(initializers))
        return """\
%(name)s()%(initializers)s {
}""" % locals()

    def _cpp_constructor_protocol(self):
        name = self.cpp_name()
        return """\
%(name)s(::thryft::protocol::InputProtocol& iprot) {
  read(iprot);
}

%(name)s(::thryft::protocol::InputProtocol& iprot, ::thryft::protocol::Type::Enum as_type) {
  read(iprot, as_type);
}""" % locals()

    def _cpp_constructor_required(self):
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor
        elif len(set([field.required for field in self.fields])) <= 1:
            # All fields are optional or all fields are required
            return None  # Will be covered by total constructor

        initializers = []
        name = self.cpp_name()
        parameters = []
        for field in self.fields:
            if field.required:
                initializers.append(field.cpp_initializer())
                parameters.append(field.cpp_parameter())
            else:
                default_initializer = field.cpp_default_initializer()
                if default_initializer is not None:
                    initializers.append(default_initializer)
        initializers = \
            lpad("\n  : ", ', '.join(initializers))
        parameters = ", ".join(parameters)
        return """\
%(name)s(%(parameters)s)%(initializers)s {
}""" % locals()

    def _cpp_constructor_total(self):
        if len(self.fields) == 0:
            return None  # Will be covered by default constructor

        initializers = \
            lpad("\n  : ", ', '.join(
                (field.cpp_initializer()
                 for field in self.fields)
            ))
        name = self.cpp_name()
        parameters = ', '.join(field.cpp_parameter()
                                for field in self.fields)
        return """\
%(name)s(%(parameters)s)%(initializers)s {
}""" % locals()

    def _cpp_constructors(self):
        constructors = []
        for constructor in (
            self._cpp_constructor_default(),
            self._cpp_constructor_protocol(),
            self._cpp_constructor_required(),
            self._cpp_constructor_total()
        ):
            if constructor is not None:
                constructors.append(constructor)
        return constructors

    def cpp_default_value(self):
        return None

    def _cpp_destructor(self):
        name = self.cpp_name()
        return """\
virtual ~%(name)s() {
}""" % locals()

    def _cpp_extends(self):
        return '::thryft::Struct'

    def cpp_includes_definition(self):
        includes = ['<thryft.hpp>']
        for field in self.fields:
            includes.extend(field.cpp_includes_use())
        return includes

    def cpp_includes_use(self):
        parent = self.parent
        while not isinstance(parent, Document):
            parent = parent.parent
        return parent.cpp_includes_use()

    def _cpp_member_declarations(self):
        return [field.cpp_member_declaration()
                for field in self.fields]

    def _cpp_method_getters(self):
        return [field.cpp_getter() for field in self.fields]

    def _cpp_method_read(self):
        field_read_protocol_named = \
            lpad(' else ', indent(' ' * 8, ' else '.join(
                """\
if (ifield_name == "%s") {
%s
}""" % (field.name, indent(' ' * 2, field.cpp_read_protocol()))
                 for field in self.fields
            )).lstrip())
        field_read_protocol_positional = []
        for field_i, field in enumerate(self.fields):
            if field.required:
                field_required = True
            else:
                field_required = False
                # Field is optional, but it may be followed by a required field,
                # in which case it is required in a positional read
                if field_i + 1 < len(self.fields):
                    for other_field in self.fields[field_i + 1:]:
                        if other_field.required:
                            field_required = True
                            break
            field_read_protocol = field.cpp_read_protocol()
            if not field_required:
                field_read_protocol = indent(' ' * 2, field_read_protocol)
                field_read_protocol = """\
if (list_size > %(field_i)u) {
%(field_read_protocol)s
}""" % locals()
            field_read_protocol_positional.append(field_read_protocol)
        field_read_protocol_positional = \
            lpad("\n", indent(' ' * 6, "\n".join(field_read_protocol_positional)))
        name = self.cpp_name()
        return """\
void read(::thryft::protocol::InputProtocol& iprot) {
  read(iprot, ::thryft::protocol::Type::STRUCT);
}

void read(::thryft::protocol::InputProtocol& iprot, ::thryft::protocol::Type::Enum as_type) {
  switch (as_type) {
    case ::thryft::protocol::Type::LIST: {
      ::thryft::protocol::Type::Enum list_element_type;
      uint32_t list_size;
      iprot.read_list_begin(list_element_type, list_size);%(field_read_protocol_positional)s
      iprot.read_list_end();
      break;
    }

    case ::thryft::protocol::Type::STRUCT:
    default: {
      iprot.read_struct_begin();
      int16_t ifield_id;
      ::std::string ifield_name;
      ::thryft::protocol::Type::Enum ifield_type;
      for (;;) {
        iprot.read_field_begin(ifield_name, ifield_type, ifield_id);
        if (ifield_type == ::thryft::protocol::Type::STOP) {
          break;
        }%(field_read_protocol_named)s
        iprot.read_field_end();
      }
      iprot.read_struct_end();
      break;
    }
  }
}""" % locals()

    def _cpp_method_setters(self):
        return [field.cpp_setter() for field in self.fields]

    def _cpp_method_write(self):
        case_ttype_void = 'case ::thryft::protocol::Type::VOID:'
        if len(self.fields) == 1:
            field = self.fields[0]
            from thryft.generators.cpp._cpp_container_type import _CppContainerType
            from thryft.generators.cpp.cpp_struct_type import CppStructType
            if isinstance(field.type, _CppContainerType) or isinstance(field.type, CppStructType):
                field_value_cpp_write_protocol = \
                    indent(' ' * 4, field.type.cpp_write_protocol(field.cpp_getter_name() + (field.required and '()' or '().get()')))
                case_ttype_void = """\
%(case_ttype_void)s
%(field_value_cpp_write_protocol)s
    break;
""" % locals()

        field_count = len(self.fields)

        field_write_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 4,
                (field.cpp_write_protocol(write_field=True)
                 for field in self.fields)
            )))

        field_value_write_protocols = \
            pad("\n\n", "\n\n".join(indent(' ' * 4,
                (field.cpp_write_protocol(write_field=False)
                 for field in self.fields)
            )), "\n")

        name = self.cpp_name()

        return """\
void write(::thryft::protocol::OutputProtocol& oprot) const {
  write(oprot, ::thryft::protocol::Type::STRUCT);
}

void write(::thryft::protocol::OutputProtocol& oprot, ::thryft::protocol::Type::Enum as_type) const {
  switch (as_type) {
  %(case_ttype_void)s
  case ::thryft::protocol::Type::LIST:
    oprot.write_list_begin(::thryft::protocol::Type::VOID, %(field_count)u);%(field_value_write_protocols)s
    oprot.write_list_end();
    break;

  case ::thryft::protocol::Type::STRUCT:
  default:
    oprot.write_struct_begin();%(field_write_protocols)s

    oprot.write_field_stop();

    oprot.write_struct_end();
    break;
  }
}
""" % locals()

    def _cpp_methods(self):
        methods = []
        methods.extend(self._cpp_method_getters())
        methods.extend(self._cpp_method_setters())
        methods.extend(self._cpp_operators())
        methods.append(self._cpp_method_read())
        methods.append(self._cpp_method_write())
        return methods

    def _cpp_operator_equality(self):
        field_comparisons = \
            pad("\n", "\n\n".join(indent(' ' * 2, ("""\
if (!(%s() == other.%s())) {
  return false;
}""")) % (field.cpp_getter_name(), field.cpp_getter_name())
         for field in self.fields), "\n")
        name = self.cpp_name()
        return """\
bool operator==(const %(name)s& other) const {%(field_comparisons)s
  return true;
}""" % locals()

    def _cpp_operators(self):
        operators = []
        operators.append(self._cpp_operator_equality())
        return operators

    def cpp_read_protocol(self, value, optional=False):
        if optional:
            name = self.cpp_qname()
            return "%(value)s.set(%(name)s())->read(iprot);" % locals()
        else:
            return "%(value)s.read(iprot);" % locals()

    def cpp_qname(self, boxed=False):
        return _CppNamedConstruct.cpp_qname(self, name=self.name)

    def __repr__(self):
        name = self.cpp_name()
        extends = lpad(' : public ', self._cpp_extends())
        methods = self._cpp_methods()
        sections = []
        # sections.append(indent(' ' * 4, repr(self._CppBuilder(self))))
        sections.append(lpad("public:\n", "\n\n".join(indent(' ' * 2,
            self._cpp_constructors() + [self._cpp_destructor()] + self._cpp_methods()
            ))))
        sections.append(lpad("private:\n", "\n".join(indent(' ' * 2, self._cpp_member_declarations()))))
        sections = lpad("\n", "\n\n".join(section for section in sections if len(section) > 0))
        return """\
class %(name)s%(extends)s {%(sections)s
};""" % locals()
