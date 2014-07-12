from thryft.generators.dart._dart_named_construct import _DartNamedConstruct


class _DartType(_DartNamedConstruct):
    def dart_default_value(self):
        return 'null'
