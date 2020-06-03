from .math_block import math_block
import math_blocks
class number(math_block):

    def __init__(self, value, sign=True):
        implied_sign = value > 0
        math_block.__init__(self, sign=(implied_sign == sign))

        value = abs(value)
        self.value = value

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return "-{}".format(self.value)
        if show_plus:
            return "+{}".format(self.value)
        return str(self.value)

    def evaluate(self):
        if self.sign:
            return self.value
        return -self.value


    def __eq__(self, other):
        if isinstance(other, number):
            return ((self.value == other.value) and (self.sign == other.sign))
        if isinstance(other, (int, float)):
            self_value = self.value if self.sign else -self.value
            return self_value == other
        return False


    def __add__(self, other):
        if isinstance(other, number):
            return number(value=self.evaluate()+other.evaluate())
        if isinstance(other, (int,float)):
            return number(value=(self.evaluate()+other))            
        return math_blocks.chain([self, other])

    def __truediv__(self, other):
        if isinstance(other, number):
            return number(value=self.evaluate()/other.evaluate())
        if isinstance(other, (int,float)):
            return number(value=self.evaluate()/other)
        return math_blocks.fraction(self, other)

    def __mul__(self, other):
        if isinstance(other, number):
            return number(value=self.evaluate()*other.evaluate())
        elif isinstance(other, (int,float)):
            return number(value=self.evaluate()*other)
        elif isinstance(other, math_blocks.complex_number):
            return math_blocks.complex_number(real=other.real*self, imaginary=other.imaginary*self, sign=other.sign)
        elif isinstance(other, math_blocks.polynomial):
            return math_blocks.polynomial(items=[self*term for term in other.items], sign=other.sign)
        elif isinstance(other, math_blocks.polyterm):
            return math_blocks.polyterm(coeff=self*other.coeff, pcomp=other.pcomp, sign=other.sign)
        else:
            return math_blocks.product([self, other])

    def __eq__(self, other):
        if not isinstance(other, number):
            return False
        return (self.value == other.value and self.sign == other.sign)
