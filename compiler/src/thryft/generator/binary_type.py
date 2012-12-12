from thryft.generator.string_type import StringType


class BinaryType(StringType):
    def thrift_ttype_id(self):
        return 4
