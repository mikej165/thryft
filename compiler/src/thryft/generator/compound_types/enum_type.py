from thryft.generator.compound_type import CompoundType


class EnumType(CompoundType):
    def thrift_ttype_id(self):
        return 11

    def thrift_ttype_name(self):
        return 'STRING'
