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

from thryft.generator.service import Service
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct
from yutil import indent, lpad


class CppService(Service, _CppNamedConstruct):
    def cpp_includes_definition(self):
        includes = []
        for function in self.functions:
            includes.extend(function.cpp_includes_definition())
        return includes

    def cpp_extends(self):
        return self.extends

    def cpp_name(self, boxed=False):
        return self.name

    def cpp_qname(self, boxed=False):
        return _CppNamedConstruct.cpp_qname(self, name=self.name)

    def __repr__(self):
        extends = self.cpp_extends()
        if extends is None:
            extends = ''
        else:
            extends = ' : public ' + extends

        name = self.cpp_name()

        sections = []

        sections.append(
                indent(' ' * 2,
                    "\n\n".join(function.cpp_pure_virtual_declaration()
                                for function in self.functions)))

        sections = lpad("\n\n", "\n\n".join(sections))

        return """\
class %(name)s%(extends)s {
public:
  virtual ~%(name)s() {
  }%(sections)s
};""" % locals()
