from thryft.generator.include import Include
from thryft.generators.py.py_construct import PyConstruct
from yutil import upper_camelize


class PyInclude(Include, PyConstruct):
    def __init__(self, *args, **kwds):
        Include.__init__(self, *args, **kwds)
        py_module_qname = self.path.rsplit('.', 1)[0].replace('/', '.')
        py_module_name = py_module_qname.rsplit('.', 1)[1]
        self.__py_class_name = upper_camelize(py_module_name)
        try:
            py_module_qname = self.document.namespaces_by_scope['py'].name + '.' + py_module_name
        except KeyError:
            pass
        self.__py_module_qname = py_module_qname

    def py_class_name(self):
        return self.__py_class_name

    def py_module_qname(self):
        return self.__py_module_qname

    def __repr__(self):
        return 'from ' + self.py_module_qname() + ' import ' + self.py_class_name()
