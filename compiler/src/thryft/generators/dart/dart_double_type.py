from thryft.generator.double_type import DoubleType
from thryft.generators.dart._dart_numeric_type import _DartNumericType


class DartDoubleType(DoubleType, _DartNumericType):
    def dart_name(self):
        return 'double'
