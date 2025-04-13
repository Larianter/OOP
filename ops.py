#Mathematical operations for calculator app
import math

class Operation:
    def __init__(self,id):
        self.id = id

class Addition(Operation):
    def __init__(self,a,b,id):
        super().__init__(id)
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        return  result
    
    def __str__(self):
        pass

class Subtraction(Operation):
    def __init__(self,a,b,id):
        super().__init__(id)
        self.a = a
        self.b = b

    def sub(self):
        result = self.a - self.b
        return result
    
    def __str__(self):
        pass

class Division(Operation):
    def __init__(self,a,b,id):
        super().__init__(id)
        self.a = a
        self.b = b
    
    def div(self):
        result = self.a / self.b
        return result
    
    def __str__(self):
        pass

class Exponent(Operation):
    def __init__(self,a,b,id):
        super().__init__(id)
        self.a = a
        self.b = b

    def exp(self):
        result = math.pow(self.a,self.b)
        return result

    def __str__(self):
        pass

class Square(Operation):
    def __init__(self,a,id):
        super().__init__(id)
        self.a = a
    
    def sqrt(self):
        result = math.sqrt(self.a)
        return result

    def __str__(self):
        pass

class Inverse(Operation):
    def __init__(self,a,id):
        super().__init__(id)
        self.a = a

    def inv(self):
        result = 1/self.a
        return result

    def __str__(self):
        pass