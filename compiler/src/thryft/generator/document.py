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

from collections import OrderedDict
from thryft.generator.include import Include
from thryft.generator._named_construct import _NamedConstruct
from thryft.generator.namespace import Namespace
from yutil import decamelize
import os.path


class Document(_NamedConstruct):
    def __init__(self, path, definitions=None, headers=None, **kwds):
        self.__path = os.path.abspath(path)
        _NamedConstruct.__init__(
            self,
            name=os.path.splitext(os.path.split(self.__path)[1])[0],
            **kwds
        )
        self.__definitions = \
            definitions is not None and list(definitions) or []
        self.__headers = headers is not None and list(headers) or []

    @property
    def definitions(self):
        return self.__definitions

    @property
    def headers(self):
        return self.__headers

    @property
    def includes(self):
        return [header for header in self.headers
                if isinstance(header, Include)]

    def namespace_by_scope(self, scope):
        for namespace in self.namespaces:
            if namespace.scope == scope:
                return namespace
        for namespace in self.namespaces:
            if namespace.scope == '*':
                return namespace
        raise KeyError, scope

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

    def save(self, out_path, file_ext=None, language=None):
        if os.path.isdir(out_path):
            out_dir_path = out_path

            if language is None:
                assert self.__class__.__name__.endswith('Document')
                class_name_decamelized = decamelize(self.__class__.__name__)
                class_name_split = class_name_decamelized.split('_')
                if len(class_name_split) > 1:
                    language = class_name_split[-2]
                else:
                    raise ValueError('unknown language: ' + self.__class__.__name__)

            if file_ext is None:
                file_ext = '.' + language

            namespaces_by_scope = self.namespaces_by_scope
            for scope in (language, '*'):
                scope_namespace = namespaces_by_scope.get(scope)
                if scope_namespace is not None:
                    out_dir_path = \
                        os.path.join(
                            out_dir_path,
                            scope_namespace.name.replace('.', os.path.sep)
                        )
                    break

            return self._save(os.path.join(out_dir_path, self.name + file_ext))
        else:
            return self._save(out_path)

    def _save(self, out_file_path):
        out_dir_path = os.path.split(out_file_path)[0]
        if not os.path.isdir(out_dir_path):
            os.makedirs(out_dir_path)

        repr_ = repr(self)
        if len(repr_) == 0:
            return

        with open(out_file_path, 'w+b') as out_file:
            out_file.write(repr_)
            print 'wrote', out_file_path

        return out_file_path
