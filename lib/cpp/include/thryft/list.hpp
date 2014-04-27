#ifndef _THRYFT_LIST_HPP_
#define _THRYFT_LIST_HPP_

#include <vector>

#include "thryft/base.hpp"
#include "thryft/protocol/input_protocol.hpp"
#include "thryft/protocol/output_protocol.hpp"

namespace thryft {
template <typename ElementCppT, ::thryft::protocol::Type::Enum ElementThriftT>
class List : public ::thryft::Base, public ::std::vector<ElementCppT> {
  public:
    List() {
    }

    List(protocol::InputProtocol& iprot) {
      read(iprot);
    }

    virtual ~List() {
    }

  public:
    void read(protocol::InputProtocol& iprot) {
      protocol::Type::Enum element_type;
      uint32_t size = 0;
      iprot.read_list_begin(element_type, size);
      if (size == 0) {
        iprot.read_list_end();
        return;
      }
      this->resize(size);
      for (size_t i = 0; i < size; i++) {
        iprot.read((*this)[i]);
      }
      iprot.read_list_end();
    }

    void write(protocol::OutputProtocol& oprot) const {
      oprot.write_list_begin(ElementThriftT, this->size());
      for (auto i = this->cbegin(); i != this->cend(); ++i) {
        oprot.write(*i);
      }
      oprot.write_list_end();
    }
};
}

#endif  // _THRYFT_LIST_HPP_
