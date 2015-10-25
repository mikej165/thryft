from thryft.generators.ts._ts_base_type import _TsBaseType


class _TsNumericType(_TsBaseType):
    def ts_name(self):
        return 'number'
