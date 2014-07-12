from thryft.generator.map_type import MapType
from thryft.generators.dart._dart_container_type import _DartContainerType


class DartMapType(MapType, _DartContainerType):
    def _dart_imports_definition(self, caller_stack):
        raise NotImplementedError

    def _dart_imports_use(self, caller_stack):
        imports = []
        imports.extend(self.key_type.dart_imports_use(caller_stack=caller_stack))
        imports.extend(self.value_type.dart_imports_use(caller_stack=caller_stack))
        return imports

    def dart_literal(self, value):
        return \
            "<%s, %s>[%s]" % (
                self.key_type.dart_name(),
                self.value_type.dart_name(),
                ', '.join("%s: %s" % (self.key_type.dart_literal(key), self.value_type.dart_literal(value))
                                      for key, value in value.iteritems())
            )

    def dart_name(self):
        return "Map<%s, %s>" % (self.key_type.dart_name(), self.value_type.dart_name())
