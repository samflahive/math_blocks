from .math_block import math_block
from .numbers import number

class variable(math_block):
    def __init__(self, symbol, sign=True, value=None):
        math_block.__init__(self, sign=sign)
        self.symbol = symbol
        self.sign = sign
        if isinstance(value, (int, float)):
            value = number(value)
        self.value = value

    def latex(self, explicit=False):
        if not self.sign:
            return "-%s" % self.symbol
        return self.symbol
    
    def evaluate(self):
        if self.value != None:
            if isinstance(self.value, (int, float)):
                self.value = number(self.value)
            val = self.value.evaluate()
            if self.sign:
                return val
            return -val
        else:
            raise ValueError("variable (symbol=%s) does not have a value" % self.symbol)
