from .number_formatting import number_coeff

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
