import logging

from thryft.generator.generator import Generator
from yutil import class_qname, lower_camelize


class LintGenerator(Generator):
    class _Construct(object):
        def lint(self):
            pass

        @property
        def _logger(self):
            try:
                return self.__logger
            except AttributeError:
                self.__logger = logging.getLogger(class_qname(LintGenerator))
                return self.__logger

    class _NamedConstruct(_Construct):
        pass

    class _Type(_NamedConstruct):
        pass

    class _CompoundType(_Type):
        def lint(self):
            optional_field_names = []
            required_field_names = []
            for field in self.fields:
                field_name = field.name

                field_name_lower = field_name.lower()
                if field_name != field_name_lower:
                    self._logger.warn("field %s in %s not lower camelized", field_name, self._parent_document().path)

                field_names = required_field_names if field.required else optional_field_names
                if field_name not in ('start', 'end'):
                    if len(field_names) > 0 and cmp(field_name, field_names[-1]) < 0:
                        after_field_name = ''
                        for field_name_i in xrange(len(field_names) - 1, -1, -1):
                            test_field_name = field_names[field_name_i]
                            if cmp(field_name, test_field_name) >= 0:
                                after_field_name = test_field_name
                                break
                        self._logger.warn("field %s in %s is out of lexicographic order (should be right after %s)", field_name, self._parent_document().path, after_field_name)
                field_names.append(field_name)

    class _ContainerType(_Type):
        pass

    class _SequenceType(_ContainerType):
        pass

    class Const(Generator.Const, _NamedConstruct):  # @UndefinedVariable
        pass

    class Document(Generator.Document, _NamedConstruct):  # @UndefinedVariable
        def lint(self):
            for definition in self.definitions:
                definition.lint()

    class ExceptionType(Generator.ExceptionType, _CompoundType):  # @UndefinedVariable
        pass

    class EnumType(Generator.EnumType, _Type):  # @UndefinedVariable
        pass

    class I32Type(Generator.I32Type, _Type):  # @UndefinedVariable
        pass

    class I64Type(Generator.I32Type, _Type):  # @UndefinedVariable
        pass

    class ListType(Generator.ListType, _SequenceType):  # @UndefinedVariable
        pass

    class MapType(Generator.MapType, _ContainerType):  # @UndefinedVariable
        pass

    class Service(Generator.Service, _NamedConstruct):  # @UndefinedVariable
        def lint(self):
            function_names = []
            for function in self.functions:
                if len(function_names) > 0 and cmp(function.name, function_names[-1]) < 0:
                    after_function_name = ''
                    for function_name_i in xrange(len(function_names) - 1, -1, -1):
                        test_function_name = function_names[function_name_i]
                        if cmp(function.name, test_function_name) >= 0:
                            after_function_name = test_function_name
                            break
                    self._logger.warn("function %s in %s is out of lexicographic order (should be after %s)", function.name, self._parent_document().path, after_function_name)

    class SetType(Generator.SetType, _SequenceType):  # @UndefinedVariable
        pass

    class StringType(Generator.StringType, _Type):  # @UndefinedVariable
        pass

    class StructType(Generator.StructType, _CompoundType):  # @UndefinedVariable
        pass
