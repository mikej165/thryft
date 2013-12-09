#ifndef _THRYFT_PROTOCOL_STACKED_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_STACKED_PROTOCOL_HPP_

#include <stack>

#include "thryft/protocol/abstract_protocol.hpp"

namespace thryft {
namespace protocol {
class StackedProtocol : public Protocol {
public:
  virtual ~StackedProtocol() {
    while (!protocol_stack_.empty()) {
      delete protocol_stack_.top();
      protocol_stack_.pop();
    }
  }

public:
  virtual void reset() {
    while (!protocol_stack_.empty()) {
      delete protocol_stack_.top();
      protocol_stack_.pop();
    }
  }

public:
  // Protocol
  virtual void read_binary(std::string& out_value) {
    protocol_stack_.top()->read_binary(out_value);
  }

  virtual bool read_bool() {
    return protocol_stack_.top()->read_bool();
  }

  virtual int8_t read_byte() {
    return protocol_stack_.top()->read_byte();
  }

  virtual double read_double() {
    return protocol_stack_.top()->read_double();
  }

  virtual void read_field_begin(std::string& out_name, Type::Enum& out_type, int16_t& out_id) {
    protocol_stack_.top()->read_field_begin(out_name, out_type, out_id);
  }

  virtual void read_field_end() {
    protocol_stack_.top()->read_field_end();
  }

  virtual float read_float() {
    return protocol_stack_.top()->read_float();
  }

  virtual int16_t read_i16() {
    return protocol_stack_.top()->read_i16();
  }

  virtual int32_t read_i32() {
    return protocol_stack_.top()->read_i32();
  }

  virtual int64_t read_i64() {
    return protocol_stack_.top()->read_i64();
  }

  virtual void read_list_begin(Type::Enum& out_element_type, uint32_t& out_size) {
    protocol_stack_.top()->read_list_begin(out_element_type, out_size);
  }

  virtual void read_list_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
  }

  virtual void read_map_begin(Type::Enum& out_key_type, Type::Enum& out_value_type, uint32_t& out_size) {
    protocol_stack_.top()->read_map_begin(out_key_type, out_value_type, out_size);
  }

  virtual void read_map_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
  }

  virtual void read_set_begin(Type::Enum& out_element_type, uint32_t& out_size) {
    protocol_stack_.top()->read_set_begin(out_element_type, out_size);
  }

  virtual void read_set_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
  }
  
  virtual void read_string(std::string& out_value) {
    protocol_stack_.top()->read_string(out_value);
  }

  virtual void read_string(char*& out_value, size_t& out_value_len) {
    protocol_stack_.top()->read_string(out_value, out_value_len);
  }

  virtual void read_struct_begin() {
    protocol_stack_.top()->read_struct_begin();
  }

  virtual void read_struct_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
  }

  virtual void write(const void* value, size_t value_len) {
    protocol_stack_.top()->write(value, value_len);
  }
  
  // Bool
  virtual void write(bool value) {
    protocol_stack_.top()->write(value);
  }

  // Byte
  virtual void write(int8_t value) {
    protocol_stack_.top()->write(value);
  }

  // Double
  virtual void write(double value) {
    protocol_stack_.top()->write(value);
  }

  // Field
  virtual void write_field_begin(const char* name, Type::Enum type, int16_t id) {
    protocol_stack_.top()->write_field_begin(name, type, id);
  }

  virtual void write_field_end() {
    protocol_stack_.top()->write_field_end();
  }

  virtual void write_field_stop() {
    protocol_stack_.top()->write_field_stop();
  }

  virtual void write(float value) {
    protocol_stack_.top()->write(value);
  }

  virtual void write(int16_t value) {
    protocol_stack_.top()->write(value);
  }

  virtual void write(int32_t value) {
    protocol_stack_.top()->write(value);
  }

  virtual void write(int64_t value) {
    protocol_stack_.top()->write(value);
  }

  virtual void write(const ::thryft::Base& value) {
    protocol_stack_.top()->write(value);
  }

  virtual void write(const std::string& value) {
    protocol_stack_.top()->write(value);
  }

  virtual void write(const char* value, size_t value_len) {
    protocol_stack_.top()->write(value, value_len);
  }

  virtual void write_list_begin(Type::Enum element_type, uint32_t size) {
    protocol_stack_.top()->write_list_begin(element_type, size);
  }

  virtual void write_list_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
    protocol_stack_.top()->write_list_end();
  }

  virtual void write_map_begin(Type::Enum key_type, Type::Enum value_type, uint32_t size) {
    protocol_stack_.top()->write_map_begin(key_type, value_type, size);
  }

  virtual void write_map_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
    protocol_stack_.top()->write_map_end();
  }

  virtual void write_null() {
    protocol_stack_.top()->write_null();
  }

  virtual void write_set_begin(Type::Enum element_type, uint32_t size) {
    protocol_stack_.top()->write_set_begin(element_type, size);
  }

  virtual void write_set_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
    protocol_stack_.top()->write_set_end();
  }

  virtual void write_struct_begin() {
    protocol_stack_.top()->write_struct_begin();
  }

  virtual void write_struct_end() {
    delete protocol_stack_.top();
    protocol_stack_.pop();
    protocol_stack_.top()->write_struct_end();
  }

protected:
  ::std::stack< Protocol* >& protocol_stack() {
    return protocol_stack_;
  }

private:
  ::std::stack< Protocol* > protocol_stack_;
};
}
}

#endif  // _THRYFT_PROTOCOL_STACKED_PROTOCOL_HPP_