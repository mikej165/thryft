from yutil import class_qname


class _DartConstruct(object):
    def dart_imports_definition(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        imports = self._dart_imports_definition(caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return imports

    def _dart_imports_definition(self, caller_stack):
        return []

    def dart_imports_use(self, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        imports = self._dart_imports_use(caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return imports

    def _dart_imports_use(self, caller_stack):
        return self._dart_imports_definition(caller_stack=caller_stack)

    def dart_repr(self):
        raise NotImplementedError(class_qname(self) + '.dart_repr')
