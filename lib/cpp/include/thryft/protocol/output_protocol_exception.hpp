#ifndef _THRYFT_PROTOCOL_OUTPUT_PROTOCOL_EXCEPTION_HPP_
#define _THRYFT_PROTOCOL_OUTPUT_PROTOCOL_EXCEPTION_HPP_

#include "thryft/protocol/protocol_exception.hpp"

namespace thryft {
namespace protocol {
class OutputProtocolException : public ProtocolException {
  public:
    OutputProtocolException() {
    }

    OutputProtocolException(const ::std::string& what)
      : ProtocolException(what) {
    }

    virtual ~OutputProtocolException() throw() {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_OUTPUT_PROTOCOL_EXCEPTION_HPP_
