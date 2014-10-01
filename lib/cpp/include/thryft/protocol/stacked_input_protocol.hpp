#ifndef _THRYFT_PROTOCOL_STACKED_INPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_STACKED_INPUT_PROTOCOL_HPP_

#include <stack>

#include "thryft/protocol/abstract_input_protocol.hpp"

namespace thryft {
namespace protocol {
class StackedInputProtocol : public AbstractInputProtocol {
  public:
    virtual ~StackedInputProtocol() {
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
    // InputProtocol
    virtual void read_binary(std::string& out_value) override {
      protocol_stack_.top()->read_binary(out_value);
    }

    virtual bool read_bool() override {
      return protocol_stack_.top()->read_bool();
    }

    virtual int8_t read_byte() override {
      return protocol_stack_.top()->read_byte();
    }

    virtual double read_double() override {
      return protocol_stack_.top()->read_double();
    }

    virtual void read_field_begin(std::string& out_name, Type& out_type,
                                  int16_t& out_id) override {
      protocol_stack_.top()->read_field_begin(out_name, out_type, out_id);
    }

    virtual void read_field_end() override {
      protocol_stack_.top()->read_field_end();
    }

    virtual float read_float() override {
      return protocol_stack_.top()->read_float();
    }

    virtual int16_t read_i16() override {
      return protocol_stack_.top()->read_i16();
    }

    virtual int32_t read_i32() override {
      return protocol_stack_.top()->read_i32();
    }

    virtual int64_t read_i64() override {
      return protocol_stack_.top()->read_i64();
    }

    virtual void read_list_begin(Type& out_element_type, uint32_t& out_size) override {
      protocol_stack_.top()->read_list_begin(out_element_type, out_size);
    }

    virtual void read_list_end() override {
      delete protocol_stack_.top();
      protocol_stack_.pop();
    }

    virtual void read_map_begin(Type& out_key_type,
                                Type& out_value_type, uint32_t& out_size) override {
      protocol_stack_.top()->read_map_begin(out_key_type, out_value_type, out_size);
    }

    virtual void read_map_end() override {
      delete protocol_stack_.top();
      protocol_stack_.pop();
    }

    virtual void read_set_begin(Type& out_element_type, uint32_t& out_size) override {
      protocol_stack_.top()->read_set_begin(out_element_type, out_size);
    }

    virtual void read_set_end() override {
      delete protocol_stack_.top();
      protocol_stack_.pop();
    }

    virtual void read_string(std::string& out_value) override {
      protocol_stack_.top()->read_string(out_value);
    }

    virtual void read_string(char*& out_value, size_t& out_value_len) override {
      protocol_stack_.top()->read_string(out_value, out_value_len);
    }

    virtual void read_struct_begin() override {
      protocol_stack_.top()->read_struct_begin();
    }

    virtual void read_struct_end() override {
      delete protocol_stack_.top();
      protocol_stack_.pop();
    }

    virtual uint32_t read_u32() override {
      return protocol_stack_.top()->read_u32();
    }

    virtual uint64_t read_u64() override {
      return protocol_stack_.top()->read_u64();
    }

  protected:
    ::std::stack< InputProtocol* >& protocol_stack() {
      return protocol_stack_;
    }

  private:
    ::std::stack< InputProtocol* > protocol_stack_;
};
}
}

#endif  // _THRYFT_PROTOCOL_STACKED_INPUT_PROTOCOL_HPP_