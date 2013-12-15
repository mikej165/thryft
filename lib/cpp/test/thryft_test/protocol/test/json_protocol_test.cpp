#include "./protocol_test.hpp"

#include "thryft/protocol/json_input_protocol.hpp"

namespace thryft_test {
namespace protocol {
namespace test {
using ::thryft::protocol::JsonInputProtocol;

INSTANTIATE_TYPED_TEST_CASE_P(JsonInputProtocol, ProtocolTest, JsonInputProtocol);
}
}
}
