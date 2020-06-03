import math_blocks

class variable(math_blocks.math_block):
    def __init__(self, symbol, value=None, sign=True, ):
        math_blocks.math_block.__init__(self, sign=sign)
        self.symbol = symbol
        self.sign = sign
        if isinstance(value, (int, float)):
            value = math_blocks.number(value)
        self.value = value

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return "-%s" % self.symbol
        if show_plus:
            return "+%s" % self.symbol
        return self.symbol
    
    def evaluate(self):
        if self.value != None:
            if isinstance(self.value, (int, float)):
                self.value = math_blocks.number(self.value)
            val = self.value.evaluate()
            if self.sign:
                return val
            return -val
        else:
            raise ValueError("variable (symbol=%s) does not have a value" % self.symbol)


    def __mul__(self, other):
        if isinstance(other, math_blocks.complex_number):
            return math_blocks.complex_number(real=(self*other.real), imaginary=(self*other.imaginary), sign=other.sign)
        elif isinstance(other, math_blocks.polynomial):
            return math_blocks.polynomial(items=[self*term for term in other.items], sign=other.sign)
        elif isinstance(other, math_blocks.polyterm):
            return math_blocks.polyterm(coeff=self*other.coeff, pcomp=other.pcomp, sign=other.sign)
        else:
            return math_blocks.product([self, other])

    def __eq__(self, other):
        if not isinstance(other, variable):
            return False
        return (self.symbol == other.symbol and self.sign == other.sign)
            
