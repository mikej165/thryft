#ifndef _THRYFT_MAP_HPP_
#define _THRYFT_MAP_HPP_

#include <map>

#include "thryft/base.hpp"
#include "thryft/protocol/input_protocol.hpp"
#include "thryft/protocol/output_protocol.hpp"
#include "thryft/protocol/type.hpp"

namespace thryft {
template <
  typename KeyCppT,
  ::thryft::protocol::Type::Enum KeyThriftT,
  typename ValueCppT,
  ::thryft::protocol::Type::Enum ValueThriftT
  >
class Map final : public ::thryft::Base, public ::std::map< KeyCppT, ValueCppT > {
  public:
    Map() {
    }

    Map(protocol::InputProtocol& iprot) {
      read(iprot);
    }

    virtual ~Map() {
    }

  public:
    void read(protocol::InputProtocol& iprot) override {
      protocol::Type key_type, value_type;
      uint32_t size = 0;
      iprot.read_map_begin(key_type, value_type, size);
      if (size == 0) {
        iprot.read_map_end();
        return;
      }
      for (uint32_t i = 0; i < size; i++) {
        KeyCppT key;
        iprot.read(key);
        ValueCppT value;
        iprot.read(value);
        this->insert(::std::make_pair(key, value));
      }
      iprot.read_map_end();
    }

    void write(protocol::OutputProtocol& oprot) const override {
      oprot.write_map_begin(KeyThriftT, ValueThriftT, this->size());
      for (auto i = this->cbegin(); i != this->cend(); ++i) {
        oprot.write(i->first);
        oprot.write(i->second);
      }
      oprot.write_map_end();
    }
};
}

#endif  // _THRYFT_MAP_HPP_
