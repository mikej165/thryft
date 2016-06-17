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

from thryft.generator.exception_type import ExceptionType
from thryft.generators.java._java_compound_type import _JavaCompoundType


class JavaExceptionType(ExceptionType, _JavaCompoundType):
    def __init__(self, **kwds):
        ExceptionType.__init__(self, **kwds)
        _JavaCompoundType.__init__(self, message_type='EXCEPTION', java_suppress_warnings=('serial',), **kwds)

    def _java_extends(self):
        return 'org.thryft.Exception'

    def _java_method_get_message(self):
        return {'getMessage': '''\
@Override
public String getMessage() {
    return toString();
}'''}

    def _java_method_get_thrift_qualified_class_name(self):
        qname = self._parent_document().namespace_by_scope('*').name + '.' + self.parent.name + '.' + self.name
        return {'getThriftQualifiedClassName': """\
@Override
public String getThriftQualifiedClassName() {
    return "%(qname)s";
}""" % locals()}

    def _java_methods(self):
        methods = _JavaCompoundType._java_methods(self)
        methods.update(self._java_method_get_message())
        methods.update(self._java_method_get_thrift_qualified_class_name())
        return methods
