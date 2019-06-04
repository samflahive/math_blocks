from .products import product
from .chains import chain
from .fractions import fraction

class variable:
    def __init__(self, symbol):
        self.symbol = symbol
        self.sign = True

    def __eq__(self, other):
        if not isinstance(other, variable):
            return False
        return self.symbol == other.symbol

    def __mul__(self, other):
        return product(self, other)

    def __div__(self, other):
        return fraction(self, other)

    def __truediv__(self, other):
        return fraction(self, other)

    def __add__(self, other):
        return chain(adders=[self, other])
    
    def set_value(self, value):
        self.value = value

    def latex(self, explicit=False):
        return self.symbol
    
    def evaluate(self):
        return self.value
