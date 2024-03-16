# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

class SymbolicTable:
    def __init__(self):
        self._scopeStack = []

    def pushScope(self):
        self._scopeStack.append({})

    def popScope(self):
        if len(self._scopeStack) == 0:
            raise IndexError ("SymbolicTable: Scope is empty")
        self._scopeStack.pop()

    def clearScopes(self):
        self._scopeStack = []

    def insertIdentToCurrentScope(self, ident, type_, expression = None):
        if len(self._scopeStack) == 0:
            raise IndexError ("SymbolicTable: Scope is empty")
        self._scopeStack[-1][ident] = [type_, expression]

    def identExistInCurrentScope(self, ident):
        if len(self._scopeStack) == 0:
            raise IndexError ("SymbolicTable: Scope is empty")
        if ident in self._scopeStack[-1]:
            return True
        return False

    def identExistInAnyScope(self, ident):
        for i in range(len(self._scopeStack)-1, -1, -1):
            if ident in self._scopeStack[i]:
                return True
        return False

    def getIdent(self, ident):
        for i in range(len(self._scopeStack)-1, -1, -1):
            if ident in self._scopeStack[i]:
                return self._scopeStack[i][ident]
        raise NameError (f"Ident: {ident} was not found.")

    def getIdentType(self, ident):
        for i in range(len(self._scopeStack)-1, -1, -1):
            if ident in self._scopeStack[i]:
                return self._scopeStack[i][ident][0]
        raise NameError (f"Ident: {ident} was not found.")

    def getIdentExpression(self, ident):
        for i in range(len(self._scopeStack)-1, -1, -1):
            if ident in self._scopeStack[i]:
                return self._scopeStack[i][ident][1]
        raise NameError (f"Ident: {ident} was not found.")
