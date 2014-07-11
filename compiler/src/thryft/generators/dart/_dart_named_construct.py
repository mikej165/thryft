from thryft.generators.dart._dart_construct import _DartConstruct


class _DartNamedConstruct(_DartConstruct):
    def dart_name(self):
        return getattr(self, 'name')
