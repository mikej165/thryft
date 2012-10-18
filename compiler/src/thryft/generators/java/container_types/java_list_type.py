from thryft.generator.container_types.list_type import ListType
from thryft.generators.java.java_sequence_type import JavaSequenceType


class JavaListType(ListType, JavaSequenceType):
    def _java_mutable_raw_qname(self):
        return 'java.util.ArrayList'

    def java_to_summary_string(self, value):
        element_type_qname = self.element_type.java_qname(boxed=True)
        return '"list<%(element_type_qname)s>" + "(size=" + Integer.toString(%(value)s.size()) + ")"' % locals()
