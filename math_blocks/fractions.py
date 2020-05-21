from .math_block import math_block
from .number_formatting import number_coeff, object_sign
from .polynomials import polynomial
from .chains import chain
from .complex_numbers import complex_number
import copy

class fraction(math_block):
    def __init__(self, num, den, sign=True):
        # num is the fraction numerator
        # den is the fraction denominator
        self.numerator = num
        self.denominator = den
        math_block.__init__(self, sign=sign)
        

    def __add__(self, other):
        if isinstance(other, fraction) and self.denominator == other.denominator:
            return fraction(self.numerator+other.numerator, self.denominator)
        return chain([self, other])

    def __sub__(self, other):
        if isinstance(other, fraction) and self.denominator == other.denominator:
            return fraction(self.numerator-other.numerator, self.denominator)
        return chain([self, -other])
    
    def __mul__(self, other):
        if isinstance(other, (int,float, complex_number)):
                           return fraction(self.numerator*other, self.denominator)
        
        elif isinstance(other, fraction):
                           return fraction(self.numerator*other.numerator, self.denominator*other.denominator)

        return NotImplemented

    def __truediv__(self, other):
        return fraction(self.numerator, self.denominator*other)
    
    def evaluate(self):
        """
        calculate the value of this fraction at current variable values
        return number
        """
        num_val = self.numerator if isinstance(self.numerator, (int, float, complex)) else self.numerator.evaluate()
        den_val = self.denominator if isinstance(self.denominator, (int, float, complex)) else self.denominator.evaluate()

        val = num_val/den_val
        return val if self.sign else -val
    
    def latex(self, explicit=False, show_plus=False):
        """
        return the latex format of this fraction
        """
        if isinstance(self.numerator, (int, float, complex)):
            num_latex = number_coeff(self.numerator , 0, explicit=explicit, one_special=True)
        else:
            num_latex = self.numerator.latex(explicit=explicit)
        if isinstance(self.denominator, (int, float, complex)):
            den_latex = number_coeff(self.denominator , 0, explicit=explicit, one_special=True)
        else:
            den_latex = self.denominator.latex(explicit=explicit)

        out = r"\frac{{{0}}}{{{1}}}".format(num_latex, den_latex)
        out = object_sign(show_plus=show_plus, sign=self.sign)+out
        return out

    def split_numerator(self):
        """
        break down the fractions into a sum of fractions with the same denominator
        return chain
        """

        new_num = copy.deepcopy(self.numerator)
        new_den = copy.deepcopy(self.denominator)
        # two types of numerator are supported - polynomials and chains
        
        if isinstance(new_num, chain):
            new_adders = [fraction(a,new_den) for a in new_num.items]
            return chain(items=items)
        elif isinstance(new_num, polynomial):
            items = []
            for i,term in enumerate(new_num.terms):
                data = fraction(polynomial(coeffs=[abs(new_num.coeffs[i])], terms=[term]),
                                new_den)
                items.append(data)
            return chain(items=items)
        else:
            # cannot be split
            return self

    def inherent_sign(self):
        num_sign = self.numerator >= 0 if isinstance(self.numerator, (int, float, complex)) else self.numerator.sign
        den_sign = self.denominator >= 0 if isinstance(self.denominator, (int, float, complex)) else self.denominator.sign
        sign = num_sign == den_sign
        if not num_sign:
            self.numerator = -self.numerator
        if not den_sign:
            self.denominator = -self.denominator
        self.sign = sign
            
