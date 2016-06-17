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

from thryft.generator.include import Include
from thryft.generators.py._py_construct import _PyConstruct
from yutil import upper_camelize


class PyInclude(Include, _PyConstruct):
    def __init__(self, *args, **kwds):
        Include.__init__(self, *args, **kwds)
        py_module_qname = self.relpath.replace('/', '.')
        py_module_qname_split = py_module_qname.rsplit('.', 1)
        if len(py_module_qname_split) == 2:
            py_module_qname, py_module_name = py_module_qname_split
        else:
            py_module_qname = py_module_name = py_module_qname_split[0]
        self.__py_class_name = upper_camelize(py_module_name)
        try:
            py_module_qname = self.document.namespace_by_scope('py').name + '.' + py_module_name
        except KeyError:
            pass
        self.__py_module_qname = py_module_qname

    def py_class_name(self):
        return self.__py_class_name

    def py_module_qname(self):
        return self.__py_module_qname

    def py_repr(self):
        return 'import ' + self.py_module_qname()
