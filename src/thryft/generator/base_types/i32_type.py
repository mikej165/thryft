from thryft.generator.base_type import BaseType


class I32Type(BaseType):
    def thrift_ttype_id(self):
        return 8
