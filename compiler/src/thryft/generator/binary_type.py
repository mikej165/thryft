from thryft.generator.string_type import StringType


class BinaryType(StringType):
    def thrift_ttype_name(self):
        return 'STRING'
