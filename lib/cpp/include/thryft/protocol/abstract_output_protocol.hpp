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
    virtual void write(int8_t value) override {
      write(static_cast<int16_t>(value));
    }

    virtual void write(float value) override {
      static_cast<OutputProtocol*>(this)->write(static_cast<double>(value));
    }

    virtual void write(int16_t value) override {
      write(static_cast<int32_t>(value));
    }

    virtual void write(int32_t value) override {
      static_cast<OutputProtocol*>(this)->write(static_cast<int64_t>(value));
    }

    virtual void write(uint32_t value) override {
      static_cast<OutputProtocol*>(this)->write(static_cast<uint64_t>(value));
    }

    virtual void write(const ::thryft::Base& value) override {
      value.write(*this);
    }

    virtual void write(const std::string& value) override {
      static_cast<OutputProtocol*>(this)->write(value.data(), value.size());
    }

    virtual void write(const ::thryft::native::Variant& value) override {
      switch (value.type()) {
      case Type::BOOL:
        write(static_cast<bool>(value));
        break;
      case Type::BYTE:
        write(static_cast<int8_t>(value));
        break;
      case Type::DOUBLE:
        static_cast<OutputProtocol*>(this)->write(static_cast<double>(value));
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
        static_cast<OutputProtocol*>(this)->write(static_cast<int64_t>(value));
        break;    
      case Type::STRING:
        static_cast<OutputProtocol*>(this)->write(static_cast<const char*>(value), value.size());
        break;
      case Type::U64:
        static_cast<OutputProtocol*>(this)->write(static_cast<uint64_t>(value));
        break;
      case Type::STOP:
        static_cast<OutputProtocol*>(this)->write_null();
        break;
      default:
        throw OutputProtocolException("unexpected variant type");
      }
    }

    virtual void write_field_stop() override {
    }

    virtual void write_message_begin(const char* name, const MessageType& type) override {
      write_struct_begin(name);
    }

    virtual void write_message_end() override {
      write_struct_end();
    }

    virtual void write_set_begin(const Type& element_type, uint32_t size) override {
      write_list_begin(element_type, size);
    }

    virtual void write_set_end() override {
      write_list_end();
    }

    virtual void write_null() override {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_ABSTRACT_OUTPUT_PROTOCOL_HPP_
