#ifndef _THRYFPROTOCOL_PROTOCOL_HPP_
#define _THRYFPROTOCOL_PROTOCOL_HPP_

#include <cstdint>
#include <string>

namespace thryft {
namespace protocol {
class Protocol {
public:
  class Type {
  public:
    enum Enum {
      STOP       = 0,
#ifdef VOID
#undef VOID
      VOID       = 1,
#endif
      BOOL       = 2,
      BYTE       = 3,
      I08        = 3,
      I16        = 6,
      I32        = 8,
      U64        = 9,
      I64        = 10,
      DOUBLE     = 4,
      STRING     = 11,
      UTF7       = 11,
      STRUCT     = 12,
      MAP        = 13,
      SET        = 14,
      LIST       = 15,
      UTF8       = 16,
      UTF16      = 17,
      FLOAT      = 18
    };
  };

public:
  virtual ~Protocol() {
  }

public:
  virtual std::string ReadBinary() = 0;
  virtual void ReadBinary(std::string& out_value) = 0;
  virtual bool ReadBool() = 0;
  virtual int8_t ReadByte() = 0;
  virtual double ReadDouble() = 0;
  virtual void ReadFieldBegin(std::string& out_name, Type::Enum& out_type, int16_t& out_id) = 0;
  virtual void ReadFieldEnd() = 0;
  virtual float ReadFloat() = 0;
  virtual int16_t ReadI16() = 0;
  virtual int32_t ReadI32() = 0;
  virtual int64_t ReadI64() = 0;
  virtual void ReadListBegin(Type::Enum& out_element_type, uint32_t& out_size) = 0;
  virtual void ReadListEnd() = 0;
  virtual void ReadMapBegin(Type::Enum& out_key_type, Type::Enum& out_value_type, uint32_t& out_size) = 0;
  virtual void ReadMapEnd() = 0;
  virtual void ReadSetBegin(Type::Enum& out_element_type, uint32_t& out_size) = 0;
  virtual void ReadSetEnd() = 0;
  virtual std::string ReadString() = 0;
  virtual void ReadString(std::string& out_value) = 0;
  virtual void ReadString(char*& out_value, size_t& out_value_len) = 0;
  virtual void ReadStructBegin(std::string& out_name) = 0;
  virtual void ReadStructEnd() = 0;

  virtual void WriteBinary(const void* value, size_t value_len) = 0;
  virtual void WriteBool(bool value) = 0;
  virtual void WriteByte(int8_t value) = 0;
  virtual void WriteDouble(double value) = 0;
  virtual void WriteFieldBegin(const char* name, Type::Enum type, int16_t id) = 0;
  virtual void WriteFieldEnd() = 0;
  virtual void WriteFieldStop() = 0;
  virtual void WriteFloat(float value) = 0;
  virtual void WriteI16(int16_t value) = 0;
  virtual void WriteI32(int32_t value) = 0;
  virtual void WriteI64(int64_t value) = 0;
  virtual void WriteListBegin(Type::Enum element_type, uint32_t size) = 0;
  virtual void WriteListEnd() = 0;
  virtual void WriteMapBegin(Type::Enum key_type, Type::Enum value_type, uint32_t size) = 0;
  virtual void WriteMapEnd() = 0;
  virtual void WriteSetBegin(Type::Enum element_type, uint32_t size) = 0;
  virtual void WriteSetEnd() = 0;
  virtual void WriteString(const std::string& value) = 0;
  virtual void WriteString(const char* value, size_t value_len) = 0;
  virtual void WriteStructBegin(const char* name) = 0;
  virtual void WriteStructEnd() = 0;
};
}
}

#endif  // _THRYFPROTOCOL_PROTOCOL_HPP_
