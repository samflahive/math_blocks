from .number_formatting import number_coeff
from .polynomials import polynomial
from .chains import chain
import copy

class fraction:
    def __init__(self, num, den):
        # num is the fraction numerator
        # den is the fraction denominator
        self.numerator = num
        self.denominator = den
        num_sign = num > 0 if isinstance(num, (int, float, complex)) else num.sign
        den_sign = den > 0 if isinstance(den, (int, float, complex)) else den.sign
        self.sign = num_sign == den_sign

    def evaluate(self):
        """
        calculate the value of this fraction at current variable values
        return number
        """
        num_val = self.numerator if isinstance(self.numerator, (int, float, complex)) else self.numerator.evaluate()
        den_val = self.denominator if isinstance(self.denominator, (int, float, complex)) else self.denominator.evaluate()

        return num_val/den_val

    def latex(self, explicit=False):
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

        return r"\frac{{{0}}}{{{1}}}".format(num_latex, den_latex)

    def split_numerator(self):
        """
        break down the fractions into a sum of fractions with the same denominator
        return chain
        """

        new_num = copy.deepcopy(self.numerator)
        new_den = copy.deepcopy(self.denominator)
        # two types of numerator are supported - polynomials and chains
        if isinstance(new_num, chain):
            new_adders = [fraction(a,new_den) for a in new_num.adders]
            return chain(adders=new_adders)
        elif isinstance(new_num, polynomial):
            adders = []
            for i,term in enumerate(new_num.terms):
                data = fraction(polynomial(coeffs=[abs(new_num.coeffs[i])], terms=[term]), new_den)
                adders.append(data)
            return chain(adders=adders, subbers=subbers, order=order)
        else:
            # cannot be split
            return fraction(new_num, new_den)
            
