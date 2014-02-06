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

from thryft.generator._construct import _Construct


class _NamedConstruct(_Construct):
    def __init__(self, name, **kwds):
        _Construct.__init__(self, **kwds)
        assert name is not None
        self.__name = name

    @property
    def name(self):
        return self.__name

    def _qname(self, scope, include_parent_document_name=True, **kwds):
        if self.parent is None:
            return getattr(self, scope + '_name')(**kwds)
        from thryft.generator.document import Document
        parent_document = self.parent
        while not isinstance(parent_document, Document):
            parent_document = parent_document.parent
        if parent_document is None:
            return getattr(self, scope + '_name')(**kwds)
        qname = []
        try:
            qname.append(parent_document.namespace_by_scope(scope).name)
        except KeyError:
            pass
        if include_parent_document_name:
            qname.append(parent_document.name)
        qname.append(getattr(self, scope + '_name')(**kwds))
        return '.'.join(qname)

    def thrift_qname(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.name + '.' + self.name
