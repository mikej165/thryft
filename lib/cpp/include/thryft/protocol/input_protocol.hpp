#ifndef _THRYFT_PROTOCOL_INPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_INPUT_PROTOCOL_HPP_

#include <stdint.h>
#include <string>

#include "thryft/protocol/input_protocol_exception.hpp"
#include "thryft/protocol/type.hpp"

namespace thryft {
class Base;

namespace native {
class Variant;
}

namespace protocol {
class InputProtocol {
  public:
    virtual ~InputProtocol() {
    }

  public:
    virtual void read(bool& out_value) = 0;
    virtual void read(int8_t& out_value) = 0;
    virtual void read(double& out_value) = 0;
    virtual void read(float& out_value) = 0;
    virtual void read(int16_t& out_value) = 0;
    virtual void read(int32_t& out_value) = 0;
    virtual void read(int64_t& out_value) = 0;
    virtual void read(std::string& out_value) = 0;
    virtual void read(::thryft::Base& out_value) = 0;
    virtual void read(::thryft::native::Variant& out_value) = 0;

    virtual void read_binary(std::string& out_value) = 0;
    virtual bool read_bool() = 0;
    virtual int8_t read_byte() = 0;
    virtual double read_double() = 0;
    virtual void read_field_begin(std::string& out_name, Type& out_type,
                                  int16_t& out_id) = 0;
    virtual void read_field_end() = 0;
    virtual float read_float() = 0;
    virtual int16_t read_i16() = 0;
    virtual int32_t read_i32() = 0;
    virtual int64_t read_i64() = 0;
    virtual void read_list_begin(Type& out_element_type,
                                 uint32_t& out_size) = 0;
    virtual void read_list_end() = 0;
    virtual void read_map_begin(Type& out_key_type,
                                Type& out_value_type, uint32_t& out_size) = 0;
    virtual void read_map_end() = 0;
    virtual void read_set_begin(Type& out_element_type,
                                uint32_t& out_size) = 0;
    virtual void read_set_end() = 0;
    virtual ::std::string read_string() = 0;
    virtual void read_string(std::string& out_value) = 0;
    virtual void read_string(char*& out_value, size_t& out_value_len) = 0;
    virtual void read_struct_begin() = 0;
    virtual void read_struct_end() = 0;
    virtual uint32_t read_u32() = 0;
    virtual uint64_t read_u64() = 0;
    virtual ::thryft::native::Variant read_variant() = 0;
};
}
}

#endif  // _THRYFT_PROTOCOL_INPUT_PROTOCOL_HPP_
