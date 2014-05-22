#ifndef _THRYFT_PROTOCOL_JSON_INPUT_PROTOCOL_EXCEPTION_HPP_
#define _THRYFT_PROTOCOL_JSON_INPUT_PROTOCOL_EXCEPTION_HPP_

#include "thryft/protocol/input_protocol_exception.hpp"

namespace thryft {
namespace protocol {
class JsonInputProtocolException : public InputProtocolException {
  public:
    virtual ~JsonInputProtocolException() throw() {
    }

  public:
    // thryft::Base
    virtual void read(protocol::InputProtocol& iprot) {
    }

    virtual void write(protocol::OutputProtocol& oprot) const {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_INPUT_PROTOCOL_EXCEPTION_HPP_
