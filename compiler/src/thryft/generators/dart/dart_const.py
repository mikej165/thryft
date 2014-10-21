from thryft.generator.const import Const
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct


class DartConst(Const, _DartNamedConstruct):
    def dart_repr(self):
        return "%s = %s" % (self.dart_name(), self.dart_value())

    def dart_value(self):
        return self.type.dart_literal(self.value)
