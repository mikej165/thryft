from thryft.generator.named_construct import NamedConstruct
from yutil import class_qname


class Type(NamedConstruct):
    def thrift_ttype_id(self):
        raise NotImplementedError(class_qname(self) + '.thrift_ttype_id')

    def thrift_ttype_name(self):
        raise NotImplementedError(class_qname(self) + '.thrift_ttype_name')
