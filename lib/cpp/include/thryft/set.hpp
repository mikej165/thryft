#ifndef _THRYFT_SET_HPP_
#define _THRYFT_SET_HPP_

#include <set>

#include "thryft/base.hpp"
#include "thryft/protocol/protocol.hpp"

namespace thryft {
template <typename ElementCppT, ::thryft::protocol::Protocol::Type::Enum ElementThriftT>
class Set : public ::thryft::Base, public ::std::set<ElementCppT> {
  public:
    Set() {
    }

    Set(protocol::Protocol& iprot) {
      read(iprot);
    }

    virtual ~Set() {
    }

  public:
    void read(protocol::Protocol& iprot) {
      protocol::Protocol::Type::Enum element_type;
      uint32_t size = 0;
      iprot.read_set_begin(element_type, size);
      if (size == 0) {
        iprot.read_set_end();
        return;
      }
      for (uint32_t i = 0; i < size; i++) {
        ElementCppT element;
        iprot.read(element);
        insert(element);
      }
      iprot.read_set_end();
    }

    void write(protocol::Protocol& oprot) const {
      oprot.write_set_begin(ElementThriftT, size());
      for (const_iterator i = begin(); i != end(); ++i) {
        oprot.write(*i);
      }
      oprot.write_set_end();
    }
};
}

#endif  // _THRYFT_SET_HPP_
