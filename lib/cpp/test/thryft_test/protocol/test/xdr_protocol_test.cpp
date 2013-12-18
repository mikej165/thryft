#include "./protocol_test.hpp"

#include "thryft/protocol/xdr_input_protocol.hpp"

namespace thryft_test {
namespace protocol {
namespace test {
using ::thryft::protocol::XdrInputProtocol;

INSTANTIATE_TYPED_TEST_CASE_P(XdrInputProtocol, ProtocolTest, XdrInputProtocol);
}
}
}
