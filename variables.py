from .math_block import math_block
from .products import product
from .chains import chain
from .fractions import fraction
from .number_formatting import object_sign

class variable(math_block):
    def __init__(self, symbol, sign=True):
        self.symbol = symbol
        self.sign = sign
        math_block.__init__(self, sign=sign, bracketed=False)
        
            
    def __eq__(self, other):
        if not isinstance(other, variable):
            return False
        return self.symbol == other.symbol

    def __mul__(self, other):
        return product([self, other])

    def __div__(self, other):
        return fraction(self, other)

    def __truediv__(self, other):
        return fraction(self, other)

    def __add__(self, other):
        return chain(items=[self, other])

    def latex(self, explicit=False, show_plus=False):
        out = self.symbol
        out = object_sign(show_plus=show_plus, sign=self.sign)+out
        return out
    
    def evaluate(self):
        return self.value if self.sign else -self.value

    @staticmethod
    def multi_setup(letters, values):
        output = []
        for i,x in enumerate(letters):
            var = variable(x)
            var.value = values[i]
            output.append(var)
        return output

    @staticmethod
    def set_values(variables, values):
        for i,x in enumerate(variables):
            x.value = values[i]
