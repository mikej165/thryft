#ifndef _THRYFT_MAP_HPP_
#define _THRYFT_MAP_HPP_

#include <map>

#include "thryft/base.hpp"
#include "thryft/protocol/protocol.hpp"

namespace thryft {
template <
  typename KeyCppT,
  ::thryft::protocol::Protocol::Type::Enum KeyThriftT,
  typename ValueCppT,
  ::thryft::protocol::Protocol::Type::Enum ValueThriftT
>
class Map : public ::thryft::Base, public ::std::map< KeyCppT, ValueCppT > {
public:
  Map() {
  }

  Map(protocol::Protocol& iprot) {
    read(iprot);
  }

  virtual ~Map() {
  }

public:
  void read(protocol::Protocol& iprot) {
    protocol::Protocol::Type::Enum key_type, value_type;
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
      insert(::std::make_pair(key, value));
    }
    iprot.read_map_end();
  }

  void write(protocol::Protocol& oprot) const {
    oprot.write_map_begin(KeyThriftT, ValueThriftT, size());
    for (const_iterator i = begin(); i != end(); ++i) {
      oprot.write(i->first);
      oprot.write(i->second);
    }
    oprot.write_map_end();
  }
};
}

#endif  // _THRYFT_MAP_HPP_
