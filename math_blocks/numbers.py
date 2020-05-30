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
