#ifndef _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_

#include "thryft/protocol/abstract_output_protocol.hpp"

#include <rapidjson/document.h>
#include <rapidjson/writer.h>

namespace thryft {
namespace protocol {
class JsonOutputProtocol : public AbstractOutputProtocol {
  private:
    class StlStringStream {
      public:
        StlStringStream(::std::string& dst)
          : dst_(dst) {
        }

      public:
        void Put(char c) {
          dst_.append(1, c);
        }

      private:
        ::std::string& dst_;
    };

    typedef ::rapidjson::Writer< StlStringStream > StlStringWriter;

  public:
    JsonOutputProtocol()
      : writer_stream_(writer_string_), writer_(writer_stream_) {
    }

  public:
    const ::std::string& to_string() const {
      return writer_string_;
    }

  public:
    // OutputProtocol
    virtual void write(const void* value, size_t value_len) {
      writer_.String(static_cast<const char*>(value), value_len);
    }

    virtual void write(bool value) {
      writer_.Bool(value);
    }

    virtual void write(double value) {
      writer_.Double(value);
    }

    virtual void write(int32_t value) {
      writer_.Int(value);
    }

    virtual void write(int64_t value) {
      writer_.Int64(value);
    }

    virtual void write(const char* value, size_t value_len) {
      writer_.String(value, value_len);
    }

    virtual void write_field_begin(const char* name, Type::Enum type,
                                   int16_t id) {
      writer_.String(name);
    }

    virtual void write_list_begin(Type::Enum element_type, uint32_t size) {
      writer_.StartArray();
    }

    virtual void write_list_end() {
      writer_.EndArray();
    }

    virtual void write_map_begin(Type::Enum key_type, Type::Enum value_type,
                                 uint32_t size) {
      writer_.StartObject();
    }

    virtual void write_map_end() {
      writer_.EndObject();
    }

    virtual void write_null() {
      writer_.Null();
    }

    virtual void write_struct_begin() {
      writer_.StartObject();
    }

    virtual void write_struct_end() {
      writer_.EndObject();
    }

  private:
    StlStringWriter writer_;
    StlStringStream writer_stream_;
    ::std::string writer_string_;
};
}
}

#endif  // _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_