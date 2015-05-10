from __future__ import absolute_import; import decimal
from datetime import datetime
from itertools import ifilterfalse
import __builtin__
import thryft_test.protocol.test.protocol_test_enum


class NestedProtocolTestStruct(object):
    class Builder:
        def __init__(
            self,
            required_i32_field=None,
            required_string_field=None,
            binary_field=None,
            bool_field=None,
            byte_field=None,
            date_time_field=None,
            decimal_field=None,
            email_address_field=None,
            enum_field=None,
            i16_field=None,
            i32_field=None,
            i64_field=None,
            string_list_field=None,
            string_string_map_field=None,
            string_set_field=None,
            string_field=None,
            url_field=None
        ):
            self.__required_i32_field = required_i32_field
            self.__required_string_field = required_string_field
            self.__binary_field = binary_field
            self.__bool_field = bool_field
            self.__byte_field = byte_field
            self.__date_time_field = date_time_field
            self.__decimal_field = decimal_field
            self.__email_address_field = email_address_field
            self.__enum_field = enum_field
            self.__i16_field = i16_field
            self.__i32_field = i32_field
            self.__i64_field = i64_field
            self.__string_list_field = string_list_field
            self.__string_string_map_field = string_string_map_field
            self.__string_set_field = string_set_field
            self.__string_field = string_field
            self.__url_field = url_field

        def build(self):
            return NestedProtocolTestStruct(required_i32_field=self.__required_i32_field, required_string_field=self.__required_string_field, binary_field=self.__binary_field, bool_field=self.__bool_field, byte_field=self.__byte_field, date_time_field=self.__date_time_field, decimal_field=self.__decimal_field, email_address_field=self.__email_address_field, enum_field=self.__enum_field, i16_field=self.__i16_field, i32_field=self.__i32_field, i64_field=self.__i64_field, string_list_field=self.__string_list_field, string_string_map_field=self.__string_string_map_field, string_set_field=self.__string_set_field, string_field=self.__string_field, url_field=self.__url_field)

        def set_binary_field(self, binary_field):
            self.__binary_field = binary_field
            return self

        def set_bool_field(self, bool_field):
            self.__bool_field = bool_field
            return self

        def set_byte_field(self, byte_field):
            self.__byte_field = byte_field
            return self

        def set_date_time_field(self, date_time_field):
            self.__date_time_field = date_time_field
            return self

        def set_decimal_field(self, decimal_field):
            self.__decimal_field = decimal_field
            return self

        def set_email_address_field(self, email_address_field):
            self.__email_address_field = email_address_field
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

        def set_required_i32_field(self, required_i32_field):
            self.__required_i32_field = required_i32_field
            return self

        def set_required_string_field(self, required_string_field):
            self.__required_string_field = required_string_field
            return self

        def set_string_field(self, string_field):
            self.__string_field = string_field
            return self

        def set_string_list_field(self, string_list_field):
            self.__string_list_field = string_list_field
            return self

        def set_string_set_field(self, string_set_field):
            self.__string_set_field = string_set_field
            return self

        def set_string_string_map_field(self, string_string_map_field):
            self.__string_string_map_field = string_string_map_field
            return self

        def set_url_field(self, url_field):
            self.__url_field = url_field
            return self

        def update(self, nested_protocol_test_struct):
            if isinstance(nested_protocol_test_struct, NestedProtocolTestStruct):
                self.set_required_i32_field(nested_protocol_test_struct.required_i32_field)
                self.set_required_string_field(nested_protocol_test_struct.required_string_field)
                self.set_binary_field(nested_protocol_test_struct.binary_field)
                self.set_bool_field(nested_protocol_test_struct.bool_field)
                self.set_byte_field(nested_protocol_test_struct.byte_field)
                self.set_date_time_field(nested_protocol_test_struct.date_time_field)
                self.set_decimal_field(nested_protocol_test_struct.decimal_field)
                self.set_email_address_field(nested_protocol_test_struct.email_address_field)
                self.set_enum_field(nested_protocol_test_struct.enum_field)
                self.set_i16_field(nested_protocol_test_struct.i16_field)
                self.set_i32_field(nested_protocol_test_struct.i32_field)
                self.set_i64_field(nested_protocol_test_struct.i64_field)
                self.set_string_list_field(nested_protocol_test_struct.string_list_field)
                self.set_string_string_map_field(nested_protocol_test_struct.string_string_map_field)
                self.set_string_set_field(nested_protocol_test_struct.string_set_field)
                self.set_string_field(nested_protocol_test_struct.string_field)
                self.set_url_field(nested_protocol_test_struct.url_field)
            elif isinstance(nested_protocol_test_struct, dict):
                for key, value in nested_protocol_test_struct.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(nested_protocol_test_struct)
            return self

    def __init__(
        self,
        required_i32_field,
        required_string_field,
        binary_field=None,
        bool_field=None,
        byte_field=None,
        date_time_field=None,
        decimal_field=None,
        email_address_field=None,
        enum_field=None,
        i16_field=None,
        i32_field=None,
        i64_field=None,
        string_list_field=None,
        string_string_map_field=None,
        string_set_field=None,
        string_field=None,
        url_field=None
    ):
        if required_i32_field is None:
            raise ValueError('required_i32_field is required')
        if not isinstance(required_i32_field, int):
            raise TypeError(getattr(__builtin__, 'type')(required_i32_field))
        self.__required_i32_field = required_i32_field

        if required_string_field is None:
            raise ValueError('required_string_field is required')
        if not isinstance(required_string_field, basestring):
            raise TypeError(getattr(__builtin__, 'type')(required_string_field))
        self.__required_string_field = required_string_field

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

        if date_time_field is not None:
            if not isinstance(date_time_field, datetime):
                raise TypeError(getattr(__builtin__, 'type')(date_time_field))
        self.__date_time_field = date_time_field

        if decimal_field is not None:
            if not isinstance(decimal_field, decimal.Decimal):
                raise TypeError(getattr(__builtin__, 'type')(decimal_field))
        self.__decimal_field = decimal_field

        if email_address_field is not None:
            if not isinstance(email_address_field, basestring):
                raise TypeError(getattr(__builtin__, 'type')(email_address_field))
        self.__email_address_field = email_address_field

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

        if string_list_field is not None:
            if not (isinstance(string_list_field, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), string_list_field))) == 0):
                raise TypeError(getattr(__builtin__, 'type')(string_list_field))
        self.__string_list_field = string_list_field

        if string_string_map_field is not None:
            if not (isinstance(string_string_map_field, dict) and len(list(ifilterfalse(lambda __item: isinstance(__item[0], basestring) and isinstance(__item[1], basestring), string_string_map_field.iteritems()))) == 0):
                raise TypeError(getattr(__builtin__, 'type')(string_string_map_field))
        self.__string_string_map_field = string_string_map_field.copy() if string_string_map_field is not None else None

        if string_set_field is not None:
            if not (isinstance(string_set_field, frozenset) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), string_set_field))) == 0):
                raise TypeError(getattr(__builtin__, 'type')(string_set_field))
        self.__string_set_field = string_set_field

        if string_field is not None:
            if not isinstance(string_field, basestring):
                raise TypeError(getattr(__builtin__, 'type')(string_field))
        self.__string_field = string_field

        if url_field is not None:
            if not isinstance(url_field, basestring):
                raise TypeError(getattr(__builtin__, 'type')(url_field))
        self.__url_field = url_field

    def __eq__(self, other):
        if self.required_i32_field != other.required_i32_field:
            return False
        if self.required_string_field != other.required_string_field:
            return False
        if self.binary_field != other.binary_field:
            return False
        if self.bool_field != other.bool_field:
            return False
        if self.byte_field != other.byte_field:
            return False
        if self.date_time_field != other.date_time_field:
            return False
        if self.decimal_field != other.decimal_field:
            return False
        if self.email_address_field != other.email_address_field:
            return False
        if self.enum_field != other.enum_field:
            return False
        if self.i16_field != other.i16_field:
            return False
        if self.i32_field != other.i32_field:
            return False
        if self.i64_field != other.i64_field:
            return False
        if self.string_list_field != other.string_list_field:
            return False
        if self.string_string_map_field != other.string_string_map_field:
            return False
        if self.string_set_field != other.string_set_field:
            return False
        if self.string_field != other.string_field:
            return False
        if self.url_field != other.url_field:
            return False
        return True

    def __hash__(self):
        return hash((self.required_i32_field,self.required_string_field,self.binary_field,self.bool_field,self.byte_field,self.date_time_field,self.decimal_field,self.email_address_field,self.enum_field,self.i16_field,self.i32_field,self.i64_field,self.string_list_field,self.string_string_map_field,self.string_set_field,self.string_field,self.url_field,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('required_i32_field=' + repr(self.required_i32_field))
        field_reprs.append('required_string_field=' + "'" + self.required_string_field.encode('ascii', 'replace') + "'")
        if self.binary_field is not None:
            field_reprs.append('binary_field=' + "'" + self.binary_field.encode('ascii', 'replace') + "'")
        if self.bool_field is not None:
            field_reprs.append('bool_field=' + repr(self.bool_field))
        if self.byte_field is not None:
            field_reprs.append('byte_field=' + repr(self.byte_field))
        if self.date_time_field is not None:
            field_reprs.append('date_time_field=' + repr(self.date_time_field))
        if self.decimal_field is not None:
            field_reprs.append('decimal_field=' + repr(self.decimal_field))
        if self.email_address_field is not None:
            field_reprs.append('email_address_field=' + "'" + self.email_address_field.encode('ascii', 'replace') + "'")
        if self.enum_field is not None:
            field_reprs.append('enum_field=' + repr(self.enum_field))
        if self.i16_field is not None:
            field_reprs.append('i16_field=' + repr(self.i16_field))
        if self.i32_field is not None:
            field_reprs.append('i32_field=' + repr(self.i32_field))
        if self.i64_field is not None:
            field_reprs.append('i64_field=' + repr(self.i64_field))
        if self.string_list_field is not None:
            field_reprs.append('string_list_field=' + repr(self.string_list_field))
        if self.string_string_map_field is not None:
            field_reprs.append('string_string_map_field=' + repr(self.string_string_map_field))
        if self.string_set_field is not None:
            field_reprs.append('string_set_field=' + repr(self.string_set_field))
        if self.string_field is not None:
            field_reprs.append('string_field=' + "'" + self.string_field.encode('ascii', 'replace') + "'")
        if self.url_field is not None:
            field_reprs.append('url_field=' + "'" + self.url_field.encode('ascii', 'replace') + "'")
        return 'NestedProtocolTestStruct(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('required_i32_field=' + repr(self.required_i32_field))
        field_reprs.append('required_string_field=' + "'" + self.required_string_field.encode('ascii', 'replace') + "'")
        if self.binary_field is not None:
            field_reprs.append('binary_field=' + "'" + self.binary_field.encode('ascii', 'replace') + "'")
        if self.bool_field is not None:
            field_reprs.append('bool_field=' + repr(self.bool_field))
        if self.byte_field is not None:
            field_reprs.append('byte_field=' + repr(self.byte_field))
        if self.date_time_field is not None:
            field_reprs.append('date_time_field=' + repr(self.date_time_field))
        if self.decimal_field is not None:
            field_reprs.append('decimal_field=' + repr(self.decimal_field))
        if self.email_address_field is not None:
            field_reprs.append('email_address_field=' + "'" + self.email_address_field.encode('ascii', 'replace') + "'")
        if self.enum_field is not None:
            field_reprs.append('enum_field=' + repr(self.enum_field))
        if self.i16_field is not None:
            field_reprs.append('i16_field=' + repr(self.i16_field))
        if self.i32_field is not None:
            field_reprs.append('i32_field=' + repr(self.i32_field))
        if self.i64_field is not None:
            field_reprs.append('i64_field=' + repr(self.i64_field))
        if self.string_list_field is not None:
            field_reprs.append('string_list_field=' + repr(self.string_list_field))
        if self.string_string_map_field is not None:
            field_reprs.append('string_string_map_field=' + repr(self.string_string_map_field))
        if self.string_set_field is not None:
            field_reprs.append('string_set_field=' + repr(self.string_set_field))
        if self.string_field is not None:
            field_reprs.append('string_field=' + "'" + self.string_field.encode('ascii', 'replace') + "'")
        if self.url_field is not None:
            field_reprs.append('url_field=' + "'" + self.url_field.encode('ascii', 'replace') + "'")
        return 'NestedProtocolTestStruct(' + ', '.join(field_reprs) + ')'

    def as_dict(self):
        return {'required_i32_field': self.required_i32_field, 'required_string_field': self.required_string_field, 'binary_field': self.binary_field, 'bool_field': self.bool_field, 'byte_field': self.byte_field, 'date_time_field': self.date_time_field, 'decimal_field': self.decimal_field, 'email_address_field': self.email_address_field, 'enum_field': self.enum_field, 'i16_field': self.i16_field, 'i32_field': self.i32_field, 'i64_field': self.i64_field, 'string_list_field': self.string_list_field, 'string_string_map_field': self.string_string_map_field, 'string_set_field': self.string_set_field, 'string_field': self.string_field, 'url_field': self.url_field}

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
    def date_time_field(self):
        return self.__date_time_field

    @property
    def decimal_field(self):
        return self.__decimal_field

    @property
    def email_address_field(self):
        return self.__email_address_field

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

    @classmethod
    def read(cls, iprot):
        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'required_i32_field':
                init_kwds['required_i32_field'] = iprot.read_i32()
            elif ifield_name == 'required_string_field':
                init_kwds['required_string_field'] = iprot.read_string()
            elif ifield_name == 'binary_field':
                try:
                    init_kwds['binary_field'] = iprot.read_binary()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'bool_field':
                try:
                    init_kwds['bool_field'] = iprot.read_bool()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'byte_field':
                try:
                    init_kwds['byte_field'] = iprot.read_byte()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'date_time_field':
                try:
                    init_kwds['date_time_field'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'decimal_field':
                try:
                    init_kwds['decimal_field'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'email_address_field':
                try:
                    init_kwds['email_address_field'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'enum_field':
                try:
                    init_kwds['enum_field'] = thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum.value_of(iprot.read_string().strip().upper())
                except (TypeError,):
                    pass
            elif ifield_name == 'i16_field':
                try:
                    init_kwds['i16_field'] = iprot.read_i16()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i32_field':
                try:
                    init_kwds['i32_field'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i64_field':
                try:
                    init_kwds['i64_field'] = iprot.read_i64()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'string_list_field':
                init_kwds['string_list_field'] = tuple([iprot.read_string() for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'string_string_map_field':
                init_kwds['string_string_map_field'] = dict([(iprot.read_string(), iprot.read_string()) for _ in xrange(iprot.read_map_begin()[2])] + (iprot.read_map_end() is None and []))
            elif ifield_name == 'string_set_field':
                init_kwds['string_set_field'] = frozenset([iprot.read_string() for _ in xrange(iprot.read_set_begin()[1])] + (iprot.read_set_end() is None and []))
            elif ifield_name == 'string_field':
                try:
                    init_kwds['string_field'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'url_field':
                try:
                    init_kwds['url_field'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replace(self, required_i32_field=None, required_string_field=None, binary_field=None, bool_field=None, byte_field=None, date_time_field=None, decimal_field=None, email_address_field=None, enum_field=None, i16_field=None, i32_field=None, i64_field=None, string_list_field=None, string_string_map_field=None, string_set_field=None, string_field=None, url_field=None):
        if required_i32_field is None:
            required_i32_field = self.required_i32_field
        if required_string_field is None:
            required_string_field = self.required_string_field
        if binary_field is None:
            binary_field = self.binary_field
        if bool_field is None:
            bool_field = self.bool_field
        if byte_field is None:
            byte_field = self.byte_field
        if date_time_field is None:
            date_time_field = self.date_time_field
        if decimal_field is None:
            decimal_field = self.decimal_field
        if email_address_field is None:
            email_address_field = self.email_address_field
        if enum_field is None:
            enum_field = self.enum_field
        if i16_field is None:
            i16_field = self.i16_field
        if i32_field is None:
            i32_field = self.i32_field
        if i64_field is None:
            i64_field = self.i64_field
        if string_list_field is None:
            string_list_field = self.string_list_field
        if string_string_map_field is None:
            string_string_map_field = self.string_string_map_field
        if string_set_field is None:
            string_set_field = self.string_set_field
        if string_field is None:
            string_field = self.string_field
        if url_field is None:
            url_field = self.url_field
        return self.__class__(required_i32_field=required_i32_field, required_string_field=required_string_field, binary_field=binary_field, bool_field=bool_field, byte_field=byte_field, date_time_field=date_time_field, decimal_field=decimal_field, email_address_field=email_address_field, enum_field=enum_field, i16_field=i16_field, i32_field=i32_field, i64_field=i64_field, string_list_field=string_list_field, string_string_map_field=string_string_map_field, string_set_field=string_set_field, string_field=string_field, url_field=url_field)

    @property
    def required_i32_field(self):
        return self.__required_i32_field

    @property
    def required_string_field(self):
        return self.__required_string_field

    @property
    def string_field(self):
        return self.__string_field

    @property
    def string_list_field(self):
        return self.__string_list_field

    @property
    def string_set_field(self):
        return self.__string_set_field

    @property
    def string_string_map_field(self):
        return self.__string_string_map_field.copy() if self.__string_string_map_field is not None else None

    @property
    def url_field(self):
        return self.__url_field

    def write(self, oprot):
        oprot.write_struct_begin('NestedProtocolTestStruct')

        oprot.write_field_begin('required_i32_field', 8, -1)
        oprot.write_i32(self.required_i32_field)
        oprot.write_field_end()

        oprot.write_field_begin('required_string_field', 11, -1)
        oprot.write_string(self.required_string_field)
        oprot.write_field_end()

        if self.binary_field is not None:
            oprot.write_field_begin('binary_field', 11, -1)
            oprot.write_binary(self.binary_field)
            oprot.write_field_end()

        if self.bool_field is not None:
            oprot.write_field_begin('bool_field', 2, -1)
            oprot.write_bool(self.bool_field)
            oprot.write_field_end()

        if self.byte_field is not None:
            oprot.write_field_begin('byte_field', 3, -1)
            oprot.write_byte(self.byte_field)
            oprot.write_field_end()

        if self.date_time_field is not None:
            oprot.write_field_begin('date_time_field', 10, -1)
            oprot.write_date_time(self.date_time_field)
            oprot.write_field_end()

        if self.decimal_field is not None:
            oprot.write_field_begin('decimal_field', 11, -1)
            oprot.write_decimal(self.decimal_field)
            oprot.write_field_end()

        if self.email_address_field is not None:
            oprot.write_field_begin('email_address_field', 11, -1)
            oprot.write_string(self.email_address_field)
            oprot.write_field_end()

        if self.enum_field is not None:
            oprot.write_field_begin('enum_field', 11, -1)
            oprot.write_string(str(self.enum_field))
            oprot.write_field_end()

        if self.i16_field is not None:
            oprot.write_field_begin('i16_field', 6, -1)
            oprot.write_i16(self.i16_field)
            oprot.write_field_end()

        if self.i32_field is not None:
            oprot.write_field_begin('i32_field', 8, -1)
            oprot.write_i32(self.i32_field)
            oprot.write_field_end()

        if self.i64_field is not None:
            oprot.write_field_begin('i64_field', 10, -1)
            oprot.write_i64(self.i64_field)
            oprot.write_field_end()

        if self.string_list_field is not None:
            oprot.write_field_begin('string_list_field', 15, -1)
            oprot.write_list_begin(11, len(self.string_list_field))
            for _0 in self.string_list_field:
                oprot.write_string(_0)
            oprot.write_list_end()
            oprot.write_field_end()

        if self.string_string_map_field is not None:
            oprot.write_field_begin('string_string_map_field', 13, -1)
            oprot.write_map_begin(11, len(self.string_string_map_field), 11)
            for __key0, __value0 in self.string_string_map_field.iteritems():
                oprot.write_string(__key0)
                oprot.write_string(__value0)
            oprot.write_map_end()
            oprot.write_field_end()

        if self.string_set_field is not None:
            oprot.write_field_begin('string_set_field', 14, -1)
            oprot.write_set_begin(11, len(self.string_set_field))
            for _0 in self.string_set_field:
                oprot.write_string(_0)
            oprot.write_set_end()
            oprot.write_field_end()

        if self.string_field is not None:
            oprot.write_field_begin('string_field', 11, -1)
            oprot.write_string(self.string_field)
            oprot.write_field_end()

        if self.url_field is not None:
            oprot.write_field_begin('url_field', 11, -1)
            oprot.write_string(self.url_field)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
