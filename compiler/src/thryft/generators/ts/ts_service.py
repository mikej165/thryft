from thryft.generator.service import Service
from thryft.generators.ts._ts_named_construct import _TsNamedConstruct


class TsService(Service, _TsNamedConstruct):
    def ts_repr(self):
        name = self.ts_name()
        return """\
class %(name)s {
}""" % locals()
