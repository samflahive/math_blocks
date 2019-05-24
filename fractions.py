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
            new_subbers = [fraction(s,new_den) for s in new_num.subbers]
            return chain(adders=new_adders, subber=new_subbers, order=new_num.order)
        elif isinstance(new_num, polynomial):
            order = [[],[]]
            adders = []
            subbers = []
            for i,term in enumerate(new_num.terms):
                data = fraction(term.scale(abs(new_num.coeffs[i])), new_den)
                # adder
                if new_num.coeffs[i] >= 0:
                    adders.append(data)
                    order[0].append(i)
                # subber
                else:
                    subbers.append(data)
                    order[1].append(i)
            return chain(adders=adders, subbers=subbers, order=order)
        else:
            # cannot be split
            return fraction(new_num, new_den)
            
