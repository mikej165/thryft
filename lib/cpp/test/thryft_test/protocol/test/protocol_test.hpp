#include "gtest/gtest.h"

#include "./protocol_test_enum.hpp"
#include "./protocol_test_struct.hpp"

namespace thryft_test {
namespace protocol {
namespace test {
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

//@Test
//public void testBool() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setBoolField(true));
//}

//@Test
//public void testByte() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setByteField((byte) 1));
//}

//@Test
//public void testDateTime() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setDateTimeField(DateTime.now()));
//}

//@Test
//public void testDecimal() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setDecimalField(new BigDecimal(
//            100)));
//}

//@Test
//public void testEmailAddress() throws Exception {
//    _test(new ProtocolTestStruct.Builder()
//            .setEmailAddressField(new EmailAddress("test@example.com")));
//}

//@Test
//public void testEnum() throws Exception {
//    _test(new ProtocolTestStruct.Builder()
//            .setEnumField(ProtocolTestEnum.ENUMERATOR2));
//}

//@Test
//public void testI16() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setI16Field((short) 1));
//}

//@Test
//public void testI32() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setI32Field(1));
//}

//@Test
//public void testI64() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setI64Field(1));
//}

//@Test
//public void testListString() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setListStringField(ImmutableList
//            .of("test")));

//    // Empty list
//    _test(new ProtocolTestStruct.Builder().setListStringField(ImmutableList
//            .<String> of()));
//}

//@Test
//public void testMapStringString() throws Exception {
//    _test(new ProtocolTestStruct.Builder()
//            .setMapStringStringField(ImmutableMap
//                    .of("testkey", "testvalue")));

//    // Empty map
//    _test(new ProtocolTestStruct.Builder()
//            .setMapStringStringField(ImmutableMap.<String, String> of()));
//}

//@Test
//public void testSetString() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setSetStringField(ImmutableSet
//            .of("test")));

//    // Empty set
//    _test(new ProtocolTestStruct.Builder().setSetStringField(ImmutableSet
//            .<String> of()));
//}

//@Test
//public void testString() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setStringField("test"));
//}

//@Test
//public void testStruct() throws Exception {
//    _test(new ProtocolTestStruct.Builder()
//            .setStructField(new ProtocolTestStruct.Builder().setI32Field(1)
//                    .setRequiredI32Field(1).setRequiredStringField("test")
//                    .build()));

//    // Empty struct
//    _test(new ProtocolTestStruct.Builder()
//            .setStructField(new ProtocolTestStruct.Builder()
//                    .setRequiredI32Field(1).setRequiredStringField("test")
//                    .build()));
//}

//@Test
//public void testUrl() throws Exception {
//    _test(new ProtocolTestStruct.Builder().setUrlField(Url
//            .parse("http://example.com/test")));
//}

REGISTER_TYPED_TEST_CASE_P(ProtocolTest, bool_);
}
}
}
