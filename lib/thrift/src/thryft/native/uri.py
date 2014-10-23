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

from thryft.generator.string_type import StringType


class Uri(object):
    def __init__(self, *args, **kwds):
        pass

    def cpp_includes_use(self):
        return ['<string>']

    def cpp_qname(self):
        return '::std::string'

    def dart_from_core_type(self, value):
        return "Uri.parse(%(value)s)" % locals()

    def dart_name(self):
        return 'Uri'

    def dart_to_core_type(self, value):
        return value + '.toString()'

    def java_declaration_name(self, boxed=False):
        return 'org.thryft.native_.Uri'

    def java_default_value(self):
        return 'null'

    def java_name(self, boxed=False):
        return 'org.thryft.native_.Uri'

    def java_qname(self, boxed=False):
        return 'org.thryft.native_.Uri'

    def java_is_reference(self):
        return True

    def java_read_protocol(self):
        return 'org.thryft.native_.Uri.parse(iprot.readString())'

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeString(%(value)s.toString());" % locals()

    def js_schema(self):
        return {'type': 'Text', 'validators': ['url']}

    def js_validation(self, value, value_name, **kwds):
        return {'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}

    def thrift_ttype_id(self):
        return StringType.THRIFT_TTYPE_ID

    def thrift_ttype_name(self):
        return StringType.THRIFT_TTYPE_NAME
