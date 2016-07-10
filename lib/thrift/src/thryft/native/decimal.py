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

from thryft.generator.string_type import StringType


class Decimal(object):
    def __init__(self, *args, **kwds):
        pass

    def cpp_default_value(self):
        return '"0"'

    def elastic_search_mapping_dict(self):
        return {'index': 'not_analyzed', 'type': 'string'}

    def java_bean_boxed_name(self):
        return self.java_qname()

    def java_bean_boxed_qname(self):
        return self.java_qname()

    def java_boxed_name(self):
        return self.java_qname()

    def java_boxed_qname(self):
        return self.java_qname()

    def java_name(self):
        return self.java_qname()

    def java_qname(self):
        return 'java.math.BigDecimal'

    def java_is_reference(self):
        return True

    def java_read_protocol(self):
        return 'iprot.readDecimal()'

    def java_read_protocol_throws_unchecked(self):
        return ['NumberFormatException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeDecimal(%(value)s);" % locals()

    def js_default_value(self):
        return '"0"'

    def js_is_model(self):
        return False

    def js_name(self):
        return 'string'

    def js_qname(self):
        return 'string'

    def js_read_protocol(self):
        return 'iprot.readDecimal()'

    def js_schema(self):
        return {'type': 'Number'}

    def js_validation(self, value, value_name, **kwds):
        return {'pattern': 'number', 'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        return """oprot.writeDecimal(%(value)s);""" % locals()

    def py_check(self, value):
        return "isinstance(%(value)s, decimal.Decimal)" % locals()

    def py_description(self):
        return 'Decimal'

    def py_imports_use(self, caller_stack=None):
        return ['from __future__ import absolute_import; import decimal']

    def py_name(self):
        return 'Decimal'

    def py_qname(self):
        return 'decimal.Decimal'

    def py_read_protocol(self):
        return 'iprot.read_decimal()'

    def py_read_protocol_throws(self):
        return ['decimal.InvalidOperation', 'TypeError']

    def py_runtime_repr(self, value):
        return "repr(%(value)s)" % locals()

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.write_decimal(%(value)s)" % locals()

    def sql_name(self):
        return 'DECIMAL'

    def thrift_ttype_id(self):
        return StringType.THRIFT_TTYPE_ID

    def thrift_ttype_name(self):
        return StringType.THRIFT_TTYPE_NAME
