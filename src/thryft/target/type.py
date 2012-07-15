from thryft.target.construct import Construct
from yutil import class_qname


class Type(Construct):
    def thrift_protocol_name(self):
        raise NotImplementedError(class_qname(self) + '.thrift_protocol_name')
