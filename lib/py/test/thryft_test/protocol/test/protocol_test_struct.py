from __future__ import absolute_import; import decimal
from itertools import ifilterfalse
import __builtin__
import datetime
import thryft_test.protocol.test.nested_protocol_test_struct
import thryft_test.protocol.test.protocol_test_enum


class ProtocolTestStruct(object):
    class Builder(object):
        def __init__(
            self,
            required_i32_field=None,
            required_string_field=None,
            binary_field=None,
            bool_field=None,
            date_time_field=None,
            decimal_field=None,
            double_field=None,
            email_address_field=None,
            enum_field=None,
            float_field=None,
            i8_field=None,
            i16_field=None,
            i32_field=None,
            i64_field=None,
            string_list_field=None,
            string_string_map_field=None,
            string_set_field=None,
            string_field=None,
            struct_field=None,
            u32_field=None,
            u64_field=None,
            uri_field=None,
            url_field=None,
            variant_field=None,
        ):
            '''
            :type required_i32_field: int
            :type required_string_field: str
            :type binary_field: str or None
            :type bool_field: bool or None
            :type date_time_field: datetime.datetime or None
            :type decimal_field: Decimal or None
            :type double_field: float or None
            :type email_address_field: str or None
            :type enum_field: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum or None
            :type float_field: float or None
            :type i8_field: int or None
            :type i16_field: int or None
            :type i32_field: int or None
            :type i64_field: int or long or None
            :type string_list_field: tuple(str) or None
            :type string_string_map_field: dict(str: str) or None
            :type string_set_field: frozenset(str) or None
            :type string_field: str or None
            :type struct_field: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct or None
            :type u32_field: int or None
            :type u64_field: int or long or None
            :type uri_field: str or None
            :type url_field: str or None
            :type variant_field: object or None
            '''

            self.__required_i32_field = required_i32_field
            self.__required_string_field = required_string_field
            self.__binary_field = binary_field
            self.__bool_field = bool_field
            self.__date_time_field = date_time_field
            self.__decimal_field = decimal_field
            self.__double_field = double_field
            self.__email_address_field = email_address_field
            self.__enum_field = enum_field
            self.__float_field = float_field
            self.__i8_field = i8_field
            self.__i16_field = i16_field
            self.__i32_field = i32_field
            self.__i64_field = i64_field
            self.__string_list_field = string_list_field
            self.__string_string_map_field = string_string_map_field
            self.__string_set_field = string_set_field
            self.__string_field = string_field
            self.__struct_field = struct_field
            self.__u32_field = u32_field
            self.__u64_field = u64_field
            self.__uri_field = uri_field
            self.__url_field = url_field
            self.__variant_field = variant_field

        def build(self):
            return ProtocolTestStruct(required_i32_field=self.__required_i32_field, required_string_field=self.__required_string_field, binary_field=self.__binary_field, bool_field=self.__bool_field, date_time_field=self.__date_time_field, decimal_field=self.__decimal_field, double_field=self.__double_field, email_address_field=self.__email_address_field, enum_field=self.__enum_field, float_field=self.__float_field, i8_field=self.__i8_field, i16_field=self.__i16_field, i32_field=self.__i32_field, i64_field=self.__i64_field, string_list_field=self.__string_list_field, string_string_map_field=self.__string_string_map_field, string_set_field=self.__string_set_field, string_field=self.__string_field, struct_field=self.__struct_field, u32_field=self.__u32_field, u64_field=self.__u64_field, uri_field=self.__uri_field, url_field=self.__url_field, variant_field=self.__variant_field)

        @property
        def binary_field(self):
            '''
            :rtype: str
            '''

            return self.__binary_field

        @property
        def bool_field(self):
            '''
            :rtype: bool
            '''

            return self.__bool_field

        @property
        def date_time_field(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__date_time_field

        @property
        def decimal_field(self):
            '''
            :rtype: Decimal
            '''

            return self.__decimal_field

        @property
        def double_field(self):
            '''
            :rtype: float
            '''

            return self.__double_field

        @property
        def email_address_field(self):
            '''
            :rtype: str
            '''

            return self.__email_address_field

        @property
        def enum_field(self):
            '''
            :rtype: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum
            '''

            return self.__enum_field

        @property
        def float_field(self):
            '''
            :rtype: float
            '''

            return self.__float_field

        @property
        def i16_field(self):
            '''
            :rtype: int
            '''

            return self.__i16_field

        @property
        def i32_field(self):
            '''
            :rtype: int
            '''

            return self.__i32_field

        @property
        def i64_field(self):
            '''
            :rtype: int or long
            '''

            return self.__i64_field

        @property
        def i8_field(self):
            '''
            :rtype: int
            '''

            return self.__i8_field

        @property
        def required_i32_field(self):
            '''
            :rtype: int
            '''

            return self.__required_i32_field

        @property
        def required_string_field(self):
            '''
            :rtype: str
            '''

            return self.__required_string_field

        def set_binary_field(self, binary_field):
            '''
            :type binary_field: str or None
            '''

            if binary_field is not None:
                if not isinstance(binary_field, basestring):
                    raise TypeError("expected binary_field to be a str but it is a %s" % getattr(__builtin__, 'type')(binary_field))
            self.__binary_field = binary_field
            return self

        def set_bool_field(self, bool_field):
            '''
            :type bool_field: bool or None
            '''

            if bool_field is not None:
                if not isinstance(bool_field, bool):
                    raise TypeError("expected bool_field to be a bool but it is a %s" % getattr(__builtin__, 'type')(bool_field))
            self.__bool_field = bool_field
            return self

        def set_date_time_field(self, date_time_field):
            '''
            :type date_time_field: datetime.datetime or None
            '''

            if date_time_field is not None:
                if not isinstance(date_time_field, datetime.datetime):
                    raise TypeError("expected date_time_field to be a datetime.datetime but it is a %s" % getattr(__builtin__, 'type')(date_time_field))
            self.__date_time_field = date_time_field
            return self

        def set_decimal_field(self, decimal_field):
            '''
            :type decimal_field: Decimal or None
            '''

            if decimal_field is not None:
                if not isinstance(decimal_field, decimal.Decimal):
                    raise TypeError("expected decimal_field to be a Decimal but it is a %s" % getattr(__builtin__, 'type')(decimal_field))
            self.__decimal_field = decimal_field
            return self

        def set_double_field(self, double_field):
            '''
            :type double_field: float or None
            '''

            if double_field is not None:
                if not isinstance(double_field, float):
                    raise TypeError("expected double_field to be a float but it is a %s" % getattr(__builtin__, 'type')(double_field))
            self.__double_field = double_field
            return self

        def set_email_address_field(self, email_address_field):
            '''
            :type email_address_field: str or None
            '''

            if email_address_field is not None:
                if not isinstance(email_address_field, basestring):
                    raise TypeError("expected email_address_field to be a str but it is a %s" % getattr(__builtin__, 'type')(email_address_field))
            self.__email_address_field = email_address_field
            return self

        def set_enum_field(self, enum_field):
            '''
            :type enum_field: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum or None
            '''

            if enum_field is not None:
                if not isinstance(enum_field, thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum):
                    raise TypeError("expected enum_field to be a thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum but it is a %s" % getattr(__builtin__, 'type')(enum_field))
            self.__enum_field = enum_field
            return self

        def set_float_field(self, float_field):
            '''
            :type float_field: float or None
            '''

            if float_field is not None:
                if not isinstance(float_field, float):
                    raise TypeError("expected float_field to be a float but it is a %s" % getattr(__builtin__, 'type')(float_field))
            self.__float_field = float_field
            return self

        def set_i16_field(self, i16_field):
            '''
            :type i16_field: int or None
            '''

            if i16_field is not None:
                if not isinstance(i16_field, int):
                    raise TypeError("expected i16_field to be a int but it is a %s" % getattr(__builtin__, 'type')(i16_field))
            self.__i16_field = i16_field
            return self

        def set_i32_field(self, i32_field):
            '''
            :type i32_field: int or None
            '''

            if i32_field is not None:
                if not isinstance(i32_field, int):
                    raise TypeError("expected i32_field to be a int but it is a %s" % getattr(__builtin__, 'type')(i32_field))
            self.__i32_field = i32_field
            return self

        def set_i64_field(self, i64_field):
            '''
            :type i64_field: int or long or None
            '''

            if i64_field is not None:
                if not isinstance(i64_field, (int, long)):
                    raise TypeError("expected i64_field to be a int or long but it is a %s" % getattr(__builtin__, 'type')(i64_field))
            self.__i64_field = i64_field
            return self

        def set_i8_field(self, i8_field):
            '''
            :type i8_field: int or None
            '''

            if i8_field is not None:
                if not isinstance(i8_field, int):
                    raise TypeError("expected i8_field to be a int but it is a %s" % getattr(__builtin__, 'type')(i8_field))
            self.__i8_field = i8_field
            return self

        def set_required_i32_field(self, required_i32_field):
            '''
            :type required_i32_field: int
            '''

            if required_i32_field is None:
                raise ValueError('required_i32_field is required')
            if not isinstance(required_i32_field, int):
                raise TypeError("expected required_i32_field to be a int but it is a %s" % getattr(__builtin__, 'type')(required_i32_field))
            self.__required_i32_field = required_i32_field
            return self

        def set_required_string_field(self, required_string_field):
            '''
            :type required_string_field: str
            '''

            if required_string_field is None:
                raise ValueError('required_string_field is required')
            if not isinstance(required_string_field, basestring):
                raise TypeError("expected required_string_field to be a str but it is a %s" % getattr(__builtin__, 'type')(required_string_field))
            if len(required_string_field) < 1:
                raise ValueError("expected len(required_string_field) to be >= 1, was %d" % len(required_string_field))
            self.__required_string_field = required_string_field
            return self

        def set_string_field(self, string_field):
            '''
            :type string_field: str or None
            '''

            if string_field is not None:
                if not isinstance(string_field, basestring):
                    raise TypeError("expected string_field to be a str but it is a %s" % getattr(__builtin__, 'type')(string_field))
                if len(string_field) < 1:
                    raise ValueError("expected len(string_field) to be >= 1, was %d" % len(string_field))
            self.__string_field = string_field
            return self

        def set_string_list_field(self, string_list_field):
            '''
            :type string_list_field: tuple(str) or None
            '''

            if string_list_field is not None:
                if not (isinstance(string_list_field, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), string_list_field))) == 0):
                    raise TypeError("expected string_list_field to be a tuple(str) but it is a %s" % getattr(__builtin__, 'type')(string_list_field))
            self.__string_list_field = string_list_field
            return self

        def set_string_set_field(self, string_set_field):
            '''
            :type string_set_field: frozenset(str) or None
            '''

            if string_set_field is not None:
                if not (isinstance(string_set_field, frozenset) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), string_set_field))) == 0):
                    raise TypeError("expected string_set_field to be a frozenset(str) but it is a %s" % getattr(__builtin__, 'type')(string_set_field))
            self.__string_set_field = string_set_field
            return self

        def set_string_string_map_field(self, string_string_map_field):
            '''
            :type string_string_map_field: dict(str: str) or None
            '''

            if string_string_map_field is not None:
                if not (isinstance(string_string_map_field, dict) and len(list(ifilterfalse(lambda __item: isinstance(__item[0], basestring) and isinstance(__item[1], basestring), string_string_map_field.iteritems()))) == 0):
                    raise TypeError("expected string_string_map_field to be a dict(str: str) but it is a %s" % getattr(__builtin__, 'type')(string_string_map_field))
            self.__string_string_map_field = string_string_map_field
            return self

        def set_struct_field(self, struct_field):
            '''
            :type struct_field: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct or None
            '''

            if struct_field is not None:
                if not isinstance(struct_field, thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct):
                    raise TypeError("expected struct_field to be a thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct but it is a %s" % getattr(__builtin__, 'type')(struct_field))
            self.__struct_field = struct_field
            return self

        def set_u32_field(self, u32_field):
            '''
            :type u32_field: int or None
            '''

            if u32_field is not None:
                if not isinstance(u32_field, (int, long)) and u32_field >= 0:
                    raise TypeError("expected u32_field to be a int but it is a %s" % getattr(__builtin__, 'type')(u32_field))
            self.__u32_field = u32_field
            return self

        def set_u64_field(self, u64_field):
            '''
            :type u64_field: int or long or None
            '''

            if u64_field is not None:
                if not isinstance(u64_field, (int, long)) and u64_field >= 0:
                    raise TypeError("expected u64_field to be a int or long but it is a %s" % getattr(__builtin__, 'type')(u64_field))
            self.__u64_field = u64_field
            return self

        def set_uri_field(self, uri_field):
            '''
            :type uri_field: str or None
            '''

            if uri_field is not None:
                if not isinstance(uri_field, basestring):
                    raise TypeError("expected uri_field to be a str but it is a %s" % getattr(__builtin__, 'type')(uri_field))
            self.__uri_field = uri_field
            return self

        def set_url_field(self, url_field):
            '''
            :type url_field: str or None
            '''

            if url_field is not None:
                if not isinstance(url_field, basestring):
                    raise TypeError("expected url_field to be a str but it is a %s" % getattr(__builtin__, 'type')(url_field))
            self.__url_field = url_field
            return self

        def set_variant_field(self, variant_field):
            '''
            :type variant_field: object or None
            '''


            self.__variant_field = variant_field
            return self

        @property
        def string_field(self):
            '''
            :rtype: str
            '''

            return self.__string_field

        @property
        def string_list_field(self):
            '''
            :rtype: tuple(str)
            '''

            return self.__string_list_field

        @property
        def string_set_field(self):
            '''
            :rtype: frozenset(str)
            '''

            return self.__string_set_field

        @property
        def string_string_map_field(self):
            '''
            :rtype: dict(str: str)
            '''

            return self.__string_string_map_field.copy() if self.__string_string_map_field is not None else None

        @property
        def struct_field(self):
            '''
            :rtype: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct
            '''

            return self.__struct_field

        @property
        def u32_field(self):
            '''
            :rtype: int
            '''

            return self.__u32_field

        @property
        def u64_field(self):
            '''
            :rtype: int or long
            '''

            return self.__u64_field

        def update(self, protocol_test_struct):
            '''
            :type required_i32_field: int
            :type required_string_field: str
            :type binary_field: str or None
            :type bool_field: bool or None
            :type date_time_field: datetime.datetime or None
            :type decimal_field: Decimal or None
            :type double_field: float or None
            :type email_address_field: str or None
            :type enum_field: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum or None
            :type float_field: float or None
            :type i8_field: int or None
            :type i16_field: int or None
            :type i32_field: int or None
            :type i64_field: int or long or None
            :type string_list_field: tuple(str) or None
            :type string_string_map_field: dict(str: str) or None
            :type string_set_field: frozenset(str) or None
            :type string_field: str or None
            :type struct_field: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct or None
            :type u32_field: int or None
            :type u64_field: int or long or None
            :type uri_field: str or None
            :type url_field: str or None
            :type variant_field: object or None
            '''

            if isinstance(protocol_test_struct, ProtocolTestStruct):
                self.set_required_i32_field(protocol_test_struct.required_i32_field)
                self.set_required_string_field(protocol_test_struct.required_string_field)
                self.set_binary_field(protocol_test_struct.binary_field)
                self.set_bool_field(protocol_test_struct.bool_field)
                self.set_date_time_field(protocol_test_struct.date_time_field)
                self.set_decimal_field(protocol_test_struct.decimal_field)
                self.set_double_field(protocol_test_struct.double_field)
                self.set_email_address_field(protocol_test_struct.email_address_field)
                self.set_enum_field(protocol_test_struct.enum_field)
                self.set_float_field(protocol_test_struct.float_field)
                self.set_i8_field(protocol_test_struct.i8_field)
                self.set_i16_field(protocol_test_struct.i16_field)
                self.set_i32_field(protocol_test_struct.i32_field)
                self.set_i64_field(protocol_test_struct.i64_field)
                self.set_string_list_field(protocol_test_struct.string_list_field)
                self.set_string_string_map_field(protocol_test_struct.string_string_map_field)
                self.set_string_set_field(protocol_test_struct.string_set_field)
                self.set_string_field(protocol_test_struct.string_field)
                self.set_struct_field(protocol_test_struct.struct_field)
                self.set_u32_field(protocol_test_struct.u32_field)
                self.set_u64_field(protocol_test_struct.u64_field)
                self.set_uri_field(protocol_test_struct.uri_field)
                self.set_url_field(protocol_test_struct.url_field)
                self.set_variant_field(protocol_test_struct.variant_field)
            elif isinstance(protocol_test_struct, dict):
                for key, value in protocol_test_struct.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(protocol_test_struct)
            return self

        @property
        def uri_field(self):
            '''
            :rtype: str
            '''

            return self.__uri_field

        @property
        def url_field(self):
            '''
            :rtype: str
            '''

            return self.__url_field

        @property
        def variant_field(self):
            '''
            :rtype: object
            '''

            return self.__variant_field

        @binary_field.setter
        def binary_field(self, binary_field):
            '''
            :type binary_field: str or None
            '''

            self.set_binary_field(binary_field)

        @bool_field.setter
        def bool_field(self, bool_field):
            '''
            :type bool_field: bool or None
            '''

            self.set_bool_field(bool_field)

        @date_time_field.setter
        def date_time_field(self, date_time_field):
            '''
            :type date_time_field: datetime.datetime or None
            '''

            self.set_date_time_field(date_time_field)

        @decimal_field.setter
        def decimal_field(self, decimal_field):
            '''
            :type decimal_field: Decimal or None
            '''

            self.set_decimal_field(decimal_field)

        @double_field.setter
        def double_field(self, double_field):
            '''
            :type double_field: float or None
            '''

            self.set_double_field(double_field)

        @email_address_field.setter
        def email_address_field(self, email_address_field):
            '''
            :type email_address_field: str or None
            '''

            self.set_email_address_field(email_address_field)

        @enum_field.setter
        def enum_field(self, enum_field):
            '''
            :type enum_field: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum or None
            '''

            self.set_enum_field(enum_field)

        @float_field.setter
        def float_field(self, float_field):
            '''
            :type float_field: float or None
            '''

            self.set_float_field(float_field)

        @i16_field.setter
        def i16_field(self, i16_field):
            '''
            :type i16_field: int or None
            '''

            self.set_i16_field(i16_field)

        @i32_field.setter
        def i32_field(self, i32_field):
            '''
            :type i32_field: int or None
            '''

            self.set_i32_field(i32_field)

        @i64_field.setter
        def i64_field(self, i64_field):
            '''
            :type i64_field: int or long or None
            '''

            self.set_i64_field(i64_field)

        @i8_field.setter
        def i8_field(self, i8_field):
            '''
            :type i8_field: int or None
            '''

            self.set_i8_field(i8_field)

        @required_i32_field.setter
        def required_i32_field(self, required_i32_field):
            '''
            :type required_i32_field: int
            '''

            self.set_required_i32_field(required_i32_field)

        @required_string_field.setter
        def required_string_field(self, required_string_field):
            '''
            :type required_string_field: str
            '''

            self.set_required_string_field(required_string_field)

        @string_field.setter
        def string_field(self, string_field):
            '''
            :type string_field: str or None
            '''

            self.set_string_field(string_field)

        @string_list_field.setter
        def string_list_field(self, string_list_field):
            '''
            :type string_list_field: tuple(str) or None
            '''

            self.set_string_list_field(string_list_field)

        @string_set_field.setter
        def string_set_field(self, string_set_field):
            '''
            :type string_set_field: frozenset(str) or None
            '''

            self.set_string_set_field(string_set_field)

        @string_string_map_field.setter
        def string_string_map_field(self, string_string_map_field):
            '''
            :type string_string_map_field: dict(str: str) or None
            '''

            self.set_string_string_map_field(string_string_map_field)

        @struct_field.setter
        def struct_field(self, struct_field):
            '''
            :type struct_field: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct or None
            '''

            self.set_struct_field(struct_field)

        @u32_field.setter
        def u32_field(self, u32_field):
            '''
            :type u32_field: int or None
            '''

            self.set_u32_field(u32_field)

        @u64_field.setter
        def u64_field(self, u64_field):
            '''
            :type u64_field: int or long or None
            '''

            self.set_u64_field(u64_field)

        @uri_field.setter
        def uri_field(self, uri_field):
            '''
            :type uri_field: str or None
            '''

            self.set_uri_field(uri_field)

        @url_field.setter
        def url_field(self, url_field):
            '''
            :type url_field: str or None
            '''

            self.set_url_field(url_field)

        @variant_field.setter
        def variant_field(self, variant_field):
            '''
            :type variant_field: object or None
            '''

            self.set_variant_field(variant_field)

    class FieldMetadata(object):
        REQUIRED_I32_FIELD = None
        REQUIRED_STRING_FIELD = None
        BINARY_FIELD = None
        BOOL_FIELD = None
        DATE_TIME_FIELD = None
        DECIMAL_FIELD = None
        DOUBLE_FIELD = None
        EMAIL_ADDRESS_FIELD = None
        ENUM_FIELD = None
        FLOAT_FIELD = None
        I8_FIELD = None
        I16_FIELD = None
        I32_FIELD = None
        I64_FIELD = None
        STRING_LIST_FIELD = None
        STRING_STRING_MAP_FIELD = None
        STRING_SET_FIELD = None
        STRING_FIELD = None
        STRUCT_FIELD = None
        U32_FIELD = None
        U64_FIELD = None
        URI_FIELD = None
        URL_FIELD = None
        VARIANT_FIELD = None

        def __init__(self, name, type_, validation):
            object.__init__(self)
            self.__name = name
            self.__type = type_
            self.__validation = validation

        def __repr__(self):
            return self.__name

        @property
        def type(self):
            return self.__type

        @property
        def validation(self):
            return self.__validation

        @classmethod
        def values(cls):
            return (cls.REQUIRED_I32_FIELD, cls.REQUIRED_STRING_FIELD, cls.BINARY_FIELD, cls.BOOL_FIELD, cls.DATE_TIME_FIELD, cls.DECIMAL_FIELD, cls.DOUBLE_FIELD, cls.EMAIL_ADDRESS_FIELD, cls.ENUM_FIELD, cls.FLOAT_FIELD, cls.I8_FIELD, cls.I16_FIELD, cls.I32_FIELD, cls.I64_FIELD, cls.STRING_LIST_FIELD, cls.STRING_STRING_MAP_FIELD, cls.STRING_SET_FIELD, cls.STRING_FIELD, cls.STRUCT_FIELD, cls.U32_FIELD, cls.U64_FIELD, cls.URI_FIELD, cls.URL_FIELD, cls.VARIANT_FIELD,)

    FieldMetadata.REQUIRED_I32_FIELD = FieldMetadata('required_i32_field', int, None)
    FieldMetadata.REQUIRED_STRING_FIELD = FieldMetadata('required_string_field', str, {u'minLength': 1})
    FieldMetadata.BINARY_FIELD = FieldMetadata('binary_field', str, None)
    FieldMetadata.BOOL_FIELD = FieldMetadata('bool_field', bool, None)
    FieldMetadata.DATE_TIME_FIELD = FieldMetadata('date_time_field', datetime.datetime, None)
    FieldMetadata.DECIMAL_FIELD = FieldMetadata('decimal_field', decimal.Decimal, None)
    FieldMetadata.DOUBLE_FIELD = FieldMetadata('double_field', float, None)
    FieldMetadata.EMAIL_ADDRESS_FIELD = FieldMetadata('email_address_field', str, None)
    FieldMetadata.ENUM_FIELD = FieldMetadata('enum_field', thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum, None)
    FieldMetadata.FLOAT_FIELD = FieldMetadata('float_field', float, None)
    FieldMetadata.I8_FIELD = FieldMetadata('i8_field', int, None)
    FieldMetadata.I16_FIELD = FieldMetadata('i16_field', int, None)
    FieldMetadata.I32_FIELD = FieldMetadata('i32_field', int, {u'max': 100, u'min': 1})
    FieldMetadata.I64_FIELD = FieldMetadata('i64_field', long, None)
    FieldMetadata.STRING_LIST_FIELD = FieldMetadata('string_list_field', tuple, None)
    FieldMetadata.STRING_STRING_MAP_FIELD = FieldMetadata('string_string_map_field', dict, None)
    FieldMetadata.STRING_SET_FIELD = FieldMetadata('string_set_field', frozenset, None)
    FieldMetadata.STRING_FIELD = FieldMetadata('string_field', str, {u'minLength': 1})
    FieldMetadata.STRUCT_FIELD = FieldMetadata('struct_field', thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct, None)
    FieldMetadata.U32_FIELD = FieldMetadata('u32_field', int, {u'max': 100, u'min': 1})
    FieldMetadata.U64_FIELD = FieldMetadata('u64_field', long, {u'max': 100, u'min': 1})
    FieldMetadata.URI_FIELD = FieldMetadata('uri_field', str, None)
    FieldMetadata.URL_FIELD = FieldMetadata('url_field', str, None)
    FieldMetadata.VARIANT_FIELD = FieldMetadata('variant_field', object, None)

    def __init__(
        self,
        required_i32_field,
        required_string_field,
        binary_field=None,
        bool_field=None,
        date_time_field=None,
        decimal_field=None,
        double_field=None,
        email_address_field=None,
        enum_field=None,
        float_field=None,
        i8_field=None,
        i16_field=None,
        i32_field=None,
        i64_field=None,
        string_list_field=None,
        string_string_map_field=None,
        string_set_field=None,
        string_field=None,
        struct_field=None,
        u32_field=None,
        u64_field=None,
        uri_field=None,
        url_field=None,
        variant_field=None,
    ):
        '''
        :type required_i32_field: int
        :type required_string_field: str
        :type binary_field: str or None
        :type bool_field: bool or None
        :type date_time_field: datetime.datetime or None
        :type decimal_field: Decimal or None
        :type double_field: float or None
        :type email_address_field: str or None
        :type enum_field: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum or None
        :type float_field: float or None
        :type i8_field: int or None
        :type i16_field: int or None
        :type i32_field: int or None
        :type i64_field: int or long or None
        :type string_list_field: tuple(str) or None
        :type string_string_map_field: dict(str: str) or None
        :type string_set_field: frozenset(str) or None
        :type string_field: str or None
        :type struct_field: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct or None
        :type u32_field: int or None
        :type u64_field: int or long or None
        :type uri_field: str or None
        :type url_field: str or None
        :type variant_field: object or None
        '''

        if required_i32_field is None:
            raise ValueError('required_i32_field is required')
        if not isinstance(required_i32_field, int):
            raise TypeError("expected required_i32_field to be a int but it is a %s" % getattr(__builtin__, 'type')(required_i32_field))
        self.__required_i32_field = required_i32_field

        if required_string_field is None:
            raise ValueError('required_string_field is required')
        if not isinstance(required_string_field, basestring):
            raise TypeError("expected required_string_field to be a str but it is a %s" % getattr(__builtin__, 'type')(required_string_field))
        if len(required_string_field) < 1:
            raise ValueError("expected len(required_string_field) to be >= 1, was %d" % len(required_string_field))
        self.__required_string_field = required_string_field

        if binary_field is not None:
            if not isinstance(binary_field, basestring):
                raise TypeError("expected binary_field to be a str but it is a %s" % getattr(__builtin__, 'type')(binary_field))
        self.__binary_field = binary_field

        if bool_field is not None:
            if not isinstance(bool_field, bool):
                raise TypeError("expected bool_field to be a bool but it is a %s" % getattr(__builtin__, 'type')(bool_field))
        self.__bool_field = bool_field

        if date_time_field is not None:
            if not isinstance(date_time_field, datetime.datetime):
                raise TypeError("expected date_time_field to be a datetime.datetime but it is a %s" % getattr(__builtin__, 'type')(date_time_field))
        self.__date_time_field = date_time_field

        if decimal_field is not None:
            if not isinstance(decimal_field, decimal.Decimal):
                raise TypeError("expected decimal_field to be a Decimal but it is a %s" % getattr(__builtin__, 'type')(decimal_field))
        self.__decimal_field = decimal_field

        if double_field is not None:
            if not isinstance(double_field, float):
                raise TypeError("expected double_field to be a float but it is a %s" % getattr(__builtin__, 'type')(double_field))
        self.__double_field = double_field

        if email_address_field is not None:
            if not isinstance(email_address_field, basestring):
                raise TypeError("expected email_address_field to be a str but it is a %s" % getattr(__builtin__, 'type')(email_address_field))
        self.__email_address_field = email_address_field

        if enum_field is not None:
            if not isinstance(enum_field, thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum):
                raise TypeError("expected enum_field to be a thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum but it is a %s" % getattr(__builtin__, 'type')(enum_field))
        self.__enum_field = enum_field

        if float_field is not None:
            if not isinstance(float_field, float):
                raise TypeError("expected float_field to be a float but it is a %s" % getattr(__builtin__, 'type')(float_field))
        self.__float_field = float_field

        if i8_field is not None:
            if not isinstance(i8_field, int):
                raise TypeError("expected i8_field to be a int but it is a %s" % getattr(__builtin__, 'type')(i8_field))
        self.__i8_field = i8_field

        if i16_field is not None:
            if not isinstance(i16_field, int):
                raise TypeError("expected i16_field to be a int but it is a %s" % getattr(__builtin__, 'type')(i16_field))
        self.__i16_field = i16_field

        if i32_field is not None:
            if not isinstance(i32_field, int):
                raise TypeError("expected i32_field to be a int but it is a %s" % getattr(__builtin__, 'type')(i32_field))
        self.__i32_field = i32_field

        if i64_field is not None:
            if not isinstance(i64_field, (int, long)):
                raise TypeError("expected i64_field to be a int or long but it is a %s" % getattr(__builtin__, 'type')(i64_field))
        self.__i64_field = i64_field

        if string_list_field is not None:
            if not (isinstance(string_list_field, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), string_list_field))) == 0):
                raise TypeError("expected string_list_field to be a tuple(str) but it is a %s" % getattr(__builtin__, 'type')(string_list_field))
        self.__string_list_field = string_list_field

        if string_string_map_field is not None:
            if not (isinstance(string_string_map_field, dict) and len(list(ifilterfalse(lambda __item: isinstance(__item[0], basestring) and isinstance(__item[1], basestring), string_string_map_field.iteritems()))) == 0):
                raise TypeError("expected string_string_map_field to be a dict(str: str) but it is a %s" % getattr(__builtin__, 'type')(string_string_map_field))
        self.__string_string_map_field = string_string_map_field.copy() if string_string_map_field is not None else None

        if string_set_field is not None:
            if not (isinstance(string_set_field, frozenset) and len(list(ifilterfalse(lambda _: isinstance(_, basestring), string_set_field))) == 0):
                raise TypeError("expected string_set_field to be a frozenset(str) but it is a %s" % getattr(__builtin__, 'type')(string_set_field))
        self.__string_set_field = string_set_field

        if string_field is not None:
            if not isinstance(string_field, basestring):
                raise TypeError("expected string_field to be a str but it is a %s" % getattr(__builtin__, 'type')(string_field))
            if len(string_field) < 1:
                raise ValueError("expected len(string_field) to be >= 1, was %d" % len(string_field))
        self.__string_field = string_field

        if struct_field is not None:
            if not isinstance(struct_field, thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct):
                raise TypeError("expected struct_field to be a thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct but it is a %s" % getattr(__builtin__, 'type')(struct_field))
        self.__struct_field = struct_field

        if u32_field is not None:
            if not isinstance(u32_field, (int, long)) and u32_field >= 0:
                raise TypeError("expected u32_field to be a int but it is a %s" % getattr(__builtin__, 'type')(u32_field))
        self.__u32_field = u32_field

        if u64_field is not None:
            if not isinstance(u64_field, (int, long)) and u64_field >= 0:
                raise TypeError("expected u64_field to be a int or long but it is a %s" % getattr(__builtin__, 'type')(u64_field))
        self.__u64_field = u64_field

        if uri_field is not None:
            if not isinstance(uri_field, basestring):
                raise TypeError("expected uri_field to be a str but it is a %s" % getattr(__builtin__, 'type')(uri_field))
        self.__uri_field = uri_field

        if url_field is not None:
            if not isinstance(url_field, basestring):
                raise TypeError("expected url_field to be a str but it is a %s" % getattr(__builtin__, 'type')(url_field))
        self.__url_field = url_field


        self.__variant_field = variant_field

    def __eq__(self, other):
        if self.required_i32_field != other.required_i32_field:
            return False
        if self.required_string_field != other.required_string_field:
            return False
        if self.binary_field != other.binary_field:
            return False
        if self.bool_field != other.bool_field:
            return False
        if self.date_time_field != other.date_time_field:
            return False
        if self.decimal_field != other.decimal_field:
            return False
        if self.double_field != other.double_field:
            return False
        if self.email_address_field != other.email_address_field:
            return False
        if self.enum_field != other.enum_field:
            return False
        if self.float_field != other.float_field:
            return False
        if self.i8_field != other.i8_field:
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
        if self.struct_field != other.struct_field:
            return False
        if self.u32_field != other.u32_field:
            return False
        if self.u64_field != other.u64_field:
            return False
        if self.uri_field != other.uri_field:
            return False
        if self.url_field != other.url_field:
            return False
        if self.variant_field != other.variant_field:
            return False
        return True

    def __hash__(self):
        return hash((self.required_i32_field,self.required_string_field,self.binary_field,self.bool_field,self.date_time_field,self.decimal_field,self.double_field,self.email_address_field,self.enum_field,self.float_field,self.i8_field,self.i16_field,self.i32_field,self.i64_field,self.string_list_field,self.string_string_map_field,self.string_set_field,self.string_field,self.struct_field,self.u32_field,self.u64_field,self.uri_field,self.url_field,self.variant_field,))

    def __iter__(self):
        return iter(self.as_tuple())

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
        if self.date_time_field is not None:
            field_reprs.append('date_time_field=' + repr(self.date_time_field))
        if self.decimal_field is not None:
            field_reprs.append('decimal_field=' + repr(self.decimal_field))
        if self.double_field is not None:
            field_reprs.append('double_field=' + repr(self.double_field))
        if self.email_address_field is not None:
            field_reprs.append('email_address_field=' + "'" + self.email_address_field.encode('ascii', 'replace') + "'")
        if self.enum_field is not None:
            field_reprs.append('enum_field=' + repr(self.enum_field))
        if self.float_field is not None:
            field_reprs.append('float_field=' + repr(self.float_field))
        if self.i8_field is not None:
            field_reprs.append('i8_field=' + repr(self.i8_field))
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
        if self.struct_field is not None:
            field_reprs.append('struct_field=' + repr(self.struct_field))
        if self.u32_field is not None:
            field_reprs.append('u32_field=' + repr(self.u32_field))
        if self.u64_field is not None:
            field_reprs.append('u64_field=' + repr(self.u64_field))
        if self.uri_field is not None:
            field_reprs.append('uri_field=' + "'" + self.uri_field.encode('ascii', 'replace') + "'")
        if self.url_field is not None:
            field_reprs.append('url_field=' + "'" + self.url_field.encode('ascii', 'replace') + "'")
        if self.variant_field is not None:
            field_reprs.append('variant_field=' + repr(self.variant_field))
        return 'ProtocolTestStruct(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('required_i32_field=' + repr(self.required_i32_field))
        field_reprs.append('required_string_field=' + "'" + self.required_string_field.encode('ascii', 'replace') + "'")
        if self.binary_field is not None:
            field_reprs.append('binary_field=' + "'" + self.binary_field.encode('ascii', 'replace') + "'")
        if self.bool_field is not None:
            field_reprs.append('bool_field=' + repr(self.bool_field))
        if self.date_time_field is not None:
            field_reprs.append('date_time_field=' + repr(self.date_time_field))
        if self.decimal_field is not None:
            field_reprs.append('decimal_field=' + repr(self.decimal_field))
        if self.double_field is not None:
            field_reprs.append('double_field=' + repr(self.double_field))
        if self.email_address_field is not None:
            field_reprs.append('email_address_field=' + "'" + self.email_address_field.encode('ascii', 'replace') + "'")
        if self.enum_field is not None:
            field_reprs.append('enum_field=' + repr(self.enum_field))
        if self.float_field is not None:
            field_reprs.append('float_field=' + repr(self.float_field))
        if self.i8_field is not None:
            field_reprs.append('i8_field=' + repr(self.i8_field))
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
        if self.struct_field is not None:
            field_reprs.append('struct_field=' + repr(self.struct_field))
        if self.u32_field is not None:
            field_reprs.append('u32_field=' + repr(self.u32_field))
        if self.u64_field is not None:
            field_reprs.append('u64_field=' + repr(self.u64_field))
        if self.uri_field is not None:
            field_reprs.append('uri_field=' + "'" + self.uri_field.encode('ascii', 'replace') + "'")
        if self.url_field is not None:
            field_reprs.append('url_field=' + "'" + self.url_field.encode('ascii', 'replace') + "'")
        if self.variant_field is not None:
            field_reprs.append('variant_field=' + repr(self.variant_field))
        return 'ProtocolTestStruct(' + ', '.join(field_reprs) + ')'

    def as_dict(self):
        '''
        Return the fields of this object as a dictionary.

        :rtype: dict
        '''

        return {'required_i32_field': self.required_i32_field, 'required_string_field': self.required_string_field, 'binary_field': self.binary_field, 'bool_field': self.bool_field, 'date_time_field': self.date_time_field, 'decimal_field': self.decimal_field, 'double_field': self.double_field, 'email_address_field': self.email_address_field, 'enum_field': self.enum_field, 'float_field': self.float_field, 'i8_field': self.i8_field, 'i16_field': self.i16_field, 'i32_field': self.i32_field, 'i64_field': self.i64_field, 'string_list_field': self.string_list_field, 'string_string_map_field': self.string_string_map_field, 'string_set_field': self.string_set_field, 'string_field': self.string_field, 'struct_field': self.struct_field, 'u32_field': self.u32_field, 'u64_field': self.u64_field, 'uri_field': self.uri_field, 'url_field': self.url_field, 'variant_field': self.variant_field}

    def as_tuple(self):
        '''
        Return the fields of this object in declaration order as a tuple.

        :rtype: tuple
        '''

        return (self.required_i32_field, self.required_string_field, self.binary_field, self.bool_field, self.date_time_field, self.decimal_field, self.double_field, self.email_address_field, self.enum_field, self.float_field, self.i8_field, self.i16_field, self.i32_field, self.i64_field, self.string_list_field, self.string_string_map_field, self.string_set_field, self.string_field, self.struct_field, self.u32_field, self.u64_field, self.uri_field, self.url_field, self.variant_field,)

    @property
    def binary_field(self):
        '''
        :rtype: str
        '''

        return self.__binary_field

    @property
    def bool_field(self):
        '''
        :rtype: bool
        '''

        return self.__bool_field

    @property
    def date_time_field(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__date_time_field

    @property
    def decimal_field(self):
        '''
        :rtype: Decimal
        '''

        return self.__decimal_field

    @property
    def double_field(self):
        '''
        :rtype: float
        '''

        return self.__double_field

    @property
    def email_address_field(self):
        '''
        :rtype: str
        '''

        return self.__email_address_field

    @property
    def enum_field(self):
        '''
        :rtype: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum
        '''

        return self.__enum_field

    @property
    def float_field(self):
        '''
        :rtype: float
        '''

        return self.__float_field

    @property
    def i16_field(self):
        '''
        :rtype: int
        '''

        return self.__i16_field

    @property
    def i32_field(self):
        '''
        :rtype: int
        '''

        return self.__i32_field

    @property
    def i64_field(self):
        '''
        :rtype: int or long
        '''

        return self.__i64_field

    @property
    def i8_field(self):
        '''
        :rtype: int
        '''

        return self.__i8_field

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: thryft_test.protocol.test.protocol_test_struct.ProtocolTestStruct
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'required_i32_field' and ifield_id == 1:
                init_kwds['required_i32_field'] = iprot.read_i32()
            elif ifield_name == 'required_string_field' and ifield_id == 2:
                init_kwds['required_string_field'] = iprot.read_string()
            elif ifield_name == 'binary_field' and ifield_id == 3:
                try:
                    init_kwds['binary_field'] = iprot.read_binary()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'bool_field' and ifield_id == 4:
                try:
                    init_kwds['bool_field'] = iprot.read_bool()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'date_time_field' and ifield_id == 5:
                try:
                    init_kwds['date_time_field'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'decimal_field' and ifield_id == 6:
                try:
                    init_kwds['decimal_field'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'double_field' and ifield_id == 7:
                try:
                    init_kwds['double_field'] = iprot.read_double()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'email_address_field' and ifield_id == 8:
                try:
                    init_kwds['email_address_field'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'enum_field' and ifield_id == 9:
                try:
                    init_kwds['enum_field'] = thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum.value_of(iprot.read_string().strip().upper())
                except (TypeError,):
                    pass
            elif ifield_name == 'float_field' and ifield_id == 10:
                try:
                    init_kwds['float_field'] = iprot.read_double()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i8_field' and ifield_id == 11:
                try:
                    init_kwds['i8_field'] = iprot.read_byte()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i16_field' and ifield_id == 12:
                try:
                    init_kwds['i16_field'] = iprot.read_i16()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i32_field' and ifield_id == 13:
                try:
                    init_kwds['i32_field'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'i64_field' and ifield_id == 14:
                try:
                    init_kwds['i64_field'] = iprot.read_i64()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'string_list_field' and ifield_id == 15:
                init_kwds['string_list_field'] = tuple([iprot.read_string() for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'string_string_map_field' and ifield_id == 16:
                init_kwds['string_string_map_field'] = dict([(iprot.read_string(), iprot.read_string()) for _ in xrange(iprot.read_map_begin()[2])] + (iprot.read_map_end() is None and []))
            elif ifield_name == 'string_set_field' and ifield_id == 17:
                init_kwds['string_set_field'] = frozenset([iprot.read_string() for _ in xrange(iprot.read_set_begin()[1])] + (iprot.read_set_end() is None and []))
            elif ifield_name == 'string_field' and ifield_id == 18:
                try:
                    init_kwds['string_field'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'struct_field' and ifield_id == 19:
                init_kwds['struct_field'] = thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct.read(iprot)
            elif ifield_name == 'u32_field' and ifield_id == 20:
                try:
                    init_kwds['u32_field'] = iprot.read_u32()
                except (TypeError,):
                    pass
            elif ifield_name == 'u64_field' and ifield_id == 21:
                try:
                    init_kwds['u64_field'] = iprot.read_u64()
                except (TypeError,):
                    pass
            elif ifield_name == 'uri_field' and ifield_id == 22:
                try:
                    init_kwds['uri_field'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'url_field' and ifield_id == 23:
                try:
                    init_kwds['url_field'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'variant_field' and ifield_id == 24:
                init_kwds['variant_field'] = iprot.read_variant()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replace(
        self,
        required_i32_field=None,
        required_string_field=None,
        binary_field=None,
        bool_field=None,
        date_time_field=None,
        decimal_field=None,
        double_field=None,
        email_address_field=None,
        enum_field=None,
        float_field=None,
        i8_field=None,
        i16_field=None,
        i32_field=None,
        i64_field=None,
        string_list_field=None,
        string_string_map_field=None,
        string_set_field=None,
        string_field=None,
        struct_field=None,
        u32_field=None,
        u64_field=None,
        uri_field=None,
        url_field=None,
        variant_field=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type required_i32_field: int or None
        :type required_string_field: str or None
        :type binary_field: str or None
        :type bool_field: bool or None
        :type date_time_field: datetime.datetime or None
        :type decimal_field: Decimal or None
        :type double_field: float or None
        :type email_address_field: str or None
        :type enum_field: thryft_test.protocol.test.protocol_test_enum.ProtocolTestEnum or None
        :type float_field: float or None
        :type i8_field: int or None
        :type i16_field: int or None
        :type i32_field: int or None
        :type i64_field: int or long or None
        :type string_list_field: tuple(str) or None
        :type string_string_map_field: dict(str: str) or None
        :type string_set_field: frozenset(str) or None
        :type string_field: str or None
        :type struct_field: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct or None
        :type u32_field: int or None
        :type u64_field: int or long or None
        :type uri_field: str or None
        :type url_field: str or None
        :type variant_field: object or None
        :rtype: thryft_test.protocol.test.protocol_test_struct.ProtocolTestStruct
        '''

        if required_i32_field is None:
            required_i32_field = self.required_i32_field
        if required_string_field is None:
            required_string_field = self.required_string_field
        if binary_field is None:
            binary_field = self.binary_field
        if bool_field is None:
            bool_field = self.bool_field
        if date_time_field is None:
            date_time_field = self.date_time_field
        if decimal_field is None:
            decimal_field = self.decimal_field
        if double_field is None:
            double_field = self.double_field
        if email_address_field is None:
            email_address_field = self.email_address_field
        if enum_field is None:
            enum_field = self.enum_field
        if float_field is None:
            float_field = self.float_field
        if i8_field is None:
            i8_field = self.i8_field
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
        if struct_field is None:
            struct_field = self.struct_field
        if u32_field is None:
            u32_field = self.u32_field
        if u64_field is None:
            u64_field = self.u64_field
        if uri_field is None:
            uri_field = self.uri_field
        if url_field is None:
            url_field = self.url_field
        if variant_field is None:
            variant_field = self.variant_field
        return self.__class__(required_i32_field=required_i32_field, required_string_field=required_string_field, binary_field=binary_field, bool_field=bool_field, date_time_field=date_time_field, decimal_field=decimal_field, double_field=double_field, email_address_field=email_address_field, enum_field=enum_field, float_field=float_field, i8_field=i8_field, i16_field=i16_field, i32_field=i32_field, i64_field=i64_field, string_list_field=string_list_field, string_string_map_field=string_string_map_field, string_set_field=string_set_field, string_field=string_field, struct_field=struct_field, u32_field=u32_field, u64_field=u64_field, uri_field=uri_field, url_field=url_field, variant_field=variant_field)

    @property
    def required_i32_field(self):
        '''
        :rtype: int
        '''

        return self.__required_i32_field

    @property
    def required_string_field(self):
        '''
        :rtype: str
        '''

        return self.__required_string_field

    @property
    def string_field(self):
        '''
        :rtype: str
        '''

        return self.__string_field

    @property
    def string_list_field(self):
        '''
        :rtype: tuple(str)
        '''

        return self.__string_list_field

    @property
    def string_set_field(self):
        '''
        :rtype: frozenset(str)
        '''

        return self.__string_set_field

    @property
    def string_string_map_field(self):
        '''
        :rtype: dict(str: str)
        '''

        return self.__string_string_map_field.copy() if self.__string_string_map_field is not None else None

    @property
    def struct_field(self):
        '''
        :rtype: thryft_test.protocol.test.nested_protocol_test_struct.NestedProtocolTestStruct
        '''

        return self.__struct_field

    @property
    def u32_field(self):
        '''
        :rtype: int
        '''

        return self.__u32_field

    @property
    def u64_field(self):
        '''
        :rtype: int or long
        '''

        return self.__u64_field

    @property
    def uri_field(self):
        '''
        :rtype: str
        '''

        return self.__uri_field

    @property
    def url_field(self):
        '''
        :rtype: str
        '''

        return self.__url_field

    @property
    def variant_field(self):
        '''
        :rtype: object
        '''

        return self.__variant_field

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: thryft_test.protocol.test.protocol_test_struct.ProtocolTestStruct
        '''

        oprot.write_struct_begin('ProtocolTestStruct')

        oprot.write_field_begin(name='required_i32_field', type=8, id=1)
        oprot.write_i32(self.required_i32_field)
        oprot.write_field_end()

        oprot.write_field_begin(name='required_string_field', type=11, id=2)
        oprot.write_string(self.required_string_field)
        oprot.write_field_end()

        if self.binary_field is not None:
            oprot.write_field_begin(name='binary_field', type=11, id=3)
            oprot.write_binary(self.binary_field)
            oprot.write_field_end()

        if self.bool_field is not None:
            oprot.write_field_begin(name='bool_field', type=2, id=4)
            oprot.write_bool(self.bool_field)
            oprot.write_field_end()

        if self.date_time_field is not None:
            oprot.write_field_begin(name='date_time_field', type=10, id=5)
            oprot.write_date_time(self.date_time_field)
            oprot.write_field_end()

        if self.decimal_field is not None:
            oprot.write_field_begin(name='decimal_field', type=11, id=6)
            oprot.write_decimal(self.decimal_field)
            oprot.write_field_end()

        if self.double_field is not None:
            oprot.write_field_begin(name='double_field', type=4, id=7)
            oprot.write_double(self.double_field)
            oprot.write_field_end()

        if self.email_address_field is not None:
            oprot.write_field_begin(name='email_address_field', type=11, id=8)
            oprot.write_string(self.email_address_field)
            oprot.write_field_end()

        if self.enum_field is not None:
            oprot.write_field_begin(name='enum_field', type=11, id=9)
            oprot.write_string(str(self.enum_field))
            oprot.write_field_end()

        if self.float_field is not None:
            oprot.write_field_begin(name='float_field', type=4, id=10)
            oprot.write_double(self.float_field)
            oprot.write_field_end()

        if self.i8_field is not None:
            oprot.write_field_begin(name='i8_field', type=3, id=11)
            oprot.write_byte(self.i8_field)
            oprot.write_field_end()

        if self.i16_field is not None:
            oprot.write_field_begin(name='i16_field', type=6, id=12)
            oprot.write_i16(self.i16_field)
            oprot.write_field_end()

        if self.i32_field is not None:
            oprot.write_field_begin(name='i32_field', type=8, id=13)
            oprot.write_i32(self.i32_field)
            oprot.write_field_end()

        if self.i64_field is not None:
            oprot.write_field_begin(name='i64_field', type=10, id=14)
            oprot.write_i64(self.i64_field)
            oprot.write_field_end()

        if self.string_list_field is not None:
            oprot.write_field_begin(name='string_list_field', type=15, id=15)
            oprot.write_list_begin(11, len(self.string_list_field))
            for _0 in self.string_list_field:
                oprot.write_string(_0)
            oprot.write_list_end()
            oprot.write_field_end()

        if self.string_string_map_field is not None:
            oprot.write_field_begin(name='string_string_map_field', type=13, id=16)
            oprot.write_map_begin(11, len(self.string_string_map_field), 11)
            for __key0, __value0 in self.string_string_map_field.iteritems():
                oprot.write_string(__key0)
                oprot.write_string(__value0)
            oprot.write_map_end()
            oprot.write_field_end()

        if self.string_set_field is not None:
            oprot.write_field_begin(name='string_set_field', type=14, id=17)
            oprot.write_set_begin(11, len(self.string_set_field))
            for _0 in self.string_set_field:
                oprot.write_string(_0)
            oprot.write_set_end()
            oprot.write_field_end()

        if self.string_field is not None:
            oprot.write_field_begin(name='string_field', type=11, id=18)
            oprot.write_string(self.string_field)
            oprot.write_field_end()

        if self.struct_field is not None:
            oprot.write_field_begin(name='struct_field', type=12, id=19)
            self.struct_field.write(oprot)
            oprot.write_field_end()

        if self.u32_field is not None:
            oprot.write_field_begin(name='u32_field', type=8, id=20)
            oprot.write_u32(self.u32_field)
            oprot.write_field_end()

        if self.u64_field is not None:
            oprot.write_field_begin(name='u64_field', type=10, id=21)
            oprot.write_u64(self.u64_field)
            oprot.write_field_end()

        if self.uri_field is not None:
            oprot.write_field_begin(name='uri_field', type=11, id=22)
            oprot.write_string(self.uri_field)
            oprot.write_field_end()

        if self.url_field is not None:
            oprot.write_field_begin(name='url_field', type=11, id=23)
            oprot.write_string(self.url_field)
            oprot.write_field_end()

        if self.variant_field is not None:
            oprot.write_field_begin(name='variant_field', type=12, id=24)
            oprot.write_variant(self.variant_field)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
