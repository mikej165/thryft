#ifndef _THRYFT_PROTOCOL_PROTOCOL_EXCEPTION_HPP_
#define _THRYFT_PROTOCOL_PROTOCOL_EXCEPTION_HPP_

#include "thryft/exception.hpp"

namespace thryft {
namespace protocol {
class ProtocolException : public Exception {
  public:
    virtual ~ProtocolException() throw() {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_PROTOCOL_EXCEPTION_HPP_
