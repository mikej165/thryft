from yutil import class_qname


class _TsConstruct(object):
    def ts_references_definition(self, caller_file_abspath, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        references = self._ts_references_definition(caller_file_abspath=caller_file_abspath, caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return references

    def _ts_references_definition(self, caller_file_abspath, caller_stack):
        return []

    def ts_references_use(self, caller_file_abspath, caller_stack=None):
        if caller_stack is None:
            caller_stack = []
        elif self in caller_stack:
            return []
        caller_stack.append(self)

        references = self._ts_references_use(caller_file_abspath=caller_file_abspath, caller_stack=caller_stack)

        assert caller_stack[-1] is self
        caller_stack.pop(-1)

        return references

    def _ts_references_use(self, caller_file_abspath, caller_stack):
        return self._ts_references_definition(caller_file_abspath=caller_file_abspath, caller_stack=caller_stack)

    def ts_repr(self):
        raise NotImplementedError(class_qname(self) + '.ts_repr')
