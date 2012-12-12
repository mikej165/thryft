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
