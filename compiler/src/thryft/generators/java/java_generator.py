# -----------------------------------------------------------------------------
# Copyright (c) 2015, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

from thryft.generator.generator import Generator
from thryft.compiler.ast import Ast
from thryft.compiler.parser import Parser


class JavaGenerator(Generator):
    from thryft.generators.java.java_binary_type import JavaBinaryType as BinaryType  # @UnusedImport
    from thryft.generators.java.java_bool_type import JavaBoolType as BoolType  # @UnusedImport
    from thryft.generators.java.java_byte_type import JavaByteType as ByteType  # @UnusedImport
    from thryft.generators.java.java_const import JavaConst as Const  # @UnusedImport
    from thryft.generators.java.java_document import JavaDocument as Document  # @UnusedImport
    from thryft.generators.java.java_double_type import JavaDoubleType as DoubleType  # @UnusedImport
    from thryft.generators.java.java_enum_type import JavaEnumType as EnumType  # @UnusedImport
    from thryft.generators.java.java_exception_type import JavaExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.java.java_field import JavaField as Field  # @UnusedImport
    from thryft.generators.java.java_function import JavaFunction as Function  # @UnusedImport
    from thryft.generators.java.java_i16_type import JavaI16Type as I16Type  # @UnusedImport
    from thryft.generators.java.java_i32_type import JavaI32Type as I32Type  # @UnusedImport
    from thryft.generators.java.java_i64_type import JavaI64Type as I64Type  # @UnusedImport
    from thryft.generators.java.java_include import JavaInclude as Include  # @UnusedImport
    from thryft.generators.java.java_list_type import JavaListType as ListType  # @UnusedImport
    from thryft.generators.java.java_map_type import JavaMapType as MapType  # @UnusedImport
    from thryft.generators.java.java_service import JavaService as Service  # @UnusedImport
    from thryft.generators.java.java_set_type import JavaSetType as SetType  # @UnusedImport
    from thryft.generators.java.java_string_type import JavaStringType as StringType  # @UnusedImport
    from thryft.generators.java.java_struct_type import JavaStructType as StructType  # @UnusedImport

    def __init__(self, default_methods=False, function_overloads=False, mutable_compound_types=False, **kwds):
        Generator.__init__(self, **kwds)
        self.__default_methods = default_methods
        self.__function_overloads = function_overloads
        self.__mutable_compound_types = mutable_compound_types

    @property
    def default_methods(self):
        return self.__default_methods

    @property
    def function_overloads(self):
        return self.__function_overloads

    @property
    def mutable_compound_types(self):
        return self.__mutable_compound_types


def __parse_java_escape_to_string_annotation(ast_node, name, value, **kwds):
    if value is not None:
        raise ValueError("@%(name)s does not take a value" % locals())
    ast_node.annotations.append(Ast.AnnotationNode(name=name, **kwds))
Parser.register_annotation(Ast.FieldNode, 'java_escape_to_string', __parse_java_escape_to_string_annotation)


def __parse_java_exclude_from_to_string_annotation(ast_node, name, value, **kwds):
    if value is not None:
        raise ValueError("@%(name)s does not take a value" % locals())
    ast_node.annotations.append(Ast.AnnotationNode(name=name, **kwds))
Parser.register_annotation(Ast.FieldNode, 'java_exclude_from_to_string', __parse_java_exclude_from_to_string_annotation)


def __parse_java_implements(ast_node, name, value, **kwds):
    ast_node.annotations.append(Ast.AnnotationNode(name=name, value=value, **kwds))

for ast_node_type in (Ast.EnumTypeNode, Ast.ExceptionTypeNode, Ast.ServiceNode, Ast.StructTypeNode):
    Parser.register_annotation(ast_node_type, 'java_implements', __parse_java_implements)
