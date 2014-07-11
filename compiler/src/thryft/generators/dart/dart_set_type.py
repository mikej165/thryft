from thryft.generator.set_type import SetType
from thryft.generators.dart._dart_sequence_type import _DartSequenceType


class DartSetType(SetType, _DartSequenceType):
    def dart_literal(self, value):
        return \
            "new Set<%s>([%s])" % (
                self.element_type.dart_name(),
                ', '.join(self.element_type.dart_literal(element_value)
                          for element_value in value)
            )

    def dart_name(self):
        return "Set<%s>" % self.element_type.dart_name()
