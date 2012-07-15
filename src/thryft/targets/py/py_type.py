from thryft.targets.py.py_construct import PyConstruct


class PyType(PyConstruct):
    def py_from_json_object(self, json_object_variable_name):
        return json_object_variable_name
