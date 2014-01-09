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

from thryft.generator.i32_type import I32Type
from thryft.generator.native_type import NativeType
from thryft.generators.cpp.cpp_i32_type import CppI32Type
from thryft.generators.cpp.cpp_native_type import CppNativeType
from thryft.generators.java.java_native_type import JavaNativeType
from thryft.generators.js.js_native_type import JsNativeType
from thryft.generators.py.py_native_type import PyNativeType


class _U32(object):
    def thrift_ttype_id(self):
        return I32Type.THRIFT_TTYPE_ID

    def thrift_ttype_name(self):
        return I32Type.THRIFT_TTYPE_NAME


class CppU32(_U32, CppNativeType):
    __cpp_i32_type = CppI32Type()

    def cpp_default_value(self):
        return 'static_cast<uint32_t>(0)'

    def cpp_includes_use(self):
        return self.__cpp_i32_type.cpp_includes_use()

    def cpp_qname(self):
        return 'uint32_t'

    def cpp_read_protocol(self, *args, **kwds):
        return "static_cast<uint32_t>(%s)" % self.__cpp_i32_type.cpp_read_protocol(*args, **kwds)


class JavaU32(_U32, JavaNativeType):
    def java_qname(self, boxed=False):
        return 'com.google.common.primitives.UnsignedInteger'

    def java_faker(self, validation=None, **kwds):
        parameters = []
        if validation is not None:
            max_ = validation.get('max')
            if max_ is not None:
                parameters.append("com.google.common.primitives.UnsignedInteger.valueOf(%s)" % max_)
        parameters = ', '.join(parameters)
        return "org.thryft.Faker.randomU32(%(parameters)s)" % locals()

    def java_is_reference(self):
        return True

    def java_read_protocol(self):
        return 'iprot.readU32()'

    def java_read_protocol_throws_unchecked(self):
        return ['NumberFormatException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeU32(%(value)s);" % locals()


class JsU32(_U32, JsNativeType):
    def js_default_value(self):
        return '"0"'

    def js_is_model(self):
        return False

    def js_name(self):
        return 'string'

    def js_qname(self):
        return 'string'

    def js_read_protocol(self):
        return 'iprot.readU32()'

    def js_schema(self):
        return {'type': 'Number'}

    def js_validation(self, value, value_name, **kwds):
        return {'pattern': 'number', 'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        return """oprot.writeU32(%(value)s);""" % locals()


class PyU32(_U32, PyNativeType):
    def py_check(self, value):
        return "isinstance(%(value)s, int) and %(value)s >= 0" % locals()

    def _py_imports_definition(self, caller_stack):
        return []

    def _py_imports_use(self, caller_stack):
        return []

    def py_name(self):
        return 'int'

    def py_read_protocol(self):
        return 'iprot.readU32()'

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_qname(self):
        return 'int'

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.writeU32(%(value)s)" % locals()
