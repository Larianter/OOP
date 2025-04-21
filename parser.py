from lark import Lark, Transformer
import ops

# Lark grammar definition
calcGrammar = """
    ?start: expr

    ?expr: expr "+" term    -> add
         | expr "-" term    -> sub
         | term
    
    ?term: term "*" pow     -> mul
         | term "÷" pow     -> div
         | pow

    ?pow: atom "^" pow      -> exp
         | atom

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | "Ans"            -> ans
         | "√" atom        -> sqrt
         | atom "x²"       -> square
         | atom "x⁻¹"      -> inverse
         | "(" expr ")"

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

# Linking operations to parser
class CalcTransformer(Transformer):
    def __init__(self,last_answer="0"):
        self.last_answer = float(last_answer)

    def number(self,n):
        return float(n[0])
    
    def ans(self, _):
        return self.last_answer

    def add(self, args):
        op = ops.Addition(args[0], args[1])
        result = op.add()
        print(op)
        return result

    def sub(self, args):
        op = ops.Subtraction(args[0], args[1])
        result = op.sub()
        print(op)
        return result

    def mul(self, args):
        op = ops.Multiplication(args[0], args[1])
        result = op.mul()
        print(op)
        return result

    def div(self, args):
        op = ops.Division(args[0], args[1])
        result = op.div()
        print(op)
        return result

    def exp(self, args):
        op = ops.Exponent(args[0], args[1])
        result = op.exp()
        print(op)
        return result

    def neg(self, args):
        return -args[0]

    def sqrt(self, args):
        op = ops.Sqrt(args[0])
        result = op.sqrt()
        print(op)
        return result

    def square(self, args):
        op = ops.Exponent(args[0], 2)
        result = op.exp()
        print(op)
        return result

    def inverse(self, args):
        op = ops.Inverse(args[0])
        result = op.inv()
        print(op)
        return result