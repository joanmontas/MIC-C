# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

import numpy as np
from SymbolicTable.SymbolicTable import *
from AbstractSyntaxTree.AbstractSyntaxNode import *
from SemanticAnalysis.SemanticAnalyzer import MySemanticAnalyzer

class IntermediateRepresentator:
    def __init__(self, AbstractSyntaxTree):
        self.AbstractSyntaxTree = AbstractSyntaxTree
        self.currentAbstractSyntaxTree = None
        self._generatedCode = []
        self.scopeStack = []
        self.LOC = []
        self.LOClocation = 0
        self.sem = MySemanticAnalyzer(AbstractSyntaxTree)
        self.TAG = {}               # NOTE() In order to jump without having to look entire code, I will do {"x" : 6} to denote "x" is in the 6th line of source code - JoanMontas
        self._tagGroupCount = -1     # keeps track of current 'tag group'
        self.ZERO = 0
        self.MINPOSITIVE = 1
        self.MAXPOSITIVE = 32767 # 2047
        self.MINEGATIVE = 65535 # 4095
        self.MAXNEGATIVE = 32768 # 2048
        self.BIT = 16 # 12

        self.debug = []

    def generate(self):
        self._generatedCode = []
        self._generate()
        self._generatedCode.append("halt")
        return self._generatedCode

    def _generate(self):
        statementPointer = self.AbstractSyntaxTree
        while statementPointer != None:
            self._generateStatement(statementPointer.value0)
            statementPointer = statementPointer.value1
        return

    def _generateStatement(self, ast):
        # NOTE(Everyone) code generation will not be uploaded. Please contact me directly - Joan Montas
        if ast.nodeType == 'expressionStatement':  # TODO(JoanMontas) do a expression statement - Joan Montas
            self._generateExpressionStatement(ast.value)
            lastPushType = ast.valueType
            self._generatedCode.append(f"pop-{ast.value.valueType.upper()}")        # NOTE() All expressionStatement must place their result in the stack
        elif ast.nodeType == 'identAssignment':
            self._generateIdentAssignment(ast)
        elif ast.nodeType == 'identReAssignment':
            self._generateIdentReAssignment(ast)
        else:
            raise KeyError ("IntermediateRepresentation: Unkown Statement type")

