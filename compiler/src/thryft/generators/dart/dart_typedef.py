from thryft.generator.typedef import Typedef
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct


class DartTypedef(Typedef, _DartNamedConstruct):
    def dart_imports_definition(self, caller_stack=None):
        return self.type.dart_imports_definition(caller_stack=caller_stack)

    def dart_imports_use(self, caller_stack=None):
        return self.type.dart_imports_use(caller_stack=caller_stack)

    def dart_name(self):
        return self.type.dart_name()
