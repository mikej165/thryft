from thryft.generator.function import Function
from thryft.generators.py.py_construct import PyConstruct
from yutil import indent, pad


class PyFunction(Function, PyConstruct):
    def py_imports(self, caller_stack=None):
        if self.return_type is not None:
            return self.return_type.py_imports(caller_stack=None) + ['import __builtin__']
        else:
            return []

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

        parameter_checks = \
            pad("\n", "\n".join(indent(' ' * 4,
                [parameter.py_check()
                 for parameter in self.parameters]
            )), "\n")

        call = ', '.join(["%s=%s" % (parameter.py_name(), parameter.py_name())
                          for parameter in self.parameters])

        if self.return_type is not None:
            return_value = name + '_return_value'
            while True:
                renamed_return_value = False
                for parameter in self.parameters:
                    if parameter.name == return_value:
                        return_value += '_'
                        renamed_return_value = True
                        break
                if not renamed_return_value:
                    break
            return_prefix = return_value + ' = '
            return_suffix = []
            return_type_check = self.return_type.py_check(return_value)
            return_suffix.append("""\
if not %(return_type_check)s:
    raise TypeError(getattr(__builtin__, 'type')(%(return_value)s))""" % locals())
            return_suffix.append('return ' + return_value)
            return_suffix = "\n\n" + "\n\n".join(indent(' ' * 4, return_suffix))
        else:
            return_prefix = return_suffix = ''

        return """\
def %(name)s(%(parameters)s):%(parameter_checks)s
    %(return_prefix)sself._%(name)s(%(call)s)%(return_suffix)s
""" % locals()


