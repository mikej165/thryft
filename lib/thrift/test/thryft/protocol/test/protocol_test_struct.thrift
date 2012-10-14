namespace java org.thryft.protocol.test
namespace py thryft_test.protocol.test

include "protocol_test_enum.thrift"
include "thryft/util/date.thrift"
include "thryft/util/date_time.thrift"
include "thryft/util/decimal.thrift"

struct ProtocolTestStruct {
    optional bool bool_field;
    optional byte byte_field
    optional date.Date date_field;
    optional date_time.DateTime date_time_field;
    optional decimal.Decimal decimal_field;
    optional protocol_test_enum.ProtocolTestEnum enum_field;
    optional i16 i16_field;
    optional i32 i32_field;
    optional i64 i64_field;
    optional list<string> list_string_field;
    optional map<string, string> map_string_string_field;
    optional set<string> set_string_field;
    optional string string_field;
    optional ProtocolTestStruct struct_field;
}
