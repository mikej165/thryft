#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------


from time import mktime
from thryft.protocol._output_protocol import _OutputProtocol


class _AbstractOutputProtocol(_OutputProtocol):
    def writeByte(self, byte):
        self.writeI16(byte)
        return self

    def writeDateTime(self, date_time):
        self.write_i64(long(mktime(date_time.timetuple())) * 1000l)
        return self

    def writeDecimal(self, decimal):
        self.write_string(str(decimal))
        return self

    def writeEmailAddress(self, email_address):
        self.write_string(email_address)
        return self

    def writeI16(self, i16):
        self.write_i32(i16)
        return self

    def writeMixed(self, object_):
        if object_ is None:
            self.write_null()
        elif isinstance(object_, dict):
            self.write_map_begin(len(object_))
            for key, value in object_.iteritems():
                self.writeMixed(key)
                self.writeMixed(value)
            self.write_map_end()
        elif isinstance(object_, float):
            self.writeDouble(object_)
        elif isinstance(object_, frozenset):
            self.write_set_begin(len(object_))
            for item in object_:
                self.writeMixed(item)
            self.write_set_end()
        elif isinstance(object_, int):
            self.write_i32(object_)
        elif isinstance(object_, (list, tuple)):
            self.write_list_begin(len(object_))
            for item in object_:
                self.writeMixed(item)
            self.write_list_end()
        elif isinstance(object_, long):
            self.write_i64(object_)
        elif isinstance(object_, basestring):
            self.write_string(object_)
        elif hasattr(object_, 'write'):
            object_.write(self)
        else:
            raise TypeError(type(object_))
        return self

    def write_set_begin(self, *args, **kwds):
        self.write_list_begin()
        return self

    def write_set_end(self):
        self.write_list_end()
        return self

    def writeUrl(self, url):
        self.write_string(url)
        return self
