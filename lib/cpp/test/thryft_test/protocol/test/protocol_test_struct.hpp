#ifndef _THRYFT_TEST_PROTOCOL_TEST_PROTOCOL_TEST_STRUCT_HPP_
#define _THRYFT_TEST_PROTOCOL_TEST_PROTOCOL_TEST_STRUCT_HPP_

#include <string>
#include <cstdint>

#include <thryft.hpp>

#include "thryft_test/protocol/test/protocol_test_enum.hpp"
#include "thryft_test/protocol/test/nested_protocol_test_struct.hpp"

namespace thryft_test {
namespace protocol {
namespace test {
class ProtocolTestStruct : public ::thryft::Struct {
public:
  ProtocolTestStruct()
    : required_i32_field_(static_cast<int32_t>(0)) {
  }

  ProtocolTestStruct(::thryft::protocol::InputProtocol& iprot) {
    read(iprot);
  }

  ProtocolTestStruct(::thryft::protocol::InputProtocol& iprot, ::thryft::protocol::Type::Enum as_type) {
    read(iprot, as_type);
  }

  ProtocolTestStruct(const int32_t& required_i32_field, const ::std::string& required_string_field)
    : required_i32_field_(required_i32_field), required_string_field_(required_string_field) {
  }

  ProtocolTestStruct(const ::thryft::Optional< ::std::string >& binary_field, const ::thryft::Optional< bool >& bool_field, const ::thryft::Optional< int64_t >& date_time_field, const ::thryft::Optional< ::std::string >& decimal_field, const ::thryft::Optional< ::std::string >& email_address_field, const ::thryft::Optional< ::thryft_test::protocol::test::ProtocolTestEnum::Enum >& enum_field, const ::thryft::Optional< int8_t >& i8_field, const ::thryft::Optional< int16_t >& i16_field, const ::thryft::Optional< int32_t >& i32_field, const ::thryft::Optional< int64_t >& i64_field, const ::thryft::Optional< ::thryft::List< ::std::string, ::thryft::protocol::Type::STRING > >& list_string_field, const ::thryft::Optional< ::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING > >& map_string_string_field, const int32_t& required_i32_field, const ::std::string& required_string_field, const ::thryft::Optional< ::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING > >& set_string_field, const ::thryft::Optional< ::std::string >& string_field, const ::thryft::Optional< ::thryft_test::protocol::test::NestedProtocolTestStruct >& struct_field, const ::thryft::Optional< uint32_t >& u32_field, const ::thryft::Optional< uint64_t >& u64_field, const ::thryft::Optional< ::std::string >& url_field)
    : binary_field_(binary_field), bool_field_(bool_field), date_time_field_(date_time_field), decimal_field_(decimal_field), email_address_field_(email_address_field), enum_field_(enum_field), i8_field_(i8_field), i16_field_(i16_field), i32_field_(i32_field), i64_field_(i64_field), list_string_field_(list_string_field), map_string_string_field_(map_string_string_field), required_i32_field_(required_i32_field), required_string_field_(required_string_field), set_string_field_(set_string_field), string_field_(string_field), struct_field_(struct_field), u32_field_(u32_field), u64_field_(u64_field), url_field_(url_field) {
  }

  virtual ~ProtocolTestStruct() {
  }

  const ::thryft::Optional< ::std::string >& binary_field() const {
    return binary_field_;
  }

  const ::thryft::Optional< bool >& bool_field() const {
    return bool_field_;
  }

  const ::thryft::Optional< int64_t >& date_time_field() const {
    return date_time_field_;
  }

  const ::thryft::Optional< ::std::string >& decimal_field() const {
    return decimal_field_;
  }

  const ::thryft::Optional< ::std::string >& email_address_field() const {
    return email_address_field_;
  }

  const ::thryft::Optional< ::thryft_test::protocol::test::ProtocolTestEnum::Enum >& enum_field() const {
    return enum_field_;
  }

  const ::thryft::Optional< int8_t >& i8_field() const {
    return i8_field_;
  }

  const ::thryft::Optional< int16_t >& i16_field() const {
    return i16_field_;
  }

  const ::thryft::Optional< int32_t >& i32_field() const {
    return i32_field_;
  }

  const ::thryft::Optional< int64_t >& i64_field() const {
    return i64_field_;
  }

  const ::thryft::Optional< ::thryft::List< ::std::string, ::thryft::protocol::Type::STRING > >& list_string_field() const {
    return list_string_field_;
  }

  const ::thryft::Optional< ::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING > >& map_string_string_field() const {
    return map_string_string_field_;
  }

  const int32_t& required_i32_field() const {
    return required_i32_field_;
  }

  const ::std::string& required_string_field() const {
    return required_string_field_;
  }

  const ::thryft::Optional< ::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING > >& set_string_field() const {
    return set_string_field_;
  }

  const ::thryft::Optional< ::std::string >& string_field() const {
    return string_field_;
  }

  const ::thryft::Optional< ::thryft_test::protocol::test::NestedProtocolTestStruct >& struct_field() const {
    return struct_field_;
  }

  const ::thryft::Optional< uint32_t >& u32_field() const {
    return u32_field_;
  }

  const ::thryft::Optional< uint64_t >& u64_field() const {
    return u64_field_;
  }

  const ::thryft::Optional< ::std::string >& url_field() const {
    return url_field_;
  }

  ProtocolTestStruct& set_binary_field(const ::thryft::Optional< ::std::string >& binary_field) {
    this->binary_field_ = binary_field;
    return *this;
  }

  ProtocolTestStruct& set_binary_field(const ::std::string& binary_field) {
    return set_binary_field(::thryft::Optional< ::std::string >(binary_field));
  }

  ProtocolTestStruct& set_bool_field(const ::thryft::Optional< bool >& bool_field) {
    this->bool_field_ = bool_field;
    return *this;
  }

  ProtocolTestStruct& set_bool_field(const bool& bool_field) {
    return set_bool_field(::thryft::Optional< bool >(bool_field));
  }

  ProtocolTestStruct& set_date_time_field(const ::thryft::Optional< int64_t >& date_time_field) {
    this->date_time_field_ = date_time_field;
    return *this;
  }

  ProtocolTestStruct& set_date_time_field(const int64_t& date_time_field) {
    return set_date_time_field(::thryft::Optional< int64_t >(date_time_field));
  }

  ProtocolTestStruct& set_decimal_field(const ::thryft::Optional< ::std::string >& decimal_field) {
    this->decimal_field_ = decimal_field;
    return *this;
  }

  ProtocolTestStruct& set_decimal_field(const ::std::string& decimal_field) {
    return set_decimal_field(::thryft::Optional< ::std::string >(decimal_field));
  }

  ProtocolTestStruct& set_email_address_field(const ::thryft::Optional< ::std::string >& email_address_field) {
    this->email_address_field_ = email_address_field;
    return *this;
  }

  ProtocolTestStruct& set_email_address_field(const ::std::string& email_address_field) {
    return set_email_address_field(::thryft::Optional< ::std::string >(email_address_field));
  }

  ProtocolTestStruct& set_enum_field(const ::thryft::Optional< ::thryft_test::protocol::test::ProtocolTestEnum::Enum >& enum_field) {
    this->enum_field_ = enum_field;
    return *this;
  }

  ProtocolTestStruct& set_enum_field(const ::thryft_test::protocol::test::ProtocolTestEnum::Enum& enum_field) {
    return set_enum_field(::thryft::Optional< ::thryft_test::protocol::test::ProtocolTestEnum::Enum >(enum_field));
  }

  ProtocolTestStruct& set_i8_field(const ::thryft::Optional< int8_t >& i8_field) {
    this->i8_field_ = i8_field;
    return *this;
  }

  ProtocolTestStruct& set_i8_field(const int8_t& i8_field) {
    return set_i8_field(::thryft::Optional< int8_t >(i8_field));
  }

  ProtocolTestStruct& set_i16_field(const ::thryft::Optional< int16_t >& i16_field) {
    this->i16_field_ = i16_field;
    return *this;
  }

  ProtocolTestStruct& set_i16_field(const int16_t& i16_field) {
    return set_i16_field(::thryft::Optional< int16_t >(i16_field));
  }

  ProtocolTestStruct& set_i32_field(const ::thryft::Optional< int32_t >& i32_field) {
    this->i32_field_ = i32_field;
    return *this;
  }

  ProtocolTestStruct& set_i32_field(const int32_t& i32_field) {
    return set_i32_field(::thryft::Optional< int32_t >(i32_field));
  }

  ProtocolTestStruct& set_i64_field(const ::thryft::Optional< int64_t >& i64_field) {
    this->i64_field_ = i64_field;
    return *this;
  }

  ProtocolTestStruct& set_i64_field(const int64_t& i64_field) {
    return set_i64_field(::thryft::Optional< int64_t >(i64_field));
  }

  ProtocolTestStruct& set_list_string_field(const ::thryft::Optional< ::thryft::List< ::std::string, ::thryft::protocol::Type::STRING > >& list_string_field) {
    this->list_string_field_ = list_string_field;
    return *this;
  }

  ProtocolTestStruct& set_list_string_field(const ::thryft::List< ::std::string, ::thryft::protocol::Type::STRING >& list_string_field) {
    return set_list_string_field(::thryft::Optional< ::thryft::List< ::std::string, ::thryft::protocol::Type::STRING > >(list_string_field));
  }

  ProtocolTestStruct& set_map_string_string_field(const ::thryft::Optional< ::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING > >& map_string_string_field) {
    this->map_string_string_field_ = map_string_string_field;
    return *this;
  }

  ProtocolTestStruct& set_map_string_string_field(const ::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING >& map_string_string_field) {
    return set_map_string_string_field(::thryft::Optional< ::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING > >(map_string_string_field));
  }

  ProtocolTestStruct& set_required_i32_field(const int32_t& required_i32_field) {
    this->required_i32_field_ = required_i32_field;
    return *this;
  }

  ProtocolTestStruct& set_required_string_field(const ::std::string& required_string_field) {
    this->required_string_field_ = required_string_field;
    return *this;
  }

  ProtocolTestStruct& set_set_string_field(const ::thryft::Optional< ::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING > >& set_string_field) {
    this->set_string_field_ = set_string_field;
    return *this;
  }

  ProtocolTestStruct& set_set_string_field(const ::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING >& set_string_field) {
    return set_set_string_field(::thryft::Optional< ::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING > >(set_string_field));
  }

  ProtocolTestStruct& set_string_field(const ::thryft::Optional< ::std::string >& string_field) {
    this->string_field_ = string_field;
    return *this;
  }

  ProtocolTestStruct& set_string_field(const ::std::string& string_field) {
    return set_string_field(::thryft::Optional< ::std::string >(string_field));
  }

  ProtocolTestStruct& set_struct_field(const ::thryft::Optional< ::thryft_test::protocol::test::NestedProtocolTestStruct >& struct_field) {
    this->struct_field_ = struct_field;
    return *this;
  }

  ProtocolTestStruct& set_struct_field(const ::thryft_test::protocol::test::NestedProtocolTestStruct& struct_field) {
    return set_struct_field(::thryft::Optional< ::thryft_test::protocol::test::NestedProtocolTestStruct >(struct_field));
  }

  ProtocolTestStruct& set_u32_field(const ::thryft::Optional< uint32_t >& u32_field) {
    this->u32_field_ = u32_field;
    return *this;
  }

  ProtocolTestStruct& set_u32_field(const uint32_t& u32_field) {
    return set_u32_field(::thryft::Optional< uint32_t >(u32_field));
  }

  ProtocolTestStruct& set_u64_field(const ::thryft::Optional< uint64_t >& u64_field) {
    this->u64_field_ = u64_field;
    return *this;
  }

  ProtocolTestStruct& set_u64_field(const uint64_t& u64_field) {
    return set_u64_field(::thryft::Optional< uint64_t >(u64_field));
  }

  ProtocolTestStruct& set_url_field(const ::thryft::Optional< ::std::string >& url_field) {
    this->url_field_ = url_field;
    return *this;
  }

  ProtocolTestStruct& set_url_field(const ::std::string& url_field) {
    return set_url_field(::thryft::Optional< ::std::string >(url_field));
  }

  bool operator==(const ProtocolTestStruct& other) const {
    if (!(binary_field() == other.binary_field())) {
      return false;
    }

    if (!(bool_field() == other.bool_field())) {
      return false;
    }

    if (!(date_time_field() == other.date_time_field())) {
      return false;
    }

    if (!(decimal_field() == other.decimal_field())) {
      return false;
    }

    if (!(email_address_field() == other.email_address_field())) {
      return false;
    }

    if (!(enum_field() == other.enum_field())) {
      return false;
    }

    if (!(i8_field() == other.i8_field())) {
      return false;
    }

    if (!(i16_field() == other.i16_field())) {
      return false;
    }

    if (!(i32_field() == other.i32_field())) {
      return false;
    }

    if (!(i64_field() == other.i64_field())) {
      return false;
    }

    if (!(list_string_field() == other.list_string_field())) {
      return false;
    }

    if (!(map_string_string_field() == other.map_string_string_field())) {
      return false;
    }

    if (!(required_i32_field() == other.required_i32_field())) {
      return false;
    }

    if (!(required_string_field() == other.required_string_field())) {
      return false;
    }

    if (!(set_string_field() == other.set_string_field())) {
      return false;
    }

    if (!(string_field() == other.string_field())) {
      return false;
    }

    if (!(struct_field() == other.struct_field())) {
      return false;
    }

    if (!(u32_field() == other.u32_field())) {
      return false;
    }

    if (!(u64_field() == other.u64_field())) {
      return false;
    }

    if (!(url_field() == other.url_field())) {
      return false;
    }

    return true;
  }

  void read(::thryft::protocol::InputProtocol& iprot) {
    read(iprot, ::thryft::protocol::Type::STRUCT);
  }

  void read(::thryft::protocol::InputProtocol& iprot, ::thryft::protocol::Type::Enum as_type) {
    switch (as_type) {
      case ::thryft::protocol::Type::LIST: {
        ::thryft::protocol::Type::Enum list_element_type;
        uint32_t list_size;
        iprot.read_list_begin(list_element_type, list_size);
        binary_field_ = iprot.read_string();
        bool_field_ = iprot.read_bool();
        date_time_field_ = iprot.read_i64();
        decimal_field_ = iprot.read_string();
        email_address_field_ = iprot.read_string();
        enum_field_ = ::thryft_test::protocol::test::ProtocolTestEnum::read(iprot);
        i8_field_ = iprot.read_byte();
        i16_field_ = iprot.read_i16();
        i32_field_ = iprot.read_i32();
        i64_field_ = iprot.read_i64();
        list_string_field_.set(::thryft::List< ::std::string, ::thryft::protocol::Type::STRING >())->read(iprot);
        map_string_string_field_.set(::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING >())->read(iprot);
        required_i32_field_ = iprot.read_i32();
        iprot.read_string(required_string_field_);
        if (list_size > 14) {
          set_string_field_.set(::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING >())->read(iprot);
        }
        if (list_size > 15) {
          string_field_ = iprot.read_string();
        }
        if (list_size > 16) {
          struct_field_.set(::thryft_test::protocol::test::NestedProtocolTestStruct())->read(iprot);
        }
        if (list_size > 17) {
          u32_field_ = iprot.read_u32();
        }
        if (list_size > 18) {
          u64_field_ = iprot.read_u64();
        }
        if (list_size > 19) {
          url_field_ = iprot.read_string();
        }
        iprot.read_list_end();
        break;
      }

      case ::thryft::protocol::Type::STRUCT:
      default: {
        iprot.read_struct_begin();
        int16_t ifield_id;
        ::std::string ifield_name;
        ::thryft::protocol::Type::Enum ifield_type;
        for (;;) {
          iprot.read_field_begin(ifield_name, ifield_type, ifield_id);
          if (ifield_type == ::thryft::protocol::Type::STOP) {
            break;
          } else if (ifield_name == "binary_field") {
            binary_field_ = iprot.read_string();
          } else if (ifield_name == "bool_field") {
            bool_field_ = iprot.read_bool();
          } else if (ifield_name == "date_time_field") {
            date_time_field_ = iprot.read_i64();
          } else if (ifield_name == "decimal_field") {
            decimal_field_ = iprot.read_string();
          } else if (ifield_name == "email_address_field") {
            email_address_field_ = iprot.read_string();
          } else if (ifield_name == "enum_field") {
            enum_field_ = ::thryft_test::protocol::test::ProtocolTestEnum::read(iprot);
          } else if (ifield_name == "i8_field") {
            i8_field_ = iprot.read_byte();
          } else if (ifield_name == "i16_field") {
            i16_field_ = iprot.read_i16();
          } else if (ifield_name == "i32_field") {
            i32_field_ = iprot.read_i32();
          } else if (ifield_name == "i64_field") {
            i64_field_ = iprot.read_i64();
          } else if (ifield_name == "list_string_field") {
            list_string_field_.set(::thryft::List< ::std::string, ::thryft::protocol::Type::STRING >())->read(iprot);
          } else if (ifield_name == "map_string_string_field") {
            map_string_string_field_.set(::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING >())->read(iprot);
          } else if (ifield_name == "required_i32_field") {
            required_i32_field_ = iprot.read_i32();
          } else if (ifield_name == "required_string_field") {
            iprot.read_string(required_string_field_);
          } else if (ifield_name == "set_string_field") {
            set_string_field_.set(::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING >())->read(iprot);
          } else if (ifield_name == "string_field") {
            string_field_ = iprot.read_string();
          } else if (ifield_name == "struct_field") {
            struct_field_.set(::thryft_test::protocol::test::NestedProtocolTestStruct())->read(iprot);
          } else if (ifield_name == "u32_field") {
            u32_field_ = iprot.read_u32();
          } else if (ifield_name == "u64_field") {
            u64_field_ = iprot.read_u64();
          } else if (ifield_name == "url_field") {
            url_field_ = iprot.read_string();
          }
          iprot.read_field_end();
        }
        iprot.read_struct_end();
        break;
      }
    }
  }

  void write(::thryft::protocol::OutputProtocol& oprot) const {
    write(oprot, ::thryft::protocol::Type::STRUCT);
  }

  void write(::thryft::protocol::OutputProtocol& oprot, ::thryft::protocol::Type::Enum as_type) const {
    switch (as_type) {
    case ::thryft::protocol::Type::VOID:
    case ::thryft::protocol::Type::LIST:
      oprot.write_list_begin(::thryft::protocol::Type::VOID, 20);

      if (binary_field().present()) {
          oprot.write(binary_field().get());
      } else {
          oprot.write_null();
      }

      if (bool_field().present()) {
          oprot.write(bool_field().get());
      } else {
          oprot.write_null();
      }

      if (date_time_field().present()) {
          oprot.write(date_time_field().get());
      } else {
          oprot.write_null();
      }

      if (decimal_field().present()) {
          oprot.write(decimal_field().get());
      } else {
          oprot.write_null();
      }

      if (email_address_field().present()) {
          oprot.write(email_address_field().get());
      } else {
          oprot.write_null();
      }

      if (enum_field().present()) {
          ::thryft_test::protocol::test::ProtocolTestEnum::write(oprot, enum_field().get());
      } else {
          oprot.write_null();
      }

      if (i8_field().present()) {
          oprot.write(i8_field().get());
      } else {
          oprot.write_null();
      }

      if (i16_field().present()) {
          oprot.write(i16_field().get());
      } else {
          oprot.write_null();
      }

      if (i32_field().present()) {
          oprot.write(i32_field().get());
      } else {
          oprot.write_null();
      }

      if (i64_field().present()) {
          oprot.write(i64_field().get());
      } else {
          oprot.write_null();
      }

      if (list_string_field().present()) {
          oprot.write(list_string_field().get());
      } else {
          oprot.write_null();
      }

      if (map_string_string_field().present()) {
          oprot.write(map_string_string_field().get());
      } else {
          oprot.write_null();
      }

      oprot.write(required_i32_field());

      oprot.write(required_string_field());

      if (set_string_field().present()) {
          oprot.write(set_string_field().get());
      } else {
          oprot.write_null();
      }

      if (string_field().present()) {
          oprot.write(string_field().get());
      } else {
          oprot.write_null();
      }

      if (struct_field().present()) {
          oprot.write(struct_field().get());
      } else {
          oprot.write_null();
      }

      if (u32_field().present()) {
          oprot.write(u32_field().get());
      } else {
          oprot.write_null();
      }

      if (u64_field().present()) {
          oprot.write(u64_field().get());
      } else {
          oprot.write_null();
      }

      if (url_field().present()) {
          oprot.write(url_field().get());
      } else {
          oprot.write_null();
      }

      oprot.write_list_end();
      break;

    case ::thryft::protocol::Type::STRUCT:
    default:
      oprot.write_struct_begin();

      if (binary_field().present()) {
          oprot.write_field_begin("binary_field", ::thryft::protocol::Type::STRING, static_cast<int16_t>(-1));
          oprot.write(binary_field().get());
          oprot.write_field_end();
      }

      if (bool_field().present()) {
          oprot.write_field_begin("bool_field", ::thryft::protocol::Type::BOOL, static_cast<int16_t>(-1));
          oprot.write(bool_field().get());
          oprot.write_field_end();
      }

      if (date_time_field().present()) {
          oprot.write_field_begin("date_time_field", ::thryft::protocol::Type::I64, static_cast<int16_t>(-1));
          oprot.write(date_time_field().get());
          oprot.write_field_end();
      }

      if (decimal_field().present()) {
          oprot.write_field_begin("decimal_field", ::thryft::protocol::Type::STRING, static_cast<int16_t>(-1));
          oprot.write(decimal_field().get());
          oprot.write_field_end();
      }

      if (email_address_field().present()) {
          oprot.write_field_begin("email_address_field", ::thryft::protocol::Type::STRING, static_cast<int16_t>(-1));
          oprot.write(email_address_field().get());
          oprot.write_field_end();
      }

      if (enum_field().present()) {
          oprot.write_field_begin("enum_field", ::thryft::protocol::Type::STRING, static_cast<int16_t>(-1));
          ::thryft_test::protocol::test::ProtocolTestEnum::write(oprot, enum_field().get());
          oprot.write_field_end();
      }

      if (i8_field().present()) {
          oprot.write_field_begin("i8_field", ::thryft::protocol::Type::BYTE, static_cast<int16_t>(-1));
          oprot.write(i8_field().get());
          oprot.write_field_end();
      }

      if (i16_field().present()) {
          oprot.write_field_begin("i16_field", ::thryft::protocol::Type::I16, static_cast<int16_t>(-1));
          oprot.write(i16_field().get());
          oprot.write_field_end();
      }

      if (i32_field().present()) {
          oprot.write_field_begin("i32_field", ::thryft::protocol::Type::I32, static_cast<int16_t>(-1));
          oprot.write(i32_field().get());
          oprot.write_field_end();
      }

      if (i64_field().present()) {
          oprot.write_field_begin("i64_field", ::thryft::protocol::Type::I64, static_cast<int16_t>(-1));
          oprot.write(i64_field().get());
          oprot.write_field_end();
      }

      if (list_string_field().present()) {
          oprot.write_field_begin("list_string_field", ::thryft::protocol::Type::LIST, static_cast<int16_t>(-1));
          oprot.write(list_string_field().get());
          oprot.write_field_end();
      }

      if (map_string_string_field().present()) {
          oprot.write_field_begin("map_string_string_field", ::thryft::protocol::Type::MAP, static_cast<int16_t>(-1));
          oprot.write(map_string_string_field().get());
          oprot.write_field_end();
      }

      oprot.write_field_begin("required_i32_field", ::thryft::protocol::Type::I32, static_cast<int16_t>(-1));
      oprot.write(required_i32_field());
      oprot.write_field_end();

      oprot.write_field_begin("required_string_field", ::thryft::protocol::Type::STRING, static_cast<int16_t>(-1));
      oprot.write(required_string_field());
      oprot.write_field_end();

      if (set_string_field().present()) {
          oprot.write_field_begin("set_string_field", ::thryft::protocol::Type::SET, static_cast<int16_t>(-1));
          oprot.write(set_string_field().get());
          oprot.write_field_end();
      }

      if (string_field().present()) {
          oprot.write_field_begin("string_field", ::thryft::protocol::Type::STRING, static_cast<int16_t>(-1));
          oprot.write(string_field().get());
          oprot.write_field_end();
      }

      if (struct_field().present()) {
          oprot.write_field_begin("struct_field", ::thryft::protocol::Type::STRUCT, static_cast<int16_t>(-1));
          oprot.write(struct_field().get());
          oprot.write_field_end();
      }

      if (u32_field().present()) {
          oprot.write_field_begin("u32_field", ::thryft::protocol::Type::I32, static_cast<int16_t>(-1));
          oprot.write(u32_field().get());
          oprot.write_field_end();
      }

      if (u64_field().present()) {
          oprot.write_field_begin("u64_field", ::thryft::protocol::Type::I64, static_cast<int16_t>(-1));
          oprot.write(u64_field().get());
          oprot.write_field_end();
      }

      if (url_field().present()) {
          oprot.write_field_begin("url_field", ::thryft::protocol::Type::STRING, static_cast<int16_t>(-1));
          oprot.write(url_field().get());
          oprot.write_field_end();
      }

      oprot.write_field_stop();

      oprot.write_struct_end();
      break;
    }
  }

private:
  ::thryft::Optional< ::std::string > binary_field_;
  ::thryft::Optional< bool > bool_field_;
  ::thryft::Optional< int64_t > date_time_field_;
  ::thryft::Optional< ::std::string > decimal_field_;
  ::thryft::Optional< ::std::string > email_address_field_;
  ::thryft::Optional< ::thryft_test::protocol::test::ProtocolTestEnum::Enum > enum_field_;
  ::thryft::Optional< int8_t > i8_field_;
  ::thryft::Optional< int16_t > i16_field_;
  ::thryft::Optional< int32_t > i32_field_;
  ::thryft::Optional< int64_t > i64_field_;
  ::thryft::Optional< ::thryft::List< ::std::string, ::thryft::protocol::Type::STRING > > list_string_field_;
  ::thryft::Optional< ::thryft::Map< ::std::string, ::thryft::protocol::Type::STRING, ::std::string, ::thryft::protocol::Type::STRING > > map_string_string_field_;
  int32_t required_i32_field_;
  ::std::string required_string_field_;
  ::thryft::Optional< ::thryft::Set< ::std::string, ::thryft::protocol::Type::STRING > > set_string_field_;
  ::thryft::Optional< ::std::string > string_field_;
  ::thryft::Optional< ::thryft_test::protocol::test::NestedProtocolTestStruct > struct_field_;
  ::thryft::Optional< uint32_t > u32_field_;
  ::thryft::Optional< uint64_t > u64_field_;
  ::thryft::Optional< ::std::string > url_field_;
};
}
}
}

#endif  // _THRYFT_TEST_PROTOCOL_TEST_PROTOCOL_TEST_STRUCT_HPP_
