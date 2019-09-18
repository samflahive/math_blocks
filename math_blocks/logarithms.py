from .math_block import math_block
from .chains import chain
from .products import product
from .polynomials import polynomial
from .exponentials import exponential
from .fractions import fraction
import math
from .number_formatting import object_sign

class logarithm(math_block):
    # list of functionality
    # 1) add and subtract
    # 2) division and multiplication
    # 3) latex print
    # 4) evaluate
    
    def __init__(self, exponent, base, sign=True):
        self.exponent = exponent
        self.base = base
        self.sign = sign
        math_block.__init__(self, sign=sign)
        
    def __add__(self, other):
        if not isinstance(other, logarithm) or self.base != other.base:
            return chain([self, other])
        return logarithm(self.exponent*other.exponent, self.base)

    def __sub__(self, other):
        if not isinstance(other, logarithm) or self.base != other.base:
            return chain([self, -other])
        new_expo = self.exponent/other.exponent if self.exponent%other.exponent != 0 else int(self.exponent/other.exponent)
        return logarithm(new_expo, self.base)

    def __truediv__(self, other):
        if isinstance(other, logarithm) and (self.base == other.base or self.exponent == other.exponent):
            if self.base == other.base:
                # log_b(Y)/log_b(X) = log_X(Y)
                return logarithm(self.exponent, other.exponent)
            else:
                # log_b(Y)/log_x(Y) = log_b(X)
                return logarithm(other.base, self.base)

        return fraction(self, other)
        
        
        

    def __mul__(self, other):
        if isinstance(other, logarithm) and (other.exponent == self.base or self.exponent == other.base):
            
            if self.exponent == other.base:
                return logarithm(other.exponent, self.base)
            else:
                return logarithm(self.exponent, other.base)
        else:
            return product([self, other])

    def evaluate(self):
        # extract the value of the base whether its a number or variable
        exponent_value = self.exponent if isinstance(self.exponent, (int, float, complex)) else self.exponent.evaluate()
        base_value = self.base if isinstance(self.base, (int, float, complex)) else self.base.evaluate()
        value_out =  math.log(exponent_value, base_value)

        # correct value out for machine artifacts
        if exponent_value**round(value_out) == base_value:
            value_out = round(value_out)
        
        return value_out if self.sign else -value_out
    

    def latex(self, explicit=False, show_plus=False):
        # extract the value of the components whether they are numbers or variables
        exponent_symbol = self.exponent if isinstance(self.exponent, (int, float, complex)) else self.exponent.latex()
        base_symbol = self.base if isinstance(self.base, (int, float, complex)) else self.base.latex()
        if explicit:
            out = "log_{{({})}}({})".format(base_symbol, exponent_symbol)
        else:
            out = "log_{{{}}}({})".format(base_symbol, exponent_symbol)
        out = object_sign(show_plus=show_plus, sign=self.sign)+out
        return out
        
        
