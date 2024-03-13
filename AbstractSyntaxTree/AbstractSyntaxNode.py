# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from abc import ABC, abstractmethod,ABCMeta

class MetaAst(ABCMeta):
    def __new__(cls, name, bases, attrs):
        # Check for the required attribute
        if 'nodeType' not in attrs:
            raise TypeError("Concrete classes must define a 'nodeType'.")

        # Proceed with class creation
        return super().__new__(cls, name, bases, attrs)

class Ast(metaclass=MetaAst):
    nodeType = "AbstractNode"
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __type__(self):
        pass

class AstStatements(Ast):
    nodeType = "statements"
    def __init__(self, first, second=None):
        # TODO(JoanMontas) I do not like they have value0 and value1, have a simple value but have an array
        # then do the same even if 
        self.value0 = first
        self.value1 = second
        self.value = []
        self.__convertingStatementsIntoIterableContainer(first)
        self.__convertingStatementsIntoIterableContainer(second)

    def __str__(self):
        if self.value1 != None:
            return self.value0.__str__() + " " +self.value1.__str__()
        return self.value0.__str__()

    def __type__(self):
        return self.nodeType
    
    def __convertingStatementsIntoIterableContainer(self, value_):
        if value_ == None:
            return
        if(value_.nodeType == "statements"):
            self.value.append(value_.value0)
            self.__convertingStatementsIntoIterableContainer(value_.value1)
        else:
            self.value.append(value_)

class AstExpressionStatement(Ast):
    nodeType = "expressionStatement"

    def __init__(self, value):
        self.value = value
        self.valueType = None

    def __str__(self):
        return str(self.value.__str__()) + ";"

    def __type__(self):
        return self.nodeType

class AstNumberLiteral(Ast):
    nodeType = "numberLiteral"

    def __init__(self, value):
        self.value = value
        self.valueType = 'number'

    def __str__(self):
        return str(self.value)

    def __type__(self):
        return self.nodeType

class AstStringLiteral(Ast):
    nodeType = "stringLiteral"

    def __init__(self, value):
        self.value = value
        self.valueType = 'string'

    def __str__(self):
        return f"'{self.value}'"

    def __type__(self):
        return self.nodeType

class AstTypeLiteral(Ast):
    # NOTE() Still not implemented, just predicting the future - Joan
    nodeType = "typeLiteral"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return value

    def __type__(self):
        return self.nodeType

class AstBinaryExpression(Ast):
    nodeType = "binaryExpression"

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.leftType = None
        self.right = right
        self.rightType = None
        self.valueType = None

    def __str__(self):
        return f"{self.left.__str__()} {self.op} {self.right.__str__()}"

    def __type__(self):
        return self.nodeType

class AstDereference(Ast):
    # NOTE() Still needs to be implemented, just predicting the future - Joan
    nodeType = "dereference"

    def __init__(self, value):
        self.value = value
        self.valueType = None

    def __str__(self):
        return f"*{self.value.__str__()}"

    def __type__(self):
        return self.nodeType

class AstGroupExpression(Ast):
    nodeType = "groupExpression"

    def __init__(self, value):
        self.value = value
        self.valueType = None

    def __str__(self):
        return f"({self.value.__str__()})"

    def __type__(self):
        return self.nodeType

class AstIdentLiteral(Ast):
    nodeType = "identLiteral"

    def __init__(self, value):
        self.value = value
        self.valueType = None

    def __str__(self):
        return self.value

    def __type__(self):
        return self.nodeType

class AstIdentAssignment(Ast):
    nodeType = "identAssignment"

    def __init__(self, type_, identifier, value):
        self.type_ = type_
        self.identifier = identifier
        self.value = value

    def __str__(self):
        return f"{self.type_.__str__()} {self.identifier} = {self.value};"

    def __type__(self):
        return self.nodeType

class AstIdentReAssignment(Ast):
    nodeType = "identReAssignment"

    def __init__(self, identifier, value):
        self.type_ = None
        self.identifier = identifier
        self.value = value

    def __str__(self):
        return f"{self.identifier.__str__()} = {self.value.__str__()};"

    def __type__(self):
        return self.nodeType

class AstTypeLiteral(Ast):
    nodeType = "typeLiteral"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __type__(self):
        return self.nodeType

class AstBlockStatement(Ast):
    nodeType = "blockStatement"
    def __init__(self, value):
        self.value = []
        self.original = value
        self.__convertingStatementsIntoIterableContainer(value)

    def __str__(self):
        stringVersion = "{"
        for i in self.value:
            stringVersion += i.__str__() + " "
        if stringVersion[-1] == " ":
            stringVersion = stringVersion[:-1]
        stringVersion += "}"
        return stringVersion

    def __type__(self):
        return self.nodeType

    def __convertingStatementsIntoIterableContainer(self, value_):
        if value_ == None:
            return
        if(value_.nodeType == "statements"):
            self.value.append(value_.value0)
            self.__convertingStatementsIntoIterableContainer(value_.value1)
        else:
            self.value.append(value_)
        
# NOTE(JoanMontas) can consolidate both AstIfStatement and AstIfElseStatement into a single one
class AstIfStatement(Ast):
    nodeType = "ifStatement"

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __str__(self):
        return f"if ({self.condition.__str__()}) {self.body.__str__()};"

    def __type__(self):
        return self.nodeType

class AstIfElseStatement(Ast):
    nodeType = "ifElseStatement"

    def __init__(self, condition, body, elseBody):
        self.condition = condition
        self.body = body
        self.elseBody = elseBody

    def __str__(self):
        return f"if ({self.condition.__str__()}) {self.body.__str__()} else {self.elseBody.__str__()};"

    def __type__(self):
        return self.nodeType

class AstWhileStatement(Ast):
    nodeType = "whileStatement"

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __str__(self):
        return f"while ({self.condition.__str__()}) {self.body.__str__()}"

    def __type__(self):
        return self.nodeType

class AstSemanticError(Ast):
    nodeType = "semanticError"

    def __init__(self, value, ast):
        self.value = value
        self.ast = ast

    def __str__(self):
        return self.value.__str__()

    def __type__(self):
        return self.nodeType
