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

from thryft.generators.py._py_construct import _PyConstruct
from yutil import class_qname


class _PyNamedConstruct(_PyConstruct):
    def py_imports_check(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        imports = self._py_imports_check(caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return imports

    def _py_imports_check(self, caller_stack):
        raise NotImplementedError(class_qname(self) + '._py_imports_check')

    def py_imports_definition(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        imports = self._py_imports_definition(caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return imports

    def _py_imports_definition(self, caller_stack):
        raise NotImplementedError(class_qname(self) + '._py_imports_definition')

    def py_imports_use(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        imports = self._py_imports_use(caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return imports

    def _py_imports_use(self, caller_stack):
        raise NotImplementedError(class_qname(self) + '._py_imports_use')

    def py_name(self):
        return getattr(self, 'name')

    def py_qname(self):
        return self._qname(scope='py')
