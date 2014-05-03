#ifndef _THRYFT_PROTOCOL_XDR_INPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_XDR_INPUT_PROTOCOL_HPP_

#include "thryft/protocol/abstract_input_protocol.hpp"
#include "thryft/protocol/xdr_output_protocol.hpp"

namespace thryft {
namespace protocol {
class XdrInputProtocol : public AbstractInputProtocol {
  public:
    typedef XdrOutputProtocol OutputProtocolT;

  public:
    XdrInputProtocol(const ::std::string& xdr)
      : xdr_(xdr) {
      xdr_p_ = reinterpret_cast<const uint8_t*>(xdr_.data());
      xdr_pe_ = xdr_p_ + xdr_.size();
    }

    XdrInputProtocol(const uint8_t* xdr, size_t xdr_len) {
      xdr_p_ = xdr;
      xdr_pe_ = xdr_p_ + xdr_len;
    }

  public:
    // InputProtocol
    bool read_bool() {
      return read_i32() == 1;
    }

    double read_double() {
      int64_t int64_value = read_i64();
      double value;
#ifdef _WIN32
      memcpy_s(&value, sizeof(value), &int64_value, sizeof(int64_value));
#else
      memcpy(&value, &int64_value, sizeof(int64_value));
#endif
      return value;
    }

    void read_field_begin(std::string& out_name, Type& out_type,
                          int16_t& out_id) {
      read_string(out_name);
      out_type = static_cast<Type>(read_i32());
      out_id = read_i16();
    }

    float read_float() {
      int32_t int32_value = read_i32();
      float value;
#ifdef _WIN32
      memcpy_s(&value, sizeof(value), &int32_value, sizeof(int32_value));
#else
      memcpy(&value, &int32_value, sizeof(int32_value));
#endif
      return value;
    }

    int32_t read_i32() {
      int32_t value;
      read(&value, sizeof(value));
      return static_cast<int32_t>(my_ntohl(static_cast<uint32_t>(value)));
    }

    int64_t read_i64() {
      int64_t value;
      read(&value, sizeof(value));
      return static_cast<int64_t>(my_ntohll(static_cast<uint64_t>(value)));
    }

    void read_list_begin(Type& out_element_type,
                         size_t& out_size) {
      //out_element_type = static_cast<Type>(read_i32());
      // Stick with ONC-RPC variable-sized array rules = size + contents
      out_size = static_cast<size_t>(read_i32());
    }

    void read_list_end() {
    }

    virtual void read_map_begin(Type& out_key_type,
                                Type& out_value_type, uint32_t& out_size) {
      //out_key_type = static_cast<Type>(read_i32());
      //out_value_type = static_cast<Type>(read_i32());
      out_size = static_cast<uint32_t>(read_i32());
    }

    void read_string(std::string& out_value) {
      size_t size = static_cast<size_t>(read_i32());
      if (size > 0 && size < UINT16_MAX) {
        size_t padded_size = size % 4;
        if (padded_size == 0) {
          padded_size = size;
        } else {
          padded_size = size + 4 - padded_size;
        }

        out_value.resize(padded_size);
        read(const_cast<char*>(out_value.data()), padded_size);
        out_value.resize(size);
      }
    }

    void read_string(char*& out_value, size_t& out_value_len) {
      size_t size = static_cast<size_t>(read_i32());
      if (size > 0 && size < UINT16_MAX) {
        size_t padded_size = size % 4;
        if (padded_size == 0) {
          padded_size = size;
        } else {
          padded_size = size + 4 - padded_size;
        }

        out_value = new char[padded_size];
        read(out_value, padded_size);
        out_value_len = size;
      } else {
        out_value_len = 0;
      }
    }

  private:
    static inline uint32_t my_ntohl(uint32_t x) {
#ifdef __BIG_ENDIAN__
      return x;
#else
      return (x >> 24) |
             ((x << 8) & 0x00FF0000) |
             ((x >> 8) & 0x0000FF00) |
             (x << 24);
#endif
    }

    static inline uint64_t my_ntohll(uint64_t x) {
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

    void read(void* buf, size_t len) {
      if (xdr_p_ + len <= xdr_pe_) {
        memcpy(buf, xdr_p_, len);
        xdr_p_ += len;
      }
    }

  private:
    ::std::string xdr_;
    const uint8_t* xdr_p_, *xdr_pe_;
};
}
}

#endif  // _THRYFT_PROTOCOL_XDR_INPUT_PROTOCOL_HPP_
