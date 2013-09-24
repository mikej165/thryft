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
    return 0;
  }

  virtual double ReadDouble() {
    return 0.0;
  }

  virtual int16_t ReadI16() {
    return 0;
  }

  virtual int32_t ReadI32() {
    return 0;
  }

  virtual int64_t ReadI64() {
    return 0;
  }

  virtual void ReadFieldBegin(std::string& out_name, std::string& out_type, int16_t& out_id) {
  }

  virtual void ReadFieldEnd() {
  }

  virtual void ReadListBegin(uint16_t& out_element_type, uint32_t& out_size) {
  }

  virtual void ReadListEnd() {
  }

  virtual void ReadMapBegin(uint16_t& out_key_type, uint16_t& out_value_type, uint32_t& out_size) {
  }

  virtual void ReadMapEnd() {
  }

  virtual void ReadSetBegin(uint16_t& out_element_type, uint32_t& out_size) {
  }

  virtual void ReadSetEnd() {
  }

  virtual std::string ReadString() {
    std::string value;
    ReadString(value);
    return value;
  }

  virtual void ReadString(std::string& out_value) {
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
  }

  virtual void WriteDouble(double value) {
  }

  virtual void WriteI16(int16_t value) {
  }

  virtual void WriteI32(int32_t value) {
  }

  virtual void WriteI64(int64_t value) {
  }

  virtual void WriteFieldBegin(const char* name, uint16_t type, int16_t id) {
  }

  virtual void WriteFieldEnd() {
  }

  virtual void WriteFieldStop() {
  }

  virtual void WriteListBegin(uint16_t element_type, uint32_t size) {
  }

  virtual void WriteListEnd() {
  }

  virtual void WriteMapBegin(uint16_t key_type, uint16_t value_type, uint32_t size) {
  }

  virtual void WriteMapEnd() {
  }

  virtual void WriteSetBegin(uint16_t element_type, uint32_t size) {
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
