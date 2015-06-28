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

from thryft.generator.service import Service
from thryft.generators.py._py_named_construct import _PyNamedConstruct
from yutil import indent


class PyService(Service, _PyNamedConstruct):
    def _py_extends(self):
        return ['object']

    def py_imports_definition(self, caller_stack=None):
        imports = []
        for function in self.functions:
            imports.extend(function.py_imports_definition(caller_stack=caller_stack))
        return imports

    def _py_imports_use(self, caller_stack):
        raise NotImplementedError

    def _py_methods(self):
        methods = []
        for function in self.functions:
            methods.append(function.py_public_delegating_definition())
            methods.append(function.py_protected_abstract_definition())
        return methods

    def py_qname(self):
        return self._qname(scope='py', name=self.name)

    def py_repr(self):
        extends = ', '.join(self._py_extends())

        name = self.py_name()

        if len(self.functions) == 0:
            return """\
class %(name)s(%(extends)s):
    pass
""" % locals()

        methods = "\n\n".join(indent(' ' * 4, self._py_methods()))

        return """\
class %(name)s(%(extends)s):
%(methods)s""" % locals()
