from thryft.generator._base_type import _BaseType
from thryft.generators.py import py_generator
from thryft.generators.py.py_document import PyDocument
from thryft.generators.py.py_function import PyFunction
from thryft.generators.py.py_service import PyService
from yutil import indent
import os.path


class JsonrpcClientPyGenerator(py_generator.PyGenerator):
    class JsonrpcClientPyDocument(PyDocument):
        def _save(self, out_file_path):
            out_dir_path, out_file_name = os.path.split(out_file_path)

            py_namespace = self.namespaces_by_scope['py']
            py_namespace_prefix = 'yogento.api.services.'
            assert py_namespace.name.startswith(py_namespace_prefix), py_namespace.name
            out_root_dir_path = out_dir_path[:-len(py_namespace.name)]
            out_dir_path = \
                os.path.join(
                    out_root_dir_path,
                    'yogento',
                    'client',
                    'services',
                    py_namespace.name[len(py_namespace_prefix):].replace('.', os.path.sep),
                    'impl'
                )

            out_file_name = 'yogento_jsonrpc_' + out_file_name

            out_file_path = os.path.join(out_dir_path, out_file_name)

            return PyDocument._save(self, out_file_path)

    Document = JsonrpcClientPyDocument

    class Function(PyFunction):
        def __repr__(self):
            if self.return_type is not None:
                if isinstance(self.return_type, _BaseType):
                    call_prefix = 'return '
                    call_suffix = ''
                else:
                    call_prefix = 'return_value = '
                    call_suffix = """
    iprot = thryft.protocol.json_protocol.JsonProtocol(return_value)
    return %s""" % self.return_type.py_read_protocol()
            else:
                call_prefix = call_suffix = ''
            name = self.py_name()
            return """\
def _%(name)s(self, **kwds):
    %(call_prefix)sself._request('%(name)s', **kwds)%(call_suffix)s
""" % locals()

    class Service(PyService):
        def py_imports_definition(self):
            return ['import yogento.client.services._yogento_jsonrpc_service',
                    'import ' + PyService.py_qname(self).rsplit('.', 1)[0],
                    'import thryft.protocol.json_protocol'] + \
                   PyService.py_imports_definition(self)

        def _py_name(self):
            return 'YogentoJsonrpc' + PyService.py_name(self)

        def __repr__(self):
            name = self._py_name()
            if len(self.functions) > 0:
                methods = \
                    "\n\n".join(indent(' ' * 4,
                        [repr(function) for function in self.functions]
                    ))
            else:
                methods = indent(' ' * 4, 'pass')
            service_endpoint_name = self.parent.namespaces_by_scope['py'].name.rsplit('.', 1)[-1]
            service_qname = PyService.py_qname(self)
            return """\
class %(name)s(yogento.client.services._yogento_jsonrpc_service._YogentoJsonrpcService, %(service_qname)s):
    def __init__(self, api_url, headers=None):
        api_url = api_url.rstrip('/')
        if not api_url.endswith('/jsonrpc/%(service_endpoint_name)s'):
            api_url += '/jsonrpc/%(service_endpoint_name)s'
        yogento.client.services._yogento_jsonrpc_service._YogentoJsonrpcService.__init__(self, api_url=api_url, headers=headers)

%(methods)s
""" % locals()
