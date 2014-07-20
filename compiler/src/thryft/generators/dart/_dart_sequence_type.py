from thryft.generators.dart._dart_container_type import _DartContainerType


class _DartSequenceType(_DartContainerType):
    def dart_from_core_type(self, value):
        element_type_name = self.element_type.dart_name()
        element_from_core_type = self.element_type.dart_from_core_type('e')
        raw_name = self._dart_raw_name()
        return """new %(raw_name)s<%(element_type_name)s>.from((%(value)s as List).map((e) => %(element_from_core_type)s))""" % locals()

    def _dart_imports_definition(self, caller_stack):
        raise NotImplementedError

    def _dart_imports_use(self, caller_stack):
        return self.element_type.dart_imports_use(caller_stack=caller_stack)

    def dart_literal(self, value):
        return \
            "<%s>[%s]" % (
                self.element_type.dart_name(),
                ', '.join(self.element_type.dart_literal(element_value)
                          for element_value in value)
            )

    def dart_name(self):
        return "%s<%s>" % (self._dart_raw_name(), self.element_type.dart_name())
