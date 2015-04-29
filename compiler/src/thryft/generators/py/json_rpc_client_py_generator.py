#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

from thryft.generator._base_type import _BaseType
from thryft.generators.py import py_generator
from thryft.generators.py.py_function import PyFunction
from thryft.generators.py.py_service import PyService
from yutil import indent, decamelize


class JsonRpcClientPyGenerator(py_generator.PyGenerator):
    class Function(PyFunction):
        def py_repr(self):
            if self.return_field is not None:
                if isinstance(self.return_field.type, _BaseType):
                    call_prefix = 'return '
                    call_suffix = ''
                else:
                    call_prefix = 'return_value = '
                    call_suffix = """
    iprot = thryft.protocol.json_input_protocol.JsonInputProtocol(return_value)
    return %s""" % self.return_field.type.py_read_protocol()
            else:
                call_prefix = call_suffix = ''
            name = self.py_name()
            return """\
def _%(name)s(self, **kwds):
    %(call_prefix)sself.__request('%(name)s', **kwds)%(call_suffix)s
""" % locals()

    class Service(PyService):
        def py_imports_definition(self):
            return ['import ' + PyService.py_qname(self).rsplit('.', 1)[0],
                    'import thryft.protocol.builtins_input_protocol',
                    'import thryft.protocol.builtins_output_protocol',
                    'import thryft.protocol.json_input_protocol',
                    'from urlparse import urlparse',
                    'import base64',
                    'import json',
                    'import logging',
                    'import re',
                    'import urllib2',
                    ] + \
                    PyService.py_imports_definition(self)

        def __py_methods(self):
            methods = {}
            methods.update(self.__py_method_import_exception_class())
            methods.update(self.__py_method_init())
            methods.update(self.__py_method_request())
            for function in self.functions:
                methods[function.py_name()] = function.py_repr()
            return [methods[method_name] for method_name in sorted(methods.iterkeys())]

        def __py_method_import_exception_class(self):
            return {'__import_exception_class': """\
@staticmethod
def __import_exception_class(exception_class_qname):
    def decamelize(name):
        return re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\\\1', name)\\
                   .lower()\\
                   .strip('_')

    exception_class_qname_split = exception_class_qname.split('.')
#     if len(exception_class_qname) < 2:
#         raise
#     elif exception_class_qname[0] not in ('com', 'org'):
#         raise

    exception_class_name = exception_class_qname_split[-1]
    exception_module_qname = \\
        exception_class_qname_split[:-1] + \\
            [decamelize(exception_class_name)]

    exception_module = __import__('.'.join(exception_module_qname))
    for module_name in exception_module_qname[1:]:
        exception_module = getattr(exception_module, module_name)

    return getattr(exception_module, exception_class_name)
""" % locals()}

        def __py_method_init(self):
            name = self._py_name()
            service_endpoint_name = decamelize(PyService.py_name(self)).rsplit('_', 1)[0]
            service_qname = PyService.py_qname(self)
            return {'__init__': """\
def __init__(self, api_url, headers=None):
    %(service_qname)s.__init__(self)

    if headers is None:
        headers = {}
    else:
        if not isinstance(headers, dict):
            raise TypeError(headers)
        headers = headers.copy()

    api_url = api_url.rstrip('/')
    if not api_url.endswith('/jsonrpc/%(service_endpoint_name)s'):
        api_url += '/jsonrpc/%(service_endpoint_name)s'
    self.__api_url = api_url.rstrip('/')
    parsed_api_url = urlparse(api_url)
    parsed_api_url_netloc = parsed_api_url.netloc.split('@', 1)
    if len(parsed_api_url_netloc) == 2:
        username_password = parsed_api_url_netloc[0].split(':', 1)
        if len(username_password) == 2:
            username, password = username_password
            netloc = parsed_api_url_netloc[1]
            headers['Authorization'] = \\
                'Basic ' + \\
                    base64.b64encode(
                        "%%s:%%s" %% (
                            username,
                            password
                        )
                    )
            self.__api_url = \\
                parsed_api_url.scheme + '://' + netloc + \\
                    parsed_api_url.path + \\
                    parsed_api_url.query

#            auth_handler = urllib2.HTTPBasicAuthHandler()
#            auth_handler.add_password(realm='Realm',
#                                      uri=self.__api_url,
#                                      user=username,
#                                      passwd=password)
#            opener = urllib2.build_opener(auth_handler)
#            urllib2.install_opener(opener)

    self.__headers = headers

    self.__logger = logging.getLogger(self.__class__.__module__ + '.' + self.__class__.__name__)

    self.__next_id = 1
""" % locals()}

        def __py_method_request(self):
            return {'__request': """\
def __request(self, method, headers=None, **kwds):
    request = {'jsonrpc': '2.0', 'method': method}
    request['id'] = id(request)
    params_oprot = thryft.protocol.builtins_output_protocol.BuiltinsOutputProtocol()
    params_oprot.write_struct_begin()
    for key, value in kwds.iteritems():
        if value is None:
            continue
        params_oprot.write_field_begin(key)
        params_oprot.write_variant(value)
        params_oprot.write_field_end()
    params_oprot.write_struct_end()
    request['params'] = params_oprot.value
    request_json = json.dumps(request)

    if headers is not None:
        headers = headers.copy()
        headers.update(self.__headers)
    else:
        headers = self.__headers

    http_request = urllib2.Request(self.__api_url, request_json, headers)
    http_request.get_method = lambda: 'POST'

    http_response = urllib2.urlopen(http_request)

    response_json = []
    while True:
        response_datum = http_response.read()
        if len(response_datum) == 0:
            break
        response_json.append(response_datum)
    response_json = ''.join(response_json)

    response = json.loads(response_json)
    if str(response.get('id')) != str(request['id']):
        raise RuntimeError("JSON-RPC: mismatched id: got %%s, expected %%s" %% (response.get('id'), request['id']))
    if response.get('jsonrpc') != '2.0':
        raise RuntimeError("JSON-RPC: unexpected version: " + str(response.get('jsonrpc')))
    error = response.get('error')
    if error is not None:
        code = error.get('code')
        if code is None:
            raise RuntimeError("JSON-RPC: error response is missing code")
        message = error.get('message')
        if message is None:
            raise RuntimeError("JSON-RPC: error response is missing message")
        exception_class_qname = error.get('@class')
        if exception_class_qname is not None:
            try:
                exception_class = self.__import_exception_class(exception_class_qname)
            except ImportError:
                raise RuntimeError("JSON-RPC: error: code=%%(code)u, message='%%(message)s'" %% locals())
            data = error.get('data')
            if isinstance(data, dict):
                data_iprot = thryft.protocol.builtins_input_protocol.BuiltinsInputProtocol(data)
                exception_ = exception_class.read(data_iprot)
                raise exception_
            else:
                raise exception_class()
        else:
            raise RuntimeError("JSON-RPC error: code=%%s, message='%%s'" %% (code, message))
    return response.get('result')
""" % locals()}

        def _py_name(self):
            return 'JsonRpcClient' + PyService.py_name(self)

        def py_repr(self):
            methods = indent(' ' * 4, "\n".join(self.__py_methods()))
            name = self._py_name()
            service_qname = PyService.py_qname(self)
            return """\
class %(name)s(%(service_qname)s):
%(methods)s
""" % locals()
