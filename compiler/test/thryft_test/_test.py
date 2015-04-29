#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------

import os.path
import sys
import unittest


class _Test(unittest.TestCase):
    def __init__(self, *args, **kwds):
        self.__thrift_file_path = kwds.pop('thrift_file_path', None)
        unittest.TestCase.__init__(self, *args, **kwds)

    def shortDescription(self):
        return "%s(%s)" % (self.__class__.__name__, os.path.split(self.__thrift_file_path)[1])

    @classmethod
    def suite(cls):
        suite = unittest.TestSuite()

        for dir_path, _, file_names in \
            os.walk(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    '_tests'
                )
            ):
            for file_name in file_names:
                if os.path.splitext(file_name)[1] != '.thrift':
                    continue
                thrift_file_path = os.path.join(dir_path, file_name)
                suite.addTest(cls(thrift_file_path=thrift_file_path))

        return suite

    def runTest(self):
        if self.__thrift_file_path is None:
            return

        thrift_file_name = os.path.split(self.__thrift_file_path)[1]
        # print thrift_file_name
        try:
            self._runTest(self.__thrift_file_path)
        except RuntimeError:
            if thrift_file_name != 'include.thrift':
                raise
        except:
            # print
            raise

    def _runTest(self, thrift_file_path):
        pass
