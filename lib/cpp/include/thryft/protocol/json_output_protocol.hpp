#ifndef _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_

#include "thryft/protocol/abstract_output_protocol.hpp"

#ifdef _WIN32
#pragma warning(push)
#pragma warning(disable: 4265 4242 4365)
#endif
#include <rapidjson/document.h>
#include <rapidjson/writer.h>
#ifdef _WIN32
#pragma warning(pop)
#endif

namespace thryft {
namespace protocol {
class JsonOutputProtocol final : public AbstractOutputProtocol {
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
    virtual void write(const void* value, size_t value_len) override {
      writer_.String(static_cast<const char*>(value), static_cast< ::rapidjson::SizeType >(value_len));
    }

    virtual void write(bool value) override {
      writer_.Bool(value);
    }

    virtual void write(double value) override {
      writer_.Double(value);
    }

    virtual void write(int32_t value) override {
      writer_.Int(value);
    }

    virtual void write(int64_t value) override {
      writer_.Int64(value);
    }

    virtual void write(const char* value, size_t value_len) override {
      writer_.String(value, static_cast< ::rapidjson::SizeType >(value_len));
    }

    virtual void write(uint32_t value) override {
      writer_.Uint(value);
    }

    virtual void write(uint64_t value) override {
      writer_.Uint64(value);
    }

    virtual void write_field_begin(const char* name, const Type& type,
                                   int16_t id) override {
      writer_.String(name);
    }

    virtual void write_field_end() override {
    }

    virtual void write_list_begin(const Type& element_type, uint32_t size) override {
      writer_.StartArray();
    }

    virtual void write_list_end() override {
      writer_.EndArray();
    }

    virtual void write_map_begin(const Type& key_type, const Type& value_type,
                                 uint32_t size) override {
      writer_.StartObject();
    }

    virtual void write_map_end() override {
      writer_.EndObject();
    }

    virtual void write_null() override {
      writer_.Null();
    }

    virtual void write_struct_begin(const char* name) override {
      writer_.StartObject();

      ::std::string cpp_type_name(name);
      if (!cpp_type_name.empty()) {
        ::std::string java_type_name;
        java_type_name.reserve(cpp_type_name.size());
        auto i = cpp_type_name.cbegin();
        for (; i != cpp_type_name.cend(); ++i) {
          if (*i != ':') {
            break;
          }
        }
        for (; i != cpp_type_name.cend(); ++i) {
          if (*i == ':') {
            java_type_name.append(1, '.');
            ++i;
          } else {
            java_type_name.append(1, *i);
          }
        }
        if (!java_type_name.empty()) {
          write_field_begin("@class", ::thryft::protocol::Type::STRING, -1);
          static_cast<OutputProtocol*>(this)->write(java_type_name);
          write_field_end();
        }
      }
    }

    virtual void write_struct_end() override {
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