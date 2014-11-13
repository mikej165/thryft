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
      static_cast<InputProtocol*>(this)->read_string(out_value);
    }

    void read(::thryft::Base& out_value) override {
      out_value.read(*this);
    }

    virtual void read_binary(std::string& out_value) override {
      static_cast<InputProtocol*>(this)->read_string(out_value);
    }

    virtual int8_t read_byte() override {
      return static_cast<int8_t>(read_i16());
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

    virtual void read_set_begin(Type& out_element_type, uint32_t& out_size) override {
      read_list_begin(out_element_type, out_size);
    }

    virtual void read_set_end() override {
      read_list_end();
    }

    virtual std::string read_string() override {
      std::string value;
      static_cast<InputProtocol*>(this)->read_string(value);
      return value;
    }

    virtual uint32_t read_u32() override {
      return static_cast<uint32_t>(read_u64());
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_ABSTRACT_INPUT_PROTOCOL_HPP_
