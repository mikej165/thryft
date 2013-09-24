#ifndef _THRYFT_BASE_HPP_
#define _THRYFT_BASE_HPP_

namespace thryft {
namespace protocol {
class Protocol;
}

class Base {
public:
  virtual void Write(protocol::Protocol& oprot) = 0;
};
}

#endif  // _THRYFT_BASE_HPP_
