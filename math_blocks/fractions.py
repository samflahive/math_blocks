from .math_block import math_block
from .numbers import number
from .products import product

class fraction(math_block):
    def __init__(self, numerator, denominator, sign=True):
        math_block.__init__(self, sign=sign)

        if isinstance(numerator, (int, float)):
            numerator = number(numerator)
        if isinstance(denominator, (int, float)):
            denominator = number(denominator)

        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self):
        val = self.numerator.evaluate() / self.denominator.evaluate()
        if self.sign:
            return val
        return -val

    def latex(self, explicit=False):
        if self.sign:
            return "\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))
        else:
            return "-\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))

    def __mul__(self, other):
        return product([self, other])
