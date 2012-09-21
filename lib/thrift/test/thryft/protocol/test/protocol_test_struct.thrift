namespace java org.thryft.protocol.test

include "thryft/generator/native_types/date_type.thrift"
include "thryft/generator/native_types/date_time_type.thrift"
include "thryft/generator/native_types/decimal_type.thrift"
include "thryft/protocol/test/protocol_test_enum.thrift"

struct ProtocolTestStruct {
    optional bool bool_field;
    optional byte byte_field
    optional date_type.DateType date_field;
    optional date_time_type.DateTimeType date_time_field;
    optional decimal_type.DecimalType decimal_field;
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
