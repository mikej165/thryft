from thryft.target.compound_type import CompoundType


class EnumType(CompoundType):
    def thrift_protocol_name(self):
        return 'STRING'
