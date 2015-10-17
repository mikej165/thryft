from thryft.generator.struct_type import StructType
from thryft.generators.ts._ts_compound_type import _TsCompoundType


class TsStructType(StructType, _TsCompoundType):
    def ts_repr(self):
        return _TsCompoundType.ts_repr(self)
