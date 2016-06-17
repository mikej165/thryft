# -----------------------------------------------------------------------------
# Copyright (c) 2016, Minor Gordon
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


class PyGenerator(Generator):
    from thryft.generators.py.py_binary_type import PyBinaryType as BinaryType  # @UnusedImport
    from thryft.generators.py.py_bool_type import PyBoolType as BoolType  # @UnusedImport
    from thryft.generators.py.py_byte_type import PyByteType as ByteType  # @UnusedImport
    from thryft.generators.py.py_const import PyConst as Const  # @UnusedImport
    from thryft.generators.py.py_document import PyDocument as Document  # @UnusedImport
    from thryft.generators.py.py_double_type import PyDoubleType as DoubleType  # @UnusedImport
    from thryft.generators.py.py_enum_type import PyEnumType as EnumType  # @UnusedImport
    from thryft.generators.py.py_exception_type import PyExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.py.py_field import PyField as Field  # @UnusedImport
    from thryft.generators.py.py_function import PyFunction as Function  # @UnusedImport
    from thryft.generators.py.py_i16_type import PyI16Type as I16Type  # @UnusedImport
    from thryft.generators.py.py_i32_type import PyI32Type as I32Type  # @UnusedImport
    from thryft.generators.py.py_i64_type import PyI64Type as I64Type  # @UnusedImport
    from thryft.generators.py.py_include import PyInclude as Include  # @UnusedImport
    from thryft.generators.py.py_list_type import PyListType as ListType  # @UnusedImport
    from thryft.generators.py.py_map_type import PyMapType as MapType  # @UnusedImport
    from thryft.generators.py.py_service import PyService as Service  # @UnusedImport
    from thryft.generators.py.py_set_type import PySetType as SetType  # @UnusedImport
    from thryft.generators.py.py_string_type import PyStringType as StringType  # @UnusedImport
    from thryft.generators.py.py_struct_type import PyStructType as StructType  # @UnusedImport
    from thryft.generators.py.py_typedef import PyTypedef as Typedef  # @UnusedImport
