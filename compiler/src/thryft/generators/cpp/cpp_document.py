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

from thryft.generator.document import Document
from thryft.generator.typedef import Typedef
from thryft.generators.cpp._cpp_named_construct import _CppNamedConstruct
import os.path
from yutil import deduplist, rpad


class CppDocument(Document, _CppNamedConstruct):
    def cpp_includes_use(self):
        namespace = self.cpp_namespace()
        include = []
        if namespace is not None:
            include.extend(namespace.split('.'))
        include.append(self.cpp_name() + '.hpp')
        return ('"' + '/'.join(include) + '"',)

    def cpp_includes_definition(self):
        includes = []
        for definition in self.definitions:
            includes.extend(definition.cpp_includes_definition())
        normalized_includes = []
        for include in includes:
            normalized_include = include.strip()
            if not normalized_include.startswith('#include '):
                normalized_include = '#include ' + normalized_include
            normalized_includes.append(normalized_include)
        normalized_includes = deduplist(normalized_includes)

        std_includes = []
        lib_includes = []
        other_includes = []
        for include in normalized_includes:
            if include.endswith('.hpp>') or include.endswith('.h>'):
                lib_includes.append(include)
            elif include.endswith('"'):
                other_includes.append(include)
            elif include.endswith('>'):
                std_includes.append(include)
            else:
                raise NotImplementedError
        includes = std_includes
        if len(lib_includes) > 0:
            if len(includes) > 0:
                includes.append('')
            includes.extend(lib_includes)
        if len(other_includes) > 0:
            if len(includes) > 0:
                includes.append('')
            includes.extend(other_includes)
        return includes

    def cpp_name(self):
        return self.name

    def cpp_namespace(self):
        namespaces_by_scope = self.namespaces_by_scope
        for scope in ('cpp', '*'):
            try:
                return namespaces_by_scope[scope].name
            except KeyError:
                pass

    def __repr__(self):
        sections = []
        sections.append(
            "\n\n".join(repr(definition)
                         for definition in self.definitions)
        )
        repr_ = "\n\n".join(sections)
        if len(repr_) == 0:
            return repr_

        guard = []
        namespace = self.cpp_namespace()
        if namespace is not None:
            namespace_split = namespace.split('.')
            guard.extend(s.upper() for s in namespace_split)
            repr_ = """\
%s
%s
%s""" % (
    "\n".join("namespace %s {" % s for s in namespace_split),
    repr_,
    "\n".join('}' for _ in namespace_split)
)
        guard.append(self.cpp_name().upper())
        guard = '_' + '_'.join(guard) + '_HPP_'

        repr_ = rpad("\n".join(self.cpp_includes_definition()), "\n\n") + repr_

        repr_ = """\
#ifndef %(guard)s
#define %(guard)s

%(repr_)s

#endif  // %(guard)s
""" % locals()

        return repr_

    def save(self, out_path):
        return Document.save(self, out_path, file_ext='.hpp')
