# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import unittest
from SyntacticAnalysis import SyntacticAnalyzer
from LexicalAnalysis import LexicalAnalyzer

class testSyntacticAnalysisCodeRegeneration(unittest.TestCase):
    maxDiff = None

    def testSyntancticAnalysisOfSingleNumberPositive(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "123;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntancticAnalysisOfSingleNumberNegative(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "123;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)
        
    def testSyntancticAnalysisOfSingleString(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "'Hello, World!';"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntancticAnalysisOfSinglebinaryExpression0(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "1 + 2;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntancticAnalysisOfSinglebinaryExpression1(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "1 * 2;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntancticAnalysisOfSinglebinaryExpression2(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "2 == 3;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntancticAnalysisOfDereferencingExpression(self):
        # NOTE(JoanMontas) I should not dereference expressions but rather statement... FIX THE GRAMMAR!
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "*SomeVariableBeingDereference;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisGroupSingleBinaryExpression(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "(1 / 2);"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisGroupSingleString(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "('Hi, I am grouped');"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisGroupMultipleBinaryExpression(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "(2 + 3) * 4;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisLiteralSingleVariable(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "SomeRandomVariableThatIhaveJustCreated;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisLiteralSingleType(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "number;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisVariableDeclaration(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "number yetAgainHereIsAnother = 123;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisVariableAssignment(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "CompilersAreReallyCool = 123;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisBlockStatement0(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "{'Look Mah, I am a block';}"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)
        
    def testSyntacticAnalysisBlockStatement1(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "{'Look Mah, I am a block'; 'I am still a block?'; 456456; 'still?';}"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisIfStatement(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "if (1) {2;};"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysisIfElseStatement(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "if (1) {2;} else {3; 4; 5; 6;};"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

    def testSyntacticAnalysis(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "if (1) {2;} else {3; 4; 5; 6;};"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)

class testSyntacticAnalysisSyntaxTreeShape(unittest.TestCase):
    maxDiff = None

    def testFoo(self):
        self.assertEqual(1, 1)

    def testSyntacticAnalysisOfNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "123;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)
        self.assertEqual(ast.value0.nodeType, 'expressionStatement')
        self.assertEqual(ast.value0.value.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.value, 123)

    def testSyntacticAnalysisOfNegativeNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "-2;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)
        self.assertEqual(ast.value0.nodeType, 'expressionStatement')
        self.assertEqual(ast.value0.value.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.value, -2)

    def testSyntacticAnalysisOfStringLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "'kjfgdf$%6f3236^fghh';"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)
        self.assertEqual(ast.value0.nodeType, 'expressionStatement')
        self.assertEqual(ast.value0.value.nodeType, 'stringLiteral')
        self.assertEqual(ast.value0.value.value, 'kjfgdf$%6f3236^fghh')

    def testSyntacticAnalysisOfbinaryExpressionOfTwoNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "8767 + 543;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)
        self.assertEqual(ast.value0.nodeType, 'expressionStatement')
        self.assertEqual(ast.value0.value.nodeType, 'binaryExpression')
        self.assertEqual(ast.value0.value.op, '+')
        self.assertEqual(ast.value0.value.left.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.left.value, 8767)
        self.assertEqual(ast.value0.value.right.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.right.value, 543)

    def testSyntacticAnalysisOfbinaryExpressionOfThreeNumberLiteralPrecedence0(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "8767 + 543 + 456456;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)
        self.assertEqual(ast.value0.nodeType, 'expressionStatement')
        self.assertEqual(ast.value0.value.nodeType, 'binaryExpression')
        self.assertEqual(ast.value0.value.op, '+')
    
        self.assertEqual(ast.value0.value.left.nodeType, 'binaryExpression')
        self.assertEqual(ast.value0.value.left.op, '+')
        self.assertEqual(ast.value0.value.left.left.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.left.left.value, 8767)
        self.assertEqual(ast.value0.value.left.right.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.left.right.value, 543)

        self.assertEqual(ast.value0.value.right.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.right.value, 456456)

    def testSyntacticAnalysisOfbinaryExpressionOfThreeNumberLiteralPrecedence1(self):
        """                                                           statements
                                                            /                          \
                                                    statement                               None
                                                        |
                                                expressionStatement
                                                        |
                                                binaryExpression '+'
                                                    /               \
                                    numberLiteral 8767             binaryExpression *
                                                                    /               \
                                                            numberLiteral 543    numberliteral 456456
        """
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "8767 + 543 * 456456;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)
        self.assertEqual(ast.value0.nodeType, 'expressionStatement')
        self.assertEqual(ast.value0.value.nodeType, 'binaryExpression')
        self.assertEqual(ast.value0.value.op, '+')
    
        self.assertEqual(ast.value0.value.left.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.left.value, 8767)

        self.assertEqual(ast.value0.value.right.left.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.right.left.value, 543)
        self.assertEqual(ast.value0.value.right.right.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.right.right.value, 456456)

    def testSyntacticAnalysisOfbinaryExpressionGrouped(self):
        """                                                        statements
                                                          /                        \ 
                                                    expressionStatement              None
                                                            |
                                                    groupExpression
                                                            |
                                                    binaryExpression '+'
                                                    /              \
                                                45054390          56080
        """

        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "(45054390 + 56080);"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)
        self.assertEqual(ast.value0.nodeType, 'expressionStatement')
        self.assertEqual(ast.value0.value.nodeType, 'groupExpression')
        self.assertEqual(ast.value0.value.value.nodeType, 'binaryExpression')

        self.assertEqual(ast.value0.value.value.op, '+')

        self.assertEqual(ast.value0.value.value.left.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.value.left.value, 45054390)

        self.assertEqual(ast.value0.value.value.right.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.value.right.value, 56080)

    def testSyntacticAnalysisOfbinaryExpressionGroupedPrecedence(self):
        """                                                           statements
                                                            /                          \
                                                    statement                               None
                                                        |
                                                expressionStatement
                                                        |
                                                binaryExpression '*'
                                                    /           \
                                    groupExpression             numberLiteral 58932
                                        |
                                binaryExpression +
                                /               \
                    numberLiteral 45054390    numberliteral 56080
        """
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "(45054390 + 56080) * 58932;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)

        self.assertEqual(ast.nodeType, 'statements')
        self.assertEqual(ast.value1, None)

        self.assertEqual(ast.value0.nodeType, 'expressionStatement')

        self.assertEqual(ast.value0.value.nodeType, 'binaryExpression')
        self.assertEqual(ast.value0.value.op, '*')

        self.assertEqual(ast.value0.value.left.nodeType, 'groupExpression')
        self.assertEqual(ast.value0.value.left.value.nodeType, 'binaryExpression')
        self.assertEqual(ast.value0.value.left.value.op, '+')
        self.assertEqual(ast.value0.value.left.value.left.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.left.value.left.value, 45054390)
        self.assertEqual(ast.value0.value.left.value.right.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.left.value.right.value, 56080)

        self.assertEqual(ast.value0.value.right.nodeType, 'numberLiteral')
        self.assertEqual(ast.value0.value.right.value, 58932)

if __name__ == '__main__':
    unittest.main()
