namespace java org.thryft.protocol.test
namespace * thryft_test.protocol.test

include "nested_protocol_test_struct.thrift"
include "protocol_test_enum.thrift"
include "thryft/native/date_time.thrift"
include "thryft/native/decimal.thrift"
include "thryft/native/i8.thrift"
include "thryft/native/email_address.thrift"
include "thryft/native/float.thrift"
include "thryft/native/u32.thrift"
include "thryft/native/u64.thrift"
include "thryft/native/uri.thrift"
include "thryft/native/url.thrift"
include "thryft/native/variant.thrift"

struct ProtocolTestStruct {
    1: required i32 required_i32_field;
    // @validation {"minLength": 1}
    2: required string required_string_field;

    3: optional binary binary_field;
    4: optional bool bool_field;
    5: optional date_time.DateTime date_time_field;
    6: optional decimal.Decimal decimal_field;
    7: optional double double_field;
    8: optional email_address.EmailAddress email_address_field;
    9: optional protocol_test_enum.ProtocolTestEnum enum_field;
    10: optional float.float float_field;
    11: optional i8.i8 i8_field;
    12: optional i16 i16_field;
    // @validation {"max": 100, "min": 1}
    13: optional i32 i32_field;
    14: optional i64 i64_field;
    15: optional list<string> string_list_field;
    16: optional map<string, string> string_string_map_field;
    17: optional set<string> string_set_field;
    // @validation {"minLength": 1}
    18: optional string string_field;
    19: optional nested_protocol_test_struct.NestedProtocolTestStruct struct_field;
    // @validation {"max": 100, "min": 1}
    20: optional u32.u32 u32_field;
    // @validation {"max": 100, "min": 1}
    21: optional u64.u64 u64_field;
    22: optional uri.Uri uri_field;
    23: optional url.Url url_field;
    24: optional variant.Variant variant_field;
}
