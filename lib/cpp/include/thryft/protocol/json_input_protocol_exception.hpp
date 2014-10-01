#ifndef _THRYFT_PROTOCOL_JSON_INPUT_PROTOCOL_EXCEPTION_HPP_
#define _THRYFT_PROTOCOL_JSON_INPUT_PROTOCOL_EXCEPTION_HPP_

#include "thryft/protocol/input_protocol_exception.hpp"

namespace thryft {
namespace protocol {
class JsonInputProtocolException final : public InputProtocolException {
  public:
    virtual ~JsonInputProtocolException() throw() {
    }
};
}
}

#endif  // _THRYFT_PROTOCOL_INPUT_PROTOCOL_EXCEPTION_HPP_
