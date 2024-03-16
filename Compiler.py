# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from LexicalAnalysis.LexicalAnalyzer import MyLexicalAnalyzer
from SyntacticAnalysis.SyntacticAnalyzer import MySyntacticAnalyzer
from SemanticAnalysis.SemanticAnalyzer import MySemanticAnalyzer

lexer_instance = MyLexicalAnalyzer()
parser_instance = MySyntacticAnalyzer(lexer_instance)

input_string0  = "number v = -2;"
input_string0 += "number y = 2;"
input_string0 += "v = v + y;"

ast0 = parser_instance.parser.parse(input_string0, lexer=lexer_instance.lexer)
if parser_instance.er:
    pass
else:
    print("\nSourceCode:", ast0)
    sem0 = MySemanticAnalyzer(ast0)
    print("Is the expression Semantically Valid: ", sem0.isSemanticallyValid())
