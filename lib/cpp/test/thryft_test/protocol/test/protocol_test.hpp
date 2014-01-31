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

TYPED_TEST_P(ProtocolTest, list_string) {
  List< ::std::string, Type::STRING > list_string;
  list_string.push_back("test");
  test(ProtocolTestStruct().set_list_string_field(list_string));
}

TYPED_TEST_P(ProtocolTest, list_string_empty) {
  test(ProtocolTestStruct().set_list_string_field(
         List<::std::string, Type::STRING>()));
}

TYPED_TEST_P(ProtocolTest, map_string_string) {
  Map<::std::string, Type::STRING, ::std::string, Type::STRING> map_string_string;
  map_string_string.insert(make_pair("test", "test"));
  test(ProtocolTestStruct().set_map_string_string_field(map_string_string));
}

TYPED_TEST_P(ProtocolTest, map_string_string_empty) {
  test(ProtocolTestStruct().set_map_string_string_field(
         Map<::std::string, Type::STRING, ::std::string, Type::STRING>()));
}

TYPED_TEST_P(ProtocolTest, set_string) {
  Set<::std::string, Type::STRING> set_string;
  set_string.insert("test");
  test(ProtocolTestStruct().set_set_string_field(set_string));
}

TYPED_TEST_P(ProtocolTest, set_string_empty) {
  test(ProtocolTestStruct().set_set_string_field(
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
  list_string, list_string_empty,
  map_string_string, map_string_string_empty,
  set_string, set_string_empty,
  string,
  struct_, struct_empty
);
}
}
}
