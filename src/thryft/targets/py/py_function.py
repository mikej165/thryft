from thryft.target.function import Function


class PyFunction(Function):
    def py_name(self):
        return self.name

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
    raise NotImplementedError
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


