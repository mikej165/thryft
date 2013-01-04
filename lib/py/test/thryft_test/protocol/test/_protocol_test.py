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
from thryft_test.protocol.test.protocol_test_enum import ProtocolTestEnum
from thryft_test.protocol.test.protocol_test_struct import ProtocolTestStruct
import unittest


class _ProtocolTest(unittest.TestCase):
    def test_bool(self):
        self._test(ProtocolTestStruct(bool_field=True))

    def test_byte(self):
        self._test(ProtocolTestStruct(byte_field=1))

#    def test_date(self):
#        self._test(ProtocolTestStruct.Builder().setDateField(DateTime.now())
#                .build());
#
#    def test_dateTime(self):
#        self._test(ProtocolTestStruct.Builder()
#                .setDateTimeField(DateTime.now()).build());

    def test_decimal(self):
        self._test(ProtocolTestStruct(decimal_field=Decimal(100)))

    def test_enum(self):
        self._test(ProtocolTestStruct(enum_field=ProtocolTestEnum.ENUMERATOR2))

    def test_i16(self):
        self._test(ProtocolTestStruct(i16_field=1))

    def test_i32(self):
        self._test(ProtocolTestStruct(i32_field=1))

    def test_i64(self):
        self._test(ProtocolTestStruct(i64_field=1l))

    def test_list_string(self):
        self._test(ProtocolTestStruct(list_string_field=('test1', 'test2')))

    def test_map_string_string(self):
        self._test(ProtocolTestStruct(map_string_string_field={'testkey': 'testvalue', 'testkey2': 'testvalue2'}))

    def test_set_string(self):
        self._test(ProtocolTestStruct(set_string_field=frozenset(('test1', 'test2'))))

    def test_string(self):
        self._test(ProtocolTestStruct(string_field='test'))

    def test_Struct(self):
        self._test(ProtocolTestStruct(struct_field=ProtocolTestStruct()))

    def _test(self, in_object):
        pass
