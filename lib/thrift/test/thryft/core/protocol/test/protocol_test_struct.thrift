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
    required i32 required_i32_field;
    // @validation {"minLength": 1}
    required string required_string_field;

    optional binary binary_field;
    optional bool bool_field;
    optional date_time.DateTime date_time_field;
    optional decimal.Decimal decimal_field;
    optional email_address.EmailAddress email_address_field;
    optional protocol_test_enum.ProtocolTestEnum enum_field;
    optional float.float float_field;
    optional i8.i8 i8_field;
    optional i16 i16_field;
    optional i32 i32_field;
    optional i64 i64_field;
    optional list<string> string_list_field;
    optional map<string, string> string_string_map_field;
    optional set<string> string_set_field;
    // @validation {"minLength": 1}
    optional string string_field;
    optional nested_protocol_test_struct.NestedProtocolTestStruct struct_field;
    optional u32.u32 u32_field;
    optional u64.u64 u64_field;
    optional uri.Uri uri_field;
    optional url.Url url_field;
    optional variant.Variant variant_field;
}
