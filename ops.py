#Mathematical operations for calculator app
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

class Square(Operation):
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

'''
def test():
    addOperation = Addition(2,2)
    addOperation.add()
    print(addOperation)
    print(addOperation.id)

    subOperation = Subtraction(4,2)
    subOperation.sub()
    print(subOperation)
    print(subOperation.id)

    divOperation = Division(8,4)
    divOperation.div()
    print(divOperation)
    print(divOperation.id)

    expOperation = Exponent(3,3)
    expOperation.exp()
    print(expOperation)
    print(expOperation.id)

    sqrtOperation = Square(64)
    sqrtOperation.sqrt()
    print(sqrtOperation)
    print(sqrtOperation.id)

    invOperation = Inverse(4)
    invOperation.inv()
    print(invOperation)
    print(invOperation.id)

test()
'''