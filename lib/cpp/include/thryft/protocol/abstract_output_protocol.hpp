#ifndef _THRYFT_PROTOCOL_ABSTRACT_OUTPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_ABSTRACT_OUTPUT_PROTOCOL_HPP_

#include "thryft/base.hpp"
#include "thryft/protocol/output_protocol.hpp"
#include "thryft/protocol/output_protocol_exception.hpp"

namespace thryft {
namespace protocol {
class AbstractOutputProtocol : public OutputProtocol {
  public:
    virtual ~AbstractOutputProtocol() {
    }

  public:
    virtual void write(const void* value, size_t value_len) {
    }

    virtual void write(bool value) {
    }

    virtual void write(int8_t value) {
      write(static_cast<int16_t>(value));
    }

    virtual void write(double value) {
    }

    virtual void write(float value) {
      write(static_cast<double>(value));
    }

    virtual void write(int16_t value) {
      write(static_cast<int32_t>(value));
    }

    virtual void write(int32_t value) {
      write(static_cast<int64_t>(value));
    }

    virtual void write(int64_t value) {
    }

    virtual void write(uint32_t value) {
      write(static_cast<uint64_t>(value));
    }

    virtual void write(uint64_t value) {
    }

    virtual void write(const ::thryft::Base& value) {
      value.write(*this);
    }

    virtual void write(const std::string& value) {
      write(value.data(), value.size());
    }

    virtual void write(const char* value, size_t value_len) {
    }

    virtual void write(const ::thryft::native::Variant& value) {
      switch (value.type()) {
      case Type::BOOL:
        write(static_cast<bool>(value));
        break;
      case Type::BYTE:
        write(static_cast<int8_t>(value));
        break;
      case Type::DOUBLE:
        write(static_cast<double>(value));
        break;
      case Type::FLOAT:
        write(static_cast<float>(value));
        break;
      case Type::I16:
        write(static_cast<int16_t>(value));
        break;
      case Type::I32:
        write(static_cast<int32_t>(value));
        break;
      case Type::I64:
        write(static_cast<int64_t>(value));
        break;    
      case Type::STRING:
        write(static_cast<const char*>(value), value.size());
        break;
      case Type::U64:
        write(static_cast<uint64_t>(value));
        break;
      default:
        throw OutputProtocolException();
      }
    }

    virtual void write_field_begin(const char* name, const Type& type, int16_t id) {
    }

    virtual void write_field_end() {
    }

    virtual void write_field_stop() {
    }

    virtual void write_list_begin(const Type& element_type, uint32_t size) {
    }

    virtual void write_list_end() {
    }

    virtual void write_map_begin(const Type& key_type, const Type& value_type,
                                 uint32_t size) {
    }

    virtual void write_map_end() {
    }

    virtual void write_set_begin(const Type& element_type, uint32_t size) {
      write_list_begin(element_type, size);
    }

    virtual void write_set_end() {
      write_list_end();
    }

    virtual void write_struct_begin() {
    }

    virtual void write_struct_end() {
    }

    virtual void write_null() {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_ABSTRACT_OUTPUT_PROTOCOL_HPP_
