#ifndef _THRYFT_PROTOCOL_ABSTRACT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_ABSTRACT_PROTOCOL_HPP_

#include "thryft/protocol/protocol.hpp"

namespace thryft {
namespace protocol {
class AbstractProtocol : public Protocol {
public:
  virtual ~AbstractProtocol() {
  }

public:
  virtual std::string ReadBinary() {
    std::string value;
    ReadBinary(value);
    return value;
  }

  virtual void ReadBinary(std::string& out_value) {
  }

  virtual bool ReadBool() {
    return false;
  }

  virtual int8_t ReadByte() {
    return static_cast<int8_t>(ReadI16());
  }

  virtual double ReadDouble() {
    return 0.0;
  }

  virtual void ReadFieldBegin(std::string& out_name, Type::Enum& out_type, int16_t& out_id) {
  }

  virtual void ReadFieldEnd() {
  }

  virtual float ReadFloat() {
    return static_cast<float>(ReadDouble());
  }

  virtual int16_t ReadI16() {
    return static_cast<int16_t>(ReadI32());
  }

  virtual int32_t ReadI32() {
    return static_cast<int32_t>(ReadI64());
  }

  virtual int64_t ReadI64() {
    return 0;
  }

  virtual void ReadListBegin(Type::Enum& out_element_type, uint32_t& out_size) {
    out_size = 0;
  }

  virtual void ReadListEnd() {
  }

  virtual void ReadMapBegin(Type::Enum& out_key_type, Type::Enum& out_value_type, uint32_t& out_size) {
    out_size = 0;
  }

  virtual void ReadMapEnd() {
  }

  virtual void ReadSetBegin(Type::Enum& out_element_type, uint32_t& out_size) {
    ReadListBegin(out_element_type, out_size);
  }

  virtual void ReadSetEnd() {
    ReadListEnd();
  }

  virtual std::string ReadString() {
    std::string value;
    ReadString(value);
    return value;
  }

  virtual void ReadString(std::string& out_value) {
  }

  virtual void ReadString(char*& out_value, size_t& out_value_len) {
    out_value = NULL;
    out_value_len = 0;
  }

  virtual void ReadStructBegin(std::string& out_name) {
  }

  virtual void ReadStructEnd() {
  }

  virtual void WriteBinary(const void* value, size_t value_len) {
  }

  virtual void WriteBool(bool value) {
  }

  virtual void WriteByte(int8_t value) {
    WriteI16(value);
  }

  virtual void WriteDouble(double value) {
  }

  virtual void WriteFieldBegin(const char* name, Type::Enum type, int16_t id) {
  }

  virtual void WriteFieldEnd() {
  }

  virtual void WriteFieldStop() {
  }

  virtual void WriteFloat(float value) {
    WriteDouble(value);
  }

  virtual void WriteI16(int16_t value) {
    WriteI32(value);
  }

  virtual void WriteI32(int32_t value) {
    WriteI64(value);
  }

  virtual void WriteI64(int64_t value) {
  }

  virtual void WriteListBegin(Type::Enum element_type, uint32_t size) {
  }

  virtual void WriteListEnd() {
  }

  virtual void WriteMapBegin(Type::Enum key_type, Type::Enum value_type, uint32_t size) {
  }

  virtual void WriteMapEnd() {
  }

  virtual void WriteSetBegin(Type::Enum element_type, uint32_t size) {
    WriteListBegin(element_type, size);
  }

  virtual void WriteSetEnd() {
    WriteListEnd();
  }

  virtual void WriteString(const std::string& value) {
    WriteString(value.data(), value.size());
  }

  virtual void WriteString(const char* value, size_t value_len) {
  }

  virtual void WriteStructBegin(const char* name) {
  }

  virtual void WriteStructEnd() {
  }
};
}
}

#endif  // _THRYFT_PROTOCOL_ABSTRACT_PROTOCOL_HPP_
