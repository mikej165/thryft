from spark import GenericParser
from thryft.compiler.parser_exception import ParserException


class Parser(GenericParser):
    def __init__(self):
        GenericParser.__init__(self, start='document')

    def error(self, token):
        raise ParserException(token)

    def p_document(self, args):
        '''
        document ::= headers definitions EOF
        '''
        pass

    def p_definition(self, args):
        '''
        definition ::= service
        '''
        pass

    def p_definitions(self, args):
        '''
        definitions ::= definitions definition
        definitions ::= definition
        '''
        pass

    def p_function(self, args):
        '''
        function ::= identifier identifier LEFT_PARENTHESIS RIGHT_PARENTHESIS list_separator
        '''
        pass

    def p_functions(self, args):
        '''
        functions ::= function functions
        functions ::=
        '''
        pass

    def p_header(self, args):
        '''
        header ::= include
        header ::= namespace
        '''
        pass

    def p_headers(self, args):
        '''
        headers ::= headers header
        headers ::= header
        headers ::=
        '''
        pass

    def p_identifier(self, args):
        '''
        identifier ::= ALPHAS identifier_body
        '''
        pass

    def p_identifier_body(self, args):
        '''
        identifier_body ::= ALPHAS identifier_body
        identifier_body ::= DIGITS identifier_body
        identifier_body ::=
        '''
        pass

    def p_list_separator(self, args):
        '''
        list_separator ::= COMMA
        list_separator ::= SEMICOLON
        '''
        pass

    def p_service(self, args):
        '''
        service ::= KEYWORD_SERVICE identifier LEFT_BRACE functions RIGHT_BRACE
        '''
        pass

    def typestring(self, token):
        return token.type
