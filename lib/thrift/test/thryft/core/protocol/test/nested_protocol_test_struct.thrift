namespace java org.thryft.protocol.test
namespace * thryft_test.protocol.test

include "protocol_test_enum.thrift"
include "thryft/native/date_time.thrift"
include "thryft/native/decimal.thrift"
include "thryft/native/email_address.thrift"
include "thryft/native/url.thrift"

struct NestedProtocolTestStruct {
    optional binary binary_field;
    optional bool bool_field;
    optional byte byte_field
    optional date_time.DateTime date_time_field;
    optional decimal.Decimal decimal_field;
    optional email_address.EmailAddress email_address_field;
    optional protocol_test_enum.ProtocolTestEnum enum_field;
    optional i16 i16_field;
    optional i32 i32_field;
    optional i64 i64_field;
    optional list<string> string_list_field;
    optional map<string, string> string_string_map_field;
    required i32 required_i32_field;
    // @validation {"minLength": 1}
    // @faker Name.firstName()
    required string required_string_field;
    optional set<string> string_set_field;
    // @validation {"minLength": 1}
    optional string string_field;
    optional url.Url url_field;
}
