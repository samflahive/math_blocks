from .math_block import math_block


class variable(math_block):
    def __init__(self, symbol, sign=True):
        math_block.__init__(self, sign=sign)
        self.symbol = symbol
        self.sign = sign

    def latex(self, explicit=False):
        if self.sign:
            return "-%s" % self.symbol
        return self.symbol
    
    def evaluate(self):
        return self.value if self.sign else -self.value
