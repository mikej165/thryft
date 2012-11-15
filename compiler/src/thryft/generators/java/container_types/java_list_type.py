from thryft.generator.container_types.list_type import ListType
from thryft.generators.java.java_sequence_type import JavaSequenceType


class JavaListType(ListType, JavaSequenceType):
    def _java_mutable_raw_qname(self):
        return 'java.util.ArrayList'
