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

from thryft.compiler.parser import Parser
from thryft.compiler.scanner import Scanner
from thryft_test import _test
import sys
import traceback


class ParserTest(_test._Test):
    def _runTest(self, thrift_file_path):
#        import logging
#        logging.basicConfig(level=logging.DEBUG)
#        import os.path
#        if os.path.split(thrift_file_path)[1] != 'struct_type.thrift':
#            return
        tokens = []
        try:
            tokens = Scanner().tokenize(thrift_file_path)
            ast = Parser().parse(tokens)  # @UnusedVariable
            # import pprint; pprint.pprint(ast.to_dict())
        except:
            print >> sys.stderr, 'Error parsing', thrift_file_path
            traceback.print_exc()
            for token in tokens:
                print >> sys.stderr, token.index, token.type, ':', len(token.text), ':', token.text
            print >> sys.stderr
            raise

def load_tests(*args, **kwds):
    return ParserTest.suite()
