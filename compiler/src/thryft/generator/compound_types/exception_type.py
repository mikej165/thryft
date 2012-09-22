from thryft.generator.compound_type import CompoundType


class ExceptionType(CompoundType): #@ReservedAssignment
    @property
    def fields(self):
        return self._fields
