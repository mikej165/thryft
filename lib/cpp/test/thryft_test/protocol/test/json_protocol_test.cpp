#include "./protocol_test.hpp"

#include "thryft/protocol/json_protocol.hpp"

namespace thryft_test {
namespace protocol {
namespace test {
using ::thryft::protocol::JsonProtocol;

INSTANTIATE_TYPED_TEST_CASE_P(JsonProtocol, ProtocolTest, JsonProtocol);
}
}
}
