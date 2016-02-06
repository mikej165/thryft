from thryft.generator.map_type import MapType
from thryft.generators.dart._dart_container_type import _DartContainerType


class DartMapType(MapType, _DartContainerType):
    def dart_from_core_type(self, value):
        key_type_name = self.key_type.dart_name()
        key_from_core_type = self.key_type.dart_from_core_type('key_')
        value_type_name = self.value_type.dart_name()
        value_from_core_type = self.value_type.dart_from_core_type("(%(value)s as Map)[key_]" % locals())
        return """new Map<%(key_type_name)s, %(value_type_name)s>.fromIterable((%(value)s as Map).keys, key: (key_) => %(key_from_core_type)s, value: (key_) => %(value_from_core_type)s)""" % locals()

# Map<String, int> map = new Map.fromIterable(list,
#     key: (item) => item.toString(),
#     value: (item) => item * item));

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
                                      for key, value in value)
            )

    def dart_name(self):
        return "Map<%s, %s>" % (self.key_type.dart_name(), self.value_type.dart_name())
