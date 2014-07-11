from thryft.generator.bool_type import BoolType
from thryft.generators.dart._dart_base_type import _DartBaseType


class DartBoolType(BoolType, _DartBaseType):
    def dart_literal(self, value):
        return 'true' if value else 'false'

    def dart_name(self):
        return 'bool'
