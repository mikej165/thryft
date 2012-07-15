from thryft.target.compound_types.struct_type import StructType
from thryft.targets.py.py_compound_type import PyCompoundType
from yutil import indent, pad


class PyStructType(StructType, PyCompoundType):
    def _py_constructor(self):
        assert len(self.fields) > 0
        parameters = []
        for field in self.fields:
            if field.required:
                parameters.append(field.py_parameter())
        for field in self.fields:
            if not field.required:
                parameters.append(field.py_parameter())
        parameters = ",\n".join(indent(' ' * 4, parameters))
        initializers = \
            "\n".join(indent(' ' * 4,
                [field.py_initializer() for field in self.fields]
            ))
        return """\
def __init__(
    self,
%(parameters)s
):
%(initializers)s
""" % locals()

    def _py_from_json_methods(self):
        from_json_methods = {}
        fields_from_json_object = []
        for field in self.fields:
            fields_from_json_object.append(field.py_from_json_object('json_object'))
        fields_from_json_object = \
            pad("\n\n", "\n\n".join(
                fields_from_json_object),
            "\n")
        from_cls_json_object = """\
init_kwds = {}%(fields_from_json_object)s
return cls(**init_kwds)""" % locals()
        from_cls_json_object = indent(' ' * 4, from_cls_json_object)
        name = self.name
        from_json_methods['from_json_object'] = """\
@classmethod
def from_json_object(cls, json_object):
    '''
    Construct a %(name)s from a JSON object.

    @param json_object: JSON object (dict) with optional @class property
    @type json_object: list
    @return: a new %(name)s
    @rtype: %(name)s
    '''

    json_object_class_qname = json_object.get('@class')
    if json_object_class_qname is not None:
        from yogento.common.utils import decamelize

        # Pythonize the type name
        json_object_class_qname_split = json_object_class_qname.split('.')
        json_object_module_name_list = \\
            json_object_class_qname_split[:-1] + \\
                [decamelize(json_object_class_qname_split[-1].split('$', 1)[0])]
        json_object_module_name_str = '.'.join(json_object_module_name_list)
        json_object_class_qname_tail = json_object_class_qname_split[-1].replace('$', '.')
        json_object_class_qname_tail_split = json_object_class_qname_tail.split('.')

        # Check if json_object is an instance of this cls
        if json_object_module_name_str != cls.__module__ or \\
           json_object_class_qname_tail_split[-1] != cls.__name__:
            # json_object is not an instance of this cls;
            # find its actual cls, which should be a subclass of this cls.

            # Import the subclass's module
            json_object_module = __import__(json_object_module_name_str)
            for module_name in json_object_module_name_list[1:]:
                json_object_module = getattr(json_object_module, module_name)

            json_object_class = json_object_module
            for json_object_class_qname_part in json_object_class_qname_tail_split:
                json_object_class = getattr(json_object_class, json_object_class_qname_part)

            # Call the subclass's from_json_object factory method
            return json_object_class.from_json_object(json_object)
        # Else drop down to deserialize this class
    # Else drop down to deserialize this class

%(from_cls_json_object)s
""" % locals()

#        from_json_methods['from_json_str'] = """\
#@classmethod
#def from_json_str(cls, json_str):
#    import json
#    return cls.from_json_object(json.loads(json_str))
#""" % locals()

        return from_json_methods

    def py_from_json_object(self, json_object_variable_name):
        name = self.py_name()
        return "%(name)s.from_json_object(%(json_object_variable_name)s)" % locals()

    def _py_getters(self):
        return dict((field.py_getter_name(), field.py_getter())
                    for field in self.fields)

    def _py_methods(self):
        methods_dict = {}
        methods_dict.update(self._py_from_json_methods())
        methods_dict.update(self._py_getters())
        methods_list = \
           [methods_dict[method_name]
            for method_name in sorted(methods_dict.iterkeys())]
        if len(self.fields) > 0:
            methods_list.insert(0, self._py_constructor())
        return methods_list

    def py_imports(self):
        imports = []
        for field in self.fields:
            imports.extend(field.py_imports())
        return list(set(imports))

    def __repr__(self):
        if len(self.fields) > 0:
            methods = indent(' ' * 4, "\n".join(self._py_methods()))
        else:
            methods = ' ' * 4 + 'pass'
        name = self.py_name()
        return """\
class %(name)s(object):
%(methods)s""" % locals()
