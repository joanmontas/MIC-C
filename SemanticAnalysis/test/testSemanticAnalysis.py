# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import unittest
from LexicalAnalysis import LexicalAnalyzer
from SyntacticAnalysis import SyntacticAnalyzer
from SemanticAnalysis import SemanticAnalyzer

class testSemanticAnalysisOfSimpleExpressionStatement(unittest.TestCase):
    maxDiff = None

    def testSemanticAnalysisOfSingleExpressionStatementSingleNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "7;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSingleExpressionStatementMultiNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "93757495465846;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSingleExpressionStatementSingleNegativeNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "-9;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSingleExpressionStatementMultiNegativeNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "-345987345345;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSingleCharacterString(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "'k';"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfMultiCharacterString(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "'kjlFGHdfgGjhsg';"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSimpleValidBinaryExpression(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "1 + 2;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSimpleInvalidBinaryExpression(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "123 + 'asd';"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 1)

    def testSemanticAnalysisOfSimpleBinaryGroupedExpression(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "(4567 - 8745);"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSimpleGroupNumberLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "(4567);"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfSimpleGroupStringLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "('jhdfgkdfbbadffvb45ERR5e5645');"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        self.assertEqual(ast.__str__(), testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

class testSemanticAnalysisOfComplexExpressionStatement(unittest.TestCase):
    maxDiff = None

    def testSemanticAnalysisOfComplexBinaryExpression(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "7 + 345 - 620096970885740 + 8940375 + 948560;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfComplexGroupedBinaryExpression(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "(7 + 345 - 620096970885740) + (8940375) + 948560;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfComplexIdentLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "number ldjfkf = 456456; ldjfkf;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfComplexInvalidIdentLiteral(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "ldjfkf;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 1)
        self.assertEqual(sem.theErrors[-1].value, "SemanticError: Identifier has not been declared in any scope: ldjfkf")

    def testSemanticAnalysisOfComplexIdentLiteralReAssignment(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "number ldjfkf = 456456; number someOtherValue = ldjfkf;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 0)

    def testSemanticAnalysisOfComplexInvalidIdentLiteralReAssignment(self):
        lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
        syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)
        testInput = "string ldjfkf = '98734503450456$%^'; number someOtherValue = ldjfkf;"
        ast = syntacticAnalyzerInstance.parser.parse(testInput)
        sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
        sem.isSemanticallyValid()
        self.assertEqual(len(sem.theErrors), 1)
        self.assertEqual(sem.theErrors[-1].value, "SemanticError: Identifier's type does not match its expressionStatement's type")

if __name__ == '__main__':
    unittest.main()
