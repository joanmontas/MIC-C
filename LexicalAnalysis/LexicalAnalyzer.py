# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from ply import lex

class MyLexicalAnalyzer:
    def __init__(self):
        self.reserved = {
            'if': 'IF',
            'else': 'ELSE',
            'while': 'WHILE',
        }
        self.test = None

        self.tokens = (
            'IDENT',
            'TYPE',
            'NUMBER',
            'STRING',
            'LESSER',
            'EQUAL',
            'ASSIGN',
            'PLUS',
            'MINUS',
            'TIMES',
            'DIVIDE',
            'LPAREN',
            'RPAREN',
            'LCURL',
            'RCURL',
            'SEMICOLON',
        ) + tuple(self.reserved.values())

        self.types = ('number', 'string')
        self.lexer = lex.lex(module=self)

    def t_IDENT(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value in self.types:
            t.type = "TYPE"
        elif t.value in self.reserved.keys():
            t.type = self.reserved[t.value]
        else:
            t.type = "IDENT"
        # t.type = 'IDENT' if t.value not in self.types else 'TYPE'
        self.test = t
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r"'([^\\']+|\\')*'"
        t.value = t.value[1:-1]  # Remove single quotes
        return t

    def t_PLUS(self, t):
        r'\+'
        return t

    def t_MINUS(self, t):
        r'-'
        return t

    def t_TIMES(self, t):
        r'\*'
        return t

    def t_DIVIDE(self, t):
        r'/'
        return t

    def t_LESSER(self, t):
        r'\<'
        return t

    def t_EQUAL(self, t):
        r'=='
        return t

    def t_ASSIGN(self, t):
        r'='
        return t

    def t_LPAREN(self, t):
        r'\('
        return t

    def t_RPAREN(self, t):
        r'\)'
        return t

    def t_LCURL(self, t):
        r'\{'
        return t

    def t_RCURL(self, t):
        r'\}'
        return t

    def t_SEMICOLON(self, t):
        r'\;'
        return t

    def t_TYPE(self, t):
        r'number|string'
        return t

    t_ignore = ' \t'

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)
