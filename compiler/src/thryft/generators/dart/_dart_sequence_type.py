from thryft.generators.dart._dart_container_type import _DartContainerType


class _DartSequenceType(_DartContainerType):
    def _dart_imports_definition(self, caller_stack):
        raise NotImplementedError

    def _dart_imports_use(self, caller_stack):
        return self.element_type.dart_imports_use(caller_stack=caller_stack)
