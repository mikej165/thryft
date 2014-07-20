from thryft.generator.list_type import ListType
from thryft.generators.dart._dart_sequence_type import _DartSequenceType


class DartListType(ListType, _DartSequenceType):
    def _dart_raw_name(self):
        return 'List'
