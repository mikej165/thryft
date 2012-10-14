from thryft.protocol.json_protocol import BuiltinsProtocol
from thryft_test.protocol.test._protocol_test import _ProtocolTest


class BuiltinsProtocolTest(_ProtocolTest):
    def _test(self, in_object):
        obuiltin = []
        oprot = BuiltinsProtocol(obuiltin)
        in_object.write(oprot)
        iprot = BuiltinsProtocol(obuiltin)
        out_object = in_object.read(iprot)
        self.assertEquals(in_object, out_object)
