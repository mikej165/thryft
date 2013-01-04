#-------------------------------------------------------------------------------
# Copyright (c) 2013, Minor Gordon
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


 # @PydevCodeAnalysisIgnore
class PyGenerator(Generator):
    from thryft.generators.py.py_binary_type import PyBinaryType as BinaryType
    from thryft.generators.py.py_bool_type import PyBoolType as BoolType
    from thryft.generators.py.py_byte_type import PyByteType as ByteType
    from thryft.generators.py.py_double_type import PyDoubleType as DoubleType
    from thryft.generators.py.py_i16_type import PyI16Type as I16Type
    from thryft.generators.py.py_i32_type import PyI32Type as I32Type
    from thryft.generators.py.py_i64_type import PyI64Type as I64Type
    from thryft.generators.py.py_string_type import PyStringType as StringType
    from thryft.generators.py.py_enum_type import PyEnumType as EnumType
    from thryft.generators.py.py_exception_type import PyExceptionType as ExceptionType
    from thryft.generators.py.py_struct_type import PyStructType as StructType
    from thryft.generators.py.py_list_type import PyListType as ListType
    from thryft.generators.py.py_map_type import PyMapType as MapType
    from thryft.generators.py.py_set_type import PySetType as SetType
    from thryft.generators.py.py_document import PyDocument as Document
    from thryft.generators.py.py_field import PyField as Field
    from thryft.generators.py.py_function import PyFunction as Function
    from thryft.generators.py.py_include import PyInclude as Include
    from thryft.generators.py.py_service import PyService as Service
