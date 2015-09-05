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

from thryft.generator.include import Include
from thryft.generators.java._java_construct import _JavaConstruct
from yutil import upper_camelize, rpad


class JavaInclude(Include, _JavaConstruct):
    def __init__(self, *args, **kwds):
        Include.__init__(self, *args, **kwds)

        java_class_qname = self.path.rsplit('.', 1)[0].replace('/', '.')
        java_class_qname_split = java_class_qname.rsplit('.', 1)

        java_class_name = upper_camelize(java_class_qname_split.pop(-1))

        java_package = self.document.java_package()
        if java_package is None:
            if len(java_class_qname_split) > 0:
                java_package = java_class_qname_split[0]
            else:
                java_package = ''

        self.__java_class_name = java_class_name
        self.__java_package = java_package

    def java_class_name(self):
        return self.__java_class_name

    def java_class_qname(self):
        return rpad(self.__java_package, '.') + self.__java_class_name

    def java_package(self):
        return self.__java_package

    def java_repr(self):
        return 'import ' + self.java_class_qname() + ';'
