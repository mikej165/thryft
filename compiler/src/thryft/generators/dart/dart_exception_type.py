from thryft.generator.exception_type import ExceptionType
from thryft.generators.dart._dart_compound_type import _DartCompoundType


class DartExceptionType(ExceptionType, _DartCompoundType):
    def __repr__(self):
        return _DartCompoundType.__repr__(self)
