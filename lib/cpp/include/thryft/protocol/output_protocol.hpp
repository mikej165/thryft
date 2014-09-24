#ifndef _THRYFT_PROTOCOL_OUTPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_OUTPUT_PROTOCOL_HPP_

#include <cstdint>
#include <string>

#include "thryft/protocol/output_protocol_exception.hpp"

namespace thryft {
class Base;

namespace native {
class Variant;
}

namespace protocol {
class Type;

class OutputProtocol {
  public:
    virtual ~OutputProtocol() {
    }

  public:
    // Binary
    virtual void write(const void* value, size_t value_len) = 0;

    // Bool
    virtual void write(bool value) = 0;

    // Byte
    virtual void write(int8_t value) = 0;

    // Double
    virtual void write(double value) = 0;

    // Field
    virtual void write_field_begin(const char* name, const Type& type,
                                   int16_t id) = 0;
    virtual void write_field_end() = 0;
    virtual void write_field_stop() = 0;

    // Float
    virtual void write(float value) = 0;

    // I16
    virtual void write(int16_t value) = 0;

    // I32
    virtual void write(int32_t value) = 0;

    // I64
    virtual void write(int64_t value) = 0;

    // List/Set/Struct
    virtual void write(const ::thryft::Base& value) = 0;

    // String
    virtual void write(const std::string& value) = 0;

    // String
    virtual void write(const char* value, size_t value_len) = 0;

    // U32
    virtual void write(uint32_t value) = 0;

    // U64
    virtual void write(uint64_t value) = 0;

    // Variant
    virtual void write(const ::thryft::native::Variant& value) = 0;

    virtual void write_list_begin(const Type& element_type, uint32_t size) = 0;
    virtual void write_list_end() = 0;

    virtual void write_map_begin(const Type& key_type, const Type& value_type,
                                 uint32_t size) = 0;
    virtual void write_map_end() = 0;

    virtual void write_null() = 0;

    virtual void write_set_begin(const Type& element_type, uint32_t size) = 0;
    virtual void write_set_end() = 0;

    virtual void write_struct_begin() = 0;
    virtual void write_struct_end() = 0;
};
}
}

#endif  // _THRYFT_PROTOCOL_OUTPUT_PROTOCOL_HPP_
