#include "gtest/gtest.h"

#include <string>

#include "./protocol_test_enum.hpp"
#include "./protocol_test_struct.hpp"
#include "thryft/list.hpp"
#include "thryft/protocol/type.hpp"

namespace thryft_test {
namespace protocol {
namespace test {
using ::std::make_pair;
using ::std::string;
using ::thryft::List;
using ::thryft::Map;
using ::thryft::Set;
using ::thryft::protocol::Type;

template <class TypeParam>
class ProtocolTest : public ::testing::Test {
  protected:
    void test(const ProtocolTestStruct& expected) {
      TypeParam::OutputProtocolT oprot;
      expected.write(oprot);
      ProtocolTestStruct actual(TypeParam(oprot.to_string()));
      ASSERT_EQ(expected, actual);
    }
};

TYPED_TEST_CASE_P(ProtocolTest);

TYPED_TEST_P(ProtocolTest, bool_) {
  test(ProtocolTestStruct().set_bool_field(true));
}

TYPED_TEST_P(ProtocolTest, i8) {
  test(ProtocolTestStruct().set_i8_field(1));
}

TYPED_TEST_P(ProtocolTest, i16) {
  test(ProtocolTestStruct().set_i16_field(1));
}

TYPED_TEST_P(ProtocolTest, i32) {
  test(ProtocolTestStruct().set_i32_field(1));
}

TYPED_TEST_P(ProtocolTest, i64) {
  test(ProtocolTestStruct().set_i64_field(1));
}

TYPED_TEST_P(ProtocolTest, string_list) {
  List< ::std::string, Type::STRING > string_list;
  string_list.push_back("test");
  test(ProtocolTestStruct().set_string_list_field(string_list));
}

TYPED_TEST_P(ProtocolTest, string_list_empty) {
  test(ProtocolTestStruct().set_string_list_field(
         List<::std::string, Type::STRING>()));
}

TYPED_TEST_P(ProtocolTest, string_string_map) {
  Map<::std::string, Type::STRING, ::std::string, Type::STRING> string_string_map;
  string_string_map.insert(make_pair("test", "test"));
  test(ProtocolTestStruct().set_string_string_map_field(string_string_map));
}

TYPED_TEST_P(ProtocolTest, string_string_map_empty) {
  test(ProtocolTestStruct().set_string_string_map_field(
         Map<::std::string, Type::STRING, ::std::string, Type::STRING>()));
}

TYPED_TEST_P(ProtocolTest, string_set) {
  Set<::std::string, Type::STRING> string_set;
  string_set.insert("test");
  test(ProtocolTestStruct().set_string_set_field(string_set));
}

TYPED_TEST_P(ProtocolTest, string_set_empty) {
  test(ProtocolTestStruct().set_string_set_field(
         Set<::std::string, Type::STRING>()));
}

TYPED_TEST_P(ProtocolTest, string) {
  test(ProtocolTestStruct().set_string_field(::std::string("test")));
}

TYPED_TEST_P(ProtocolTest, struct_) {
  test(ProtocolTestStruct().set_struct_field(
         NestedProtocolTestStruct().set_string_field("test")));
}

TYPED_TEST_P(ProtocolTest, struct_empty) {
  test(ProtocolTestStruct().set_struct_field(NestedProtocolTestStruct()));
}

REGISTER_TYPED_TEST_CASE_P(
  ProtocolTest,
  bool_, i8, i16, i32, i64,
  string_list, string_list_empty,
  string_string_map, string_string_map_empty,
  string_set, string_set_empty,
  string,
  struct_, struct_empty
);
}
}
}
