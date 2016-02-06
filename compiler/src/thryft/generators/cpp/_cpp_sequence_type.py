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

from thryft.generators.cpp._cpp_container_type import _CppContainerType
from yutil import indent


class _CppSequenceType(_CppContainerType):
    def cpp_includes_use(self):
        includes = ['<thryft.hpp>']
        includes.extend(self.element_type.cpp_includes_use())
        return includes

    def cpp_literal(self, value):
        return self.cpp_qname() + '()'

    def cpp_qname(self):
        return \
            "::thryft::%s< %s, ::thryft::protocol::Type::%s >" % (
                self._thrift_name(),
                self.element_type.cpp_qname(),
                self.element_type.thrift_ttype_name()
            )

    def cpp_to_string(self, depth, oss, value):
        element_to_string = \
            indent(' ' * 2,
                   self.element_type.cpp_to_string(
                       depth=depth+1,
                       oss=oss,
                       value="*i%(depth)u" % locals()
                    )
            )
        qname = self.cpp_qname()
        return """\
oss << "[";
for (%(qname)s::const_iterator i%(depth)u = %(value)s.begin(); i%(depth)u != %(value)s.end(); ++i%(depth)u) {
  if (i%(depth)u != %(value)s.begin()) {
    oss << ", ";
  }
%(element_to_string)s
}
oss << "]";""" % locals()
