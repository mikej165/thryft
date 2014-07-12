from thryft.generator.string_type import StringType
from thryft.generators.dart._dart_base_type import _DartBaseType


class DartStringType(StringType, _DartBaseType):
    def dart_literal(self, value):
        return "'%s'" % value

    def dart_name(self):
        return 'String'
