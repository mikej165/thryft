from thryft.generators.ts._ts_container_type import _TsContainerType


class _TsSequenceType(_TsContainerType):
    def ts_qname(self):
        return "%s[]" % self.element_type.ts_qname()
