#ifndef _THRYFT_LIST_HPP_
#define _THRYFT_LIST_HPP_

#include <vector>

#include "thryft/base.hpp"
#include "thryft/protocol/protocol.hpp"

namespace thryft {
template <typename ElementCppT, ::thryft::protocol::Protocol::Type::Enum ElementThriftT>
class List : public ::thryft::Base, public ::std::vector<ElementCppT> {
  public:
    List() {
    }

    List(protocol::Protocol& iprot) {
      read(iprot);
    }

    virtual ~List() {
    }

  public:
    void read(protocol::Protocol& iprot) {
      protocol::Protocol::Type::Enum element_type;
      uint32_t size = 0;
      iprot.read_list_begin(element_type, size);
      if (size == 0) {
        iprot.read_list_end();
        return;
      }
      resize(size);
      for (size_t i = 0; i < size; i++) {
        iprot.read((*this)[i]);
      }
      iprot.read_list_end();
    }

    void write(protocol::Protocol& oprot) const {
      oprot.write_list_begin(ElementThriftT, size());
      for (const_iterator i = begin(); i != end(); ++i) {
        oprot.write(*i);
      }
      oprot.write_list_end();
    }
};
}

#endif  // _THRYFT_LIST_HPP_
