from thryft.generator.field import Field
from thryft.generators.dart._dart_named_construct import _DartNamedConstruct
from yutil import lower_camelize


class DartField(Field, _DartNamedConstruct):
    def _dart_imports_definition(self, caller_stack):
        return self.type.dart_imports_definition(caller_stack)

    def _dart_imports_use(self, caller_stack):
        return self.type.dart_imports_use(caller_stack)

    def dart_initializer(self):
        name = self.dart_name()
        return "%(name)s = %(name)s" % locals()

    def dart_member_declaration(self):
        return "%s %s;" % (self.type.dart_name(), self.dart_name())

    def dart_parameter(self):
        parameter = "%s %s" % (self.type.dart_name(), self.dart_name())
        if not self.required:
            parameter += ': '
            if self.value is not None:
                parameter += self.type.dart_literal(self.value)
            else:
                parameter += self.type.dart_default_value()
        return parameter

    def dart_name(self):
        return lower_camelize(self.name)
