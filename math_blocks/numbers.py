from .math_block import math_block
import math_blocks
class number(math_block):

    def __init__(self, value, sign=True):
        implied_sign = value > 0
        math_block.__init__(self, sign=(implied_sign == sign))
        value = abs(value)
        self.value = value
        self.num_collapsable = True

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
        block = math_block.__add__(self, other)
        block.num_collapsable = isinstance(other, number)
        return block

    def __mul__(self, other):
        if isinstance(other, math_blocks.complex_number):
            return math_blocks.complex_number(real=other.real*self, imaginary=other.imaginary*self, sign=other.sign)
        elif isinstance(other, math_blocks.polynomial):
            return math_blocks.polynomial(items=[self*term for term in other.items], sign=other.sign)
        elif isinstance(other, math_blocks.polyterm):
            return math_blocks.polyterm(coeff=self*other.coeff, pcomp=other.pcomp, sign=other.sign)
        else:
            block = math_block.__mul__(self, other)
            block.num_collapsable = isinstance(other, number)
            return block

    def __truediv__(self, other):
        block = math_block.__truediv__(self, other)
        block.num_collapsable = isinstance(other, number)
        return block

    def __eq__(self, other):
        if not isinstance(other, number):
            if isinstance(other, (int, float)):
                return other == self.evaluate()
            return False
        return (self.value == other.value and self.sign == other.sign)

    def check_num_collapsable():
        return True