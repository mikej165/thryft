from thryft.generator._base_type import _BaseType
from thryft.generators.py import py_generator
from thryft.generators.py.py_function import PyFunction
from thryft.generators.py.py_service import PyService
from thryft.generators._rest_generator import _RestGenerator
from yutil import indent
from thryft.generator.bool_type import BoolType


class RestClientPyGenerator(py_generator.PyGenerator, _RestGenerator):
    class Function(PyFunction, _RestGenerator._RestFunction):
        def __repr__(self):
            name = self.py_name()
            parameters = ['self']
            path_parameter = self.rest_path_parameter()
            if path_parameter is not None:
                parameters.append(path_parameter.py_name())
                if len(self.parameters) > 1:
                    parameters.append('**kwds')
            elif len(self.parameters) > 0:
                parameters.append('**kwds')
            parameters = ', '.join(parameters)

            request_method = self.rest_request_method()
            request_url = "'" + self.parent.rest_path_prefix().rstrip('/') + self.rest_path_prefix() + "'"
            if path_parameter is not None:
                request_url += ' + urllib.quote(' + path_parameter.py_name() + ', safe=\'\')'
            data = query = 'None'
            if request_method in ('POST', 'PUT'):
                if '**kwds' in parameters:
                    data = 'str(thryft.core.protocol.json_protocol.JsonProtocol().writeMixed(dict((key, value) for key, value in kwds.iteritems() if value is not None)))'
            elif '**kwds' in parameters:
                query = 'thryft.core.protocol.string_map_protocol.StringMapProtocol().writeMixed(dict((key, value) for key, value in kwds.iteritems() if value is not None)).to_string_map()'
            super_call = """self._request('%(request_method)s', %(request_url)s, data=%(data)s, query=%(query)s)""" % locals()

            if self.return_type is not None:
                if isinstance(self.return_type, BoolType) and \
                   self.rest_request_method() in ('DELETE', 'HEAD'):
                    super_call = """\
try:
    %(super_call)s
    return True
except urllib2.HTTPError, e:
    if e.code == 404:
        return False
    else:
        raise""" % locals()
                elif isinstance(self.return_type, _BaseType):
                    return_type_read = self.return_type.py_read_protocol()
                    super_call = """\
__return_value = %(super_call)s
iprot = thryft.core.protocol.json_protocol.JsonProtocol(__return_value)
iprot.readListBegin()
__return_value = %(return_type_read)s
iprot.readListEnd()
return __return_value""" % locals()
                else:
                    return_type_read = self.return_type.py_read_protocol()
                    super_call = """\
__return_value = %(super_call)s
iprot = thryft.core.protocol.json_protocol.JsonProtocol(__return_value)
return %(return_type_read)s""" % locals()

            super_call = indent(' ' * 4, super_call)

            return """\
def _%(name)s(%(parameters)s):
%(super_call)s
""" % locals()

    class Service(PyService, _RestGenerator._RestService):
        def py_imports_definition(self):
            imports = \
                   ['import ' + PyService.py_qname(self).rsplit('.', 1)[0],
                    'import thryft.core.protocol.json_protocol',
                    'import thryft.core.protocol.string_map_protocol',
                    'import thryft.web.client.service._rest_client_service'] + \
                   PyService.py_imports_definition(self)
            for function in self.functions:
                if function.rest_request_method() in ('DELETE', 'HEAD') and isinstance(function.return_type, BoolType):
                    imports.append('import urllib2')
                    break
            for function in self.functions:
                if function.rest_path_parameter() is not None:
                    imports.append('import urllib')
                    break
            return imports

        def _py_name(self):
            return 'RestClient' + PyService.py_name(self)

        def __repr__(self):
            name = self._py_name()
            if len(self.functions) > 0:
                methods = \
                    "\n\n".join(indent(' ' * 4,
                        [repr(function) for function in self.functions]
                    ))
            else:
                methods = indent(' ' * 4, 'pass')
            try:
                py_namespace = self.parent.namespaces_by_scope['py']
            except KeyError:
                py_namespace = self.parent.namespaces_by_scope['*']
            service_endpoint_name = py_namespace.name.rsplit('.', 1)[-1]
            service_qname = PyService.py_qname(self)
            return """\
class %(name)s(thryft.web.client.service._rest_client_service._RestClientService, %(service_qname)s):
    def __init__(self, api_url, headers=None):
        api_url = api_url.rstrip('/')
        if not api_url.endswith('/rest/'):
            api_url += '/rest/'
        thryft.web.client.service._rest_client_service._RestClientService.__init__(self, api_url=api_url, headers=headers)

%(methods)s
""" % locals()
