class variable:
    def __init__(self, symbol):
        self.symbol = symbol
        self.sign = True

    def __eq__(self, other):
        if not isinstance(other, variable):
            return False
        return self.symbol == other.symbol

    def set_value(self, value):
        self.value = value

    def latex(self):
        return self.symbol
    
    def evaluate(self):
        return self.value
