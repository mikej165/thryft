#ifndef _THRYFT_TEST_PROTOCOL_TEST_PROTOCOL_TEST_ENUM_HPP_
#define _THRYFT_TEST_PROTOCOL_TEST_PROTOCOL_TEST_ENUM_HPP_

#include <thryft.hpp>

namespace thryft_test {
namespace protocol {
namespace test {
class ProtocolTestEnum {
public:
  enum Enum {
    ENUMERATOR1 = 1,
    ENUMERATOR2 = 2
  };

public:
  ProtocolTestEnum()
    : enum_(ENUMERATOR1) {
  }

  ProtocolTestEnum(Enum enum_)
    : enum_(enum_) {
    switch (enum_) {
    case ENUMERATOR1: break;
    case ENUMERATOR2: break;
    default:
      throw ::thryft::EnumValueException();
    }
  }

  ProtocolTestEnum(const ProtocolTestEnum& other)
    : enum_(other.enum_) {
    switch (enum_) {
    case ENUMERATOR1: break;
    case ENUMERATOR2: break;
    default:
      throw ::thryft::EnumValueException();
    }
  }

public:
  operator Enum() const {
    return enum_;
  }

  static ProtocolTestEnum read(::thryft::protocol::InputProtocol& iprot) {
    ::std::string name;
    iprot.read_string(name);
    if (name == "ENUMERATOR1") {
      return ENUMERATOR1;
    } else if (name == "ENUMERATOR2") {
      return ENUMERATOR2;
    }
    return ENUMERATOR1;
  }

  void write(::thryft::protocol::OutputProtocol& oprot) const {
    switch (enum_) {
    case ENUMERATOR1: oprot.write("ENUMERATOR1", 11); break;
    case ENUMERATOR2: oprot.write("ENUMERATOR2", 11); break;
    default:
      oprot.write_null();
      break;
    }
  }

private:
  Enum enum_;
};
}
}
}

#endif  // _THRYFT_TEST_PROTOCOL_TEST_PROTOCOL_TEST_ENUM_HPP_
