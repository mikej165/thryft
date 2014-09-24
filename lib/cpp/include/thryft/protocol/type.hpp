#ifndef _THRYFT_PROTOCOL_TYPE_HPP_
#define _THRYFT_PROTOCOL_TYPE_HPP_

#include <thryft.hpp>

namespace thryft {
namespace protocol {
class Type {
public:
  enum Enum {
    STOP = 0,
    VOID_ = 1,
    BOOL = 2,
    BYTE = 3,
    DOUBLE = 4,
    FLOAT = 18,
    I16 = 6,
    I32 = 8,
    I64 = 10,
    LIST = 15,
    MAP = 13,
    SET = 14,
    STRING = 11,
    STRUCT = 12,
    U64 = 9
  };

public:
  Type()
    : enum_(STOP) {
  }

  Type(Enum enum_)
    : enum_(enum_) {
    switch (enum_) {
    case STOP: break;
    case VOID_: break;
    case BOOL: break;
    case BYTE: break;
    case DOUBLE: break;
    case FLOAT: break;
    case I16: break;
    case I32: break;
    case I64: break;
    case LIST: break;
    case MAP: break;
    case SET: break;
    case STRING: break;
    case STRUCT: break;
    case U64: break;
    default:
      throw ::thryft::EnumValueException();
    }
  }

  Type(const Type& other)
    : enum_(other.enum_) {
    switch (enum_) {
    case STOP: break;
    case VOID_: break;
    case BOOL: break;
    case BYTE: break;
    case DOUBLE: break;
    case FLOAT: break;
    case I16: break;
    case I32: break;
    case I64: break;
    case LIST: break;
    case MAP: break;
    case SET: break;
    case STRING: break;
    case STRUCT: break;
    case U64: break;
    default:
      throw ::thryft::EnumValueException();
    }
  }

public:
  operator Enum() const {
    return enum_;
  }

  static Type read(::thryft::protocol::InputProtocol& iprot) {
    ::std::string name;
    iprot.read_string(name);
    if (name == "STOP") {
      return STOP;
    } else if (name == "VOID_") {
      return VOID_;
    } else if (name == "BOOL") {
      return BOOL;
    } else if (name == "BYTE") {
      return BYTE;
    } else if (name == "DOUBLE") {
      return DOUBLE;
    } else if (name == "FLOAT") {
      return FLOAT;
    } else if (name == "I16") {
      return I16;
    } else if (name == "I32") {
      return I32;
    } else if (name == "I64") {
      return I64;
    } else if (name == "LIST") {
      return LIST;
    } else if (name == "MAP") {
      return MAP;
    } else if (name == "SET") {
      return SET;
    } else if (name == "STRING") {
      return STRING;
    } else if (name == "STRUCT") {
      return STRUCT;
    } else if (name == "U64") {
      return U64;
    }
    return STOP;
  }

  void write(::thryft::protocol::OutputProtocol& oprot) const {
    switch (enum_) {
    case STOP: oprot.write("STOP", 4); break;
    case VOID_: oprot.write("VOID_", 5); break;
    case BOOL: oprot.write("BOOL", 4); break;
    case BYTE: oprot.write("BYTE", 4); break;
    case DOUBLE: oprot.write("DOUBLE", 6); break;
    case FLOAT: oprot.write("FLOAT", 5); break;
    case I16: oprot.write("I16", 3); break;
    case I32: oprot.write("I32", 3); break;
    case I64: oprot.write("I64", 3); break;
    case LIST: oprot.write("LIST", 4); break;
    case MAP: oprot.write("MAP", 3); break;
    case SET: oprot.write("SET", 3); break;
    case STRING: oprot.write("STRING", 6); break;
    case STRUCT: oprot.write("STRUCT", 6); break;
    case U64: oprot.write("U64", 3); break;
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

#endif  // _THRYFT_PROTOCOL_TYPE_HPP_
