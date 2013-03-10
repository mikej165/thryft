class Ast(object):
    class Node(object):
        def __init__(self, children=None):
            object.__init__(self)
            if children is None:
                self.__children = tuple()
            else:
                assert isinstance(children, tuple)
                for child in children:
                    assert child is not None
                self.__children = children

        def __getitem__(self, i):
            return self.__children[i]

    class _NamedNode(Node):
        def __init__(self, name, children=None):
            Ast.Node.__init__(self, children=children)

            assert isinstance(name, str) and len(name) > 0
            self.__name = name

        @property
        def name(self):
            return self.__name

    class _CompoundTypeNode(_NamedNode):
        def __init__(self, fields, name):
            Ast.Node.__init__(self, children=fields, name=name)

            assert isinstance(fields, tuple)
            for field in fields:
                assert isinstance(field, Ast.Node.FieldNode)
            self.__fields = fields

        @property
        def fields(self):
            return self.__fields

        def __repr__(self):
            return "Ast.%s(name=%s, fields=%s)" % (self.__class__.__name__, self.name, self.fields)

    class ConstNode(_NamedNode):
        def __init__(self, name, type_, value):
            Ast._NamedNode.__init__(self, name=name)

            assert type_ is not None
            self.__type = type_

            assert value is not None
            self.__value = value

        @property
        def type(self):
            return self.__type

        def __repr__(self):
            return "Ast.%s(name=%s, type=%s, value=%s)" % (self.__class__.__name__, self.name, self.type, self.value)

        @property
        def value(self):
            return self.__value

    class DocumentNode(Node):
        def __init__(self, headers, definitions):
            Ast.Node.__init__(self, tuple(list(headers) + list(definitions)))

            assert isinstance(headers, tuple)
            self.__headers = headers

            assert isinstance(definitions, tuple)
            self.__definitions = definitions

        @property
        def definitions(self):
            return self.__definitions

        @property
        def headers(self):
            return self.__headers

        def __repr__(self):
            return "Ast.%s(definitions=%s, headers=%s)" % (self.__class__.__name__, self.definitions, self.headers)

    class FieldNode(_NamedNode):
        def __init__(self, name, type_, default_value=None, id_=None):
            Ast._NamedNode.__init__(self, name=name)

            self.__default_value = default_value

            assert id_ is None or (isinstance(id_, int) and id_ >= 0)
            self.__id = id_

            assert type_ is not None
            self.__type = type_

        @property
        def id(self):
            return self.__id

        @property
        def type(self):
            return self.__type

        def __repr__(self):
            return "Ast.%s(id=%s, name=%s, type=%s)" % (self.__class__.__name__, self.id, self.name, self.type)

    class FunctionNode(_NamedNode):
        def __init__(self, name, parameters, return_type_name):
            Ast._NamedNode.__init__(self, children=parameters, name=name)

            assert isinstance(parameters, tuple)
            for parameter in parameters:
                assert isinstance(parameter, Ast.FieldNode)
            self.__parameters = parameters

            assert isinstance(return_type_name, str) and len(return_type_name) > 0
            self.__return_type_name = return_type_name

        @property
        def parameters(self):
            return self.__parameters

        def __repr__(self):
            return "Ast.%s(name=%s, parameters=%s)" % (self.__class__.__name__, self.name, self.parameters)

    class IdentifierNode(str, Node):
        def __init__(self, text):
            Ast.Node.__init__(self)

    class _SequenceTypeNode(object):
        def __init__(self, element_type):
            Ast.Node.__init__(self, (element_type,))

            assert element_type is not None
            self.__element_type = element_type

        @property
        def element_type(self):
            return self.__element_type

        def __repr__(self):
            return "Ast.%s(element_type=%s)" % (self.__class__.__name__, self.element_type)

    class ListTypeNode(_SequenceTypeNode):
        pass

    class MapTypeNode(Node):
        def __init__(self, key_type, value_type):
            Ast.Node.__init__(self, (key_type, value_type))

            assert key_type is not None
            self.__key_type = key_type

        @property
        def key_type(self):
            return self.__key_type

        def __repr__(self):
            return "Ast.%s(key_type=%s, value_type=%s)" % (self.__class__.__name__, self.key_type, self.value_type)

        @property
        def value_type(self):
            return self.__value_type

    class ServiceNode(_NamedNode):
        def __init__(self, functions, name):
            Ast._NamedNode.__init__(self, children=functions, name=name)

            assert isinstance(functions, tuple)
            for function in functions:
                assert isinstance(function, Ast.FunctionNode), type(function)
            self.__functions = functions

        @property
        def functions(self):
            return self.__functions

        def __repr__(self):
            return "Ast.%s(name=%s, functions=%s)" % (self.__class__.__name__, self.name, self.functions)

    class SetTypeNode(_SequenceTypeNode):
        pass
