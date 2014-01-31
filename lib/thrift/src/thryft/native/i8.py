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

from thryft.generators.cpp.cpp_byte_type import CppByteType
from thryft.generators.cpp.cpp_native_type import CppNativeType



class CppI8(CppNativeType):
    __cpp_byte_type = CppByteType()

    def cpp_includes_definition(self):
        return self.__cpp_byte_type.cpp_includes_definition()

    def cpp_includes_use(self):
        return self.__cpp_byte_type.cpp_includes_use()

    def cpp_qname(self):
        return self.__cpp_byte_type.cpp_qname()

    def cpp_read_protocol(self, *args, **kwds):
        return self.__cpp_byte_type.cpp_read_protocol(*args, **kwds)

    def thrift_ttype_id(self):
        return self.__cpp_byte_type.thrift_ttype_id()

    def thrift_ttype_name(self):
        return self.__cpp_byte_type.thrift_ttype_name()

    @property
    def type(self):
        return self