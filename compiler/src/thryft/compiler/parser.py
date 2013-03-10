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

    def p_document(self, args):
        '''
        document ::= headers definitions EOF
        '''
        return Ast.DocumentNode(definitions=args[1], headers=args[0])

    def p_definition(self, args):
        '''
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
        identifier_body ::=
        '''
        return ''.join(str(arg) for arg in args)

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

    def p_map_type(self, args):
        '''
        map_type ::= MAP_TYPE LEFT_ANGLE_BRACKET type COMMA type RIGHT_ANGLE_BRACKET
        '''
        return Ast.MapTypeNode(key_type=args[2], value_type=args[4])

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
