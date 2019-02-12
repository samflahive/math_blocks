import math

class logarithm:
    # list of functionality
    # 1) add and subtract
    # 2) division and multiplication
    # 3) latex print
    # 4) evaluate
    
    def __init__(self, exponent, base):
        self.exponent = exponent
        self.base = base

    def __add__(self, other):
        # add two logarithm objects
        # log_x(Y) + log_x(Z) = log_x(YZ)
        return logarithm(self.base, self.exponent*other.exponent)

    def __sub__(self, other):
        # subtract one logarithm object from another
        # log_x(Y) - log_x(Z) = log_x(Y/Z)
        return logarithm(self.base, self.exponent/other.exponent)

    def __div__(self, other):
        # divide one log object by another
        # 2 cases
        # 1) common base
        if self.base == other.base:
            # log_b(Y)/log_b(X) = log_X(Y)
            return logarithm(self.exponent, other.exponent)
        # 2) common exponent
        else:
            # log_b(Y)/log_x(Y) = log_b(X)
            return logarithm(other.base, self.base)

    def __mul__(slef, other):
        # multiply two logarithm objects
        # if the base of one is the exponent of the other eg. X
        # the result is the non X base and non X exponent
        exponent = self.exponent if self.exponent != other.base else other.exponent
        base = self.base if self.base != other.exponent else other.base
        return logarithm(exponent, base)

    def evaluate(self):
        # extract the value of the base whether its a number or variable
        exponent_value = self.exponent if isinstance(self.exponent, (int, float, complex)) else self.exponent.evaluate()
        base_value = self.base if isinstance(self.base, (int, float, complex)) else self.base.evaluate()
        return math.log(exponent_value, base_value)

    def latex(self):
        # extract the value of the components whether they are numbers or variables
        exponent_symbol = self.exponent if isinstance(self.exponent, (int, float, complex)) else self.exponent.latex()
        base_symbol = self.base if isinstance(self.base, (int, float, complex)) else self.base.latex()
        return "log_{}({})".format(base_symbol, exponent_symbol)

        
        
