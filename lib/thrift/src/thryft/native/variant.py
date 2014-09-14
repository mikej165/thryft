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

from thryft.generator.native_type import NativeType
from thryft.generator.struct_type import StructType
from thryft.generators.cpp.cpp_native_type import CppNativeType
from thryft.generators.java.java_native_type import JavaNativeType
from thryft.generators.py.py_native_type import PyNativeType


class _Variant(object):
    def thrift_ttype_id(self):
        return StructType.THRIFT_TTYPE_ID

    def thrift_ttype_name(self):
        return StructType.THRIFT_TTYPE_NAME


class CppVariant(_Variant, CppNativeType):
    def cpp_default_value(self):
        pass

    def cpp_includes_use(self):
        return ('<thryft.hpp>',)

    def cpp_qname(self):
        return '::thryft::native::Variant'

    def cpp_read_protocol(self, value, optional=False):
        return "%(value)s = iprot.read_variant();" % locals()


class JavaVariant(_Variant, JavaNativeType):
    def java_compare_to(self, this_value, other_value):
        return "org.thryft.Comparators.compare(%(this_value)s, %(other_value)s)" % locals()

    def java_declaration_name(self, boxed=True):
        return 'java.lang.Object'

    def java_default_value(self):
        return 'null'

    def java_faker(self, **kwds):
        return 'org.thryft.Faker.Internet.url()'

    def java_is_reference(self):
        return True

    def java_qname(self):
        return 'java.lang.Object'

    def java_read_protocol(self):
        return "iprot.readVariant()" % locals()

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeVariant(%(value)s);" % locals()


class PyVariant(_Variant, PyNativeType):
    def py_check(self, value):
        return 'True'

    def py_read_protocol(self):
        return 'iprot.read_variant()'

    def py_write_protocol(self, value, depth=0):
        return "oprot.write_variant(%(value)s)" % locals()
