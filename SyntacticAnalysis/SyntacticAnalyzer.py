# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from ply import yacc
from LexicalAnalysis.LexicalAnalyzer import MyLexicalAnalyzer
from AbstractSyntaxTree.AbstractSyntaxNode import *

class MySyntacticAnalyzer:
    # <statements> ::= statement
    #              | statement statements               # like a cons in lisp
    # <statement> ::= <TYPE> <ID> '=' <<expressionStatement> ';'                # assignment
    #             |   <ID> '=' <<expressionStatement> ';'                       # re-assignment
    #             |   <TYPE> <ID> ';'                                           # NOTE(JoanMontas) need to add it to the grammar
    #             |   <BLOCK>           # is the job of the statemetns with <Block> to account for ';'
    #             |   IF <LPAREN> <<expressionStatement> <RPAREN> <LCURL> <<expressionStatement> <RCURL> ';'
    #             |   IF <LPAREN> <<expressionStatement> <RPAREN> <LCURL> <<expressionStatement> <RCURL> ELSE <LCURL> <<expressionStatement> <RCURL> ';'
    #             |   WHILE <LPAREN> <expressionStatement> <RPAREN> <LCURL> <<expressionStatement> <RCURL> ';'
    #             |   <expressionStatement> ';'

    # <expressionStatement> ::= <expression> '+' <expression>
    #             |   <expression> '-' <expression>
    #             |   <expression> '*' <expression>
    #             |   <expression> '/' <expression>
    #             |   <expression> '==' <expression>
    #             |   <LPAREN> <expression> <RPAREN>
    #             |   '*' <expression>                                         # TODO(JoanMontas) need more research
    #             |   '-' <expression>                                         # TODO(JoanMontas) need more research
    #             |   <ID> '
    #             |   <TYPE>
    #             |   <NUMBER>
    #             |   <STRING>

    # DEFINITIONS
    # <TYPE>      ::= 'number'
    #             |   'string'
    # <ID>        ::= [a-zA-Z_][a-zA-Z0-9_]*

    # <NUMBER>    ::= \d+

    # <STRING>    ::= '\'' ([^\\']+|\\')* '\''
    # <BLOCK>     ::= LCURL <statements> RCURL                                 # TODO(JoanMontas) replace other statement's LCURL <statements> RCURL with this

    def __init__(self, lexer):
        self.lex = lexer
        self.tokens = lexer.tokens
        self.parser = yacc.yacc(module=self)
        self.er = None

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('left', 'EQUAL'),
        ('right', 'UMINUS'),
        ('nonassoc', 'LPAREN', 'RPAREN'),
    )

    def p_statements_single(self, p):
        '''statements : statement'''
        p[0] = AstStatements(p[1])


    def p_statements_multi(self, p):                # just like a cons in lisp
        '''statements : statement statements'''
        p[0] = AstStatements(p[1], p[2])

    def p_statement_expression(self, p):
        '''statement : expression SEMICOLON'''
        p[0] = AstExpressionStatement(p[1])

    def p_statement_declare_assign(self, p):
        '''statement : TYPE IDENT ASSIGN expression SEMICOLON'''
        p[0] = AstIdentAssignment(p[1], p[2], p[4])

    def p_statement_reassign(self, p):
        '''statement : IDENT ASSIGN expression SEMICOLON'''
        p[0] = AstIdentReAssignment(p[1], p[3])

    def p_statement_block(self, p):
        '''statement : LCURL statements RCURL'''
        p[0] = AstBlockStatement(p[2])

    def p_statement_IF(self, p):
        '''statement : IF LPAREN expression RPAREN LCURL statements RCURL SEMICOLON'''
        p[0] = AstIfStatement(p[3], AstBlockStatement(p[6]))

    def p_statement_IF_ELSE(self, p):
        '''statement : IF LPAREN expression RPAREN LCURL statements RCURL ELSE LCURL statements RCURL SEMICOLON'''
        p[0] = AstIfElseStatement(p[3],  AstBlockStatement(p[6]),  AstBlockStatement(p[10]))

    def p_statement_WHILE(self, p):
        '''statement : WHILE LPAREN expression RPAREN LCURL statements RCURL SEMICOLON'''
        p[0] = AstWhileStatement(p[3],  AstBlockStatement(p[6]))

    def p_expression_ident(self, p):
        '''expression : IDENT'''
        p[0] = AstIdentLiteral(p[1])

    def p_expression_type(self, p):
        '''expression : TYPE'''
        p[0] = AstTypeLiteral(p[1])

    def p_expression_number(self, p):
        '''expression : NUMBER'''
        p[0] = AstNumberLiteral(p[1])

    def p_expression_string(self, p):
        '''expression : STRING'''
        p[0] = AstStringLiteral(p[1])

    def p_expression_binop(self, p):
        '''expression : expression PLUS expression
                      | expression MINUS expression
                      | expression TIMES expression
                      | expression DIVIDE expression
                      | expression LESSER expression
                      | expression EQUAL expression'''
        p[0] = AstBinaryExpression(p[2], p[1], p[3])

    def p_expression_uminus(self, p):
        '''expression : MINUS NUMBER %prec UMINUS'''
        p[0] = AstNumberLiteral(-1*p[2])

    def p_expression_unary_times(self, p):
        '''statement : TIMES statement %prec UMINUS'''
        p[0] = AstDereference(p[2])

    def p_expression_group(self, p):
        '''expression : LPAREN expression RPAREN'''
        p[0] = AstGroupExpression(p[2])

    def p_error(self, p):
        # TODO(JoanMontas)
        print ("Syntax error at token", p)
        self.er =  f"Syntax error at token {p}"
        yacc.errok
