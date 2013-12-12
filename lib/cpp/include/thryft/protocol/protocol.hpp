#ifndef _THRYFPROTOCOL_PROTOCOL_HPP_
#define _THRYFPROTOCOL_PROTOCOL_HPP_

#include <cstdint>
#include <string>

#include "thryft/optional.hpp"

namespace thryft {
namespace protocol {
class Protocol {
  public:
    class Type {
      public:
        enum Enum {
          STOP       = 0,
#ifdef VOID
#undef VOID
#endif
          VOID       = 1,
          BOOL       = 2,
          BYTE       = 3,
          I08        = 3,
          I16        = 6,
          I32        = 8,
          U64        = 9,
          I64        = 10,
          DOUBLE     = 4,
          STRING     = 11,
          UTF7       = 11,
          STRUCT     = 12,
          MAP        = 13,
          SET        = 14,
          LIST       = 15,
          UTF8       = 16,
          UTF16      = 17,
          FLOAT      = 18
        };
    };

  public:
    virtual ~Protocol() {
    }

  public:
    template <typename T>
    void read(Optional<T>& out_value) {
      T temp_value;
      read(out_value);
      out_value = temp_value;
    }

    // Byte
    void read(int8_t& out_value) {
      out_value = read_byte();
    }

    // Bool
    void read(bool& out_value) {
      out_value = read_bool();
    }

    // Double
    void read(double& out_value) {
      out_value = read_double();
    }

    // Float
    void read(float& out_value) {
      out_value = read_float();
    }

    // I16
    void read(int16_t& out_value) {
      out_value = read_i16();
    }

    // I32
    void read(int32_t& out_value) {
      out_value = read_i32();
    }

    // I64
    void read(int64_t& out_value) {
      out_value = read_i16();
    }

    // String
    void read(std::string& out_value) {
      read_string(out_value);
    }

    void read(::thryft::Base& out_value) {
      out_value.read(*this);
    }

    virtual void read_binary(std::string& out_value) = 0;
    virtual bool read_bool() = 0;
    virtual int8_t read_byte() = 0;
    virtual double read_double() = 0;
    virtual void read_field_begin(std::string& out_name, Type::Enum& out_type,
                                  int16_t& out_id) = 0;
    virtual void read_field_end() = 0;
    virtual float read_float() = 0;
    virtual int16_t read_i16() = 0;
    virtual int32_t read_i32() = 0;
    virtual int64_t read_i64() = 0;
    virtual void read_list_begin(Type::Enum& out_element_type,
                                 uint32_t& out_size) = 0;
    virtual void read_list_end() = 0;
    virtual void read_map_begin(Type::Enum& out_key_type,
                                Type::Enum& out_value_type, uint32_t& out_size) = 0;
    virtual void read_map_end() = 0;
    virtual void read_set_begin(Type::Enum& out_element_type,
                                uint32_t& out_size) = 0;
    virtual void read_set_end() = 0;

    void read_string(Optional< ::std::string >& out_value) {
      std::string temp_value;
      read_string(temp_value);
      out_value = temp_value;
    }
    virtual void read_string(std::string& out_value) = 0;
    virtual void read_string(char*& out_value, size_t& out_value_len) = 0;

    virtual void read_struct_begin() = 0;
    virtual void read_struct_end() = 0;

    // Binary
    virtual void write(const void* value, size_t value_len) = 0;

    // Bool
    virtual void write(bool value) = 0;

    // Byte
    virtual void write(int8_t value) = 0;

    // Double
    virtual void write(double value) = 0;

    // Field
    virtual void write_field_begin(const char* name, Type::Enum type,
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

    virtual void write_list_begin(Type::Enum element_type, uint32_t size) = 0;
    virtual void write_list_end() = 0;

    virtual void write_map_begin(Type::Enum key_type, Type::Enum value_type,
                                 uint32_t size) = 0;
    virtual void write_map_end() = 0;

    virtual void write_null() = 0;

    virtual void write_set_begin(Type::Enum element_type, uint32_t size) = 0;
    virtual void write_set_end() = 0;

    virtual void write_struct_begin() = 0;
    virtual void write_struct_end() = 0;
};
}
}

#endif  // _THRYFPROTOCOL_PROTOCOL_HPP_
