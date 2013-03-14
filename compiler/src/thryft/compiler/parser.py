from spark import GenericParser
from thryft.compiler.ast import Ast
from thryft.compiler.parse_exception import ParseException
from thryft.compiler.token import Token
from yutil import class_qname
import logging


# Helper functions
class Parser(GenericParser):
    def __init__(self):
        GenericParser.__init__(self, start='document')
        self.__logger = logging.getLogger(class_qname(self))

    def __dispatch(self, p_method, args):
        ret = p_method(args)
        self.__logger.debug("%s(%s) -> %s", p_method.im_func.func_name, repr(args), repr(ret))
        return ret

    def error(self, token):
        raise ParseException(token)

    @staticmethod
    def __flatten_args(args):
        flattened_args = []
        for arg in args:
            if isinstance(arg, (list, tuple)):
                flattened_args.extend(arg)
            else:
                flattened_args.append(arg)
        return tuple(flattened_args)

    @staticmethod
    def __join_arg_texts(args):
        return ''.join(str(arg) for arg in args)

    @staticmethod
    def __p(args, doc=True, start_token=True, stop_token=True):
        if doc:
            comments = args[0]
            merged_comment = []
            for comment in comments:
                assert isinstance(comment, Token) and comment.type == Token.Type.COMMENT
                merged_comment.append(comment.text)
            doc = ''.join(merged_comment)
        else:
            doc = None

        if start_token:
            start_token = None
            if doc is not None:
                comments = args[0]
                if len(comments) > 0:
                    start_token = comments[0]
            if start_token is None:
                for arg in args:
                    if isinstance(arg, Token):
                        start_token = arg
                        break
        else:
            stop_token = None

        if stop_token:
            stop_token = None
            for arg in reversed(args):
                if isinstance(arg, Token):
                    stop_token = arg
                    break
            if stop_token is None:
                stop_token = start_token
        else:
            stop_token = None

        return doc, start_token, stop_token

    def p_base_type(self, args):
        '''
        base_type ::= KEYWORD_BINARY
        base_type ::= KEYWORD_BOOL
        base_type ::= KEYWORD_BYTE
        base_type ::= KEYWORD_DOUBLE
        base_type ::= KEYWORD_FLOAT
        base_type ::= KEYWORD_I16
        base_type ::= KEYWORD_I32
        base_type ::= KEYWORD_I64
        base_type ::= KEYWORD_STRING
        '''
        return self.__dispatch(self.__p_base_type, args)

    def __p_base_type(self, args):
        return Ast.BaseTypeNode(name=args[0].text, start_token=args[0], stop_token=args[0])

    def p_bool_literal(self, args):
        '''
        bool_literal ::= KEYWORD_FALSE
        bool_literal ::= KEYWORD_TRUE
        '''
        return self.__dispatch(self.__p_bool_literal, args)

    def __p_bool_literal(self, args):
        return Ast.BoolLiteralNode(start_token=args[0], stop_token=args[0], value=args[0].text.lower() == 'true')

    def p_comments(self, args):
        '''
        comments ::= COMMENT comments
        comments ::=
        '''
        return self.__dispatch(self.__p_comments, args)

    def __p_comments(self, args):
        return self.__flatten_args(args)

    def p_compound_type_field(self, args):
        '''
        compound_type_field ::= comments field list_separator_optional
        '''
        return self.__dispatch(self.__p_compound_type_field, args)

    def __p_compound_type_field(self, args):
        doc, start_token, stop_token = self.__p(args)
        field = args[1]
        return \
            Ast.FieldNode(
                doc=doc,
                id_=field.id,
                name=field.name,
                required=field.required,
                start_token=start_token,
                stop_token=stop_token,
                type_=field.type,
                value=field.value
            )

    def p_compound_type_fields(self, args):
        '''
        compound_type_fields ::= compound_type_field compound_type_fields
        compound_type_fields ::=
        '''
        return self.__dispatch(self.__p_compound_type_fields, args)

    def __p_compound_type_fields(self, args):
        return self.__flatten_args(args)

    def p_const(self, args):
        '''
        const ::= comments KEYWORD_CONST type identifier EQUALS literal semicolon_optional
        '''
        return self.__dispatch(self.__p_const, args)

    def __p_const(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.ConstNode(
                doc=doc,
                name=args[3].text,
                start_token=start_token,
                stop_token=stop_token,
                type_=args[2],
                value=args[5]
            )

    def p_document(self, args):
        '''
        document ::= headers definitions EOF
        document ::= comments EOF
        '''
        return self.__dispatch(self.__p_document, args)

    def __p_document(self, args):
        if len(args) == 2:
            return \
                Ast.DocumentNode(
                    definitions=tuple(),
                    headers=tuple(),
                    path=args[1].input_filename
                )
        else:
            return \
                Ast.DocumentNode(
                    definitions=args[1],
                    doc=None,
                    headers=args[0],
                    path=args[2].input_filename
                )

    def p_definition(self, args):
        '''
        definition ::= const
        definition ::= enum
        definition ::= exception_type
        definition ::= service
        definition ::= struct_type
        definition ::= typedef
        '''
        return self.__dispatch(self.__p_definition, args)

    def __p_definition(self, args):
        return args[0]

    def p_definitions(self, args):
        '''
        definitions ::= definition definitions
        definitions ::= definition
        definitions ::=
        '''
        return self.__dispatch(self.__p_definitions, args)

    def __p_definitions(self, args):
        return self.__flatten_args(args)

    def p_enum(self, args):
        '''
        enum ::= comments KEYWORD_ENUM identifier LEFT_BRACE enumerators RIGHT_BRACE
        '''
        return self.__dispatch(self.__p_enum, args)

    def __p_enum(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.EnumTypeNode(
                doc=doc,
                enumerators=args[4],
                name=args[2].text,
                start_token=start_token,
                stop_token=stop_token
            )

    def p_enumerator(self, args):
        '''
        enumerator ::= comments identifier enumerator_value list_separator_optional
        '''
        return self.__dispatch(self.__p_enumerator, args)

    def __p_enumerator(self, args):
        doc, start_token, stop_token = self.__p(args)
        if args[2] is not None:
            value = args[2].value
        else:
            value = None
        return Ast.EnumeratorNode(doc=doc, name=args[1].text, start_token=start_token, stop_token=stop_token, value=value)

    def p_enumerators(self, args):
        '''
        enumerators ::= enumerator enumerators
        enumerators ::=
        '''
        return self.__dispatch(self.__p_enumerators, args)

    def __p_enumerators(self, args):
        return self.__flatten_args(args)

    def p_enumerator_value(self, args):
        '''
        enumerator_value ::= EQUALS literal
        enumerator_value ::=
        '''
        return self.__dispatch(self.__p_enumerator_value, args)

    def __p_enumerator_value(self, args):
        if len(args) > 0:
            return args[1]

    def p_exception_type(self, args):
        '''
        exception_type ::= comments KEYWORD_EXCEPTION identifier LEFT_BRACE compound_type_fields RIGHT_BRACE
        '''
        return self.__dispatch(self.__p_exception_type, args)

    def __p_exception_type(self, args):
        doc, start_token, stop_token = self.__p(args)
        return Ast.ExceptionTypeNode(doc=doc, name=args[2].text, fields=args[4], start_token=start_token, stop_token=stop_token)

    def p_field(self, args):
        '''
        field ::= field_id field_required type identifier field_value
        '''
        return self.__dispatch(self.__p_field, args)

    def __p_field(self, args):
        _, start_token, stop_token = self.__p(args, doc=False)
        id_ = value = None
        if args[0] is not None:
            id_ = args[0].value
        if args[-1] is not None:
            value = args[-1].value
        return Ast.FieldNode(id_=id_, name=args[3].text, required=args[1], start_token=start_token, stop_token=stop_token, type_=args[2], value=value)

    def p_field_id(self, args):
        '''
        field_id ::=
        field_id ::= int_literal COLON
        '''
        return self.__dispatch(self.__p_field_id, args)

    def __p_field_id(self, args):
        if len(args) > 0:
            return args[0]

    def p_field_required(self, args):
        '''
        field_required ::=
        field_required ::= KEYWORD_REQUIRED
        field_required ::= KEYWORD_OPTIONAL
        '''
        return self.__dispatch(self.__p_field_required, args)

    def __p_field_required(self, args):
        if len(args) == 1:
            return args[0].text == 'required'
        else:
            return True

    def p_field_value(self, args):
        '''
        field_value ::=
        field_value ::= EQUALS literal
        '''
        return self.__dispatch(self.__p_field_value, args)

    def __p_field_value(self, args):
        if len(args) > 0:
            return args[1]

    def p_float_literal(self, args):
        '''
        float_literal ::= FLOAT_LITERAL
        '''
        return self.__dispatch(self.__p_float_literal, args)

    def __p_float_literal(self, args):
        return Ast.FloatLiteralNode(start_token=args[0], stop_token=args[0], value=float(args[0].text))

    def p_function(self, args):
        '''
        function ::= comments function_oneway function_return_type identifier LEFT_PARENTHESIS function_parameters RIGHT_PARENTHESIS function_throws list_separator_optional
        '''
        return self.__dispatch(self.__p_function, args)

    def __p_function(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.FunctionNode(
                doc=doc,
                name=args[3].text,
                oneway=args[1],
                parameters=args[5],
                return_type=args[2],
                start_token=start_token,
                stop_token=stop_token,
                throws=args[7]
            )

    def p_function_oneway(self, args):
        '''
        function_oneway ::= KEYWORD_ONEWAY
        function_oneway ::=
        '''
        return self.__dispatch(self.__p_function_oneway, args)

    def __p_function_oneway(self, args):
        return len(args) > 0

    def p_function_parameters(self, args):
        '''
        function_parameters ::= field
        function_parameters ::= field COMMA function_parameters
        function_parameters ::=
        '''
        return self.__dispatch(self.__p_function_parameters, args)

    def __p_function_parameters(self, args):
        function_parameters = []
        for arg in args:
            if isinstance(arg, tuple):
                function_parameters.extend(arg)
            elif isinstance(arg, Ast.FieldNode):
                function_parameters.append(arg)
        return tuple(function_parameters)

    def p_function_return_type(self, args):
        '''
        function_return_type ::= KEYWORD_VOID
        function_return_type ::= type
        '''
        return self.__dispatch(self.__p_function_return_type, args)

    def __p_function_return_type(self, args):
        if isinstance(args[0], Token):
            return Ast.TypeNode(name='void')
        else:
            return args[0]

    def p_function_throws(self, args):
        '''
        function_throws ::=
        function_throws ::= KEYWORD_THROWS LEFT_PARENTHESIS function_throws_body RIGHT_PARENTHESIS
        '''
        return self.__dispatch(self.__p_function_throws, args)

    def __p_function_throws(self, args):
        if len(args) > 0:
            return args[2]
        else:
            return tuple()

    def p_function_throws_body(self, args):
        '''
        function_throws_body ::= field
        function_throws_body ::= field COMMA function_throws_body
        '''
        return self.__dispatch(self.__p_function_throws_body, args)

    def __p_function_throws_body(self, args):
        return self.__flatten_args(args[i] for i in xrange(0, len(args), 2))

    def p_functions(self, args):
        '''
        functions ::= function functions
        functions ::=
        '''
        return self.__dispatch(self.__p_functions, args)

    def __p_functions(self, args):
        return self.__flatten_args(args)

    def p_header(self, args):
        '''
        header ::= include
        header ::= namespace
        '''
        return self.__dispatch(self.__p_header, args)

    def __p_header(self, args):
        return args[0]

    def p_headers(self, args):
        '''
        headers ::= headers header
        headers ::= header
        headers ::=
        '''
        return self.__dispatch(self.__p_headers, args)

    def __p_headers(self, args):
        return self.__flatten_args(args)

    def p_identifier(self, args):
        '''
        identifier ::= IDENTIFIER
        identifier ::= KEYWORD_LIST
        '''
        return self.__dispatch(self.__p_identifier, args)

    def __p_identifier(self, args):
        return Ast.IdentifierNode(start_token=args[0], stop_token=args[-1], text=args[0].text)

    def p_include(self, args):
        '''
        include ::= comments KEYWORD_INCLUDE QUOTED_STRING
        '''
        return self.__dispatch(self.__p_include, args)

    def __p_include(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.IncludeNode(
                doc=doc,
                path=args[2].text[1:-1],
                start_token=start_token,
                stop_token=stop_token
            )

    def p_int_literal(self, args):
        '''
        int_literal ::= INT_LITERAL
        '''
        return self.__dispatch(self.__p_int_literal, args)

    def __p_int_literal(self, args):
        return Ast.IntLiteralNode(start_token=args[0], stop_token=args[0], value=int(args[0].text))

    def p_list_literal(self, args):
        '''
        list_literal ::= LEFT_SQUARE_BRACKET list_literal_body RIGHT_SQUARE_BRACKET
        '''
        return self.__dispatch(self.__p_list_literal, args)

    def __p_list_literal(self, args):
        return Ast.ListLiteralNode(start_token=args[0], stop_token=args[-1], value=args[1])

    def p_list_literal_body(self, args):
        '''
        list_literal_body ::= literal
        list_literal_body ::= literal COMMA list_literal_body
        '''
        return self.__dispatch(self.__p_list_literal_body, args)

    def __p_list_literal_body(self, args):
        if len(args) == 1:
            return args[0]
        else:
            return self.__flatten_args(args[i] for i in xrange(0, len(args), 2))

    def p_list_separator(self, args):
        '''
        list_separator ::= COMMA
        list_separator ::= SEMICOLON
        '''
        return self.__dispatch(self.__p_list_separator, args)

    def __p_list_separator(self, args):
        pass

    def p_list_type(self, args):
        '''
        list_type ::= KEYWORD_LIST LEFT_ANGLE_BRACKET type RIGHT_ANGLE_BRACKET
        '''
        return self.__dispatch(self.__p_list_type, args)

    def __p_list_type(self, args):
        return Ast.ListTypeNode(element_type=args[2], start_token=args[0], stop_token=args[-1])

    def p_list_separator_optional(self, args):
        '''
        list_separator_optional ::= list_separator
        list_separator_optional ::=
        '''
        return self.__dispatch(self.__p_list_separator_optional, args)

    def __p_list_separator_optional(self, args):
        pass

    def p_literal(self, args):
        '''
        literal ::= bool_literal
        literal ::= float_literal
        literal ::= int_literal
        literal ::= list_literal
        literal ::= map_literal
        literal ::= string_literal
        '''
        return self.__dispatch(self.__p_literal, args)

    def __p_literal(self, args):
        return args[0]

    def p_map_literal(self, args):
        '''
        map_literal ::= LEFT_BRACE map_literal_items RIGHT_BRACE
        '''
        return self.__dispatch(self.__p_map_literal, args)

    def __p_map_literal(self, args):
        return Ast.MapLiteralNode(start_token=args[0], stop_token=args[-1], value=args[1])

    def p_map_literal_item(self, args):
        '''
        map_literal_item ::= literal COLON literal
        '''
        return self.__dispatch(self.__p_map_literal_item, args)

    def __p_map_literal_item(self, args):
        return (args[0], args[2])

    def p_map_literal_items(self, args):
        '''
        map_literal_items ::= map_literal_item
        map_literal_items ::= map_literal_item COMMA map_literal_items
        '''
        return self.__dispatch(self.__p_map_literal_items, args)

    def __p_map_literal_items(self, args):
        if len(args) == 1:
            return args[0]
        else:
            return dict(args[i] for i in xrange(0, len(args), 2))

    def p_map_type(self, args):
        '''
        map_type ::= KEYWORD_MAP LEFT_ANGLE_BRACKET type COMMA type RIGHT_ANGLE_BRACKET
        '''
        return self.__dispatch(self.__p_map_type, args)

    def __p_map_type(self, args):
        return Ast.MapTypeNode(key_type=args[2], start_token=args[0], stop_token=args[-1], value_type=args[4])

    def p_namespace(self, args):
        '''
        namespace ::= comments KEYWORD_NAMESPACE namespace_scope namespace_name
        '''
        return self.__dispatch(self.__p_namespace, args)

    def __p_namespace(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.NamespaceNode(
                doc=doc,
                name=args[3],
                scope=args[2],
                start_token=start_token,
                stop_token=stop_token
            )

    def p_namespace_name(self, args):
        '''
        namespace_name ::= identifier PERIOD namespace_name
        namespace_name ::= identifier
        '''
        return self.__dispatch(self.__p_namespace_name, args)

    def __p_namespace_name(self, args):
        return self.__join_arg_texts(self.__flatten_args(args))

    def p_namespace_scope(self, args):
        '''
        namespace_scope ::= ASTERISK
        namespace_scope ::= identifier
        '''
        return self.__dispatch(self.__p_namespace_scope, args)

    def __p_namespace_scope(self, args):
        return str(args[0])

    def p_semicolon_optional(self, args):
        '''
        semicolon_optional ::= SEMICOLON
        semicolon_optional ::=
        '''
        return self.__dispatch(self.__p_semicolon_optional, args)

    def __p_semicolon_optional(self, args):
        if len(args) > 0:
            return args[0]

    def p_service(self, args):
        '''
        service ::= comments KEYWORD_SERVICE identifier LEFT_BRACE functions RIGHT_BRACE
        '''
        return self.__dispatch(self.__p_service, args)

    def __p_service(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.ServiceNode(
                doc=doc,
                name=args[2].text,
                functions=args[4],
                start_token=start_token,
                stop_token=stop_token
            )

    def p_set_type(self, args):
        '''
        set_type ::= KEYWORD_SET LEFT_ANGLE_BRACKET type RIGHT_ANGLE_BRACKET
        '''
        return self.__dispatch(self.__p_set_type, args)

    def __p_set_type(self, args):
        return Ast.SetTypeNode(element_type=args[2], start_token=args[0], stop_token=args[-1])

    def p_string_literal(self, args):
        '''
        string_literal ::= QUOTED_STRING
        '''
        return self.__dispatch(self.__p_string_literal, args)

    def __p_string_literal(self, args):
        return Ast.StringLiteralNode(start_token=args[0], stop_token=args[0], value=args[0].text[1:-1])

    def p_struct_type(self, args):
        '''
        struct_type ::= comments KEYWORD_STRUCT identifier LEFT_BRACE compound_type_fields RIGHT_BRACE
        '''
        return self.__dispatch(self.__p_struct_type, args)

    def __p_struct_type(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.StructTypeNode(
                doc=doc,
                name=args[2].text,
                fields=args[4],
                start_token=start_token,
                stop_token=stop_token
            )

    def p_type(self, args):
        '''
        type ::= base_type
        type ::= list_type
        type ::= map_type
        type ::= set_type
        type ::= type_qname
        '''
        return self.__dispatch(self.__p_type, args)

    def __p_type(self, args):
        return args[0]

    def p_type_qname(self, args):
        '''
        type_qname ::= identifier PERIOD identifier
        type_qname ::= identifier
        '''
        return self.__dispatch(self.__p_type_qname, args)

    def __p_type_qname(self, args):
        if len(args) == 1:
            return Ast.TypeNode(name=args[0].text, start_token=args[0].start_token, stop_token=args[0].start_token)
        else:
            return Ast.TypeNode(name=args[2].text, qname=self.__join_arg_texts(args), start_token=args[0].start_token, stop_token=args[-1].stop_token)

    def p_typedef(self, args):
        '''
        typedef ::= comments KEYWORD_TYPEDEF type identifier
        '''
        return self.__dispatch(self.__p_typedef, args)

    def __p_typedef(self, args):
        doc, start_token, stop_token = self.__p(args)
        return \
            Ast.TypedefNode(
                doc=doc,
                name=args[3].text,
                start_token=start_token,
                stop_token=stop_token,
                type_=args[2]
            )

    def typestring(self, token):
        return token.type
