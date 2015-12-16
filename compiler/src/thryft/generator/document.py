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

from collections import OrderedDict
from thryft.generator.include import Include
from thryft.generator._named_construct import _NamedConstruct
from thryft.generator.namespace import Namespace
from yutil import class_qname
import os.path


class Document(_NamedConstruct):
    def __init__(self, path, definitions=None, document_root_dir_path=None, headers=None, **kwds):
        self.__path = path = os.path.abspath(path)
        _NamedConstruct.__init__(
            self,
            name=os.path.splitext(os.path.split(path)[1])[0],
            **kwds
        )
        self.__definitions = \
            definitions is not None and list(definitions) or []
        self.__document_root_dir_path = document_root_dir_path
        self.__headers = headers is not None and list(headers) or []

    @property
    def definitions(self):
        return self.__definitions

    @property
    def document_root_dir_path(self):
        return self.__document_root_dir_path

    @property
    def headers(self):
        return self.__headers

    @property
    def includes(self):
        return [header for header in self.headers
                if isinstance(header, Include)]

    def namespace_by_scope(self, scopes):
        if isinstance(scopes, str):
            scopes = (scopes,)
        if not isinstance(scopes, (list, tuple)):
            raise TypeError(type(scopes))

        for scope in scopes:
            for namespace in self.namespaces:
                if namespace.scope == scope:
                    return namespace
        if '*' not in scopes:
            for namespace in self.namespaces:
                if namespace.scope == '*':
                    return namespace

        raise KeyError("scope(s) %s in %s (available: %s)" % (scopes, self.path, [namespace.scope for namespace in self.namespaces]))

    @property
    def namespaces(self):
        return [header for header in self.headers
                if isinstance(header, Namespace)]

    @property
    def namespaces_by_scope(self):
        return OrderedDict((namespace.scope, namespace)
                            for namespace in self.namespaces)

    @property
    def path(self):
        return self.__path

    def save(self, out_path):
        if os.path.isdir(out_path):
            return self._save_to_dir(out_path)
        else:
            return self._save_to_file(out_path)

    def _save_to_dir(self, out_dir_path):
        raise NotImplementedError(class_qname(self))

    def _save_to_file(self, out_dir_path):
        raise NotImplementedError(class_qname(self))

    def _save_to_file_helper(self, out_file_contents, out_file_path):
        if out_file_contents is None or len(out_file_contents) == 0:
            return

        out_dir_path = os.path.split(out_file_path)[0]
        if not os.path.isdir(out_dir_path):
            os.makedirs(out_dir_path)

        with open(out_file_path, 'w+b') as out_file:
            out_file.write(out_file_contents)
            self._logger.info('wrote ' + out_file_path)

        return out_file_path
