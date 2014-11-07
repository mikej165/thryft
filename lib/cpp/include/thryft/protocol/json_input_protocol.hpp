#ifndef _THRYFT_PROTOCOL_JSON_INPUT_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_JSON_INPUT_PROTOCOL_HPP_

#include <sstream>
#include <stack>

#include "thryft/protocol/stacked_input_protocol.hpp"
#include "thryft/protocol/json_input_protocol_exception.hpp"
#include "thryft/protocol/json_output_protocol.hpp"

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
class JsonInputProtocol : public StackedInputProtocol {
  public:
    typedef JsonOutputProtocol OutputProtocolT;

  private:
    class IovecStream final {
      public:
        IovecStream(const char* src, size_t src_len)
          : src_(src), src_p_(src), src_len_(src_len_) {
        }

      public:
        char peek() const {
          if (src_p_ - src_ >= src_len_) {
            throw JsonInputProtocolException();
          }
          return *src_p_;
        }

        char* put_begin() {
          RAPIDJSON_ASSERT(false);
          return 0;
        }

        void put(char) {
          RAPIDJSON_ASSERT(false);
        }

        size_t put_end(char*) {
          RAPIDJSON_ASSERT(false);
          return 0;
        }

        char take() {
          if (src_p_ - src_ >= src_len_) {
            throw JsonInputProtocolException();
          }
          return *src_p_++;
        }

        size_t tell() const {
          if (src_p_ - src_ >= src_len_) {
            throw JsonInputProtocolException();
          }
          return static_cast<size_t>(src_p_ - src_);
        }

      private:
        const char* src_, *src_p_;
        size_t src_len_;
    };

  protected:
    class JsonValueInputProtocolFactory;

    class JsonValueInputProtocol : public AbstractInputProtocol {
      public:
        // InputProtocol
        bool read_bool() override {
          return read_child_node().GetBool();
        }

        double read_double() override {
          return read_child_node().GetDouble();
        }

        void read_field_begin(std::string& out_name, Type& out_type,
                              int16_t& out_id) override {
          throw InputProtocolException("unexpected read_field_begin");
        }

        void read_field_end() override {
          throw InputProtocolException("unexpected read_field_end");
        }

        int32_t read_i32() override {
          return static_cast<int32_t>(read_child_node().GetInt());
        }

        int64_t read_i64() override {
          return static_cast<int64_t>(read_child_node().GetInt64());
        }

        void read_list_begin(Type& out_element_type, uint32_t& out_size) override {
          const ::rapidjson::Value& child_node = read_child_node();
          if (!child_node.IsArray()) {
            throw JsonInputProtocolException();
          }
          out_element_type = Type::VOID_;
          out_size = child_node.Size();
          protocol_stack_.push(reader_protocol_factory_.create_json_array_input_protocol(
                                 child_node, protocol_stack_));
        }

        void read_list_end() override {
          throw InputProtocolException("unexpected read_list_end");
        }

        void read_map_begin(Type& out_key_type, Type& out_value_type,
                            uint32_t& out_size) override {
          const ::rapidjson::Value& child_node = read_child_node();
          if (!child_node.IsObject()) {
            throw JsonInputProtocolException();
          }
          out_key_type = Type::VOID_;
          out_value_type = Type::VOID_;
          out_size = 0;
          for (::rapidjson::Value::ConstMemberIterator i = child_node.MemberBegin();
               i != child_node.MemberEnd(); ++i) {
            out_size++;
          }
          protocol_stack_.push(
            reader_protocol_factory_.create_json_map_object_input_protocol(
              child_node, protocol_stack_));
        }

        void read_map_end() override {
          throw InputProtocolException("unexpected read_map_end");
        }

        void read_string(std::string& out_value) override {
          const ::rapidjson::Value& child_node = read_child_node();
          switch (child_node.GetType()) {
          case ::rapidjson::kStringType:
            out_value.assign(child_node.GetString(), child_node.GetStringLength());
            break;
          case ::rapidjson::kNumberType: {
            ::std::ostringstream oss;
            oss << child_node.GetInt64();
            out_value.assign(oss.str());
            break;
          }
          default:
            RAPIDJSON_ASSERT(false);
            break;
          }
        }

        void read_string(char*& out_value, size_t& out_value_len) override {
          const ::rapidjson::Value& child_node = read_child_node();
          out_value_len = child_node.GetStringLength();
          out_value = new char[out_value_len];
          memcpy(out_value, child_node.GetString(), out_value_len);
        }

        void read_struct_begin() override {
          const ::rapidjson::Value& child_node = read_child_node();
          if (!child_node.IsObject()) {
            throw JsonInputProtocolException();
          }
          protocol_stack_.push(
            reader_protocol_factory_.create_json_struct_object_input_protocol(child_node,
                protocol_stack_));
        }

        void read_struct_end() override {
          throw InputProtocolException("unexpected read_struct_end");
        }

        uint32_t read_u32() override {
          return static_cast<uint32_t>(read_child_node().GetUint());
        }

        uint64_t read_u64() override {
          return static_cast<uint64_t>(read_child_node().GetUint64());
        }

        ::thryft::native::Variant read_variant() override {
          const rapidjson::Value& value = read_child_node();
          switch (value.GetType()) {
          case rapidjson::Type::kFalseType:
            return ::thryft::native::Variant(false);
          case rapidjson::Type::kNullType:
            return ::thryft::native::Variant();
          case rapidjson::Type::kNumberType:
            return ::thryft::native::Variant(value.GetDouble());
          case rapidjson::Type::kStringType:
            return ::thryft::native::Variant(value.GetString(), value.GetStringLength());
          case rapidjson::Type::kTrueType:
            return ::thryft::native::Variant(true);
          default:
            throw InputProtocolException("unexpected variant type");
          }
        }

      protected:
        JsonValueInputProtocol(const ::rapidjson::Value& node,
                               ::std::stack< InputProtocol* >& protocol_stack,
                               const JsonValueInputProtocolFactory& reader_protocol_factory)
          : node_(node), protocol_stack_(protocol_stack),
            reader_protocol_factory_(reader_protocol_factory) {
        }

      protected:
        virtual const ::rapidjson::Value& read_child_node() = 0;

      protected:
        const ::rapidjson::Value& node() {
          return node_;
        }

      private:
        const ::rapidjson::Value& node_;
        ::std::stack< InputProtocol* >& protocol_stack_;
        const JsonValueInputProtocolFactory& reader_protocol_factory_;
    };

    class JsonValueInputProtocolFactory {
      public:
        virtual JsonValueInputProtocol* create_json_array_input_protocol(
          const ::rapidjson::Value&
          node, ::std::stack< InputProtocol* >& protocol_stack) const = 0;
        virtual JsonValueInputProtocol* create_json_map_object_input_protocol(
          const ::rapidjson::Value& node,
          ::std::stack< InputProtocol* >& protocol_stack) const = 0;
        virtual JsonValueInputProtocol* create_json_root_input_protocol(
          const ::rapidjson::Document&
          node, ::std::stack< InputProtocol* >& protocol_stack) const = 0;
        virtual JsonValueInputProtocol* create_json_struct_object_input_protocol(
          const ::rapidjson::Value& node,
          ::std::stack< InputProtocol* >& protocol_stack) const = 0;
    };

    class JsonArrayInputProtocol : public JsonValueInputProtocol {
      public:
        JsonArrayInputProtocol(const ::rapidjson::Value& node,
                               ::std::stack< InputProtocol* >& protocol_stack,
                               const JsonValueInputProtocolFactory& reader_protocol_factory)
          : JsonValueInputProtocol(node, protocol_stack, reader_protocol_factory) {
          next_child_node_index = 0;
        }

      protected:
        const ::rapidjson::Value& read_child_node() override {
          return node()[next_child_node_index++];
        }

      private:
        size_t next_child_node_index;
    };

    class JsonMapObjectInputProtocol : public JsonValueInputProtocol {
      public:
        JsonMapObjectInputProtocol(const ::rapidjson::Value& node,
                                   ::std::stack< InputProtocol* >& protocol_stack,
                                   const JsonValueInputProtocolFactory& reader_protocol_factory)
          : JsonValueInputProtocol(node, protocol_stack, reader_protocol_factory) {
          next_child_node_i = node.MemberBegin();
          next_read_is_key_ = true;
        }
       
      protected:
        const ::rapidjson::Value& read_child_node() override {
          if (next_read_is_key_) {
            next_read_is_key_ = false;
            return next_child_node_i->name;
          } else {
            next_read_is_key_ = true;
            const ::rapidjson::Value& next_child_node_value = next_child_node_i->value;
            ++next_child_node_i;
            return next_child_node_value;
          }
        }

      private:
        ::rapidjson::Value::ConstMemberIterator next_child_node_i;
        bool next_read_is_key_;
    };

    class JsonRootInputProtocol : public JsonValueInputProtocol {
      public:
        JsonRootInputProtocol(const ::rapidjson::Document& node,
                              ::std::stack< InputProtocol* >& protocol_stack,
                              const JsonValueInputProtocolFactory& reader_protocol_factory)
          : JsonValueInputProtocol(node, protocol_stack, reader_protocol_factory) {
        }

      protected:
        const ::rapidjson::Value& read_child_node() {
          return node();
        }
    };

    class JsonStructObjectReaderProtocol : public JsonValueInputProtocol {
      public:
        JsonStructObjectReaderProtocol(const ::rapidjson::Value& node,
                                       ::std::stack< InputProtocol* >& protocol_stack,
                                       const JsonValueInputProtocolFactory& reader_protocol_factory)
          : JsonValueInputProtocol(node, protocol_stack, reader_protocol_factory) {
          next_child_node_i = node.MemberBegin();
        }

      public:
        // InputProtocol
        void read_field_begin(std::string& out_name, Type& out_type,
                              int16_t& out_id) override {
          if (next_child_node_i != node().MemberEnd()) {
            out_name.assign(next_child_node_i->name.GetString(),
                            next_child_node_i->name.GetStringLength());
            if (next_child_node_i->value.IsArray()) {
              out_type = Type::LIST;
            } else if (next_child_node_i->value.IsBool()) {
              out_type = Type::BOOL;
            } else if (next_child_node_i->value.IsDouble()) {
              out_type = Type::DOUBLE;
            } else if (next_child_node_i->value.IsInt()) {
              out_type = Type::I32;
            } else if (next_child_node_i->value.IsInt64()) {
              out_type = Type::I64;
            } else if (next_child_node_i->value.IsObject()) {
              out_type = Type::STRUCT;
            } else if (next_child_node_i->value.IsString()) {
              out_type = Type::STRING;
            } else {
              RAPIDJSON_ASSERT(false);
            }
            out_id = -1;
          } else {
            out_name.clear();
            out_type = Type::STOP;
            out_id = 0;
          }
        }

        void read_field_end() override {
          next_child_node_i++;
        }

      protected:
        const ::rapidjson::Value& read_child_node() override {
          return next_child_node_i->value;
        }

      private:
        ::rapidjson::Value::ConstMemberIterator next_child_node_i;
    };

    class DefaultReaderProtocolFactory : public JsonValueInputProtocolFactory {
      public:
        virtual JsonValueInputProtocol* create_json_array_input_protocol(
          const ::rapidjson::Value&
          node, ::std::stack< InputProtocol* >& protocol_stack) const {
          return new JsonArrayInputProtocol(node, protocol_stack, *this);
        }

        virtual JsonValueInputProtocol* create_json_map_object_input_protocol(
          const ::rapidjson::Value& node,
          ::std::stack< InputProtocol* >& protocol_stack) const {
          return new JsonMapObjectInputProtocol(node, protocol_stack, *this);
        }

        virtual JsonValueInputProtocol* create_json_root_input_protocol(
          const ::rapidjson::Document&
          node, ::std::stack< InputProtocol* >& protocol_stack) const {
          return new JsonRootInputProtocol(node, protocol_stack, *this);
        }

        virtual JsonValueInputProtocol* create_json_struct_object_input_protocol(
          const ::rapidjson::Value& node,
          ::std::stack< InputProtocol* >& protocol_stack) const {
          return new JsonStructObjectReaderProtocol(node, protocol_stack, *this);
        }
    };

  public:
    JsonInputProtocol(const ::std::string& json) {
      init(json.data(), json.size(), new DefaultReaderProtocolFactory);
    }

    JsonInputProtocol(const char* json, size_t json_len) {
      init(json, json_len, new DefaultReaderProtocolFactory);
    }

    ~JsonInputProtocol() {
      delete reader_protocol_factory_;
    }

  public:
    // StackedProtocol
    void reset() override {
      StackedInputProtocol::reset();
      protocol_stack().push(reader_protocol_factory_->create_json_root_input_protocol(
                              document_, protocol_stack()));
    }

  private:
    void init(const char* json, size_t json_len,
              JsonValueInputProtocolFactory* reader_protocol_factory) {
      this->reader_protocol_factory_ = reader_protocol_factory;

      //IovecStream stream(json, json_len);
      document_.Parse<0>(::std::string(json, json_len).c_str());
      //document_.ParseStream<0>(stream);
      if (document_.HasParseError()) {
        throw JsonInputProtocolException();
      }
      reset();
    }

  private:
    ::rapidjson::Document document_;
    JsonValueInputProtocolFactory* reader_protocol_factory_;
};
}
}

#endif  // _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_