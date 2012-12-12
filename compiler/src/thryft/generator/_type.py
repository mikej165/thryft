from thryft.generator._named_construct import _NamedConstruct
from yutil import class_qname


class _Type(_NamedConstruct):
    def thrift_ttype_id(self):
        raise NotImplementedError(class_qname(self) + '.thrift_ttype_id')

    def thrift_ttype_name(self):
        raise NotImplementedError(class_qname(self) + '.thrift_ttype_name')
