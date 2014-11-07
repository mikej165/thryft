#ifndef _THRYFT_PROTOCOL_XDR_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_XDR_PROTOCOL_HPP_

#include "thryft/protocol/abstract_output_protocol.hpp"

namespace thryft {
namespace protocol {
class XdrOutputProtocol final : public AbstractOutputProtocol {
  public:
    XdrOutputProtocol() {
    }

  public:
    const ::std::string& to_string() const {
      return to_string_;
    }

  public:
    // OutputProtocol
    void write(const void* value, size_t value_len) override {
      do_write(value, value_len);
    }

    void write(bool value) override {
      write(static_cast<int32_t>(value ? 1 : 0));
    }

    void write(double value) override {
      int64_t int64_value;

#ifdef _WIN32
      memcpy_s(
        &int64_value,
        sizeof(int64_value),
        &value,
        sizeof(value)
      );
#else
      memcpy(
        &int64_value,
        &value,
        sizeof(value)
     );
#endif

      write(int64_value);
    }

    void write(float value) override {
      int32_t int32_value;

#ifdef _WIN32
      memcpy_s(
        &int32_value,
        sizeof(int32_value),
        &value,
        sizeof(value)
      );
#else
      memcpy(
        &int32_value,
        &value,
        sizeof(value)
     );
#endif

      write(int32_value);
    }

    void write(int32_t value) override {
      value = static_cast<int32_t>(my_htonl(static_cast<uint32_t>(value)));
      write(&value, sizeof(value));
    }

    void write(int64_t value) override {
      value = static_cast<int64_t>(my_htonll(static_cast<uint64_t>(value)));
      write(&value, sizeof(value));
    }

    void write(const char* value, size_t value_len) override {
      write(static_cast<int32_t>(value_len));

      write(static_cast<const void*>(value), value_len);

      if (value_len % 4 != 0) {
        static char zeros[] = { 0, 0, 0 };
        write(static_cast<const void*>(zeros), 4 - (value_len % 4));
      }
    }

    void write(uint32_t value) override {
      write(static_cast<int32_t>(value));
    }

    void write(uint64_t value) override {
      write(static_cast<int64_t>(value));
    }

    void write_field_begin(const char* name, const Type& type,
                                   int16_t id) override {
      write(name, strlen(name));
      write(static_cast<int32_t>(type));
      write(id);
    }

    void write_field_end() override {
    }

    void write_field_stop() override {
      write_field_begin("", Type::STOP, -1);
    }

    void write_list_begin(const Type& element_type, uint32_t size) override {
      //write(static_cast<int32_t>(element_type));
      // Stick with ONC-RPC variable-sized array rules = size + contents
      write(static_cast<int32_t>(size));
    }

    void write_list_end() override {
    }

    void write_map_begin(const Type& key_type, const Type& value_type,
                                 uint32_t size) override {
      //write(static_cast<int32_t>(key_type));
      //write(static_cast<int32_t>(value_type));
      write(static_cast<int32_t>(size));
    }

    void write_map_end() override {
    }

    void write_null() override {
      write(static_cast<int32_t>(0));
    }

    void write_struct_begin() override {
    }

    void write_struct_end() override {
    }



  private:
    static inline uint32_t my_htonl(uint32_t x) {
#ifdef __BIG_ENDIAN__
      return x;
#else
      return (x >> 24) |
             ((x << 8) & 0x00FF0000) |
             ((x >> 8) & 0x0000FF00) |
             (x << 24);
#endif
    }

    static inline uint64_t my_htonll(uint64_t x) {
#ifdef __BIG_ENDIAN__
      return x;
#else
      return (x >> 56) |
             ((x << 40) & 0x00FF000000000000ULL) |
             ((x << 24) & 0x0000FF0000000000ULL) |
             ((x << 8)  & 0x000000FF00000000ULL) |
             ((x >> 8)  & 0x00000000FF000000ULL) |
             ((x >> 24) & 0x0000000000FF0000ULL) |
             ((x >> 40) & 0x000000000000FF00ULL) |
             (x << 56);
#endif
    }

    void do_write(const void* value, size_t value_len) {
      to_string_.append(static_cast<const char*>(value), value_len);
    }

  private:
    ::std::string to_string_;
};
}
}

#endif  // _THRYFT_PROTOCOL_XDR_PROTOCOL_HPP_ 
