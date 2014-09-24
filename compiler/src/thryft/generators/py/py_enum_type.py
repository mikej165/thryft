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

from thryft.generator.enum_type import EnumType
from thryft.generators.py._py_type import _PyType
from yutil import indent, lpad, pad


class PyEnumType(EnumType, _PyType):
    def py_check(self, value):
        qname = self.py_qname()
        return "isinstance(%(value)s, %(qname)s)" % locals()

    def _py_imports_use(self, caller_stack):
        return ['import ' + self.py_qname().rsplit('.', 1)[0]]

    def py_read_protocol(self):
        qname = self.py_qname()
        return "%(qname)s.value_of(iprot.read_string().strip().upper())" % locals()

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.write_string(str(%(value)s))" % locals()

    def __repr__(self):
        name = self.py_name()

        enumerators = []
        enumerator_placeholders = []
        value_of_statements = []
        if len(self.enumerators) > 0:
            for enumerator in self.enumerators:
                enumerator_name = enumerator.name
                enumerator_value = enumerator.value
                enumerator_placeholders.append("%(enumerator_name)s = None" % locals())
                enumerators.append("%(name)s.%(enumerator_name)s = %(name)s('%(enumerator_name)s', %(enumerator_value)u)" % locals())
                value_of_statements.append("""\
if name == '%(enumerator_name)s' or name == '%(enumerator_value)u':
    return getattr(%(name)s, '%(enumerator_name)s')
""" % locals())
        enumerators = \
            lpad("\n\n", "\n".join(enumerators))
        enumerator_placeholders = \
            pad("\n", "\n".join(indent(' ' * 4,
                enumerator_placeholders
            )), "\n")
        value_of_statements = \
            lpad("\n", indent(' ' * 8, 'el'.join(value_of_statements)))
        return """\
class %(name)s(object):%(enumerator_placeholders)s
    def __init__(self, name, value):
        object.__init__(self)
        self.__name = name
        self.__value = value

    def __int__(self):
        return self.__value

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name

    @classmethod
    def value_of(cls, name):%(value_of_statements)s
        raise ValueError(name)%(enumerators)s""" % locals()
