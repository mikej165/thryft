from thryft.generator._compound_type import _CompoundType


class ExceptionType(_CompoundType):
    @property
    def fields(self):
        return self._fields
