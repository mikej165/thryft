from thryft.generator.service import Service
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct


class DartService(Service, _DartNamedConstruct):
#     def dart_imports_definition(self, caller_stack=None):
#         imports = []
#         for function in self.functions:
#             imports.extend(function.dart_imports_definition(caller_stack=caller_stack))
#         return imports
#
#     def _dart_imports_use(self, caller_stack):
#         raise NotImplementedError

    def __repr__(self):
        return ''
