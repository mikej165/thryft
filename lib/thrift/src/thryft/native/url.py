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

from thryft.generator.struct_type import StructType
from thryft.generators.java.java_struct_type import JavaStructType
from thryft.generators.js.js_struct_type import JsStructType
from thryft.generators.py.py_struct_type import PyStructType


class JavaUrl(JavaStructType):
    def __init__(self, *args, **kwds):
        JavaStructType.__init__(self, *args, **kwds)

    def java_declaration_name(self, boxed=False):
        return 'org.thryft.native_.Url'

    def java_faker(self, **kwds):
        return 'org.thryft.Faker.Internet.url()'

    def java_read_protocol(self):
        return 'iprot.readUrl()'

    def java_read_protocol_throws_checked(self):
        return ['java.net.MalformedURLException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeUrl(%(value)s);" % locals()


class JsUrl(JsStructType):
    def js_default_value(self):
        return '""'

    def js_is_model(self):
        return False

    def js_name(self):
        return 'string'

    def js_qname(self):
        return 'string'

    def js_read_protocol(self):
        return 'iprot.readUrl()'

    def js_schema(self):
        return {'type': 'Text', 'validators': ['url']}

    def js_validation(self, value, value_name, **kwds):
        return {'pattern': 'url', 'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        return "oprot.writeUrl(%(value)s);" % locals()


class PyUrl(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, str)" % locals()

    def _py_imports_definition(self, caller_stack):
        return []

    def _py_imports_use(self, caller_stack):
        return []

    def py_read_protocol(self):
        return 'iprot.readString()'

    def py_read_protocol_throws(self):
        return []

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.writeUrl(%(value)s)" % locals()
