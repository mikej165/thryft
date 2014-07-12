from thryft.generator.field import Field
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct
from yutil import lower_camelize


class DartField(Field, _DartNamedConstruct):
    def _dart_imports_definition(self, caller_stack):
        return self.type.dart_imports_definition(caller_stack)

    def _dart_imports_use(self, caller_stack):
        return self.type.dart_imports_use(caller_stack)

    def dart_member_declaration(self):
        return "%s %s;" % (self.type.dart_name(), self.dart_name())

    def dart_name(self):
        return lower_camelize(self.name)
