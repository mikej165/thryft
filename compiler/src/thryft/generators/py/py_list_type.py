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

from thryft.generator.list_type import ListType
from thryft.generators.py._py_sequence_type import _PySequenceType


class PyListType(ListType, _PySequenceType):
    def py_check(self, value):
        element_check = self.element_type.py_check('_')
        return "(isinstance(%(value)s, tuple) and len(list(ifilterfalse(lambda _: %(element_check)s, %(value)s))) == 0)" % locals()

    def py_description(self):
        return "tuple(%s)" % self.element_type.py_description()

    def py_literal(self, value):
        if len(value) == 0:
            return 'tuple()'
        return "(%s,)" % ', '.join(self.element_type.py_literal(element_value) for element_value in value)

    def _py_name(self):
        return 'tuple'

    def py_read_protocol(self):
        element_read_protocol = self.element_type.py_read_protocol()
        return """tuple([%(element_read_protocol)s for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))""" % locals()
