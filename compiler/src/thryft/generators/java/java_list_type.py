from thryft.generator.list_type import ListType
from thryft.generators.java._java_sequence_type import _JavaSequenceType


class JavaListType(ListType, _JavaSequenceType):
    def _java_mutable_raw_qname(self):
        return 'java.util.ArrayList'
