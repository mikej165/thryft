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

from thryft.generator.const import Const
from thryft.generators.java._java_named_construct import _JavaNamedConstruct
from thryft.generators.java.java_list_type import JavaListType
from thryft.generators.java.java_set_type import JavaSetType


class JavaConst(Const, _JavaNamedConstruct):
    def java_value(self):
        return self._java_value(self.value)

    def _java_value(self, value):
        if isinstance(value, dict):
            return "ImmutableMap.<%s, %s> of(%s)" % (
                self.type.key_type.java_qname(boxed=True),
                self.type.value_type.java_qname(boxed=True),
                ', '.join(self._java_value(key) + ', ' + self._java_value(value_) for key, value_ in value.iteritems())
            )
        elif isinstance(value, (float, int)):
            return str(value)
        elif isinstance(value, str):
            return "\"%s\"" % value
        elif isinstance(value, tuple):
            out_value = ".<%s> of(%s)" % (self.type.element_type.java_qname(boxed=True), ', '.join(self._java_value(element_value) for element_value in value))
            if isinstance(self.type, JavaListType):
                return 'ImmutableList' + out_value
            elif isinstance(self.type, JavaSetType):
                return 'ImmutableSet' + out_value
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError(type(value))

    def __repr__(self):
        name = self.java_name()
        type_name = self.type.java_qname()
        value = self.java_value()
        return "public final static %(type_name)s %(name)s = %(value)s;" % locals()
