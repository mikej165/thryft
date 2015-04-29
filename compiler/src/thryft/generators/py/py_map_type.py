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

from thryft.generator.map_type import MapType
from thryft.generators.py._py_container_type import _PyContainerType
from yutil import indent


class PyMapType(MapType, _PyContainerType):
    def py_check(self, value):
        key_check = self.key_type.py_check('__item[0]')
        value_check = self.value_type.py_check('__item[1]')
        return "(isinstance(%(value)s, dict) and len(list(ifilterfalse(lambda __item: %(key_check)s and %(value_check)s, %(value)s.iteritems()))) == 0)" % locals()

    def py_defensive_copy(self, value):
        return "%(value)s.copy() if %(value)s is not None else None" % locals()

    def _py_imports_definition(self, caller_stack):
        imports = list(self.key_type.py_imports_definition(caller_stack=caller_stack))
        imports.extend(self.value_type.py_imports_definition(caller_stack=caller_stack))
        imports.append('from itertools import ifilterfalse')
        return imports

    def py_literal(self, value):
        return "{%s}" % ', '.join(self.key_type.py_literal(key) + ':' + self.value_type.py_literal(value_) for key, value_ in value.iteritems())

    def py_name(self):
        return 'dict'

    def py_read_protocol(self):
        key_read_protocol = self.key_type.py_read_protocol()
        value_read_protocol = self.value_type.py_read_protocol()
        return """dict([(%(key_read_protocol)s, %(value_read_protocol)s) for _ in xrange(iprot.read_map_begin()[2])] + (iprot.read_map_end() is None and []))""" % locals()

    def py_write_protocol(self, value, depth=0):
        key_ttype_id = self.key_type.thrift_ttype_id()
        key_write_protocol = \
            indent(' ' * 4,
                self.key_type.py_write_protocol(
                    "__key%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        value_ttype_id = self.value_type.thrift_ttype_id()
        value_write_protocol = \
            indent(' ' * 4,
                self.value_type.py_write_protocol(
                    "__value%(depth)u" % locals(),
                    depth=depth + 1
                )
            )
        return """\
oprot.write_map_begin(%(key_ttype_id)u, len(%(value)s), %(value_ttype_id)u)
for __key%(depth)u, __value%(depth)u in %(value)s.iteritems():
%(key_write_protocol)s
%(value_write_protocol)s
oprot.write_map_end()""" % locals()
