from thryft.generator._base_type import _BaseType
from thryft.generator.enum_type import EnumType
from yutil import decamelize


class _RestGenerator(object):
    class _RestFunction(object):
        def rest_path_prefix(self):
            name_split = self.name.split('_')
            request_method = self.rest_request_method()
            if request_method in ('GET', 'DELETE', 'HEAD'):
                try:
                    by_i = name_split.index('by')
                except ValueError:
                    by_i = None
                if by_i is not None:
                    path_prefix = '/' + '_'.join(name_split[1:by_i]) + '/'
                else:
                    path_prefix = '/' + '_'.join(name_split[1:])
            elif request_method in ('POST', 'PUT'):
                path_prefix = '/' + '_'.join(name_split[1:])
            else:
                raise NotImplementedError(request_method)

            parent_path_prefix = self.parent.rest_path_prefix()
            assert parent_path_prefix.endswith('/') and len(parent_path_prefix) > 1, parent_path_prefix
            if path_prefix.startswith(parent_path_prefix.rstrip('/')):
                path_prefix = path_prefix[len(parent_path_prefix) - 1:]
                if len(path_prefix) > 0 and path_prefix[0] == '_':
                    path_prefix = '/' + path_prefix[1:]
            return path_prefix

        def rest_path_parameter(self):
            parameters = self.parameters
            if len(parameters) == 0:
                return None
            if self.rest_request_method() not in ('GET', 'DELETE', 'HEAD'):
                return None
            if parameters[0].required and \
               (isinstance(parameters[0].type, _BaseType) or isinstance(parameters[0].type, EnumType)) and \
               (len(parameters) == 1 or \
                len([parameter for parameter in parameters[1:] if not parameter.required]) == 0):
                return parameters[0]
            else:
                return None

        def rest_request_method(self):
            request_method = self.name.split('_', 1)[0].upper()
            assert request_method in ('GET', 'DELETE', 'HEAD', 'POST', 'PUT'), request_method
            return request_method

    class _RestService(object):
        def rest_path_prefix(self):
            assert self.name.endswith('Service')
            return '/' + decamelize(self.name[:-len('Service')]) + '/'


