#ifndef _THRYFT_PROTOCOL_ABSTRACT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_ABSTRACT_PROTOCOL_HPP_

#include <string>

#include "thryft/protocol/protocol.hpp"

namespace thryft {
namespace protocol {
class AbstractProtocol : public Protocol {
  public:
    virtual ~AbstractProtocol() {
    }

  public:
    virtual std::string read_binary() {
      std::string value;
      read_binary(value);
      return value;
    }

    virtual void read_binary(std::string& out_value) {
    }

    virtual bool read_bool() {
      return false;
    }

    virtual int8_t read_byte() {
      return static_cast<int8_t>(read_i16());
    }

    virtual double read_double() {
      return 0.0;
    }

    virtual void read_field_begin(std::string& out_name, Type::Enum& out_type,
                                  int16_t& out_id) {
    }

    virtual void read_field_end() {
    }

    virtual float read_float() {
      return static_cast<float>(read_double());
    }

    virtual int16_t read_i16() {
      return static_cast<int16_t>(read_i32());
    }

    virtual int32_t read_i32() {
      return static_cast<int32_t>(read_i64());
    }

    virtual int64_t read_i64() {
      return 0;
    }

    virtual void read_list_begin(Type::Enum& out_element_type, uint32_t& out_size) {
      out_size = 0;
    }

    virtual void read_list_end() {
    }

    virtual void read_map_begin(Type::Enum& out_key_type,
                                Type::Enum& out_value_type, uint32_t& out_size) {
      out_size = 0;
    }

    virtual void read_map_end() {
    }

    virtual void read_set_begin(Type::Enum& out_element_type, uint32_t& out_size) {
      read_list_begin(out_element_type, out_size);
    }

    virtual void read_set_end() {
      read_list_end();
    }

    virtual std::string read_string() {
      std::string value;
      read_string(value);
      return value;
    }

    virtual void read_string(std::string& out_value) {
    }

    virtual void read_string(char*& out_value, size_t& out_value_len) {
      out_value = NULL;
      out_value_len = 0;
    }

    virtual void read_struct_begin() {
    }

    virtual void read_struct_end() {
    }

    virtual void write(const void* value, size_t value_len) {
    }

    virtual void write(bool value) {
    }

    virtual void write(int8_t value) {
      write(static_cast<int16_t>(value));
    }

    virtual void write(double value) {
    }

    virtual void write(float value) {
      write(static_cast<double>(value));
    }

    virtual void write(int16_t value) {
      write(static_cast<int32_t>(value));
    }

    virtual void write(int32_t value) {
      write(static_cast<int64_t>(value));
    }

    virtual void write(int64_t value) {
    }

    virtual void write(const ::thryft::Base& value) {
      value.write(*this);
    }

    virtual void write(const std::string& value) {
      write(value.data(), value.size());
    }

    virtual void write(const char* value, size_t value_len) {
    }

    virtual void write_field_begin(const char* name, Type::Enum type, int16_t id) {
    }

    virtual void write_field_end() {
    }

    virtual void write_field_stop() {
    }

    virtual void write_list_begin(Type::Enum element_type, uint32_t size) {
    }

    virtual void write_list_end() {
    }

    virtual void write_map_begin(Type::Enum key_type, Type::Enum value_type,
                                 uint32_t size) {
    }

    virtual void write_map_end() {
    }

    virtual void write_set_begin(Type::Enum element_type, uint32_t size) {
      write_list_begin(element_type, size);
    }

    virtual void write_set_end() {
      write_list_end();
    }

    virtual void write_struct_begin() {
    }

    virtual void write_struct_end() {
    }

    virtual void write_null() {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_ABSTRACT_PROTOCOL_HPP_
