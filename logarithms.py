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
        if self.base != other.base:
            raise ValueError("Logarithm objects must have the same base to be summed.")
        return logarithm(self.exponent*other.exponent, self.base)

    def __sub__(self, other):
        # subtract one logarithm object from another
        # log_x(Y) - log_x(Z) = log_x(Y/Z)
        new_expo = self.exponent/other.exponent if self.exponent%other.exponent != 0 else int(self.exponent/other.exponent)
        return logarithm(new_expo, self.base)

    def __truediv__(self, other):
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

    def __mul__(self, other):
        # multiply two logarithm objects
        # if the base of one is the exponent of the other eg. X
        # the result is the non X base and non X exponent

        # required condition
        if self.exponent == other.base:
            return logarithm(other.exponent, self.base)
        elif other.exponent == self.base:
            return logarithm(self.exponent, other.base)
        raise ValueError("The base of one log must be the exponent of the other, to multiply the two")

    def evaluate(self):
        # extract the value of the base whether its a number or variable
        exponent_value = self.exponent if isinstance(self.exponent, (int, float, complex)) else self.exponent.evaluate()
        base_value = self.base if isinstance(self.base, (int, float, complex)) else self.base.evaluate()
        value_out =  math.log(exponent_value, base_value)

        # correct value out for machine artifacts
        if exponent_value**round(value_out) == base_value:
            return round(value_out)
        
        return value_out
        

    def latex(self):
        # extract the value of the components whether they are numbers or variables
        exponent_symbol = self.exponent if isinstance(self.exponent, (int, float, complex)) else self.exponent.latex()
        base_symbol = self.base if isinstance(self.base, (int, float, complex)) else self.base.latex()
        return "log_{{{}}}({})".format(base_symbol, exponent_symbol)

        
        
