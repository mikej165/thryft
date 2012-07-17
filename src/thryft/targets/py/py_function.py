from thryft.target.function import Function
from thryft.targets.py.py_construct import PyConstruct


class PyFunction(Function, PyConstruct):
    def py_parameters(self):
        parameters = []
        for parameter in self.parameters:
            if parameter.required:
                parameters.append(parameter.py_parameter())
        for parameter in self.parameters:
            if not parameter.required:
                parameters.append(parameter.py_parameter())
        return parameters

    def py_protected_abstract_definition(self):
        name = self.py_name()
        parameters = ', '.join(['self'] + self.py_parameters())
        return """\
def _%(name)s(%(parameters)s):
    raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._%(name)s')
""" % locals()

    def py_public_delegating_definition(self):
        name = self.py_name()
        parameters = ', '.join(['self'] + self.py_parameters())
        call = ', '.join(["%s=%s" % (parameter.py_name(), parameter.py_name())
                          for parameter in self.parameters])
        return """\
def %(name)s(%(parameters)s):
    return self._%(name)s(%(call)s)
""" % locals()


