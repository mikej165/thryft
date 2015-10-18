from thryft.generator.enum_type import EnumType
from thryft.generators.ts._ts_type import _TsType
from yutil import indent


class TsEnumType(EnumType, _TsType):
    def ts_from_json(self, value):
        qname = self.ts_qname()
        return "%(qname)s[%(value)s]" % locals()

    def ts_repr(self):
        enumerators = \
            indent(' ' * 4, ', '.join(
                "%s = %u" % (enumerator.name, enumerator.value)
                             for enumerator in self.enumerators))
        name = self.ts_name()
        return """\
export enum %(name)s {
%(enumerators)s
}""" % locals()

    def ts_to_json(self, value):
        qname = self.ts_qname()
        return "%(qname)s[%(value)s]" % locals()
