from thryft.target.compound_types.struct_type import StructType
from thryft.targets.py.py_compound_type import PyCompoundType
from yutil import indent, pad, lpad


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

    def _py_method_getters(self):
        return dict((field.py_getter_name(), field.py_getter())
                    for field in self.fields)

    def _py_method_read_protocol(self):
        field_read_protocols = \
            lpad("\n\n", "\n\n".join(indent(' ' * 8,
                [field.java_read_protocol()
                 for field in self.fields]
            )))
        name = self.java_name()
        return {'read': """\
@classmethod
def read(cls, iprot):
    struct_begin = iprot.readStructBegin()
    if struct_begin is None:
        return None
    while True:
        (fname, ftype, fid) = iprot.readFieldBegin()
        if ftype == 
        if (ifield.type == org.apache.thrift.protocol.TType.STOP) {
            break;
        }%(field_read_protocols)s

        iprot.readFieldEnd()
    }
    iprot.readStructEnd();

    return builder.build();
}""" % locals()}

    def _py_methods(self):
        methods_dict = {}
        methods_dict.update(self._py_method_getters())
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
