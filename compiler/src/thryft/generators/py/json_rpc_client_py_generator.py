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

from thryft.generator._base_type import _BaseType
from thryft.generators.py import py_generator
from thryft.generators.py.py_function import PyFunction
from thryft.generators.py.py_service import PyService
from yutil import indent, decamelize


class JsonRpcClientPyGenerator(py_generator.PyGenerator):
    def __init__(self, api_url_default=None, service_imports_definition=None):
        py_generator.PyGenerator.__init__(self)
        self._api_url_default = api_url_default
        self._service_imports_definition = tuple(service_imports_definition) if service_imports_definition is not None else tuple()

    class Function(PyFunction):
        def _py_imports_definition(self, caller_stack):
            imports = []
#             for parameter in self.parameters:
#                 imports.extend(parameter.py_imports_use(caller_stack=caller_stack))
            if self.return_field is not None:
                imports.extend(self.return_field.py_imports_use(caller_stack=caller_stack))
            for throw in self.throws:
                for import_ in throw.py_imports_use(caller_stack=caller_stack):
                    imports.append(import_ + '  # @UnusedImport')
            return imports

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
            parameters = ', '.join(['self'] + [parameter.py_parameter()
                                              for parameter in self.parameters])
            if len(self.parameters) > 0:
                parameter_writes = ''.join(parameter.py_write_protocol(value=parameter.py_name())
                                             for parameter in self.parameters)
                construct_params = indent(' ' * 4, """
oprot = thryft.protocol.builtins_output_protocol.BuiltinsOutputProtocol()
oprot.write_struct_begin()
%(parameter_writes)soprot.write_struct_end()

""" % locals())
                params_value = 'oprot.value'
            else:
                construct_params = ''
                params_value = '{}'
            return """\
def _%(name)s(%(parameters)s):%(construct_params)s
    %(call_prefix)sself.__request(method='%(name)s', params=%(params_value)s)%(call_suffix)s
""" % locals()

    class Service(PyService):
        def py_imports_definition(self, caller_stack=None):
            imports = [
                    'import ' + PyService.py_qname(self).rsplit('.', 1)[0],
                    'import thryft.protocol.builtins_input_protocol',
                    'import thryft.protocol.builtins_output_protocol',
                    'import thryft.protocol.json_input_protocol',
                    'from urlparse import urlparse',
                    'import base64',
                    'import json',
                    'import urllib2',
            ]
            for function in self.functions:
                imports.extend(function.py_imports_definition(caller_stack=caller_stack))
            imports.extend(self._parent_generator()._service_imports_definition)
            return imports

        def _py_methods(self):
            methods = {}
            methods.update(self._py_method_init())
            methods.update(self._py_method_request())
            for function in self.functions:
                methods[function.py_name()] = function.py_repr()
            return [methods[method_name] for method_name in sorted(methods.iterkeys())]

        def _py_method_init(self):
            api_url_default = self._parent_generator()._api_url_default
            if api_url_default is not None:
                api_url_parameter = 'api_url=None'
                set_api_url_default = """

    if api_url is None:
        api_url = %(api_url_default)s""" % locals()
            else:
                api_url_parameter = 'api_url'
                set_api_url_default = ''
            name = self.py_name()
            service_endpoint_name = decamelize(PyService.py_name(self)).rsplit('_', 1)[0]
            service_qname = PyService.py_qname(self)
            return {'__init__': """\
def __init__(self, %(api_url_parameter)s, headers=None):
    %(service_qname)s.__init__(self)%(set_api_url_default)s

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

    self.__headers = headers

    self.__next_id = 1
""" % locals()}

#            auth_handler = urllib2.HTTPBasicAuthHandler()
#            auth_handler.add_password(realm='Realm',
#                                      uri=self.__api_url,
#                                      user=username,
#                                      passwd=password)
#            opener = urllib2.build_opener(auth_handler)
#            urllib2.install_opener(opener)

        def _py_method_request(self):
            return {'__request': """\
def __request(self, method, params, headers=None):
    request = {'jsonrpc': '2.0', 'method': method, 'params': params}
    request['id'] = id(request)
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
                exception_class = None
                for exception_class_qname_component in exception_class_qname.split('.'):
                    if exception_class is None:
                        exception_class = globals()[exception_class_qname_component]
                    else:
                        exception_class = getattr(exception_class, exception_class_qname_component)
            except (AttributeError, KeyError):
                exception_class = None

            if exception_class is not None and issubclass(exception_class, Exception):
                data = error.get('data')
                if isinstance(data, dict):
                    data_iprot = thryft.protocol.builtins_input_protocol.BuiltinsInputProtocol(data)
                    exception_ = exception_class.read(data_iprot)
                    raise exception_
                else:
                    raise exception_class()

        raise RuntimeError("JSON-RPC error: code=%%s, message='%%s'" %% (code, message))

    return response.get('result')
""" % locals()}

        def py_name(self):
            return PyService.py_name(self) + 'JsonRpcClient'

        def py_repr(self):
            methods = indent(' ' * 4, "\n".join(self._py_methods()))
            name = self.py_name()
            service_qname = PyService.py_qname(self)
            return """\
class %(name)s(%(service_qname)s):
%(methods)s
""" % locals()
