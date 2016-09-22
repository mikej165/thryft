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

from thryft.generator.i64_type import I64Type


class DateTime(object):
    def __init__(self, *args, **kwds):
        pass

    def dart_from_core_type(self, value):
        return "new DateTime.fromMillisecondsSinceEpoch(%(value)s)" % locals()

    def dart_imports_definition(self, caller_stack=None):
        return []

    def dart_imports_use(self, caller_stack=None):
        return []

    def dart_name(self):
        return 'DateTime'

    def dart_to_core_type(self, value):
        return value + '.millisecondsSinceEpoch'

    def elastic_search_mapping_dict(self):
        return {'type': 'date'}

    def java_bean_boxed_name(self):
        return self.java_qname()

    def java_bean_boxed_qname(self):
        return self.java_qname()

    def java_boxed_name(self):
        return self.java_qname()

    def java_boxed_qname(self):
        return self.java_qname()

    def java_default_value(self):
        return 'null'

    def java_equals(self, this_value, other_value, **kwds):
        return "%(this_value)s.equals(%(other_value)s)" % locals()

    def java_hash_code(self, value, **kwds):
        return "%(value)s.hashCode()" % locals()

    def java_name(self):
        return self.java_qname()

    def java_qname(self):
        return 'java.util.Date'

    def java_is_reference(self):
        return True

    def java_read_protocol(self):
        return 'iprot.readDateTime()'

    def java_read_protocol_throws_unchecked(self):
        return ['IllegalArgumentException']

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeDateTime(%(value)s);" % locals()

    def js_default_value(self):
        return 'new Date()'

    def js_is_model(self):
        return False

    def js_name(self):
        return 'Date'

    def js_qname(self):
        return 'Date'

    def js_read_protocol(self):
        return 'iprot.readDateTime()'

    def js_schema(self):
        return {'type': 'DateTime'}

    def js_validation(self, value, value_name, **kwds):
        return {'type': """\
if (!(%(value)s instanceof Date)) {
    return "expected %(value_name)s to be a Date";
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        return "oprot.writeDateTime(%(value)s);" % locals()

    def py_check(self, value):
        return "isinstance(%(value)s, datetime.datetime)" % locals()

    def py_description(self):
        return 'datetime.datetime'

    def py_imports_check(self, caller_stack=None):
        return ['import datetime']

    def py_imports_definition(self, caller_stack=None):
        return []

    def py_imports_use(self, caller_stack=None):
        return ['import datetime']

    def py_name(self):
        return 'datetime'

    def py_qname(self):
        return 'datetime.datetime'

    def py_read_protocol(self):
        return 'iprot.read_date_time()'

    def py_read_protocol_throws(self):
        return ['TypeError']

    def py_write_protocol(self, value, depth=0):
        return "oprot.write_date_time(%(value)s)" % locals()

    def sql_name(self):
        return 'TIMESTAMP'

    def thrift_ttype_id(self):
        return I64Type.THRIFT_TTYPE_ID

    def thrift_ttype_name(self):
        return I64Type.THRIFT_TTYPE_NAME

    def ts_qname(self):
        return 'Date'
