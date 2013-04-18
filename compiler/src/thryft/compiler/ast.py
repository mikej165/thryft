from thryft.compiler.token import Token
from yutil import decamelize


class Ast(object):
    class Node(object):
        def __init__(self, annotations=None, doc=None, start_token=None, stop_token=None):
            object.__init__(self)

            if doc is not None:
                assert isinstance(doc, Ast.DocNode)
            self.__doc = doc

            if annotations is not None:
                assert isinstance(annotations, tuple), type(annotations)
                for annotation in annotations:
                    assert isinstance(annotation, Ast.AnnotationNode)
            self.__annotations = annotations

            if start_token is not None:
                assert isinstance(start_token, Token), repr(start_token)
                assert stop_token is not None
            else:
                assert stop_token is None
            self.__start_token = start_token

            if stop_token is not None:
                assert isinstance(stop_token, Token), repr(stop_token)
                assert stop_token.index >= start_token.index
            self.__stop_token = stop_token

        def accept(self, visitor):
            return getattr(visitor, 'visit_' + decamelize(self.__class__.__name__))(self)

        @property
        def annotations(self):
            return self.__annotations

        @property
        def doc(self):
            return self.__doc

        @doc.setter
        def doc(self, doc):
            assert doc is None or isinstance(doc, Ast.DocNode)
            self.__doc = doc

        def __properties(self):
            properties = {}
            for attr in dir(self):
                if attr[0] == '_' or attr in ('accept', 'to_dict'):
                    continue
                value = getattr(self, attr)
                if value is None:
                    continue
                elif attr == 'stop_token' and value == self.start_token:
                    continue
                properties[attr] = value
            return properties

        def __repr__(self):
            properties = self.__properties()
            return "Ast.%s(%s)" % (self.__class__.__name__, ', '.join("%s=%s" % (key, repr(properties[key])) for key in sorted(properties.iterkeys())))

        @property
        def start_token(self):
            return self.__start_token

        @property
        def stop_token(self):
            return self.__stop_token

        def to_dict(self):
            dict_ = {}
            properties = self.__properties()
            for key in sorted(properties.iterkeys()):
                dict_[key] = self.__to_dict_value(properties[key])
            return dict_

        @staticmethod
        def __to_dict_value(value):
            if isinstance(value, tuple):
                return tuple(Ast.Node.__to_dict_value(value) for value in value)
            elif hasattr(value, 'to_dict'):
                return value.to_dict()
            else:
                return value

    class _LiteralNode(Node):
        def __init__(self, value, **kwds):
            Ast.Node.__init__(self, **kwds)
            assert value is not None
            self.__value = value

        @property
        def value(self):
            return self.__value

    class _NamedNode(Node):
        def __init__(self, name, **kwds):
            Ast.Node.__init__(self, **kwds)

            assert isinstance(name, str) and len(name) > 0, name
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

    class AnnotationNode(_NamedNode):
        def __init__(self, value=None, **kwds):
            Ast._NamedNode.__init__(self, **kwds)
            self.__value = value

        @property
        def value(self):
            return self.__value

    class BaseTypeNode(TypeNode):
        pass

    class BoolLiteralNode(_LiteralNode):
        def __init__(self, **kwds):
            Ast._LiteralNode.__init__(self, **kwds)
            assert isinstance(self.value, bool)

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

            assert isinstance(type_, Ast.TypeNode)
            self.__type = type_

            assert isinstance(value, Ast._LiteralNode)
            self.__value = value

        @property
        def type(self):
            return self.__type

        @property
        def value(self):
            return self.__value

    class DocNode(Node):
        def __init__(self, tags, text, **kwds):
            Ast.Node.__init__(self, **kwds)

            assert isinstance(tags, dict)
            self.__tags = tags

            assert isinstance(text, str)
            self.__text = text

        @property
        def tags(self):
            return self.__tags

        @property
        def text(self):
            return self.__text

        def __str__(self):
            return self.text

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
                assert isinstance(value, Ast.IntLiteralNode)
            self.__value = value

        @property
        def value(self):
            return self.__value

    class ExceptionTypeNode(_CompoundTypeNode):
        pass

    class FieldNode(_NamedNode):
        def __init__(self, id_, required, type_, value, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert id_ is None or (isinstance(id_, int) and id_ >= 0), id_
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

    class FloatLiteralNode(_LiteralNode):
        def __init__(self, **kwds):
            Ast._LiteralNode.__init__(self, **kwds)
            assert isinstance(self.value, float)

    class FunctionNode(_NamedNode):
        def __init__(self, oneway, parameters, return_field, throws, **kwds):
            Ast._NamedNode.__init__(self, **kwds)

            assert isinstance(oneway, bool)
            self.__oneway = oneway

            assert isinstance(parameters, tuple)
            for parameter in parameters:
                assert isinstance(parameter, Ast.FieldNode)
            self.__parameters = parameters

            if return_field is not None:
                assert isinstance(return_field, Ast.FieldNode), type(return_field)
            self.__return_field = return_field

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
        def return_field(self):
            return self.__return_field

        @property
        def throws(self):
            return self.__throws

    class IdentifierNode(Node):
        def __init__(self, text, **kwds):
            Ast.Node.__init__(self, **kwds)
            assert isinstance(text, str) and len(text) > 0
            self.__text = text

        def __str__(self):
            return self.text

        @property
        def text(self):
            return self.__text

    class IncludeNode(Node):
        def __init__(self, path, **kwds):
            Ast.Node.__init__(self, **kwds)

            assert isinstance(path, str) and len(path) > 0
            self.__path = path

        @property
        def path(self):
            return self.__path

    class IntLiteralNode(_LiteralNode):
        def __init__(self, **kwds):
            Ast._LiteralNode.__init__(self, **kwds)
            assert isinstance(self.value, int)

    class _SequenceTypeNode(TypeNode):
        def __init__(self, element_type, **kwds):
            Ast.TypeNode.__init__(self, **kwds)

            assert element_type is not None
            self.__element_type = element_type

        @property
        def element_type(self):
            return self.__element_type

    class ListLiteralNode(_LiteralNode):
        def __init__(self, **kwds):
            Ast._LiteralNode.__init__(self, **kwds)
            assert isinstance(self.value, tuple)

    class ListTypeNode(_SequenceTypeNode):
        def __init__(self, element_type, **kwds):
            Ast._SequenceTypeNode.__init__(self, element_type=element_type, name="list<%s>" % element_type.qname)

    class MapLiteralNode(_LiteralNode):
        def __init__(self, **kwds):
            Ast._LiteralNode.__init__(self, **kwds)
            assert isinstance(self.value, dict)

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

    class StringLiteralNode(_LiteralNode):
        def __init__(self, **kwds):
            Ast._LiteralNode.__init__(self, **kwds)
            assert isinstance(self.value, str)

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
