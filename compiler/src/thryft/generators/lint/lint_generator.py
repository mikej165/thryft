import logging

from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser
from thryft.compiler.valueless_annotation_parser import ValuelessAnnotationParser
from thryft.generator.generator import Generator
from yutil import class_qname


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
            for annotation in self.annotations:
                if annotation.name == 'lint_suppress':
                    return

            optional_field_names = []
            required_field_names = []
            for field in self.fields:
                field_name = field.name

                field_name_lower = field_name.lower()
                if field_name != field_name_lower:
                    self._logger.warn("field %s in %s not lower camelized", field_name, self._parent_document().path)

                field_names = required_field_names if field.required else optional_field_names
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

    class BinaryType(Generator.BinaryType, _Type):  # @UndefinedVariable
        pass

    class Const(Generator.Const, _NamedConstruct):  # @UndefinedVariable
        pass

    class Document(Generator.Document, _NamedConstruct):  # @UndefinedVariable
        def lint(self):
            for definition in self.definitions:
                definition.lint()

            include_relpaths = []
            for include in self.includes:
                if len(include_relpaths) > 0 and cmp(include.relpath, include_relpaths[-1]) < 0:
                    after_include_relpath = ''
                    for include_relpath_i in xrange(len(include_relpaths) - 1, -1, -1):
                        test_include_relpath = include_relpaths[include_relpath_i]
                        if cmp(include.relpath, test_include_relpath) >= 0:
                            after_include_relpath = test_include_relpath
                            break
                    self._logger.warn("include %s in %s is out of lexicographic order (should be right after %s)", include.relpath, self._parent_document().path, after_include_relpath)
                include_relpaths.append(include.relpath)

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
                function_names.append(function.name)

    class SetType(Generator.SetType, _SequenceType):  # @UndefinedVariable
        pass

    class StringType(Generator.StringType, _Type):  # @UndefinedVariable
        pass

    class StructType(Generator.StructType, _CompoundType):  # @UndefinedVariable
        pass

Parser.register_annotation_parser(ValuelessAnnotationParser('lint_suppress', (Ast.EnumTypeNode, Ast.ExceptionTypeNode, Ast.ServiceNode, Ast.StructTypeNode)))
