from thryft.generator._base_type import _BaseType
from thryft.generators.py import py_generator
from thryft.generators.py.py_function import PyFunction
from thryft.generators.py.py_service import PyService
from yutil import indent, decamelize


class JsonrpcClientPyGenerator(py_generator.PyGenerator):
    class Function(PyFunction):
        def __repr__(self):
            if self.return_field is not None:
                if isinstance(self.return_field.type, _BaseType):
                    call_prefix = 'return '
                    call_suffix = ''
                else:
                    call_prefix = 'return_value = '
                    call_suffix = """
    iprot = thryft.core.protocol.json_protocol.JsonProtocol(return_value)
    return %s""" % self.return_field.type.py_read_protocol()
            else:
                call_prefix = call_suffix = ''
            name = self.py_name()
            return """\
def _%(name)s(self, **kwds):
    %(call_prefix)sself._request('%(name)s', **kwds)%(call_suffix)s
""" % locals()

    class Service(PyService):
        def py_imports_definition(self):
            return ['import ' + PyService.py_qname(self).rsplit('.', 1)[0],
                    'import thryft.core.protocol.json_protocol',
                    'import thryft.web.client.service._jsonrpc_client_service'] + \
                   PyService.py_imports_definition(self)

        def _py_name(self):
            return 'JsonrpcClient' + PyService.py_name(self)

        def __repr__(self):
            name = self._py_name()
            if len(self.functions) > 0:
                methods = \
                    "\n\n".join(indent(' ' * 4,
                        [repr(function) for function in self.functions]
                    ))
            else:
                methods = indent(' ' * 4, 'pass')
            service_endpoint_name = decamelize(PyService.py_name(self)).rsplit('_', 1)[0]
            service_qname = PyService.py_qname(self)
            return """\
class %(name)s(thryft.web.client.service._jsonrpc_client_service._JsonrpcClientService, %(service_qname)s):
    def __init__(self, api_url, headers=None):
        api_url = api_url.rstrip('/')
        if not api_url.endswith('/jsonrpc/%(service_endpoint_name)s'):
            api_url += '/jsonrpc/%(service_endpoint_name)s'
        thryft.web.client.service._jsonrpc_client_service._JsonrpcClientService.__init__(self, api_url=api_url, headers=headers)

%(methods)s
""" % locals()
