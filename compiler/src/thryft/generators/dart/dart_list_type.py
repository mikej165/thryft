from thryft.generator.list_type import ListType
from thryft.generators.dart._dart_sequence_type import _DartSequenceType


class DartListType(ListType, _DartSequenceType):
    def dart_literal(self, value):
        return "[%s]" % ', '.join(self.element_type.dart_literal(element_value) for element_value in value)

    def dart_name(self):
        return "List<%s>" % self.element_type.dart_name()
