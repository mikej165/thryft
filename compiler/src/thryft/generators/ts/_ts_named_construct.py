from thryft.generators.ts._ts_construct import _TsConstruct


class _TsNamedConstruct(_TsConstruct):
    def ts_name(self):
        return getattr(self, 'name')

    def ts_qname(self):
        return self._qname(include_parent_document_name=False, scope='ts')
