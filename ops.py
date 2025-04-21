# File name: ops.py
# Author: Lari Vainio
# Description: Defines calculator operations as class methods.

import math

class Operation:
    idCounter = 1

    #Unique ID generation for each operation
    def __init__(self):
        self.id = Operation.idCounter
        Operation.idCounter += 1

class Addition(Operation):
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b

    def add(self):
        self.result = self.a + self.b
        return  self.result
    
    def __str__(self):
        return f"{self.a} + {self.b} = {self.result}"

class Subtraction(Operation):
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b

    def sub(self):
        self.result = self.a - self.b
        return self.result
    
    def __str__(self):
        return f"{self.a} - {self.b} = {self.result}"

class Division(Operation):
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b
    
    def div(self):
        self.result = self.a / self.b
        return self.result
    
    def __str__(self):
        return f"{self.a} / {self.b} = {self.result}"
    
class Multiplication(Operation):
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b

    def mul(self):
        self.result = self.a * self.b
        return self.result

    def __str__(self):
        return f"{self.a} * {self.b} = {self.result}"

class Exponent(Operation):
    def __init__(self,a,b):
        super().__init__()
        self.a = a
        self.b = b

    def exp(self):
        self.result = math.pow(self.a,self.b)
        return self.result

    def __str__(self):
        return f"{self.a}^{self.b} = {self.result}"

class Sqrt(Operation):
    def __init__(self,a):
        super().__init__()
        self.a = a
    
    def sqrt(self):
        self.result = math.sqrt(self.a)
        return self.result

    def __str__(self):
        return f"sqrt({self.a} = {self.result})"

class Inverse(Operation):
    def __init__(self,a):
        super().__init__()
        self.a = a

    def inv(self):
        self.result = 1/self.a
        return self.result

    def __str__(self):
        return f"{self.a}^-1 = {self.result}"


def test(a,b):
    addOperation = Addition(a,b)
    addOperation.add()
    print(addOperation)
    print(addOperation.id)

    subOperation = Subtraction(a,b)
    subOperation.sub()
    print(subOperation)
    print(subOperation.id)

    divOperation = Division(a,b)
    divOperation.div()
    print(divOperation)
    print(divOperation.id)

    expOperation = Exponent(a,b)
    expOperation.exp()
    print(expOperation)
    print(expOperation.id)

    sqrtOperation = Sqrt(a)
    sqrtOperation.sqrt()
    print(sqrtOperation)
    print(sqrtOperation.id)

    sqrtOperation = Sqrt(b)
    sqrtOperation.sqrt()
    print(sqrtOperation)
    print(sqrtOperation.id)

    invOperation = Inverse(a)
    invOperation.inv()
    print(invOperation)
    print(invOperation.id)

    invOperation = Inverse(b)
    invOperation.inv()
    print(invOperation)
    print(invOperation.id)