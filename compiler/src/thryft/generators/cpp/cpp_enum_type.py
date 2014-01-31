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
from thryft.generator.enum_type import EnumType
from thryft.generators.cpp._cpp_type import _CppType
from yutil import indent, lpad


class CppEnumType(EnumType, _CppType):
    def cpp_default_value(self):
        if len(self.enumerators) > 0:
            return _CppType.cpp_qname(self) + '::' + self.enumerators[0].name
        else:
            return 0

    def cpp_includes_definition(self):
        return ('<thryft.hpp>',)

    def cpp_includes_use(self):
        return self._parent_document().cpp_includes_use()

    def cpp_qname(self):
        return _CppType.cpp_qname(self) + '::Enum'

    def cpp_read_protocol(self, value, optional=False):
        name = _CppType.cpp_qname(self)
        return "%(value)s = %(name)s::read(iprot);" % locals()

    def cpp_write_protocol(self, value, depth=0):
        name = _CppType.cpp_qname(self)
        return "%(name)s::write(oprot, %(value)s);" % locals()

    def __repr__(self):
        if len(self.enumerators) > 0:
            default_value = self.enumerators[0].name
        else:
            default_value = 'static_cast<Enum>(0)'
        enumerators = \
            lpad("\n", ",\n".join(indent(' ' * 4,
                ("%s = %u" % (enumerator.name, enumerator.value)
                 for enumerator in self.enumerators)
            )))
        enumerator_value_ofs = \
            lpad("\n", indent(' ' * 4, ' else '.join("""\
if (name == "%s") {
  return %s;
}""" % (enumerator.name, enumerator.name) for enumerator in self.enumerators)))
        enumerator_write_cases = \
            lpad("\n", "\n".join(indent(' ' * 4, ("""\
case %s: oprot.write("%s", %u); break;
""" % (enumerator.name, enumerator.name, len(enumerator.name))
                for enumerator in self.enumerators))))
        name = self.cpp_name()
        return """\
class %(name)s {
public:
  enum Enum {%(enumerators)s
  };

  static Enum read(::thryft::protocol::InputProtocol& iprot) {
    ::std::string name;
    iprot.read_string(name);%(enumerator_value_ofs)s
    return %(default_value)s;
  }

  static void write(::thryft::protocol::OutputProtocol& oprot, Enum value) {
    switch (value) {%(enumerator_write_cases)s
    default:
      oprot.write_null();
      break;
    }
  }
};""" % locals()
