#ifndef _THRYFT_NATIVE_VARIANT_HPP_
#define _THRYFT_NATIVE_VARIANT_HPP_

#include <cstdint>
#include <sstream>

#include "thryft/protocol/input_protocol.hpp"
#include "thryft/protocol/output_protocol.hpp"
#include "thryft/protocol/type.hpp"
#include "thryft/struct.hpp"

namespace thryft {
namespace native {
#ifdef _WIN32
#pragma warning(push)
#pragma warning(disable: 4127 4826)
#endif
class Variant {
  public:
    typedef ::thryft::protocol::Type Type;

  public:
    Variant()
      : type_(Type::VOID_) {
      string_value_ = { 0, 0 };
    }

    Variant(const Type& type, uint64_t value) {
      switch (type) {
      case Type::BOOL:
        init(value == 0);
        break;
      case Type::DOUBLE:
        init(static_cast<double>(value));
        break;
      case Type::I64:
        init(static_cast<int64_t>(value));
        break;
      case Type::U64:
        init(value);
        break;
      case Type::VOID_:
      default:
        string_value_ = { 0, 0 };
        type_ = Type::VOID_;
        break;
      }
    }

    Variant(bool value) {
      init(value);
    }

    Variant(double value) {
      init(value);
    }

    Variant(int32_t value) {
      init(static_cast<int64_t>(value));
    }

    Variant(int64_t value) {
      init(value);
    }

    Variant(uint32_t value) {
      init(static_cast<uint64_t>(value));
    }

    Variant(uint64_t value) {
      init(value);
    }

    Variant(const char* value) {
      init(value, strlen(value));
    }

    Variant(char* value) {
      init(value, strlen(value));
    }

    Variant(const void* value, size_t value_len) {
      init(value, value_len);
    }

    Variant(void* value, size_t value_len) {
      init(value, value_len);
    }

    Variant(const ::std::string& value) {
      init(value.data(), value.size());
    }

    Variant(const Variant& other) {
      init(other);
    }

    ~Variant() {
      reset();
    }

  public:
    size_t size() const {
      switch (type_) {
      case Type::BOOL:
        return sizeof(bool_value_);
      case Type::DOUBLE:
        return sizeof(double_value_);
      case Type::I64:
        return sizeof(signed_integer_value_);
      case Type::STRING:
        return static_cast<size_t>(string_value_.len);
      case Type::U64:
        return sizeof(unsigned_integer_value_);
      default:
        return 0;
      }
    }

    const Type& type() const {
      return type_;
    }

  public:
    bool is_null() const {
      return type_ == Type::VOID_;
    }

    operator bool() const {
      return bool_value_;
    }

    operator const char* () const {
      return reinterpret_cast<const char*>(string_value_.base);
    }

    operator float() const {
      return static_cast<float>(static_cast<double>(*this));
    }

    operator double() const {
      return double_value_;
    }

    operator int8_t() const {
      return static_cast<int8_t>(static_cast<int64_t>(*this));
    }

    operator int16_t() const {
      return static_cast<int16_t>(static_cast<int64_t>(*this));
    }

    operator int32_t() const {
      return static_cast<int32_t>(static_cast<int64_t>(*this));
    }

    operator int64_t() const {
      return signed_integer_value_;
    }

    operator uint32_t() const {
      return static_cast<uint32_t>(static_cast<uint64_t>(*this));
    }

    operator uint64_t() const {
      return unsigned_integer_value_;
    }

    operator const void* () const {
      return string_value_.base;
    }

    operator ::std::string () const {
      switch (type_) {
      case Type::BOOL:
        return static_cast<bool>(*this) ? "true" : "false";
      case Type::DOUBLE: {
        ::std::ostringstream oss;
        oss << static_cast<double>(*this);
        return oss.str();
      }
      case Type::I64: {
        ::std::ostringstream oss;
        oss << static_cast<int64_t>(*this);
        return oss.str();
      }
      case Type::STRING:
        return ::std::string(static_cast<const char*>(*this), static_cast<size_t>(string_value_.len));
      case Type::U64: {
        ::std::ostringstream oss;
        oss << static_cast<uint64_t>(*this);
        return oss.str();
      }
      case Type::VOID_:
      default:
        return "null";
      }
    }

    bool operator==(bool value) const {
      return operator==(Variant(value));
    }

    bool operator==(double value) const {
      return operator==(Variant(value));
    }

    bool operator==(int32_t value) const {
      return operator==(Variant(value));
    }

    bool operator==(int64_t value) const {
      return operator==(Variant(value));
    }

    bool operator==(uint32_t value) const {
      return operator==(Variant(value));
    }

    bool operator==(uint64_t value) const {
      return operator==(Variant(value));
    }

    bool operator==(const char* value) const {
      return operator==(Variant(value));
    }

    bool operator==(const Variant& other) const {
      switch (type_) {
      case Type::STRING: {
        if (other.type_ != Type::STRING) {
          return false;
        }
        if (string_value_.len != other.string_value_.len) {
          return false;
        }
        return memcmp(static_cast<const void*>(*this), static_cast<const void*>(other),
                      static_cast<size_t>(string_value_.len)) == 0;
      }
      case Type::BOOL:
        return static_cast<bool>(*this) == static_cast<bool>(other);
      case Type::DOUBLE:
        return static_cast<double>(*this) == static_cast<double>(other);
      case Type::VOID_:
        return other.type_ == Type::VOID_;
      case Type::I64:
        return static_cast<int64_t>(*this) == static_cast<int64_t>(other);
      case Type::U64:
        return static_cast<uint64_t>(*this) == static_cast<uint64_t>(other);
      default:
        return false;
      }
    }

    bool operator!=(bool value) const {
      return !operator==(value);
    }

    bool operator!=(double value) const {
      return !operator==(value);
    }

    bool operator!=(int32_t value) const {
      return !operator==(value);
    }

    bool operator!=(int64_t value) const {
      return !operator==(value);
    }

    bool operator!=(uint32_t value) const {
      return !operator==(value);
    }

    bool operator!=(uint64_t value) const {
      return !operator==(value);
    }

    bool operator!=(const char* value) const {
      return !operator==(value);
    }

    bool operator!=(const Variant& other) const {
      return !operator==(other);
    }

    Variant& operator=(const Variant& other) {
      reset();
      init(other);
      return *this;
    }

    //void read(::thryft::protocol::InputProtocol& iprot) {
    //  reset();
    //  iprot.read_struct_begin();
    //  int16_t field_id;
    //  ::std::string field_name;
    //  ::thryft::protocol::Type field_type;
    //  iprot.read_field_begin(field_name, field_type, field_id);
    //  if (field_type != ::thryft::protocol::Type::STOP) {
    //    init(iprot, field_type);
    //  } else {
    //    type_ = Type::VOID_;
    //  }
    //  iprot.read_field_end();
    //  iprot.read_struct_end();
    //}

    //static Variant read(::thryft::protocol::InputProtocol& iprot,
    //                  ::thryft::protocol::Type field_type) {
    //  Variant value;
    //  value.init(iprot, field_type);
    //  return value;
    //}

    //void write(::thryft::protocol::OutputProtocol& oprot) const {
    //  oprot.write_struct_begin();
    //  switch (type()) {
    //  case Type::STRING:
    //    oprot.write_field_begin("blob_value", ::thryft::protocol::Type::STRING, -1);
    //    oprot.write(static_cast<const char*>(*this), size());
    //    oprot.write_field_end();
    //  case Type::BOOL:
    //    oprot.write_field_begin("bool_value", ::thryft::protocol::Type::BOOL, -1);
    //    oprot.write(static_cast<bool>(*this));
    //    oprot.write_field_end();
    //  case Type::DOUBLE:
    //    oprot.write_field_begin("double_value", ::thryft::protocol::Type::DOUBLE, -1);
    //    oprot.write(static_cast<double>(*this));
    //    oprot.write_field_end();
    //  case Type::VOID_:
    //    break;
    //  case Type::I64:
    //    oprot.write_field_begin("signed_integer_value", ::thryft::protocol::Type::I64, -1);
    //    oprot.write(static_cast<int64_t>(*this));
    //    oprot.write_field_end();
    //  case Type::U64:
    //    oprot.write_field_begin("unsigned_integer_value", ::thryft::protocol::Type::U64, -1);
    //    oprot.write(static_cast<uint64_t>(*this));
    //    oprot.write_field_end();
    //    break;
    //  }
    //  oprot.write_struct_end();
    //}

  private:
    void init(void* value, size_t value_len) {
      string_value_.base = static_cast<char*>(value);
      string_value_.len = value_len;
      type_ = Type::STRING;
    }

    void init(const void* value, size_t value_len) {
      string_value_.base = new char[value_len];
      memcpy_s(string_value_.base, value_len, value, value_len);
      string_value_.len = value_len;
      type_ = Type::STRING;
    }

    void init(bool value) {
      bool_value_ = value;
      type_ = Type::BOOL;
    }

    void init(double value) {
      double_value_ = value;
      type_ = Type::DOUBLE;
    }

    void init(int64_t value) {
      signed_integer_value_ = value;
      type_ = Type::I64;
    }

    void init(uint64_t value) {
      type_ = Type::U64;
      unsigned_integer_value_ = value;
    }

    void init(const Variant& other) {
      switch (other.type_) {
      case Type::BOOL:
        init(static_cast<bool>(other));
        break;
      case Type::DOUBLE:
        init(static_cast<double>(other));
        break;
      case Type::I64:
        init(static_cast<int64_t>(other));
        break;
      case Type::U64:
        init(static_cast<uint64_t>(other));
        break;
      case Type::STRING:
        init(reinterpret_cast<const void*>(other.string_value_.base), static_cast<size_t>(other.string_value_.len));
        break;
      default:
        string_value_ = { 0, 0 };
        type_ = other.type_;
      }
    }

    void init(::thryft::protocol::InputProtocol& iprot,
          ::thryft::protocol::Type field_type) {
      switch (field_type) {
      case ::thryft::protocol::Type::BOOL:
        init(iprot.read_bool());
        break;

      case ::thryft::protocol::Type::BYTE:
        init(static_cast<int64_t>(iprot.read_byte()));
        break;

      case ::thryft::protocol::Type::DOUBLE:
        init(iprot.read_double());
        break;

      case ::thryft::protocol::Type::I16:
        init(static_cast<int64_t>(iprot.read_i16()));
        break;

      case ::thryft::protocol::Type::I32:
        init(static_cast<int64_t>(iprot.read_i32()));
        break;

      case ::thryft::protocol::Type::FLOAT:
        init(iprot.read_float());
        break;

      case ::thryft::protocol::Type::STRING: {
        char* out_value = NULL;
        size_t out_value_len = 0;
        iprot.read_string(out_value, out_value_len);
        init(out_value, out_value_len);
        break;
      }

      default:
        string_value_ = { 0, 0 };
        type_ = Type::VOID_;
        break;
      }
    }

    void reset() {
      if (type_ == Type::STRING) {
        delete [] string_value_.base;
      }
      string_value_ = { 0, 0 };
      type_ = Type::VOID_;
    }

  private:
    union {
      bool bool_value_;
      double double_value_;
      int64_t signed_integer_value_;
      struct {
        char* base;
        uint64_t len;
      } string_value_;
      uint64_t unsigned_integer_value_;
    };
    Type type_;
};
#ifdef _WIN32
#pragma warning(pop)
#endif
}
}

static inline
::std::ostream&
operator<<(
  ::std::ostream& os,
  const ::thryft::native::Variant& value
) {
  os << value.operator ::std::string();
  return os;
}

#endif  // _THRYFT_NATIVE_VARIANT_HPP_
