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

import os.path
import sys; sys.path.append(os.path.dirname(__file__))
from uri import Uri


class Url(Uri):
    def elastic_search_mapping_dict(self):
        return {'analyzer': 'email_and_url', 'type': 'string'}

    def java_declaration_name(self, boxed=False):
        return 'org.thryft.native_.Url'

    def java_from_string(self, value):
        return "org.thryft.native_.Url.parse(%(value)s)" % locals()

    def java_literal(self, value):
        return "org.thryft.native_.Url.parse(\"%s\")" % value

    def java_name(self, boxed=False):
        return 'org.thryft.native_.Url'

    def java_qname(self, boxed=False):
        return 'org.thryft.native_.Url'

    def java_read_protocol(self):
        return 'org.thryft.native_.Url.parse(iprot.readString())'

    def java_write_protocol(self, value, depth=0):
        return "oprot.writeString(%(value)s.toString());" % locals()

    def js_validation(self, value, value_name, **kwds):
        return {'pattern': 'url', 'type': """\
if (typeof %(value)s !== "string") {
    return "expected %(value_name)s to be a string";
}""" % locals()}
