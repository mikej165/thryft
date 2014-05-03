#ifndef _THRYFT_PROTOCOL_STACKED_OUTPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_STACKED_OUTPUT_PROTOCOL_HPP_

#include <stack>

#include "thryft/protocol/abstract_output_protocol.hpp"

namespace thryft {
namespace protocol {
class StackedOutputProtocol : public AbstractOutputProtocol {
  public:
    virtual ~StackedOutputProtocol() {
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
    // OutputProtocol
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
    virtual void write_field_begin(const char* name, Type type, int16_t id) {
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

    virtual void write(uint32_t value) {
      protocol_stack_.top()->write(value);
    }

    virtual void write(uint64_t value) {
      protocol_stack_.top()->write(value);
    }

    virtual void write_list_begin(Type element_type, uint32_t size) {
      protocol_stack_.top()->write_list_begin(element_type, size);
    }

    virtual void write_list_end() {
      delete protocol_stack_.top();
      protocol_stack_.pop();
      protocol_stack_.top()->write_list_end();
    }

    virtual void write_map_begin(Type key_type, Type value_type,
                                 uint32_t size) {
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

    virtual void write_set_begin(Type element_type, uint32_t size) {
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
    ::std::stack< OutputProtocol* >& protocol_stack() {
      return protocol_stack_;
    }

  private:
    ::std::stack< OutputProtocol* > protocol_stack_;
};
}
}

#endif  // _THRYFT_PROTOCOL_STACKED_OUTPUT_PROTOCOL_HPP_