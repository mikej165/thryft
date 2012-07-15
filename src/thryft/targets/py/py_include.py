from thryft.target.include import Include
from thryft.targets.py.py_construct import PyConstruct
from yutil import upper_camelize


class PyInclude(Include, PyConstruct):
    def __init__(self, *args, **kwds):
        Include.__init__(self, *args, **kwds)
        self.__py_module_name = self.path.rsplit('.', 1)[0].replace('/', '.')
        self.__py_class_name = upper_camelize(self.__py_module_name.rsplit('.', 1)[1])

    def py_class_name(self):
        return self.__py_class_name

    def py_module_name(self):
        return self.__py_module_name

    def __repr__(self):
        return 'from ' + self.py_module_name() + ' import ' + self.py_class_name()
