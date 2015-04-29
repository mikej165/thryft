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
from thryft.generators.thrift.thrift_base_type import ThriftBaseType


class ThriftGenerator(Generator):
    from thryft.generators.thrift.thrift_enum_type import ThriftEnumType as EnumType  # @UnusedImport
    from thryft.generators.thrift.thrift_exception_type import ThriftExceptionType as ExceptionType  # @UnusedImport
    from thryft.generators.thrift.thrift_const import ThriftConst as Const  # @UnusedImport
    from thryft.generators.thrift.thrift_document import ThriftDocument as Document  # @UnusedImport
    from thryft.generators.thrift.thrift_field import ThriftField as Field  # @UnusedImport
    from thryft.generators.thrift.thrift_function import ThriftFunction as Function  # @UnusedImport
    from thryft.generators.thrift.thrift_include import ThriftInclude as Include  # @UnusedImport
    from thryft.generators.thrift.thrift_list_type import ThriftListType as ListType  # @UnusedImport
    from thryft.generators.thrift.thrift_map_type import ThriftMapType as MapType  # @UnusedImport
    from thryft.generators.thrift.thrift_namespace import ThriftNamespace as Namespace  # @UnusedImport
    from thryft.generators.thrift.thrift_service import ThriftService as Service  # @UnusedImport
    from thryft.generators.thrift.thrift_set_type import ThriftSetType as SetType  # @UnusedImport
    from thryft.generators.thrift.thrift_struct_type import ThriftStructType as StructType  # @UnusedImport
    from thryft.generators.thrift.thrift_typedef import ThriftTypedef as Typedef  # @UnusedImport

for __base_type_name in ('byte', 'double', 'i16', 'i32', 'i64', 'string'):
    __base_class_name = __base_type_name.capitalize() + 'Type'
    setattr(
        ThriftGenerator,
        __base_class_name,
        type(
            __base_class_name,
            (getattr(Generator, __base_class_name), ThriftBaseType),
            {}
        )
    )
