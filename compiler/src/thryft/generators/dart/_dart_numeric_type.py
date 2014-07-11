from thryft.generators.dart._dart_base_type import _DartBaseType


class _DartNumericType(_DartBaseType):
    def dart_literal(self, value):
        return str(value)
