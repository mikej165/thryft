from thryft.generators.py.py_generator import PyGenerator
from yutil import indent, lpad, decamelize


class PropertiesPyGenerator(PyGenerator):
    def __init__(self, project_name):
        PyGenerator.__init__(self)
        self._project_name = project_name

    class StructType(PyGenerator.StructType):
        def _py_imports_definition(self, caller_stack=None):
            return PyGenerator.StructType._py_imports_definition(self, caller_stack=caller_stack) + ['import os.path']

        def _py_method_load(self):
            field_conversions = []
            for field in self.fields:
                field_name = field.py_name()
                field_value = "properties['%s']" % field_name
                field_from_string = field.type.py_from_string(field_value)
                if field_value == field_from_string:
                    continue
                field_conversion = "%(field_value)s = %(field_from_string)s" % locals()
                if field.required:
                    if field.value is not None:
                        field_conversions.append("""\
if '%(field_name)s' in properties:
    %(field_conversion)s
""" % locals())
                    else:
                        field_conversions.append(field_conversion)
                else:
                    field_conversions.append("""\
if '%(field_name)s' in properties:
    %(field_conversion)s
""" % locals())
            field_conversions = indent(' ' * 4, "\n".join(field_conversions))
            field_names = ', '.join("'%s'" % field.py_name() for field in self.fields)
            project_name = self._parent_generator()._project_name
            project_name_upper = self._parent_generator()._project_name.upper()
            properties_file_name = decamelize(self.name)
            if properties_file_name.endswith('_properties'):
                properties_file_name = properties_file_name[:-len('_properties')]
            properties_file_name = properties_file_name + '.properties'
            set_property_defaults = lpad("\n\n", indent(' ' * 4, self._py_set_property_defaults()))
            return {'load': """\
@classmethod
def load(cls, command_line_properties_file_path=None):
    '''
    Load properties, in order of precedence, from one of four places:
    1 - Those specified on the command line via the --properties option
    1 - The user's home directory: ~/.%(project_name)s/%(properties_file_name)s
    2 - The system properties file: /etc/%(project_name)s/server.properties
    3 - Environment variables (%(project_name_upper)s_{property_name_upper})
    '''

    properties = {}

    for property_name in (%(field_names)s,):
        property_value = os.getenv('%(project_name_upper)s_' + property_name.upper())
        if property_value is not None and len(property_value) > 0:
            properties[property_name] = property_value

    properties_file_paths = []
    properties_file_paths.append(os.path.join('/', 'etc', '%(project_name)s', '%(properties_file_name)s'))
    properties_file_paths.append(os.path.join(os.path.expanduser('~'), '.%(project_name)s', '%(properties_file_name)s'))
    if command_line_properties_file_path is not None:
        properties_file_paths.append(command_line_properties_file_path)
    for properties_file_path in properties_file_paths:
        if not os.path.isfile(properties_file_path):
            continue
        try:
            with open(properties_file_path, 'r') as properties_file:
                for line in properties_file.readlines():
                    line = line.strip()
                    if len(line) == 0:
                        continue
                    property_name, property_value = line.split('=', 1)
                    property_name = property_name.strip()
                    property_value = property_value.strip().replace("\\:", ':')
                    properties[property_name] = property_value
        except IOError:
            raise IOError("failed to load properties file %%s" %% properties_file_path)%(set_property_defaults)s

%(field_conversions)s

    return cls(**properties)
""" % locals()}

        def _py_methods(self):
            return PyGenerator.StructType._py_methods(self, methods_dict=self._py_method_load())

        def _py_set_property_defaults(self):
            return ''
