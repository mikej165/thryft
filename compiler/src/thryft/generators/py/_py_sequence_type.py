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

from thryft.generators.py._py_container_type import _PyContainerType
from yutil import indent


class _PySequenceType(_PyContainerType):
    def py_from_string(self, value):
        element_from_string = self.element_type.py_from_string('e')
        name = self._py_name()
        return "%(name)s(%(element_from_string)s for e in %(value)s.split(','))" % locals()

#     def _py_imports_definition(self, caller_stack):
#         return self.element_type.py_imports_definition(caller_stack=caller_stack) + \
#                ['from itertools import ifilterfalse']

    def _py_imports_check(self, caller_stack):
        return self.element_type.py_imports_check(caller_stack=caller_stack) + ['from itertools import ifilterfalse']

    def _py_imports_use(self, caller_stack):
        return []

    def py_name(self):
        return self._py_name()

    def _py_name(self):
        raise NotImplementedError

    def py_write_protocol(self, value, depth=0):
        element_ttype_id = self.element_type.thrift_ttype_id()
        element_write_protocol = \
            indent(' ' * 4,
                self.element_type.py_write_protocol(
                    "_%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        from thryft.generators.py.py_set_type import PySetType
        type_name = 'set' if isinstance(self, PySetType) else 'list'
        return """\
oprot.write_%(type_name)s_begin(%(element_ttype_id)u, len(%(value)s))
for _%(depth)u in %(value)s:
%(element_write_protocol)s
oprot.write_%(type_name)s_end()""" % locals()
