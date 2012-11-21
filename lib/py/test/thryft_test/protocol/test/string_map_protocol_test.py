from thryft.protocol.string_map_protocol import StringMapProtocol
from thryft_test.protocol.test._protocol_test import _ProtocolTest


class StringMapProtocolTest(_ProtocolTest):
    def _test(self, in_object):
        oprot = StringMapProtocol()
        in_object.write(oprot)
        string_map = oprot.to_string_map()
        self.assertTrue(isinstance(string_map, dict))
        # print string_map
