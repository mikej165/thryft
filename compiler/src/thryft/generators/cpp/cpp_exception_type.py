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

from thryft.generator.exception_type import ExceptionType
from thryft.generators.cpp._cpp_compound_type import _CppCompoundType
from yutil import indent, lpad


class CppExceptionType(ExceptionType, _CppCompoundType):
    def __init__(self, **kwds):
        ExceptionType.__init__(self, **kwds)
        _CppCompoundType.__init__(self)
        for field in self.fields:
            assert field.name != 'what'

    def _cpp_constructor_body(self):
        fields_to_string = \
            lpad("\n", indent(' ' * 2, "\n".join(
                "oss << \"%s%s=\";\n" % (', ' if field_i > 0 else '', field.cpp_name()) + \
                    field.cpp_to_string(depth=0, oss='oss')
                for field_i, field in enumerate(self.fields)
            )))
        name = self.cpp_name()
        return """\
::std::ostringstream oss;
oss << "%(name)s(";%(fields_to_string)s
oss << ")";
what_ = oss.str();""" % locals()

    def _cpp_extends(self):
        return 'ExceptionT'

    def cpp_global_operators(self):
        return []

    def _cpp_method_what(self):
        qname = self.cpp_qname()
        return {'what': """\
virtual const char* what() const {
  return what_.c_str();
}""" % locals()}

    def _cpp_member_declarations(self):
        member_declarations = _CppCompoundType._cpp_member_declarations(self)
        member_declarations.append('::std::string what_;')
        return member_declarations

    def _cpp_methods_map(self):
        methods = _CppCompoundType._cpp_methods_map(self)
        methods.update(self._cpp_method_what())
        return methods

    def _cpp_operator_cast_to_string(self):
        return {'operator ::std::string()': """\
operator ::std::string() const {
  return what_;
}"""}

    def _cpp_template_parameters(self):
        return 'template <class ExceptionT = ::thryft::Exception>'
