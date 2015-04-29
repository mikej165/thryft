#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------

from thryft.generator.generator import Generator


class CppGenerator(Generator):
    from thryft.generators.cpp.cpp_binary_type import CppBinaryType as BinaryType  # @UnusedImport
    from thryft.generators.cpp.cpp_bool_type import CppBoolType as BoolType  # @UnusedImport
    from thryft.generators.cpp.cpp_byte_type import CppByteType as ByteType  # @UnusedImport
    from thryft.generators.cpp.cpp_const import CppConst as Const  # @UnusedImport
    from thryft.generators.cpp.cpp_document import CppDocument as Document  # @UnusedImport
    from thryft.generators.cpp.cpp_double_type import CppDoubleType as DoubleType  # @UnusedImport
    from thryft.generators.cpp.cpp_enum_type import CppEnumType as EnumType  # @UnusedImport
    from thryft.generators.cpp.cpp_exception_type import CppExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.cpp.cpp_field import CppField as Field  # @UnusedImport
    from thryft.generators.cpp.cpp_function import CppFunction as Function  # @UnusedImport
    from thryft.generators.cpp.cpp_i16_type import CppI16Type as I16Type  # @UnusedImport
    from thryft.generators.cpp.cpp_i32_type import CppI32Type as I32Type  # @UnusedImport
    from thryft.generators.cpp.cpp_i64_type import CppI64Type as I64Type  # @UnusedImport
    from thryft.generators.cpp.cpp_include import CppInclude as Include  # @UnusedImport
    from thryft.generators.cpp.cpp_list_type import CppListType as ListType  # @UnusedImport
    from thryft.generators.cpp.cpp_map_type import CppMapType as MapType  # @UnusedImport
    from thryft.generators.cpp.cpp_service import CppService as Service  # @UnusedImport
    from thryft.generators.cpp.cpp_set_type import CppSetType as SetType  # @UnusedImport
    from thryft.generators.cpp.cpp_string_type import CppStringType as StringType  # @UnusedImport
    from thryft.generators.cpp.cpp_struct_type import CppStructType as StructType  # @UnusedImport
    from thryft.generators.cpp.cpp_typedef import CppTypedef as Typedef  # @UnusedImport

    def __init__(
        self,
        cpp_exception_includes_definition=None,
        cpp_exception_parent_class_qname='::thryft::Exception',
        cpp_service_includes_definition=None,
        cpp_service_parent_class_qname='::thryft::Service',
    ):
        Generator.__init__(self)
        self.__cpp_exception_includes_definition = cpp_exception_includes_definition if cpp_exception_includes_definition is not None else tuple()
        self.__cpp_exception_parent_class_qname = cpp_exception_parent_class_qname
        self.__cpp_service_includes_definition = cpp_service_includes_definition if cpp_service_includes_definition is not None else tuple()
        self.__cpp_service_parent_class_qname = cpp_service_parent_class_qname

    @property
    def cpp_exception_includes_definition(self):
        return self.__cpp_exception_includes_definition

    @property
    def cpp_exception_parent_class_qname(self):
        return self.__cpp_exception_parent_class_qname

    @property
    def cpp_service_includes_definition(self):
        return self.__cpp_service_includes_definition

    @property
    def cpp_service_parent_class_qname(self):
        return self.__cpp_service_parent_class_qname
