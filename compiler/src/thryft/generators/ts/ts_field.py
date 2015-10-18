from thryft.generator.field import Field
from thryft.generators.ts._ts_named_construct import _TsNamedConstruct


class TsField(Field, _TsNamedConstruct):
    def ts_accessors(self):
        name = self.ts_name()
        type_qname = self.type.ts_qname()
        return """\
get %(name)s(): %(type_qname)s {
    return this.get('%(name)s');
}

set %(name)s(value: %(type_qname)s) {
    this.set('%(name)s', value);
}""" % locals()

    def _ts_references_use(self, **kwds):
        return self.type.ts_references_use(**kwds)
