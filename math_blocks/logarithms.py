from .math_block import math_block
from .numbers import number
from .complex_numbers import complex_number

import math

class logarithm(math_block):
    
    def __init__(self, exponent, base, sign=True):
        math_block.__init__(self, sign=sign)

        self.eval_complex_flag = False
        
        if isinstance(base, (int, float)):
            base = number(base)
        elif isinstance(base, complex_number):
            self.eval_complex_flag = True
            
        if isinstance(exponent, (int, float)):
            exponent = number(exponent)
        elif isinstance(exponent, complex_number):
            self.eval_complex_flag = True
            
        self.exponent = exponent
        self.base = base


    def evaluate(self):
        if self.eval_complex_flag:
            raise ValueError("evaluated logarithms cannot contain complex numbers")
        
        exponent_value = self.exponent.evaluate()
        base_value = self.base.evaluate()
        value_out =  math.log(exponent_value, base_value)

        # correct value out for machine artifacts
        if exponent_value**round(value_out) == base_value:
            value_out = round(value_out)
        
        return value_out if self.sign else -value_out
    

    def latex(self, explicit=False):
        exponent_symbol = self.exponent.latex()
        base_symbol = self.base.latex()
        if explicit:
            out = "log_{%s}(%s)" % (base_symbol, exponent_symbol)
        else:
            out = "log_{%s}%s" % (base_symbol, exponent_symbol)
        if self.sign:
            return out
        return "-%s" % out
        
        
