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


class JavaDecimal(JavaStructType):
    def java_declaration_name(self, boxed=False):
        return 'java.math.BigDecimal'

    def java_read_protocol(self):
        return "(iprot instanceof org.thryft.core.protocol.Protocol) ? ((org.thryft.core.protocol.Protocol)iprot).readDecimal() : new java.math.BigDecimal(iprot.readString())" % locals()

    def java_read_protocol_throws_unchecked(self):
        return ['NumberFormatException']

    def java_write_protocol(self, value, depth=0):
        return "if (oprot instanceof org.thryft.core.protocol.Protocol) { ((org.thryft.core.protocol.Protocol)oprot).writeDecimal(%(value)s); } else { oprot.writeString(%(value)s.toString()); }" % locals()


class JsDecimal(JsStructType):
    def js_name(self):
        return 'string'

    def js_qname(self):
        return 'string'

    def js_read_protocol(self):
        return '((typeof iprot.readDecimal !== "undefined") ? iprot.readDecimal() : iprot.readString())'

    def js_schema(self):
        return {'type': 'Number'}

    def js_validation(self, value, value_name, **kwds):
        return {'pattern': 'number', 'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        return """if (typeof oprot.writeDecimal !== "undefined") { oprot.writeDecimal(%(value)s); } else { oprot.writeString(%(value)s); }""" % locals()


class PyDecimal(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, decimal.Decimal)" % locals()

    def _py_imports_definition(self, caller_stack):
        return []

    def _py_imports_use(self, caller_stack):
        return ['from __future__ import absolute_import; import decimal']

    def py_read_protocol(self):
        return "iprot.readDecimal() if hasattr(iprot, 'readDecimal') else decimal.Decimal(iprot.readString())" % locals()

    def py_read_protocol_throws(self):
        return ['decimal.InvalidOperation', 'TypeError']

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.writeDecimal(%(value)s) if hasattr(oprot, 'writeDecimal') else oprot.writeString(str(%(value)s))" % locals()
