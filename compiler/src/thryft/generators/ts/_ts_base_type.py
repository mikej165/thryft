from thryft.generators.ts._ts_type import _TsType


class _TsBaseType(_TsType):
    def ts_from_json(self, value):
        return value

    def ts_to_json(self, value):
        return value
