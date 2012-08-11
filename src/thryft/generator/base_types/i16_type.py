from thryft.generator.base_type import BaseType


class I16Type(BaseType):
    def thrift_ttype_id(self):
        return 6
