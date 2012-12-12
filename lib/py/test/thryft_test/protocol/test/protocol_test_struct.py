from __future__ import absolute_import; import decimal
from datetime import datetime
from itertools import ifilterfalse
from time import mktime
import __builtin__
import thryft_test.protocol.test.protocol_test_enum


class ProtocolTestStruct(object):
    class Builder:
        def __init__(
            self,
            binary_field=None,
            bool_field=None,
            byte_field=None,
            date_field=None,
            date_time_field=None,
            decimal_field=None,
            enum_field=None,
            i16_field=None,
            i32_field=None,
            i64_field=None,
            list_string_field=None,
            map_string_string_field=None,
            set_string_field=None,
            string_field=None,
            struct_field=None
        ):
            self.__binary_field = binary_field
            self.__bool_field = bool_field
            self.__byte_field = byte_field
            self.__date_field = date_field
            self.__date_time_field = date_time_field
            self.__decimal_field = decimal_field
            self.__enum_field = enum_field
            self.__i16_field = i16_field
            self.__i32_field = i32_field
            self.__i64_field = i64_field
            self.__list_string_field = list_string_field
            self.__map_string_string_field = map_string_string_field
            self.__set_string_field = set_string_field
            self.__string_field = string_field
            self.__struct_field = struct_field

        def build(self):
            return ProtocolTestStruct(binary_field=self.__binary_field, bool_field=self.__bool_field, byte_field=self.__byte_field, date_field=self.__date_field, date_time_field=self.__date_time_field, decimal_field=self.__decimal_field, enum_field=self.__enum_field, i16_field=self.__i16_field, i32_field=self.__i32_field, i64_field=self.__i64_field, list_string_field=self.__list_string_field, map_string_string_field=self.__map_string_string_field, set_string_field=self.__set_string_field, string_field=self.__string_field, struct_field=self.__struct_field)

        def set_binary_field(self, binary_field):
            self.__binary_field = binary_field
            return self

        def set_bool_field(self, bool_field):
            self.__bool_field = bool_field
            return self

        def set_byte_field(self, byte_field):
            self.__byte_field = byte_field
            return self

        def set_date_field(self, date_field):
            self.__date_field = date_field
            return self

        def set_date_time_field(self, date_time_field):
            self.__date_time_field = date_time_field
            return self

        def set_decimal_field(self, decimal_field):
            self.__decimal_field = decimal_field
            return self

        def set_enum_field(self, enum_field):
            self.__enum_field = enum_field
            return self

        def set_i16_field(self, i16_field):
            self.__i16_field = i16_field
            return self

        def set_i32_field(self, i32_field):
            self.__i32_field = i32_field
            return self

        def set_i64_field(self, i64_field):
            self.__i64_field = i64_field
            return self

        def set_list_string_field(self, list_string_field):
            self.__list_string_field = list_string_field
            return self

        def set_map_string_string_field(self, map_string_string_field):
            self.__map_string_string_field = map_string_string_field
            return self

        def set_set_string_field(self, set_string_field):
            self.__set_string_field = set_string_field
            return self

        def set_string_field(self, string_field):
            self.__string_field = string_field
            return self

        def set_struct_field(self, struct_field):
            self.__struct_field = struct_field
            return self

        def update(self, protocol_test_struct):
            if isinstance(protocol_test_struct, ProtocolTestStruct):
                self.set_binary_field(protocol_test_struct.binary_field)
                self.set_bool_field(protocol_test_struct.bool_field)
                self.set_byte_field(protocol_test_struct.byte_field)
                self.set_date_field(protocol_test_struct.date_field)
                self.set_date_time_field(protocol_test_struct.date_time_field)
                self.set_decimal_field(protocol_test_struct.decimal_field)
                self.set_enum_field(protocol_test_struct.enum_field)
                self.set_i16_field(protocol_test_struct.i16_field)
                self.set_i32_field(protocol_test_struct.i32_field)
                self.set_i64_field(protocol_test_struct.i64_field)
                self.set_list_string_field(protocol_test_struct.list_string_field)
                self.set_map_string_string_field(protocol_test_struct.map_string_string_field)
                self.set_set_string_field(protocol_test_struct.set_string_field)
                self.set_string_field(protocol_test_struct.string_field)
                self.set_struct_field(protocol_test_struct.struct_field)
            elif isinstance(protocol_test_struct, dict):
                for key, value in protocol_test_struct.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(protocol_test_struct)
            return self

    def __init__(
        self,
        binary_field=None,
        bool_field=None,
        byte_field=None,
        date_field=None,
        date_time_field=None,
        decimal_field=None,
        enum_field=None,
        i16_field=None,
        i32_field=None,
        i64_field=None,
        list_string_field=None,
        map_string_string_field=None,
        set_string_field=None,
        string_field=None,
        struct_field=None
    ):
        if binary_field is not None:
            if not isinstance(binary_field, basestring):
                raise TypeError(getattr(__builtin__, 'type')(binary_field))
        self.__binary_field = binary_field

        if bool_field is not None:
            if not isinstance(bool_field, bool):
                raise TypeError(getattr(__builtin__, 'type')(bool_field))
        self.__bool_field = bool_field

        if byte_field is not None:
            if not isinstance(byte_field, int):
                raise TypeError(getattr(__builtin__, 'type')(byte_field))
        self.__byte_field = byte_field

        if date_field is not None:
            if not isinstance(date_field, datetime):
                raise TypeError(getattr(__builtin__, 'type')(date_field))
        self.__date_field = date_field

        if date_time_field is not None:
            if not isinstance(date_time_field, datetime):
                raise TypeError(getattr(__builtin__, 'type')(date_time_field))
        self.__date_time_field = date_time_field

        if decimal_field is not None:
            if not isinstance(decimal_field, decimal.Decimal):
                raise TypeError(getattr(__builtin__, 'type')(decimal_field))
        self.__decimal_field = decimal_field

        if enum_field is not None:
            if not isinstance(enum_field, thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum):
                raise TypeError(getattr(__builtin__, 'type')(enum_field))
        self.__enum_field = enum_field

        if i16_field is not None:
            if not isinstance(i16_field, int):
                raise TypeError(getattr(__builtin__, 'type')(i16_field))
        self.__i16_field = i16_field

        if i32_field is not None:
            if not isinstance(i32_field, int):
                raise TypeError(getattr(__builtin__, 'type')(i32_field))
        self.__i32_field = i32_field

        if i64_field is not None:
            if not isinstance(i64_field, (int, long)):
                raise TypeError(getattr(__builtin__, 'type')(i64_field))
        self.__i64_field = i64_field

        if list_string_field is not None:
            if not (isinstance(list_string_field, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), list_string_field))) == 0):
                raise TypeError(getattr(__builtin__, 'type')(list_string_field))
        self.__list_string_field = list_string_field

        if map_string_string_field is not None:
            if not (isinstance(map_string_string_field, dict) and len(list(ifilterfalse(lambda __item: isinstance(__item[0], basestring) and isinstance(__item[1], basestring), map_string_string_field.iteritems()))) == 0):
                raise TypeError(getattr(__builtin__, 'type')(map_string_string_field))
        self.__map_string_string_field = map_string_string_field.copy() if map_string_string_field is not None else None

        if set_string_field is not None:
            if not (isinstance(set_string_field, frozenset) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), set_string_field))) == 0):
                raise TypeError(getattr(__builtin__, 'type')(set_string_field))
        self.__set_string_field = set_string_field

        if string_field is not None:
            if not isinstance(string_field, basestring):
                raise TypeError(getattr(__builtin__, 'type')(string_field))
        self.__string_field = string_field

        if struct_field is not None:
            if not isinstance(struct_field, thryft_test.protocol.test.protocol_test_struct.ProtocolTestStruct):
                raise TypeError(getattr(__builtin__, 'type')(struct_field))
        self.__struct_field = struct_field

    def __eq__(self, other):
        if self.binary_field != other.binary_field:
            return False
        if self.bool_field != other.bool_field:
            return False
        if self.byte_field != other.byte_field:
            return False
        if self.date_field != other.date_field:
            return False
        if self.date_time_field != other.date_time_field:
            return False
        if self.decimal_field != other.decimal_field:
            return False
        if self.enum_field != other.enum_field:
            return False
        if self.i16_field != other.i16_field:
            return False
        if self.i32_field != other.i32_field:
            return False
        if self.i64_field != other.i64_field:
            return False
        if self.list_string_field != other.list_string_field:
            return False
        if self.map_string_string_field != other.map_string_string_field:
            return False
        if self.set_string_field != other.set_string_field:
            return False
        if self.string_field != other.string_field:
            return False
        if self.struct_field != other.struct_field:
            return False
        return True

    def __hash__(self):
        return hash((self.binary_field,self.bool_field,self.byte_field,self.date_field,self.date_time_field,self.decimal_field,self.enum_field,self.i16_field,self.i32_field,self.i64_field,self.list_string_field,self.map_string_string_field,self.set_string_field,self.string_field,self.struct_field,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        if self.binary_field is not None:
            field_reprs.append('binary_field=' + "'" + self.binary_field.encode('ascii', 'replace') + "'")
        if self.bool_field is not None:
            field_reprs.append('bool_field=' + repr(self.bool_field))
        if self.byte_field is not None:
            field_reprs.append('byte_field=' + repr(self.byte_field))
        if self.date_field is not None:
            field_reprs.append('date_field=' + repr(self.date_field))
        if self.date_time_field is not None:
            field_reprs.append('date_time_field=' + repr(self.date_time_field))
        if self.decimal_field is not None:
            field_reprs.append('decimal_field=' + repr(self.decimal_field))
        if self.enum_field is not None:
            field_reprs.append('enum_field=' + repr(self.enum_field))
        if self.i16_field is not None:
            field_reprs.append('i16_field=' + repr(self.i16_field))
        if self.i32_field is not None:
            field_reprs.append('i32_field=' + repr(self.i32_field))
        if self.i64_field is not None:
            field_reprs.append('i64_field=' + repr(self.i64_field))
        if self.list_string_field is not None:
            field_reprs.append('list_string_field=' + repr(self.list_string_field))
        if self.map_string_string_field is not None:
            field_reprs.append('map_string_string_field=' + repr(self.map_string_string_field))
        if self.set_string_field is not None:
            field_reprs.append('set_string_field=' + repr(self.set_string_field))
        if self.string_field is not None:
            field_reprs.append('string_field=' + "'" + self.string_field.encode('ascii', 'replace') + "'")
        if self.struct_field is not None:
            field_reprs.append('struct_field=' + repr(self.struct_field))
        return 'ProtocolTestStruct(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        if self.binary_field is not None:
            field_reprs.append('binary_field=' + "'" + self.binary_field.encode('ascii', 'replace') + "'")
        if self.bool_field is not None:
            field_reprs.append('bool_field=' + repr(self.bool_field))
        if self.byte_field is not None:
            field_reprs.append('byte_field=' + repr(self.byte_field))
        if self.date_field is not None:
            field_reprs.append('date_field=' + repr(self.date_field))
        if self.date_time_field is not None:
            field_reprs.append('date_time_field=' + repr(self.date_time_field))
        if self.decimal_field is not None:
            field_reprs.append('decimal_field=' + repr(self.decimal_field))
        if self.enum_field is not None:
            field_reprs.append('enum_field=' + repr(self.enum_field))
        if self.i16_field is not None:
            field_reprs.append('i16_field=' + repr(self.i16_field))
        if self.i32_field is not None:
            field_reprs.append('i32_field=' + repr(self.i32_field))
        if self.i64_field is not None:
            field_reprs.append('i64_field=' + repr(self.i64_field))
        if self.list_string_field is not None:
            field_reprs.append('list_string_field=' + repr(self.list_string_field))
        if self.map_string_string_field is not None:
            field_reprs.append('map_string_string_field=' + repr(self.map_string_string_field))
        if self.set_string_field is not None:
            field_reprs.append('set_string_field=' + repr(self.set_string_field))
        if self.string_field is not None:
            field_reprs.append('string_field=' + "'" + self.string_field.encode('ascii', 'replace') + "'")
        if self.struct_field is not None:
            field_reprs.append('struct_field=' + repr(self.struct_field))
        return 'ProtocolTestStruct(' + ', '.join(field_reprs) + ')'

    def as_dict(self):
        return {'binary_field': self.binary_field, 'bool_field': self.bool_field, 'byte_field': self.byte_field, 'date_field': self.date_field, 'date_time_field': self.date_time_field, 'decimal_field': self.decimal_field, 'enum_field': self.enum_field, 'i16_field': self.i16_field, 'i32_field': self.i32_field, 'i64_field': self.i64_field, 'list_string_field': self.list_string_field, 'map_string_string_field': self.map_string_string_field, 'set_string_field': self.set_string_field, 'string_field': self.string_field, 'struct_field': self.struct_field}

    @property
    def binary_field(self):
        return self.__binary_field

    @property
    def bool_field(self):
        return self.__bool_field

    @property
    def byte_field(self):
        return self.__byte_field

    @property
    def date_field(self):
        return self.__date_field

    @property
    def date_time_field(self):
        return self.__date_time_field

    @property
    def decimal_field(self):
        return self.__decimal_field

    @property
    def enum_field(self):
        return self.__enum_field

    @property
    def i16_field(self):
        return self.__i16_field

    @property
    def i32_field(self):
        return self.__i32_field

    @property
    def i64_field(self):
        return self.__i64_field

    @property
    def list_string_field(self):
        return self.__list_string_field

    @property
    def map_string_string_field(self):
        return self.__map_string_string_field.copy() if self.__map_string_string_field is not None else None

    @classmethod
    def read(cls, iprot):
        init_kwds = {}

        iprot.readStructBegin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.readFieldBegin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'binary_field':
                try:
                    init_kwds['binary_field'] = iprot.readBinary()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'bool_field':
                try:
                    init_kwds['bool_field'] = iprot.readBool()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'byte_field':
                try:
                    init_kwds['byte_field'] = iprot.readByte()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'date_field':
                try:
                    init_kwds['date_field'] = iprot.readDateTime() if hasattr(iprot, 'readDateTime') else datetime.fromtimestamp(iprot.readI64() / 1000.0)
                except (TypeError,):
                    pass
            elif ifield_name == 'date_time_field':
                try:
                    init_kwds['date_time_field'] = iprot.readDateTime() if hasattr(iprot, 'readDateTime') else datetime.fromtimestamp(iprot.readI64() / 1000.0)
                except (TypeError,):
                    pass
            elif ifield_name == 'decimal_field':
                try:
                    init_kwds['decimal_field'] = iprot.readDecimal() if hasattr(iprot, 'readDecimal') else decimal.Decimal(iprot.readString())
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'enum_field':
                try:
                    init_kwds['enum_field'] = thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum.value_of(iprot.readString().strip().upper())
                except (TypeError,):
                    pass
            elif ifield_name == 'i16_field':
                try:
                    init_kwds['i16_field'] = iprot.readI16()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i32_field':
                try:
                    init_kwds['i32_field'] = iprot.readI32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i64_field':
                try:
                    init_kwds['i64_field'] = iprot.readI64()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'list_string_field':
                init_kwds['list_string_field'] = tuple([iprot.readString() for _ in xrange(iprot.readListBegin()[1])] + (iprot.readListEnd() is None and []))
            elif ifield_name == 'map_string_string_field':
                init_kwds['map_string_string_field'] = dict([(iprot.readString(), iprot.readString()) for _ in xrange(iprot.readMapBegin()[2])] + (iprot.readMapEnd() is None and []))
            elif ifield_name == 'set_string_field':
                init_kwds['set_string_field'] = frozenset([iprot.readString() for _ in xrange(iprot.readSetBegin()[1])] + (iprot.readSetEnd() is None and []))
            elif ifield_name == 'string_field':
                try:
                    init_kwds['string_field'] = iprot.readString()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'struct_field':
                init_kwds['struct_field'] = thryft_test.protocol.test.protocol_test_struct.ProtocolTestStruct.read(iprot)
            iprot.readFieldEnd()
        iprot.readStructEnd()

        return cls(**init_kwds)

    def replace(self, binary_field=None, bool_field=None, byte_field=None, date_field=None, date_time_field=None, decimal_field=None, enum_field=None, i16_field=None, i32_field=None, i64_field=None, list_string_field=None, map_string_string_field=None, set_string_field=None, string_field=None, struct_field=None):
        if binary_field is None:
            binary_field = self.binary_field
        if bool_field is None:
            bool_field = self.bool_field
        if byte_field is None:
            byte_field = self.byte_field
        if date_field is None:
            date_field = self.date_field
        if date_time_field is None:
            date_time_field = self.date_time_field
        if decimal_field is None:
            decimal_field = self.decimal_field
        if enum_field is None:
            enum_field = self.enum_field
        if i16_field is None:
            i16_field = self.i16_field
        if i32_field is None:
            i32_field = self.i32_field
        if i64_field is None:
            i64_field = self.i64_field
        if list_string_field is None:
            list_string_field = self.list_string_field
        if map_string_string_field is None:
            map_string_string_field = self.map_string_string_field
        if set_string_field is None:
            set_string_field = self.set_string_field
        if string_field is None:
            string_field = self.string_field
        if struct_field is None:
            struct_field = self.struct_field
        return self.__class__(binary_field=binary_field, bool_field=bool_field, byte_field=byte_field, date_field=date_field, date_time_field=date_time_field, decimal_field=decimal_field, enum_field=enum_field, i16_field=i16_field, i32_field=i32_field, i64_field=i64_field, list_string_field=list_string_field, map_string_string_field=map_string_string_field, set_string_field=set_string_field, string_field=string_field, struct_field=struct_field)

    @property
    def set_string_field(self):
        return self.__set_string_field

    @property
    def string_field(self):
        return self.__string_field

    @property
    def struct_field(self):
        return self.__struct_field

    def write(self, oprot):
        oprot.writeStructBegin('ProtocolTestStruct')

        if self.binary_field is not None:
            oprot.writeFieldBegin('binary_field', 11, -1)
            oprot.writeBinary(self.binary_field)
            oprot.writeFieldEnd()

        if self.bool_field is not None:
            oprot.writeFieldBegin('bool_field', 2, -1)
            oprot.writeBool(self.bool_field)
            oprot.writeFieldEnd()

        if self.byte_field is not None:
            oprot.writeFieldBegin('byte_field', 3, -1)
            oprot.writeByte(self.byte_field)
            oprot.writeFieldEnd()

        if self.date_field is not None:
            oprot.writeFieldBegin('date_field', 12, -1)
            oprot.writeDateTime(self.date_field) if hasattr(oprot, 'writeDateTime') else oprot.writeI64(long(mktime(self.date_field.timetuple())) * 1000l)
            oprot.writeFieldEnd()

        if self.date_time_field is not None:
            oprot.writeFieldBegin('date_time_field', 12, -1)
            oprot.writeDateTime(self.date_time_field) if hasattr(oprot, 'writeDateTime') else oprot.writeI64(long(mktime(self.date_time_field.timetuple())) * 1000l)
            oprot.writeFieldEnd()

        if self.decimal_field is not None:
            oprot.writeFieldBegin('decimal_field', 12, -1)
            oprot.writeDecimal(self.decimal_field) if hasattr(oprot, 'writeDecimal') else oprot.writeString(str(self.decimal_field))
            oprot.writeFieldEnd()

        if self.enum_field is not None:
            oprot.writeFieldBegin('enum_field', 11, -1)
            oprot.writeString([attr for attr in dir(thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum) if getattr(thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum, attr) == self.enum_field][0])
            oprot.writeFieldEnd()

        if self.i16_field is not None:
            oprot.writeFieldBegin('i16_field', 6, -1)
            oprot.writeI16(self.i16_field)
            oprot.writeFieldEnd()

        if self.i32_field is not None:
            oprot.writeFieldBegin('i32_field', 8, -1)
            oprot.writeI32(self.i32_field)
            oprot.writeFieldEnd()

        if self.i64_field is not None:
            oprot.writeFieldBegin('i64_field', 10, -1)
            oprot.writeI64(self.i64_field)
            oprot.writeFieldEnd()

        if self.list_string_field is not None:
            oprot.writeFieldBegin('list_string_field', 15, -1)
            oprot.writeListBegin(11, len(self.list_string_field))
            for _0 in self.list_string_field:
                oprot.writeString(_0)
            oprot.writeListEnd()
            oprot.writeFieldEnd()

        if self.map_string_string_field is not None:
            oprot.writeFieldBegin('map_string_string_field', 13, -1)
            oprot.writeMapBegin(11, len(self.map_string_string_field), 11)
            for __key0, __value0 in self.map_string_string_field.iteritems():
                oprot.writeString(__key0)
                oprot.writeString(__value0)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()

        if self.set_string_field is not None:
            oprot.writeFieldBegin('set_string_field', 14, -1)
            oprot.writeSetBegin(11, len(self.set_string_field))
            for _0 in self.set_string_field:
                oprot.writeString(_0)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()

        if self.string_field is not None:
            oprot.writeFieldBegin('string_field', 11, -1)
            oprot.writeString(self.string_field)
            oprot.writeFieldEnd()

        if self.struct_field is not None:
            oprot.writeFieldBegin('struct_field', 12, -1)
            self.struct_field.write(oprot)
            oprot.writeFieldEnd()

        oprot.writeFieldStop()

        oprot.writeStructEnd()

        return self
