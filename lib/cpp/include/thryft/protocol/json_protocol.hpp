#ifndef _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_
#define _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_

#include <stack>

#include "thryft/protocol/abstract_protocol.hpp"
#include "thryft/protocol/stacked_protocol.hpp"

#include <rapidjson/document.h>

namespace thryft {
namespace protocol {
class JsonProtocol : public StackedProtocol {
protected:
  class ReaderProtocolFactory;

  class ReaderProtocol : public AbstractProtocol {
  public:
    // Protocol
    bool read_bool() {
      return read_child_node().GetBool();
    }

    double read_double() {
      return read_child_node().GetDouble();
    }

    int32_t read_i32() {
      return static_cast<int32_t>(read_child_node().GetInt());
    }

    int64_t read_i64() {
      return static_cast<int64_t>(read_child_node().GetInt64());
    }

    void read_list_begin(Type::Enum& out_element_type, uint32_t& out_size) {
      const ::rapidjson::Value& child_node = read_child_node();
      RAPIDJSON_ASSERT(child_node.IsArray());
      out_element_type = Type::VOID;
      out_size = child_node.Size();
      protocol_stack_.push(reader_protocol_factory_.create_array_reader_protocol(child_node, protocol_stack_));
    }

    void read_map_begin(Type::Enum& out_key_type, Type::Enum& out_value_type, uint32_t& out_size) {
      const ::rapidjson::Value& child_node = read_child_node();
      RAPIDJSON_ASSERT(child_node.IsObject());
      out_key_type = Type::VOID;
      out_value_type = Type::VOID;
      out_size = 0;
      for (::rapidjson::Value::ConstMemberIterator i = child_node.MemberBegin(); i != child_node.MemberEnd(); ++i) {
        out_size++;
      }
      protocol_stack_.push(reader_protocol_factory_.create_map_object_reader_protocol(child_node, protocol_stack_));
    }

    void read_string(std::string& out_value) {
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

    void read_string(char*& out_value, size_t& out_value_len) {
      const ::rapidjson::Value& child_node = read_child_node();
      out_value_len = child_node.GetStringLength();
      out_value = new char[out_value_len];
      memcpy(out_value, child_node.GetString(), out_value_len);
    }

    void read_struct_begin() {
      const ::rapidjson::Value& child_node = read_child_node();
      RAPIDJSON_ASSERT(child_node.IsObject());
      protocol_stack_.push(reader_protocol_factory_.create_struct_object_reader_protocol(child_node, protocol_stack_));
    }

  protected:
    ReaderProtocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack, const ReaderProtocolFactory& reader_protocol_factory) 
      : node_(node), protocol_stack_(protocol_stack), reader_protocol_factory_(reader_protocol_factory) {
    }

  protected:
    virtual const ::rapidjson::Value& read_child_node() = 0;

  protected:
    const ::rapidjson::Value& node() {
      return node_;
    }

  private:
    const ::rapidjson::Value& node_;
    ::std::stack< Protocol* >& protocol_stack_;
    const ReaderProtocolFactory& reader_protocol_factory_;
  };

  class ReaderProtocolFactory {
  public:
    virtual ReaderProtocol* create_array_reader_protocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack) const = 0;
    virtual ReaderProtocol* create_map_object_reader_protocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack) const = 0;
    virtual ReaderProtocol* create_root_reader_protocol(const ::rapidjson::Document& node, ::std::stack< Protocol* >& protocol_stack) const = 0;
    virtual ReaderProtocol* create_struct_object_reader_protocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack) const = 0;
  };

  class ArrayReaderProtocol : public ReaderProtocol {
  public:
    ArrayReaderProtocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack, const ReaderProtocolFactory& reader_protocol_factory)
      : ReaderProtocol(node, protocol_stack, reader_protocol_factory) {
      next_child_node_index = 0;
    }

  protected:
    const ::rapidjson::Value& read_child_node() {
      return node()[next_child_node_index++];
    }

  private:
    size_t next_child_node_index;
  };

  class MapObjectReaderProtocol : public ReaderProtocol {
  public:
    MapObjectReaderProtocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack, const ReaderProtocolFactory& reader_protocol_factory)
      : ReaderProtocol(node, protocol_stack, reader_protocol_factory) {
      next_child_node_i = node.MemberBegin();
      next_read_is_key_ = true;
    }

  protected:
    const ::rapidjson::Value& read_child_node() {
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

  class RootReaderProtocol : public ReaderProtocol {
  public:
    RootReaderProtocol(const ::rapidjson::Document& node, ::std::stack< Protocol* >& protocol_stack, const ReaderProtocolFactory& reader_protocol_factory)
      : ReaderProtocol(node, protocol_stack, reader_protocol_factory) {
    }

  protected:
    const ::rapidjson::Value& read_child_node() {
      return node();
    }
  };

  class StructObjectReaderProtocol : public ReaderProtocol {
  public:
    StructObjectReaderProtocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack, const ReaderProtocolFactory& reader_protocol_factory)
      : ReaderProtocol(node, protocol_stack, reader_protocol_factory) {
      next_child_node_i = node.MemberBegin();
    }

  public:
    // Protocol
    void read_field_begin(std::string& out_name, Type::Enum& out_type, int16_t& out_id) {
      if (next_child_node_i != node().MemberEnd()) {
        out_name.assign(next_child_node_i->name.GetString(), next_child_node_i->name.GetStringLength());
        out_type = Type::VOID;
        out_id = -1;
      } else {
        out_name.clear();
        out_type = Type::STOP;
        out_id = 0;
      }
    }

    void read_field_end() {
      next_child_node_i++;
    }

  protected:
    const ::rapidjson::Value& read_child_node() {
      return next_child_node_i->value;
    }

  private:
    ::rapidjson::Value::ConstMemberIterator next_child_node_i;
  };

  class DefaultReaderProtocolFactory : public ReaderProtocolFactory {
  public:
    virtual ReaderProtocol* create_array_reader_protocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack) const {
      return new ArrayReaderProtocol(node, protocol_stack, *this);
    }

    virtual ReaderProtocol* create_map_object_reader_protocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack) const {
      return new MapObjectReaderProtocol(node, protocol_stack, *this);
    }

    virtual ReaderProtocol* create_root_reader_protocol(const ::rapidjson::Document& node, ::std::stack< Protocol* >& protocol_stack) const {
      return new RootReaderProtocol(node, protocol_stack, *this);
    }

    virtual ReaderProtocol* create_struct_object_reader_protocol(const ::rapidjson::Value& node, ::std::stack< Protocol* >& protocol_stack) const {
      return new StructObjectReaderProtocol(node, protocol_stack, *this);
    }
  };

public:
  JsonProtocol(const uint8_t* json, size_t json_len) {
    init(json, json_len, new DefaultReaderProtocolFactory());
  }

  ~JsonProtocol() {
    delete reader_protocol_factory_;
  }

public:
  // StackedProtocol
  void reset() {
    StackedProtocol::reset();
    protocol_stack().push(reader_protocol_factory_->create_root_reader_protocol(document_, protocol_stack()));
  }

private:
  void init(const uint8_t* json, size_t json_len, ReaderProtocolFactory* reader_protocol_factory) {
    this->reader_protocol_factory_ = reader_protocol_factory;
    document_.Parse<0>(::std::string(reinterpret_cast<const char*>(json), json_len).c_str());
    RAPIDJSON_ASSERT(!document_.HasParseError());
    reset();
  }

private:
  ::rapidjson::Document document_;
  ReaderProtocolFactory* reader_protocol_factory_;
};
}
}

#endif  // _THRYFT_PROTOCOL_JSON_PROTOCOL_HPP_