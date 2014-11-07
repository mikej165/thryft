#ifndef _THRYFT_PROTOCOL_INPUT_PROTOCOL_EXCEPTION_HPP_
#define _THRYFT_PROTOCOL_INPUT_PROTOCOL_EXCEPTION_HPP_

#include "thryft/protocol/protocol_exception.hpp"

namespace thryft {
namespace protocol {
class InputProtocolException : public ProtocolException {
  public:
    InputProtocolException() {
    }

    InputProtocolException(const ::std::string& what)
      : ProtocolException(what) {
    }

    virtual ~InputProtocolException() throw() {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_INPUT_PROTOCOL_EXCEPTION_HPP_
