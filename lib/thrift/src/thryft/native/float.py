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


class float(object):
    def __init__(self, *args, **kwds):
        pass

    def cpp_default_value(self):
        return 'static_cast<float>(0.0)'

    def cpp_includes_use(self):
        return tuple()

    def cpp_qname(self):
        return 'float'

    def cpp_read_protocol(self, value, optional=False):
        return "%(value)s = static_cast<float>(iprot.read_double());" % locals()

    def java_compare_to(self, this_value, other_value, already_boxed):
        if already_boxed:
            return "%(this_value)s.compareTo(%(other_value)s)" % locals()
        else:
            boxed_name = self.java_name(boxed=True)
            return "((%(boxed_name)s)%(this_value)s).compareTo(%(other_value)s)" % locals()

    def java_name(self, boxed=False):
        return 'Float' if boxed else 'float'

    def java_qname(self, boxed=False):
        return 'Float' if boxed else 'float'

    def java_read_protocol(self):
        return '((float)iprot.readDouble())'

    def py_description(self):
        return 'float'

    def py_qname(self):
        return 'float'

    def py_write_protocol(self, value, depth=0):
        qname = self.py_qname()
        return "oprot.write_double(%(value)s)" % locals()
