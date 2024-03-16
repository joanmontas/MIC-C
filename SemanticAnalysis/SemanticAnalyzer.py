# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from AbstractSyntaxTree.AbstractSyntaxNode import *
from SymbolicTable.SymbolicTable import *

class MySemanticAnalyzer:
  def __init__(self, ast):
    self.ast = ast
    self.scopeStack = SymbolicTable()
    self.theErrors = []
    self.debug = []

  def isSemanticallyValid(self):
    if len(self.theErrors) != 0:
      return False
    self._semanticallyAnalyze()
    if len(self.theErrors) != 0:
      return False
    return True

  def _semanticallyAnalyze(self):
    self.scopeStack.clearScopes()
    self.scopeStack.pushScope()
    if self.ast.nodeType != 'statements':
      self.theErrors.append(AstSemanticError("Starting AST Node Should Be Of Type 'statements'"), ast)
      raise TabError("Starting AST Node Should Be Of Type 'statements'")
      return
    statementPointer = self.ast
    while statementPointer != None:
      self.semanticallyAnalyzeStatements(statementPointer.value0)
      statementPointer = statementPointer.value1

    # self.scopeStack.popScope()

  def semanticallyAnalyzeStatements(self, ast):
    if ast.nodeType == 'identAssignment':
      self._validAssingmentStatement(ast)
    elif ast.nodeType == 'identReAssignment':
      self._validReAssingmentStatement(ast)
    elif ast.nodeType == 'expressionStatement':
      ast.valueType =  self._typeOfExpression(ast.value)
    else:
      self.theErrors.append(AstSemanticError("Unkown Statement", ast))
      raise NameError (f"SemanticAnalysis: Unkown Statement Type {ast.nodeType}")
      return 'semanticError'

    # check that ident is of the same type as its statementExpression
  def _typeOfExpression(self, ast):
    if ast.nodeType == 'groupExpression':
      valueType = self._typeOfExpression(ast.value)
      ast.valueType = valueType
      return valueType
    elif ast.nodeType == 'binaryExpression':
      valueType = self._validBinaryExpression(ast)
      ast.valueType = valueType
      return valueType
    elif ast.nodeType == 'numberLiteral':           # NOTE() terminal - Joan
      return 'number'
    elif ast.nodeType == 'stringLiteral':           # NOTE() terminal - Joan
      return 'string'
    elif ast.nodeType == 'identLiteral':            # NOTE() terminal - Joan
      if not self.scopeStack.identExistInAnyScope(ast.value):
        self.theErrors.append(AstSemanticError(f"SemanticError: Identifier has not been declared in any scope: {ast.value}",ast))
        return 'semanticError'
      identType = self.scopeStack.getIdentType(ast.value)
      ast.valueType = identType
      return identType
    else:
      self.theErrors.append(AstSemanticError(f"SemanticError: Unkown Expression Type: {ast.nodeType}",ast))
      return 'semanticError'

  def _validAssingmentStatement(self, ast):

    # make sure ident has not been defined in the same scope
    if self.scopeStack.identExistInCurrentScope(ast.identifier):
      self.theErrors.append(AstSemanticError("Redefining Identifier In The Same Scope", ast))
      return 'semanticError'

    # Make sure no semanticError in the assignment's expressionStatement
    assignmentExpressionType = self._typeOfExpression(ast.value)  # NOTE(JoanMontas) dealing with expressionStatement
    if (assignmentExpressionType == 'semanticError'):
      return assignmentExpressionType
  
    # check that ident is of the same type as its statementExpression
    if (assignmentExpressionType != ast.type_):
      self.theErrors.append(AstSemanticError( "SemanticError: Identifier's type does not match its expressionStatement's type",ast))
      return 'semanticError'
    self.scopeStack.insertIdentToCurrentScope(ast.identifier, ast.type_, ast.value)

  def _validReAssingmentStatement(self, ast):
    # make sure ident has not been defined in the same scope
    if not self.scopeStack.identExistInAnyScope(ast.identifier):
        self.theErrors.append(AstSemanticError("SemanticError: Identifier has not been declared in any scope", ast))
        return 'semanticError'

    # Make sure no semanticError in the assignment's expressionStatement
    reAssignmentExpressionType = self._typeOfExpression(ast.value)  # NOTE(JoanMontas) dealing with expressionStatement
    if (reAssignmentExpressionType == 'semanticError'):
      return reAssignmentExpressionType

    identType_ = ast.value.valueType
    identType_ = self.scopeStack.getIdentType(ast.identifier)
    if identType_ != reAssignmentExpressionType:
      self.theErrors.append(AstSemanticError(f"SemanticError: Identifier '{ast.identifier}' is of type '{identType_}' but reassign '{reAssignmentExpressionType}' type", ast))
      return 'semanticError'
    ast.type_ = identType_
# less
  def _validBinaryExpression(self, ast):
    leftType = self._typeOfExpression(ast.left)
    rightType = self._typeOfExpression(ast.right)
    if leftType == 'semanticError' or rightType == 'semanticError':
      self.theErrors.append("SemanticError: Error found during Binary Expression", ast)
      return 'semanticError'
    ast.leftType = leftType
    ast.rightType = rightType

    if ast.op == '+':
      return self._validAdditionExpression(ast)
    if ast.op == '-':
      return self._validSubstractionExpression(ast)
    if ast.op == '*':
      return self._validMultiplicationExpression(ast)
    if ast.op == '<':
      return self._validLesserExpression(ast)
    if ast.op == '==':
      return self._validEqualityExpression(ast)

    self.theErrors.append(AstSemanticError("Semantic: Unkown Binary Expression",ast))
    return 'semanticError'

  def _validAdditionExpression(self, ast):
    left = ast.leftType
    right = ast.rightType
    if left == "number" and right == "number":
      return 'number'
    self.theErrors.append(AstSemanticError("SemanticError: Unkown Addition Configuration of such types", ast))
    return 'semanticError'

  def _validSubstractionExpression(self, ast):
    left = ast.leftType
    right = ast.rightType
    if left == "number" and right == "number":
      return 'number'
    self.theErrors.append(AstSemanticError("SemanticError: Unkown Substraction Configuration of such types", ast))
    return 'semanticError'

  def _validMultiplicationExpression(self, ast):
    left = ast.leftType
    right = ast.rightType
    if left == "number" and right == "number":
      return 'number'
    self.theErrors.append(AstSemanticError("SemanticError: Unkown Multiplication Configuration of such types", ast))
    return 'semanticError'

  def _validLesserExpression(self, ast):
    left = ast.leftType
    right = ast.rightType
    if left == "number" and right == "number":
      return 'number'
    self.theErrors.append(AstSemanticError("SemanticError: Unkown Lesser Configuration of such types", ast))
    return 'semanticError'


  def _validEqualityExpression(self, ast):
    left = ast.leftType
    right = ast.rightType
    if left == "number" and right == "number":
      return 'number'
    self.theErrors.append(AstSemanticError("SemanticError: Unkown Equality Configuration of such types", ast))
    return 'semanticError'
