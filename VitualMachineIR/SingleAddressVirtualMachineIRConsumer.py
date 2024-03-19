# Copyright Joan Montas
# All rights reserved.
# License under GNU General Public License v3.0

from AbstractSyntaxTree.AbstractSyntaxNode import *
import numpy as np

class MyVirtualMachineIRConsumer:
    # Althought not architecturally correct, will provide
    # In a few minutes, a quick sanity testing of IR.
    # NOTE(Everyone) Entire machine will not be uploaded, please ask for it directly - Joan
    def __init__(self, IRstack, LOC):
        self.IR = IRstack
        self._IRSize = len(IRstack)

        self.LOC = LOC                                              # NOTE() Could have used a hash table - JoanMontas

        self._LOClocation = {}                                      # NOTE() I do not have a linker, yet, so I will use this to store location of variables, and other tags
        for i in range(len(self.LOC)):
            splt = self.LOC[i].split(':')
            self._LOClocation[splt[0]] = self._IRSize + i + 1

        self._TAGlocation = {}                                      # NOTE() I do not have a linker, yet, so I will use this to store location of variables, and other tags
        for i in range(len(self.IR)):
            splt = self.IR[i].split(':')
            if len(splt) == 2:
                self._TAGlocation[self.IR[i]] = i

        self.accumulator = 0
        self._pc = 0                            # Program Counter
        self._sp = 2048                         # Stack Pointer
        self._startingSP = 2048                 # starting Stack Pointer
        self.stackMemory = [self.convertIntTo12Bit(-1) for i in range(self._sp + 1)]

        self.ZERO = 0
        self.MINPOSITIVE = 1
        self.MAXPOSITIVE = 2047
        self.MINEGATIVE = 4095
        self.MAXNEGATIVE = 2048

        self.debug = []

    def consume(self):
        for i in range(0, 999):
            # fetch
            cmd = self.IR[self._pc]
            self._pc = self._pc + 1
            # decode
            decoded = self._decode(cmd)
            cmd = cmd.split(' ')
            # execute
            if cmd[0] == "halt":
                return
            else:
                self._execute(decoded)

    def _debugVisualizer(self, cmd, decoded):
            print("******************************************")
            print(f"undecoded = {cmd} and decoded = {decoded}")
            print(f"AC: {self.accumulator} or signed: {self.convert12BitToInt(self.accumulator)}")
            print(f"PC: {self._pc}")
            print(f"Stack-first-10: {self.stackMemory[(self._startingSP - 10):]} and SP = {self._sp}")
            print(f"variable-first-10: {self.stackMemory[(self._IRSize): self._IRSize + 10]}")
            print("******************************************")
            print()
            print()

    def _decode(self, cmd):
        operator = cmd.split(' ')
        operatorr  = operator[0].split('-')
        if len(operatorr) == 1:

            if operatorr[0] == 'halt':
                return [operatorr[0], operatorr[0], operator[0]]
            elif operatorr[0] == 'insp':
                return [operator[0], operator[1]]
            elif operatorr[0] == 'jneg' or operatorr[0] == 'jpos' or  operatorr[0] == 'jump' or operatorr[0] == 'jzer':
                return [operatorr[0], operator[1]]
            elif cmd in self._TAGlocation.keys():
                return [cmd, cmd, cmd]
            else:
                raise NameError (f"VM: Unknown opcode: {cmd}")
        elif len(operatorr) == 2:

            if (operatorr[0] == 'push') or (operatorr[0] == 'pop'):
                return [operatorr[0], operatorr[1]]
            else:
                return [operatorr[0], operatorr[1], operator[1]]
        raise NameError (f"VM: Unknown opcode decode: {cmd}")

    def _execute(self, cmd):
        if cmd[0] == "loco":
            if cmd[1] == 'NUMBER':
                self.accumulator = int(cmd[2])
            else:
                print("VM: _execute: loco unkown type")
        elif cmd[0] == "push":
            if cmd[1] == 'NUMBER':
                self._sp = self._sp - 1
                self.stackMemory[self._sp] = self.accumulator
            else:
                print("VM: _execute: push unkown type")
        elif cmd[0] == "pop":
            if cmd[1] == 'NUMBER':
                self.accumulator = self.stackMemory[self._sp]
                self._sp = self._sp + 1
            else:
                print("VM: _execute: pop unkown type")
        elif cmd[0] == 'addl':
            if cmd[1] == 'NUMBER':
                self.accumulator = self.convertIntTo12Bit(self.accumulator + self.stackMemory[self._sp + int(cmd[2])])
            else:
                print("VM: _execute: addl unkown type")
        elif cmd[0] == 'subl':
            if cmd[1] == 'NUMBER':
                self.accumulator = self.convertIntTo12Bit(self.accumulator - self.stackMemory[self._sp + int(cmd[2])])
            else:
                print("VM: _execute: subl unkown type")
        elif cmd[0] == 'lodd':
            if cmd[1] == 'NUMBER':
                self.accumulator = self.stackMemory[self._LOClocation[cmd[2]]]
            else:
                print("VM: _execute: lodd unkown type")
        elif cmd[0] == 'lodl':
            if cmd[1] == 'NUMBER':
                self.accumulator = self.stackMemory[self._sp + int(cmd[2])]
            else:
                print("VM: _execute: lodl unkown type")
        elif cmd[0] == 'stod':
            if cmd[1] == 'NUMBER':
                varLctn = self._LOClocation[cmd[2]]
                self.stackMemory[varLctn] = self.accumulator
                pass
            else:
                print("VM: _execute: stod unkown type")
        elif cmd[0] == 'insp':
            # NOTE() Is insp type specific? - JoanMontas
            self._sp = self._sp + int(cmd[1])
        elif cmd[0] in self._TAGlocation.keys():
            pass
        elif cmd[0] == 'jump':
            self._pc = self._TAGlocation[cmd[1]]
        elif cmd[0] == 'jneg':
            if self.convert12BitToInt(self.accumulator) < 0:
                self._pc = self._TAGlocation[cmd[1]]
        elif cmd[0] == 'jpos':
            if self.convert12BitToInt(self.accumulator) >= 0:
                self._pc = self._TAGlocation[cmd[1]]
        else:
            self.debug.append(f"VM: _execute: unkown: {cmd[0]}")
            print(f"VM: _execute: unkown: {cmd[0]}")

    def convertIntTo12Bit(self, num):
        if num < 0:
            return (num & (2**12 - 1))
        return num % self.MINEGATIVE

    def convert12BitToInt(self, num):
        if num < self.MAXNEGATIVE:
            return num
        return num - (self.MINEGATIVE + 1)
