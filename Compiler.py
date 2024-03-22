# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from LexicalAnalysis.LexicalAnalyzer import MyLexicalAnalyzer
from SyntacticAnalysis.SyntacticAnalyzer import MySyntacticAnalyzer
from SemanticAnalysis.SemanticAnalyzer import MySemanticAnalyzer
from IntermediateRepresentation.SingleAddressIntermediateRepresentation import IntermediateRepresentator
from IntermediateRepresentation import IntermediateRepresentator
from VitualMachineIR.SingleAddressVirtualMachineIRConsumer import MyVirtualMachineIRConsumer

lexer_instance = MyLexicalAnalyzer()
parser_instance = MySyntacticAnalyzer(lexer_instance)
# Test the parser

input_string0 = "1 < 3; 2 < 3;"

ast0 = parser_instance.parser.parse(input_string0, lexer=lexer_instance.lexer)
if not parser_instance.er:
    print("\nSourceCode:", ast0)
    sem0 = MySemanticAnalyzer(ast0)
    print("Is the expression Semantically Valid: ", sem0.isSemanticallyValid())
    if (sem0.isSemanticallyValid()):
        print("codeGeneration:")
        if sem0.isSemanticallyValid():
            codeGen = IntermediateRepresentator(ast0)
            codeGen.generate()
            print("    ", ".LOC")
            for i in codeGen.LOC:
                print ("        ", i)
            print()
            print("    ", "main:")
            for i in codeGen._generatedCode:
                print ("        ", i)
        print("Consuming:")
        vm0 = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
        vm0.consume()
