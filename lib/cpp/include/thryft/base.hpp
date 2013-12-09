#ifndef _THRYFT_BASE_HPP_
#define _THRYFT_BASE_HPP_

namespace thryft {
namespace protocol {
class Protocol;
}

class Base {
public:
  virtual void read(protocol::Protocol& iprot) = 0;
  virtual void write(protocol::Protocol& oprot) const = 0;
};
}

#endif  // _THRYFT_BASE_HPP_
