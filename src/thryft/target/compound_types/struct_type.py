from thryft.target.compound_type import CompoundType


class StructType(CompoundType):
    def thrift_protocol_name(self):
        return 'STRUCT'
