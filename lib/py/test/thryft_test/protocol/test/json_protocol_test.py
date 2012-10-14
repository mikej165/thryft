from thryft.protocol.json_protocol import JsonProtocol
from thryft_test.protocol.test._protocol_test import _ProtocolTest


class JsonProtocolTest(_ProtocolTest):
    def _test(self, in_object):
        oprot = JsonProtocol()
        in_object.write(oprot)
        ojson = str(oprot)
        iprot = JsonProtocol(ojson)
        out_object = in_object.read(iprot)
        self.assertEquals(in_object, out_object)
