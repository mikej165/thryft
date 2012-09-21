from thryft.generator.construct import Construct
from yutil import class_qname


class Type(Construct):
    def thrift_ttype_id(self):
        raise NotImplementedError(class_qname(self) + '.thrift_ttype_id')

    def thrift_ttype_name(self):
        raise NotImplementedError(class_qname(self) + '.thrift_ttype_name')
