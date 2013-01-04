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
from thryft.generators.thrift.thrift_base_type import ThriftBaseType


 # @PydevCodeAnalysisIgnore
class ThriftGenerator(Generator):
    from thryft.generators.thrift.thrift_enum_type import ThriftEnumType as EnumType
    from thryft.generators.thrift.thrift_exception_type import ThriftExceptionType as ExceptionType
    from thryft.generators.thrift.thrift_struct_type import ThriftStructType as StructType
    from thryft.generators.thrift.thrift_const import ThriftConst as Const
    from thryft.generators.thrift.thrift_list_type import ThriftListType as ListType
    from thryft.generators.thrift.thrift_map_type import ThriftMapType as MapType
    from thryft.generators.thrift.thrift_set_type import ThriftSetType as SetType
    from thryft.generators.thrift.thrift_comment import ThriftComment as Comment
    from thryft.generators.thrift.thrift_document import ThriftDocument as Document
    from thryft.generators.thrift.thrift_field import ThriftField as Field
    from thryft.generators.thrift.thrift_function import ThriftFunction as Function
    from thryft.generators.thrift.thrift_include import ThriftInclude as Include
    from thryft.generators.thrift.thrift_namespace import ThriftNamespace as Namespace
    from thryft.generators.thrift.thrift_service import ThriftService as Service
    from thryft.generators.thrift.thrift_typedef import ThriftTypedef as Typedef

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
