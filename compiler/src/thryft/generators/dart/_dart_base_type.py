from thryft.generators.dart._dart_type import _DartType


class _DartBaseType(_DartType):
    def dart_from_core_type(self, value):
        return value

    def dart_to_core_type(self, value):
        return value
