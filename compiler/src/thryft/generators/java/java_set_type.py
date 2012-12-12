from thryft.generator.set_type import SetType
from thryft.generators.java._java_sequence_type import _JavaSequenceType


class JavaSetType(SetType, _JavaSequenceType):
    def _java_mutable_raw_qname(self):
        return 'java.util.LinkedHashSet'
