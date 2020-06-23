from copy import deepcopy

class Constant:
    def __init__(self, symbol, value, id, sign=True):
        self.symbol = symbol
        self.value = value
        self.id = id
        self.sign = sign
        block_type = "C"

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return f"-{self.symbol}"
        elif show_plus:
            return f"+{self.symbol}"
        else:
            return self.symbol

    def evaluate(self):
        if self.sign:
            return self.value
        else:
            return -self.value

    def __neg__(self):
        copied = deepcopy(self)
        copied.sign = not self.sign
        return copied