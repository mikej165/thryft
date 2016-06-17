import logging

from thryft.generator.generator import Generator
from yutil import class_qname


class LintGenerator(Generator):
    class _Construct(object):
        def __init__(self, *args, **kwds):
            self.__logger = logging.getLogger(class_qname(LintGenerator))

        @property
        def _logger(self):
            return self.__logger

    class _NamedConstruct(_Construct):
        pass

    class _Type(_NamedConstruct):
        pass

    class _CompoundType(_Type):
        def __init__(self, *args, **kwds):
            LintGenerator._Type.__init__(self, *args, **kwds)

            optional_field_names = []
            required_field_names = []
            for field in self.fields:
                field_name = field.name
                field_names = required_field_names if field.required else optional_field_names
                if field_name not in ('start', 'end'):
                    if len(field_names) > 0 and cmp(field_name, field_names[-1]) < 0:
                        after_field_name = ''
                        for field_name_i in xrange(len(field_names) - 1, -1, -1):
                            test_field_name = field_names[field_name_i]
                            if cmp(field_name, test_field_name) >= 0:
                                after_field_name = test_field_name
                                break
                        self.__logger.warn("field %s in %s is out of lexicographic order (should be right after %s)", field_name, self.__scope_stack[0].path, after_field_name)
                field_names.append(field_name)

    class ExceptionType(Generator.ExceptionType, _CompoundType):  # @UndefinedVariable
        def __init__(self, *args, **kwds):
            Generator.ExceptionType.__init__(self, *args, **kwds)  # @UndefinedVariable
            LintGenerator._CompoundType.__init__(self, *args, **kwds)

    class Service(Generator.Service, _NamedConstruct):  # @UndefinedVariable
        def __init__(self, *args, **kwds):
            Generator.Service.__init__(self, *args, **kwds)  # @UndefinedVariable
            LintGenerator._NamedConstruct.__init__(self, *args, **kwds)

            function_names = []
            for function in self.functions:
                if len(function_names) > 0 and cmp(function.name, function_names[-1]) < 0:
                    after_function_name = ''
                    for function_name_i in xrange(len(function_names) - 1, -1, -1):
                        test_function_name = function_names[function_name_i]
                        if cmp(function.name, test_function_name) >= 0:
                            after_function_name = test_function_name
                            break
                    self._logger.warn("function %s in %s is out of lexicographic order (should be after %s)", function.name, self._parent_document.path, after_function_name)

    class StructType(Generator.StructType, _CompoundType):  # @UndefinedVariable
        def __init__(self, *args, **kwds):
            Generator.StructType.__init__(self, *args, **kwds)  # @UndefinedVariable
            LintGenerator._CompoundType.__init__(self, *args, **kwds)
