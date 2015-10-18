from thryft.generator.enum_type import EnumType
from thryft.generators.ts._ts_type import _TsType


class TsEnumType(EnumType, _TsType):
    def ts_repr(self):
        enumerators = ', '.join("%s = %u" % (enumerator.name, enumerator.value)
                                for enumerator in self.enumerators)
        name = self.ts_name()
        return """\
export enum %(name)s {
%(enumerators)s
}""" % locals()
