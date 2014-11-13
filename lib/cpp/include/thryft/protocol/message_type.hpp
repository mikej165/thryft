#ifndef _THRYFT_PROTOCOL_MESSAGE_TYPE_HPP_
#define _THRYFT_PROTOCOL_MESSAGE_TYPE_HPP_

namespace thryft {
namespace protocol {
enum class MessageType {
  CALL = 1,
  REPLY = 2,
  EXCEPTION = 3,
  ONEWAY = 4
};
}
}

#endif  // _THRYFT_PROTOCOL_MESSAGE_TYPE_HPP_
