#ifndef _THRYFT_BASE_HPP_
#define _THRYFT_BASE_HPP_

namespace thryft {
namespace protocol {
class InputProtocol;
class OutputProtocol;
}

class Base {
  public:
    virtual void read(protocol::InputProtocol& iprot) = 0;
    virtual void write(protocol::OutputProtocol& oprot) const = 0;
};
}

#endif  // _THRYFT_BASE_HPP_
