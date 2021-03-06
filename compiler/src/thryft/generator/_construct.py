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

from yutil import class_qname
import logging


class _Construct(object):
    class Annotation(object):
        def __init__(self, name, value=None):
            self.__name = name
            self.__value = value

        @property
        def name(self):
            return self.__name

        @property
        def value(self):
            return self.__value

    def __init__(self, parent, annotations=None, doc=None, **kwds):
        object.__init__(self)
        if annotations is not None:
            annotations = tuple(annotations)
        else:
            annotations = tuple()
        self.__annotations = annotations
        assert doc is None or isinstance(doc, str), type(doc)
        self.__doc = doc
        self.__logger = None
        self.__parent = parent

    @property
    def annotations(self):
        return self.__annotations

    @property
    def doc(self):
        return self.__doc

    @property
    def _logger(self):
        if self.__logger is None:
            self.__logger = logging.getLogger(class_qname(self))
        return self.__logger

    @property
    def parent(self):
        return self.__parent

    def _parent_document(self):
        from thryft.generator.document import Document
        if isinstance(self, Document):
            return self
        else:
            parent = self.parent
            while not isinstance(parent, Document):
                parent = parent.parent
                assert parent is not None
            return parent

    def _parent_generator(self):
        from thryft.generator.generator import Generator  # @UnusedImport
        parent = self.parent
        while not isinstance(parent, Generator):
            parent = parent.parent
            assert parent is not None
        return parent

    def __repr__(self):
        raise NotImplementedError(class_qname(self) + '.__repr__')
