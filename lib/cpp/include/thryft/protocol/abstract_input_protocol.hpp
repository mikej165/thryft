#ifndef _THRYFT_PROTOCOL_ABSTRACT_INPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_ABSTRACT_INPUT_PROTOCOL_HPP_

#include "thryft/base.hpp"
#include "thryft/protocol/input_protocol.hpp"
#include "thryft/native/variant.hpp"

namespace thryft {
namespace protocol {
class AbstractInputProtocol : public InputProtocol {
  public:
    virtual ~AbstractInputProtocol() {
    }

  public:
    virtual void read(bool& out_value) override {
      out_value = read_bool();
    }

    virtual void read(int8_t& out_value) override {
      out_value = read_byte();
    }

    virtual void read(double& out_value) override {
      out_value = read_double();
    }

    virtual void read(float& out_value) override {
      out_value = read_float();
    }

    virtual void read(int16_t& out_value) override {
      out_value = read_i16();
    }

    virtual void read(int32_t& out_value) override {
      out_value = read_i32();
    }

    virtual void read(int64_t& out_value) override {
      out_value = read_i64();
    }

    virtual void read(::thryft::native::Variant& out_value) override {
      out_value = read_variant();
    }

    void read(std::string& out_value) override {
      read_string(out_value);
    }

    void read(::thryft::Base& out_value) override {
      out_value.read(*this);
    }

    virtual void read_binary(std::string& out_value) override {
    }

    virtual bool read_bool() override {
      return false;
    }

    virtual int8_t read_byte() override {
      return static_cast<int8_t>(read_i16());
    }

    virtual double read_double() override {
      return 0.0;
    }

    virtual void read_field_begin(std::string& out_name, Type& out_type,
                                  int16_t& out_id) override {
    }

    virtual void read_field_end() override {
    }

    virtual float read_float() override {
      return static_cast<float>(read_double());
    }

    virtual int16_t read_i16() override {
      return static_cast<int16_t>(read_i32());
    }

    virtual int32_t read_i32() override {
      return static_cast<int32_t>(read_i64());
    }

    virtual int64_t read_i64() override {
      return 0;
    }

    virtual void read_list_begin(Type& out_element_type, uint32_t& out_size) override {
      out_size = 0;
    }

    virtual void read_list_end() override {
    }

    virtual void read_map_begin(Type& out_key_type,
                                Type& out_value_type, uint32_t& out_size) override {
      out_size = 0;
    }

    virtual void read_map_end() override {
    }

    virtual void read_set_begin(Type& out_element_type, uint32_t& out_size) override {
      read_list_begin(out_element_type, out_size);
    }

    virtual void read_set_end() override {
      read_list_end();
    }

    virtual std::string read_string() override {
      std::string value;
      read(value);
      return value;
    }

    virtual void read_string(::std::string& out_value) override {
    }

    virtual void read_string(char*& out_value, size_t& out_value_len) override {
      out_value = NULL;
      out_value_len = 0;
    }

    virtual void read_struct_begin() override {
    }

    virtual void read_struct_end() override {
    }

    virtual uint32_t read_u32() override {
      return static_cast<uint32_t>(read_u64());
    }

    virtual uint64_t read_u64() override {
      return static_cast<uint64_t>(0);
    }

    virtual ::thryft::native::Variant read_variant() override {
      return ::thryft::native::Variant();
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_ABSTRACT_INPUT_PROTOCOL_HPP_
