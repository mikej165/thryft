from thryft.generator.compound_type import CompoundType


class StructType(CompoundType):
    def thrift_ttype_id(self):
        return 12

    def thrift_ttype_name(self):
        return 'STRUCT'
