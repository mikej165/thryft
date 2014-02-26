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

from decimal import Decimal
from thryft.protocol._input_protocol import _InputProtocol


class BuiltinsInputProtocol(_InputProtocol):
    class _Scope(object):
        def __init__(self, builtin_object, name_stack):
            self._builtin_object = builtin_object
            self._name_stack = name_stack

        @property
        def builtin_object(self):
            return self._builtin_object

        def readFieldBegin(self):
            if len(self._name_stack) == 0:
                return None, 0, None  # STOP
            assert isinstance(self._name_stack[-1], basestring), self._name_stack
            return self._name_stack[-1], None, None

        def readFieldEnd(self):
            self._name_stack.pop(-1)

        def readValue(self, expected_type=None):
            value = self._readValue()
            if expected_type is not None and not isinstance(value, expected_type):
                raise TypeError("expected %s, got %s" % (expected_type, type(value)))
            return value

        def _readValue(self):
            raise NotImplementedError

    class _ListScope(_Scope):
        def __init__(self, list_):
            if not isinstance(list_, (list, tuple)):
                raise TypeError(type(list_))
            BuiltinsInputProtocol._Scope.__init__(self, list_, list(reversed(xrange(len(list_)))))

        def _readValue(self):
            return self.builtin_object[self._name_stack.pop(-1)]

    class _MapScope(_Scope):
        def __init__(self, dict_):
            if not isinstance(dict_, dict):
                raise TypeError(type(dict_))
            BuiltinsInputProtocol._Scope.__init__(self, dict_, list(reversed(sorted(dict_.keys()))))
            self.__next_value_is_key = True

        def _readValue(self):
            if self.__next_value_is_key:
                self.__next_value_is_key = False
                return self._name_stack[-1]
            else:
                self.__next_value_is_key = True
                return self.builtin_object[self._name_stack.pop(-1)]

    class _StructScope(_MapScope):
        def _readValue(self):
            return self.builtin_object[self._name_stack[-1]]

    def __init__(self, root_builtin_object=None):
        _InputProtocol.__init__(self)
        self._scope_stack = []
        if root_builtin_object is not None:
            if isinstance(root_builtin_object, dict):
                self._scope_stack.append(self._StructScope(root_builtin_object))
            elif isinstance(root_builtin_object, (list, tuple)):
                self._scope_stack.append(self._ListScope(root_builtin_object))
            else:
                raise TypeError(type(root_builtin_object))

    def readFieldBegin(self):
        return self._scope_stack[-1].readFieldBegin()

    def readBool(self):
        return self._scope_stack[-1].readValue(bool)

    def readI32(self):
        return int(self._scope_stack[-1].readValue((Decimal, int)))

    def readI64(self):
        return long(self._scope_stack[-1].readValue((Decimal, int, long)))

    def readFieldEnd(self):
        self._scope_stack[-1].readFieldEnd()

    def readListBegin(self):
        list_ = self._scope_stack[-1].readValue(list)
        self._scope_stack.append(self._ListScope(list_))
        return None, len(list_)

    def readListEnd(self):
        self._scope_stack.pop(-1)

    def readMapBegin(self):
        map_ = self._scope_stack[-1].readValue(dict)
        self._scope_stack.append(self._MapScope(map_))
        return None, None, len(map_)

    def readMapEnd(self):
        self._scope_stack.pop(-1)

    def readSetBegin(self):
        return self.readListBegin()

    def readSetEnd(self):
        return self.readListEnd()

    def readString(self):
        return self._scope_stack[-1].readValue((Decimal, float, str, unicode))

    def readStructBegin(self):
        struct = self._scope_stack[-1].readValue(dict)
        self._scope_stack.append(self._StructScope(struct))

    def readStructEnd(self):
        self._scope_stack.pop(-1)
