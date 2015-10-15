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

from thryft.generator.service import Service
from thryft.generators.js._js_named_construct import _JsNamedConstruct
from yutil import indent


class JsService(Service, _JsNamedConstruct):
    def js_repr(self):
        qname = self.js_qname()

        if len(self.functions) == 0:
            return """\
%(qname)s = function() {
};
""" % locals()

        sections = []

        message_types = []
        for function in self.functions:
            message_types.extend(function.js_message_types())
        if len(message_types) > 0:
            sections.append("%(qname)sMessages = {};" % locals())
            message_types = \
                "\n\n".join(
                    message_type.js_repr() for message_type in message_types
                )
            sections.append(message_types)

        functions = \
            ",\n\n".join(indent(' ' * 4,
                (function.js_repr()
                 for function in self.functions)
            ))
        sections.append("""
%(qname)s = function() {
};

%(qname)s.prototype = {
%(functions)s
};""" % locals())

        return "\n\n".join(sections)
