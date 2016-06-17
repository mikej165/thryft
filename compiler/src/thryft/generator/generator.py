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

class Generator(object):
    from thryft.generator.binary_type import BinaryType  # @UnusedImport
    from thryft.generator.bool_type import BoolType  # @UnusedImport
    from thryft.generator.byte_type import ByteType  # @UnusedImport
    from thryft.generator.const import Const  # @UnusedImport
    from thryft.generator.document import Document  # @UnusedImport
    from thryft.generator.double_type import DoubleType  # @UnusedImport
    from thryft.generator.enum_type import EnumType  # @UnusedImport
    from thryft.generator.exception_type import ExceptionType  # @UnusedImport
    from thryft.generator.field import Field  # @UnusedImport
    from thryft.generator.function import Function  # @UnusedImport
    from thryft.generator.i16_type import I16Type  # @UnusedImport
    from thryft.generator.i32_type import I32Type  # @UnusedImport
    from thryft.generator.i64_type import I64Type  # @UnusedImport
    from thryft.generator.include import Include  # @UnusedImport
    from thryft.generator.list_type import ListType  # @UnusedImport
    from thryft.generator.map_type import MapType  # @UnusedImport
    from thryft.generator.namespace import Namespace  # @UnusedImport
    from thryft.generator.service import Service  # @UnusedImport
    from thryft.generator.set_type import SetType  # @UnusedImport
    from thryft.generator.string_type import StringType  # @UnusedImport
    from thryft.generator.struct_type import StructType  # @UnusedImport
    from thryft.generator.typedef import Typedef  # @UnusedImport
