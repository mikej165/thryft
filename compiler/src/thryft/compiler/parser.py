from spark import GenericParser
from thryft.compiler.ast import Ast
from thryft.compiler.parser_exception import ParserException


# Helper functions
class Parser(GenericParser):
    def __init__(self):
        GenericParser.__init__(self, start='document')

    def error(self, token):
        raise ParserException(token)

    @staticmethod
    def __flatten_args(args):
        flattened_args = []
        for arg in args:
            if isinstance(arg, tuple):
                flattened_args.extend(arg)
            else:
                flattened_args.append(arg)
        return tuple(flattened_args)

    def p_bool_literal(self, args):
        '''
        bool_literal ::= KEYWORD_FALSE
        bool_literal ::= KEYWORD_TRUE
        '''
        return args[0].text.lower() == 'true'

    def p_const(self, args):
        '''
        const ::= KEYWORD_CONST type identifier EQUALS literal semicolon_optional
        '''
        return Ast.ConstNode(name=args[2], type_=args[1], value=args[4])

    def p_document(self, args):
        '''
        document ::= headers definitions EOF
        '''
        return Ast.DocumentNode(definitions=args[1], headers=args[0])

    def p_definition(self, args):
        '''
        definition ::= const
        definition ::= service
        '''
        return args[0]

    def p_definitions(self, args):
        '''
        definitions ::= definition definitions
        definitions ::= definition
        '''
        return self.__flatten_args(args)

    def p_field(self, args):
        '''
        field ::= type identifier
        '''
        return Ast.FieldNode(name=args[1], type_=args[0])

    def p_float_literal(self, args):
        '''
        float_literal ::= DIGITS PERIOD DIGITS
        '''
        return float(''.join(arg.text for arg in args))

    def p_function(self, args):
        '''
        function ::= identifier identifier LEFT_PARENTHESIS function_parameters RIGHT_PARENTHESIS list_separator_optional
        '''
        return Ast.FunctionNode(name=args[1], parameters=args[3], return_type_name=args[0])

    def p_function_parameters(self, args):
        '''
        function_parameters ::= field
        function_parameters ::= field COMMA function_parameters
        function_parameters ::=
        '''
        function_parameters = []
        for arg in args:
            if isinstance(arg, tuple):
                function_parameters.extend(arg)
            elif isinstance(arg, Ast.FieldNode):
                function_parameters.append(arg)
        return tuple(function_parameters)

    def p_functions(self, args):
        '''
        functions ::= function functions
        functions ::=
        '''
        return self.__flatten_args(args)

    def p_header(self, args):
        '''
        header ::= include
        header ::= namespace
        '''
        raise NotImplementedError

    def p_headers(self, args):
        '''
        headers ::= headers header
        headers ::= header
        headers ::=
        '''
        return self.__flatten_args(args)

    def p_identifier(self, args):
        '''
        identifier ::= ALPHAS identifier_body
        '''
        return Ast.IdentifierNode(''.join(str(arg) for arg in args))

    def p_identifier_body(self, args):
        '''
        identifier_body ::= ALPHAS identifier_body
        identifier_body ::= DIGITS identifier_body
        identifier_body ::= UNDERSCORE identifier_body
        identifier_body ::=
        '''
        return ''.join(str(arg) for arg in args)

    def p_int_literal(self, args):
        '''
        int_literal ::= DIGITS
        '''
        return int(args[0].text)

    def p_list_literal(self, args):
        '''
        list_literal ::= LEFT_SQUARE_BRACKET list_literal_body RIGHT_SQUARE_BRACKET
        '''
        return args[1]

    def p_list_literal_body(self, args):
        '''
        list_literal_body ::= literal
        list_literal_body ::= literal COMMA list_literal_body
        '''
        return tuple(args[i] for i in len(xrange(0, len(args), 2)))

    def p_list_separator(self, args):
        '''
        list_separator ::= COMMA
        list_separator ::= SEMICOLON
        '''
        pass

    def p_list_type(self, args):
        '''
        list_type ::= LIST_KEYWORD LEFT_ANGLE_BRACKET type RIGHT_ANGLE_BRACKET
        '''
        return Ast.ListTypeNode(element_type=args[2])

    def p_list_separator_optional(self, args):
        '''
        list_separator_optional ::= list_separator
        list_separator_optional ::=
        '''
        pass

    def p_literal(self, args):
        '''
        literal ::= bool_literal
        literal ::= float_literal
        literal ::= int_literal
        literal ::= list_literal
        literal ::= map_literal
        '''
        return args[0]

    def p_map_literal(self, args):
        '''
        map_literal ::= LEFT_BRACE map_literal_body RIGHT_BRACE
        '''
        return args[1]

    def p_map_literal_body(self, args):
        '''
        map_literal_body ::= literal COLON literal
        map_literal_body ::= map_literal_body COMMA map_literal_body
        '''
        raise NotImplementedError

    def p_map_type(self, args):
        '''
        map_type ::= MAP_TYPE LEFT_ANGLE_BRACKET type COMMA type RIGHT_ANGLE_BRACKET
        '''
        return Ast.MapTypeNode(key_type=args[2], value_type=args[4])

    def p_semicolon_optional(self, args):
        '''
        semicolon_optional ::= SEMICOLON
        semicolon_optional ::=
        '''
        pass

    def p_service(self, args):
        '''
        service ::= KEYWORD_SERVICE identifier LEFT_BRACE functions RIGHT_BRACE
        '''
        return Ast.ServiceNode(name=args[1], functions=args[3])

    def p_set_type(self, args):
        '''
        set_type ::= SET_KEYWORD LEFT_ANGLE_BRACKET type RIGHT_ANGLE_BRACKET
        '''
        return Ast.SetTypeNode(element_type=args[2])

    def p_type(self, args):
        '''
        type ::= list_type
        type ::= map_type
        type ::= set_type
        type ::= identifier
        '''
        return args[0]

    def typestring(self, token):
        return token.type
