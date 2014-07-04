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
from thryft.generator.string_type import StringType
from thryft.generators.cpp.cpp_native_type import CppNativeType
from thryft.generators.cpp.cpp_string_type import CppStringType
from thryft.generators.java.java_native_type import JavaNativeType
from thryft.generators.js.js_native_type import JsNativeType
from thryft.generators.py.py_native_type import PyNativeType
from thryft.generators.sql.sql_native_type import SqlNativeType


class _Uri(object):
    def thrift_ttype_id(self):
        return StringType.THRIFT_TTYPE_ID

    def thrift_ttype_name(self):
        return StringType.THRIFT_TTYPE_NAME


class CppUri(_Uri, CppNativeType):
    __cpp_string_type = CppStringType()

    def cpp_default_value(self):
        return self.__cpp_string_type.cpp_default_value()

    def cpp_includes_use(self):
        return self.__cpp_string_type.cpp_includes_use()

    def cpp_qname(self):
        return self.__cpp_string_type.cpp_qname()

    def cpp_read_protocol(self, *args, **kwds):
        return self.__cpp_string_type.cpp_read_protocol(*args, **kwds)


class JavaUri(_Uri, JavaNativeType):
    def java_default_value(self):
        return 'null'

    def java_qname(self, boxed=False):
        return 'org.thryft.native_.Uri'

    def java_faker(self, **kwds):
        return 'org.thryft.Faker.Internet.uri()'

    def java_is_reference(self):
        return True

    def java_read_protocol(self):
        return 'iprot.readUri()'

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeUri(%(value)s);" % locals()


class JsUri(_Uri, JsNativeType):
    def js_default_value(self):
        return '""'

    def js_is_model(self):
        return False

    def js_name(self):
        return 'string'

    def js_qname(self):
        return 'string'

    def js_read_protocol(self):
        return 'iprot.readUri()'

    def js_schema(self):
        return {'type': 'Text', 'validators': ['url']}

    def js_validation(self, value, value_name, **kwds):
        return {'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        return "oprot.writeUri(%(value)s);" % locals()


class PyUri(_Uri, PyNativeType):
    def py_check(self, value):
        return "isinstance(%(value)s, str)" % locals()

    def _py_imports_definition(self, caller_stack):
        return []

    def _py_imports_use(self, caller_stack):
        return []

    def py_name(self):
        return 'str'

    def py_qname(self):
        return 'str'

    def py_read_protocol(self):
        return 'iprot.readString()'

    def py_read_protocol_throws(self):
        return []

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.writeUri(%(value)s)" % locals()


class SqlUri(_Uri, SqlNativeType):
    def sql_name(self):
        return 'VARCHAR'
