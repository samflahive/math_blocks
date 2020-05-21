from copy import deepcopy

class math_block:
    def __init__(self, sign, product_bracket=False,
                  chain_bracket=False, bracketed=True):
        self.sign = sign
        self.product_bracket = product_bracket
        self.chain_bracket = chain_bracket
        self.bracketed = bracketed
              
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
