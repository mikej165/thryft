from thryft.generator.exception_type import ExceptionType
from thryft.generators.ts._ts_compound_type import _TsCompoundType


class TsExceptionType(ExceptionType, _TsCompoundType):
    def ts_repr(self):
        return _TsCompoundType.ts_repr(self)
