from thryft.generator.i16_type import I16Type
from thryft.generators.dart._dart_numeric_type import _DartNumericType


class DartI16Type(I16Type, _DartNumericType):
    def dart_name(self):
        return 'int'
