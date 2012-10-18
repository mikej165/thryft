from thryft.generator.container_types.set_type import SetType
from thryft.generators.java.java_sequence_type import JavaSequenceType


class JavaSetType(SetType, JavaSequenceType):
    def _java_mutable_raw_qname(self):
        return 'java.util.LinkedHashSet'

    def java_to_summary_string(self, value):
        element_type_qname = self.element_type.java_qname(boxed=True)
        return '"set<%(element_type_qname)s>" + "(size=" + Integer.toString(%(value)s.size()) + ")"' % locals()
