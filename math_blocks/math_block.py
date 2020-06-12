from copy import deepcopy
import math_blocks
class math_block:
    def __init__(self, sign, product_bracket=False,
                  chain_bracket=False, bracketed=True):
        self.sign = sign
        self.product_bracket = product_bracket
        self.chain_bracket = chain_bracket
        self.bracketed = bracketed
        self.collapse_numbers = False


    def __add__(self, other):
        return math_blocks.chain([self, other])

    def __mul__(self, other):
        return math_blocks.product([self, other])

    def __truediv__(self, other):
        return math_blocks.fraction(self, other)
              
    def __neg__(self):
        new = deepcopy(self)
        new.sign = not self.sign
        return new

    def __sub__(self, other):
        return self + (-other)

    def __radd__(self, other):
        return self+other

    def __rmul__(self, other):
        return self*other
