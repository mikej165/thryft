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


class JavaDateTime(JavaStructType):
    def java_declaration_name(self, boxed=True):
        return 'org.joda.time.DateTime'

    def java_read_protocol(self):
        return "(iprot instanceof org.thryft.core.protocol.Protocol) ? ((org.thryft.core.protocol.Protocol)iprot).readDateTime() : new org.joda.time.DateTime(iprot.readI64())" % locals()

    def java_read_protocol_throws(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "if (oprot instanceof org.thryft.core.protocol.Protocol) { ((org.thryft.core.protocol.Protocol)oprot).writeDateTime(%(value)s); } else { oprot.writeI64(%(value)s.getMillis()); }" % locals()


class JsDateTime(JsStructType):
    def js_read_protocol(self):
        return '((typeof iprot.readDateTime !== "undefined") ? iprot.readDateTime() : new Date(iprot.readI64()))'

    def js_write_protocol(self, value, depth=0):
        return """if (typeof oprot.writeDateTime !== "undefined") { oprot.writeDateTime(%(value)s); } else { oprot.writeI64(%(value)s.getTime()); }""" % locals()


class PyDateTime(PyStructType):
    def py_check(self, value):
        return "isinstance(%(value)s, datetime)" % locals()

    def _py_imports_definition(self, caller_stack):
        return []

    def _py_imports_use(self, caller_stack):
        return ['from datetime import datetime', 'from time import mktime']

    def py_read_protocol(self):
        return "iprot.readDateTime() if hasattr(iprot, 'readDateTime') else datetime.fromtimestamp(iprot.readI64() / 1000.0)" % locals()

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_write_protocol(self, value, depth=0):
        return "oprot.writeDateTime(%(value)s) if hasattr(oprot, 'writeDateTime') else oprot.writeI64(long(mktime(%(value)s.timetuple())) * 1000l)" % locals()
