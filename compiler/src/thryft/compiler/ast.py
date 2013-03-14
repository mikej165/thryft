from yutil import decamelize


class Ast(object):
    class Node(object):
        def __init__(self, doc=None):
            object.__init__(self)
            self.__doc = doc

        def accept(self, visitor):
            return getattr(visitor, 'visit_' + decamelize(self.__class__.__name__))(self)

        @property
        def doc(self):
            return self.__doc

        def __repr__(self):
            properties = {}
            for attr in dir(self):
                if attr[0] == '_' or attr == 'accept':
                    continue
                value = getattr(self, attr)
                if value is None:
                    continue
                properties[attr] = value
            return "Ast.%s(%s)" % (self.__class__.__name__, ', '.join("%s=%s" % (key, properties[key]) for key in properties.iterkeys()))

    class _NamedNode(Node):
        def __init__(self, name, **kwds):
            Ast.Node.__init__(self, **kwds)

            assert isinstance(name, str) and len(name) > 0
            self.__name = name

        @property
        def name(self):
            return self.__name

    class TypeNode(_NamedNode):
        def __init__(self, name, qname=None, **kwds):
            Ast._NamedNode.__init__(self, name=name, **kwds)

            if qname is None:
                qname = name
            else:
                assert isinstance(qname, str) and len(qname) >= len(name)
            self.__qname = qname

        @property
        def qname(self):
            return self.__qname

    class BaseTypeNode(TypeNode):
        pass

    class _CompoundTypeNode(TypeNode):
        def __init__(self, fields, **kwds):
            Ast.TypeNode.__init__(self, **kwds)

            assert isinstance(fields, tuple)
            for field in fields:
                assert isinstance(field, Ast.FieldNode)
            self.__fields = fields

        @property
        def fields(self):
            return self.__fields

    class ConstNode(_NamedNode):
        def __init__(self, type_, value, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert type_ is not None
            self.__type = type_

            assert value is not None
            self.__value = value

        @property
        def type(self):
            return self.__type

        @property
        def value(self):
            return self.__value

    class DocumentNode(Node):
        def __init__(self, headers, definitions, path, **kwds):
            Ast.Node.__init__(self, **kwds)

            assert isinstance(headers, tuple)
            self.__headers = headers

            assert isinstance(definitions, tuple)
            self.__definitions = definitions

            assert isinstance(path, str) and len(path) > 0
            self.__path = path

        @property
        def definitions(self):
            return self.__definitions

        @property
        def headers(self):
            return self.__headers

        @property
        def path(self):
            return self.__path

    class EnumTypeNode(_NamedNode):
        def __init__(self, enumerators, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert isinstance(enumerators, tuple)
            for enumerator in enumerators:
                assert isinstance(enumerator, Ast.EnumeratorNode)
            self.__enumerators = enumerators

        @property
        def enumerators(self):
            return self.__enumerators

    class EnumeratorNode(_NamedNode):
        def __init__(self, value, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            if value is not None:
                assert isinstance(value, int)
            self.__value = value

        @property
        def value(self):
            return self.__value

    class ExceptionTypeNode(_CompoundTypeNode):
        pass

    class FieldNode(_NamedNode):
        def __init__(self, id_, required, type_, value, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert id_ is None or (isinstance(id_, int) and id_ >= 0)
            self.__id = id_

            assert type_ is not None
            self.__type = type_

            assert isinstance(required, bool)
            self.__required = required

            self.__value = value

        @property
        def id(self):
            return self.__id

        @property
        def required(self):
            return self.__required

        @property
        def type(self):
            return self.__type

        @property
        def value(self):
            return self.__value

    class FunctionNode(_NamedNode):
        def __init__(self, oneway, parameters, return_type, throws, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert isinstance(oneway, bool)
            self.__oneway = oneway

            assert isinstance(parameters, tuple)
            for parameter in parameters:
                assert isinstance(parameter, Ast.FieldNode)
            self.__parameters = parameters

            assert isinstance(return_type, Ast.TypeNode)
            self.__return_type = return_type

            assert isinstance(throws, tuple)
            for throw in throws:
                assert isinstance(throw, Ast.FieldNode)
            self.__throws = throws

        @property
        def oneway(self):
            return self.__oneway

        @property
        def parameters(self):
            return self.__parameters

        @property
        def return_type(self):
            return self.__return_type

        @property
        def throws(self):
            return self.__throws

    class IdentifierNode(str, Node):
        def __init__(self, text):
            Ast.Node.__init__(self)

    class IncludeNode(Node):
        def __init__(self, path, **kwds):
            Ast.Node.__init__(self, **kwds)

            assert isinstance(path, str) and len(path) > 0
            self.__path = path

        @property
        def path(self):
            return self.__path

    class _SequenceTypeNode(TypeNode):
        def __init__(self, element_type, **kwds):
            Ast.TypeNode.__init__(self, **kwds)

            assert element_type is not None
            self.__element_type = element_type

        @property
        def element_type(self):
            return self.__element_type

    class ListTypeNode(_SequenceTypeNode):
        def __init__(self, element_type, **kwds):
            Ast._SequenceTypeNode.__init__(self, element_type=element_type, name="list<%s>" % element_type.qname)

    class MapTypeNode(TypeNode):
        def __init__(self, key_type, value_type, **kwds):
            Ast.TypeNode.__init__(self, name="map<%s, %s>" % (key_type.qname, value_type.qname), **kwds)

            assert key_type is not None
            self.__key_type = key_type

            assert value_type is not None
            self.__value_type = value_type

        @property
        def key_type(self):
            return self.__key_type

        @property
        def value_type(self):
            return self.__value_type

    class NamespaceNode(_NamedNode):
        def __init__(self, scope, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert isinstance(scope, str) and len(scope) > 0
            self.__scope = scope

        @property
        def scope(self):
            return self.__scope

    class ServiceNode(_NamedNode):
        def __init__(self, functions, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert isinstance(functions, tuple)
            for function in functions:
                assert isinstance(function, Ast.FunctionNode), type(function)
            self.__functions = functions

        @property
        def functions(self):
            return self.__functions

    class SetTypeNode(_SequenceTypeNode):
        def __init__(self, element_type, **kwds):
            Ast._SequenceTypeNode.__init__(self, element_type=element_type, name="set<%s>" % element_type.qname)

    class StructTypeNode(_CompoundTypeNode):
        pass

    class TypedefNode(_NamedNode):
        def __init__(self, type_, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert type_ is not None
            self.__type = type_

        @property
        def type(self):
            return self.__type
