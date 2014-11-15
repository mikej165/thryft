#include "thryft/native/variant.hpp"

#include "gtest/gtest.h"

namespace thryft_test {
namespace native {
namespace test {
using ::thryft::native::Variant;

TEST(Variant, bool) {
  ASSERT_EQ(Variant(true).type(), Variant::Type::BOOL);
  ASSERT_EQ(Variant(false).type(), Variant::Type::BOOL);
  ASSERT_EQ(Variant(true), true);
  ASSERT_EQ(Variant(false), false);
  ASSERT_NE(Variant(true), false);
}

TEST(Variant, copy) {
  ASSERT_EQ(Variant(Variant(1)), 1);
}

TEST(Variant, double) {
  ASSERT_EQ(Variant(1.0), 1.0);
  ASSERT_EQ(Variant(DBL_MIN), DBL_MIN);
  ASSERT_EQ(Variant(DBL_MAX), DBL_MAX);
}

TEST(Variant, int64) {
  ASSERT_EQ(Variant(static_cast<int64_t>(INT32_MIN-1)), static_cast<int64_t>(INT32_MIN-1));
}

TEST(variant, string) {
  ASSERT_EQ(Variant("test"), "test");
  ASSERT_EQ(Variant("test", 3), "tes");
  ASSERT_EQ(0, strncmp(static_cast<const char*>(Variant("test")), "test", 4));
  ASSERT_EQ(0, memcmp(static_cast<const void*>(Variant("test")), "test", 4));
  char* test = new char[4];
  memcpy(test, "test", 4);
  ASSERT_EQ(Variant(test, 4), "test"); // Steals test
}

TEST(Variant, uint32) {
  ASSERT_EQ(Variant(static_cast<uint32_t>(UINT16_MAX+1)), static_cast<uint32_t>(UINT16_MAX+1));
}

TEST(Variant, uint64) {
  ASSERT_EQ(Variant(static_cast<uint64_t>(UINT32_MAX+1)), static_cast<uint64_t>(UINT32_MAX+1));
}
}
}
}
