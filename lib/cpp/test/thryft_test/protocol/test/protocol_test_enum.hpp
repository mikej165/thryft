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

    static Enum read(::thryft::protocol::InputProtocol& iprot) {
      ::std::string name;
      iprot.read_string(name);
      if (name == "ENUMERATOR1") {
        return ENUMERATOR1;
      } else if (name == "ENUMERATOR2") {
        return ENUMERATOR2;
      }
      return ENUMERATOR1;
    }

    static void write(::thryft::protocol::OutputProtocol& oprot, Enum value) {
      switch (value) {
      case ENUMERATOR1:
        oprot.write("ENUMERATOR1", 11);
        break;
      case ENUMERATOR2:
        oprot.write("ENUMERATOR2", 11);
        break;
      default:
        oprot.write_null();
        break;
      }
    }
};
}
}
}

#endif  // _THRYFT_TEST_PROTOCOL_TEST_PROTOCOL_TEST_ENUM_HPP_
