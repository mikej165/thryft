from thryft.generator.typedef import Typedef
from thryft.generators.ts._ts_named_construct import _TsNamedConstruct


class TsTypedef(Typedef, _TsNamedConstruct):
    def ts_qname(self):
        return self.type.ts_qname()

    def _ts_references_definition(self, **kwds):
        return self.type.ts_references_definition(**kwds)

    def _ts_references_use(self, **kwds):
        return self.type.ts_references_use(**kwds)

    def ts_repr(self):
        return ''

