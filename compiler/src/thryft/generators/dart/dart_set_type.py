from thryft.generator.set_type import SetType
from thryft.generators.dart._dart_sequence_type import _DartSequenceType


class DartSetType(SetType, _DartSequenceType):
    def _dart_raw_name(self):
        return 'Set'

    def dart_literal(self, value):
        return "new Set<%s>(%s)" % (self.element_type.dart_name(), _DartSequenceType.dart_literal(self, value))
