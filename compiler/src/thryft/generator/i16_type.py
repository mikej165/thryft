from thryft.generator._base_type import _BaseType


class I16Type(_BaseType):
    def thrift_ttype_id(self):
        return 6
