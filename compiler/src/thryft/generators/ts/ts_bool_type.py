from thryft.generator.bool_type import BoolType
from thryft.generators.ts._ts_base_type import _TsBaseType


class TsBoolType(BoolType, _TsBaseType):
    def ts_name(self):
        return 'boolean'