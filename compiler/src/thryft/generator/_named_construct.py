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

import imp
from inspect import isclass
import logging
import os.path
from thryft.generator._construct import _Construct


class _NamedConstruct(_Construct):
    def __init__(self, name, overrides=False, **kwds):
        _Construct.__init__(self, **kwds)
        self._overrides = None
        assert name is not None
        self.__name = name

        if overrides is False:
            return
        elif overrides is True:
            # Look for an overrides module
            overrides = False
            for annotation in self.annotations:
                if annotation.name == 'native':
                    overrides = True
                    break
            if not overrides:
                return

            from thryft.generator.document import Document
            if isinstance(self, Document):
                return
            parent_document = self._parent_document()
            overrides_module_file_path = os.path.splitext(parent_document.path)[0] + '.py'
            if not os.path.isfile(overrides_module_file_path):
                return
            overrides_module_dir_path, overrides_module_file_name = \
                os.path.split(overrides_module_file_path)
            overrides_module_name = \
                os.path.splitext(overrides_module_file_name)[0]
            try:
                overrides_module = \
                    imp.load_module(
                        overrides_module_name,
                        *imp.find_module(
                            overrides_module_name,
                            [overrides_module_dir_path]
                        )
                    )
            except ImportError:
                logging.error(
                    "error importing overrides module %s",
                    overrides_module_file_path,
                    exc_info=True
                )
                return

            try:
                overrides_class = getattr(overrides_module, name)
                if not isclass(overrides_class):
                    raise AttributeError
            except AttributeError:
                logging.error(
                    "overrides module %s has no class %s",
                    overrides_module_file_path,
                    name
                )
                return

            try:
                overrides = overrides_class(self)
            except:
                logging.error(
                    "could not instantiate overrides class %s from %s",
                    name,
                    overrides_module_file_path,
                    exc_info=True
                )
                return

        self._overrides = overrides

    def __getattribute__(self, name):
        if name[0] == '_':
            return _Construct.__getattribute__(self, name)

        overrides = object.__getattribute__(self, '_overrides')
        if overrides is None:
            return _Construct.__getattribute__(self, name)

        try:
            return getattr(overrides, name)
        except AttributeError:
            return _Construct.__getattribute__(self, name)

    @property
    def name(self):
        return self.__name

    def _qname(self, scope, include_parent_document_name=True, name=None, **kwds):
        if name is None:
            name = getattr(self, scope + '_name')(**kwds)

        if self.parent is None:
            return name
#         from thryft.generator.document import Document
#         parent_document = self.parent
#         while not isinstance(parent_document, Document):
#             parent_document = parent_document.parent
#         if parent_document is None:
#             return getattr(self, scope + '_name')(**kwds)
        parent_document = self._parent_document()
        qname = []
        try:
            qname.append(parent_document.namespace_by_scope(scope).name)
        except KeyError:
            pass
        if include_parent_document_name:
            qname.append(parent_document.name)
        qname.append(name)
        return '.'.join(qname)

    def thrift_qname(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.name + '.' + self.name
