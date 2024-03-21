# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import unittest

from IntermediateRepresentation.SingleAddressIntermediateRepresentation import IntermediateRepresentator
from VitualMachineIR.SingleAddressVirtualMachineIRConsumer import MyVirtualMachineIRConsumer

from LexicalAnalysis import LexicalAnalyzer
from SyntacticAnalysis import SyntacticAnalyzer
from SemanticAnalysis import SemanticAnalyzer

# const
ZERO = 0
MINPOSITIVE = 1
MAXPOSITIVE = 2047
MINEGATIVE = 4095
MAXNEGATIVE = 2048


class testIntermediateRepresentationOfSimpleExpressionStatement(unittest.TestCase):
        maxDiff = None

        def testIRofSingleExpressionStatementSingleNumberLiteral(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "7;"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(7))

        def testIRofArithmeticExpressionOfNumberAddition(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "999 + 67;"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(1066))


        def testIRofArithmeticExpressionOfNumberSubstraction(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "456 - 567;"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(-111))

        def testIRofArithmeticExpressionOfNumberSubstractionSubstraction(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "456 + 567 - 23 - 524 + 344;"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(820))

        def testIRofArithmeticGroupExpressionOfSingleNumber(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "(8475);"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(8475))

        def testIRofArithmeticGroupExpressionOfBinaryExpressionNumber(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "(9834 - 8734);"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(1100))


class testIntermediateRepresentationOfSimplStatement(unittest.TestCase):
        maxDiff = None

        def testIRofSimpleAssingmentStatementl(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "number x = 8756;"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.stackMemory[vm._LOClocation['x']], vm.convertIntTo12Bit(8756))
                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(8756))

        def testIRofSimpleReAssingmentStatementl(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "number jjhfnfkD = 98; 1; 2; 3; 4; 5; jjhfnfkD = jjhfnfkD + 1 + jjhfnfkD; 6; 7; 8; 9;"


                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.stackMemory[vm._LOClocation['jjhfnfkD']], vm.convertIntTo12Bit(197))

class testIntermediateRepresentationOfSimpleConditionalExpression(unittest.TestCase):
        maxDiff = None

        def testIRofSimpleLesserThanPositive_0_Positive_1_Numeric(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "0 < 1;"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(1))
                self.assertEqual(vm._sp, vm._startingSP)

        def testIRofSimpleLesserThanPositive_1_Positive_32767_Numeric(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = f"1 < {MAXPOSITIVE};"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(1))
                self.assertEqual(vm._sp, vm._startingSP)

        def testIRofSimpleNumberialEquality(self):
                lexicalAnalyzerInstance = LexicalAnalyzer.MyLexicalAnalyzer()
                syntacticAnalyzerInstance = SyntacticAnalyzer.MySyntacticAnalyzer(lexicalAnalyzerInstance)

                testInput = "857 == 857;"

                ast = syntacticAnalyzerInstance.parser.parse(testInput)

                sem = SemanticAnalyzer.MySemanticAnalyzer(ast)
                sem.isSemanticallyValid()
                self.assertEqual(len(sem.theErrors), 0)

                codeGen = IntermediateRepresentator(ast)
                codeGen.generate()

                vm = MyVirtualMachineIRConsumer(codeGen._generatedCode, codeGen.LOC)
                vm.consume()

                self.assertEqual(vm.accumulator, vm.convertIntTo12Bit(0))
                self.assertEqual(vm._sp, vm._startingSP)
