from thryft.generator.base_type import BaseType


class ByteType(BaseType):
    def thrift_ttype_id(self):
        return 3
