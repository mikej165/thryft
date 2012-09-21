from thryft.generator.container_types.set_type import SetType
from thryft.generators.java.java_sequence_type import JavaSequenceType


class JavaSetType(SetType, JavaSequenceType):
    def _java_mutable_raw_qname(self):
        return 'java.util.LinkedHashSet'
