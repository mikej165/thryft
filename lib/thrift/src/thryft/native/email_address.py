# -----------------------------------------------------------------------------
# Copyright (c) 2015, Minor Gordon
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


class EmailAddress(object):
    def __init__(self, *args, **kwds):
        pass

    def elastic_search_mapping_dict(self):
        return {'analyzer': 'email_and_url', 'type': 'string'}

    def java_default_value(self):
        return 'null'

    def java_from_string(self, value):
        return "new org.thryft.native_.EmailAddress(%(value)s)" % locals()

    def java_literal(self, value):
        return "new org.thryft.native_.EmailAddress(\"%s\")" % value

    def java_name(self, boxed=False):
        return 'org.thryft.native_.EmailAddress'

    def java_qname(self, boxed=False):
        return 'org.thryft.native_.EmailAddress'

    def java_read_protocol(self):
        return 'new org.thryft.native_.EmailAddress(iprot.readString())'

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeString(%(value)s.toString());" % locals()

    def js_default_value(self):
        return '""'

    def js_is_model(self):
        return False

    def js_name(self):
        return 'string'

    def js_qname(self):
        return 'string'

    def js_read_protocol(self):
        return 'iprot.readString()'

    def js_schema(self):
        return {'type': 'Text', 'validators': ['email']}

    def js_validation(self, value, value_name, **kwds):
        return {"minLength": 6, 'pattern': 'email', 'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}

    def js_write_protocol(self, value, depth=0):
        return """oprot.writeString(%(value)s);""" % locals()

    def py_write_protocol(self, value, depth=0):
        return "oprot.write_string(%(value)s)" % locals()
