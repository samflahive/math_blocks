class variable:
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, other):
        return self.symbol == other.symbol

    def set_value(self, value):
        self.value = value

    def latex(self):
        return self.symbol
    
    def evaluate(self):
        return self.value
