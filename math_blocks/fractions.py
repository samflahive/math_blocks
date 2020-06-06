import math_blocks

class fraction(math_blocks.math_block):
    def __init__(self, numerator, denominator, sign=True):
        math_blocks.math_block.__init__(self, sign=sign)

        if isinstance(numerator, (int, float)):
            numerator = math_blocks.number(numerator)
        if isinstance(denominator, (int, float)):
            denominator = math_blocks.number(denominator)

        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self):
        val = self.numerator.evaluate() / self.denominator.evaluate()
        if self.sign:
            return val
        return -val

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return "-\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))
        if show_plus:
            return "+\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))
        return "\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))


    def __eq__(self, other):
        if not isinstance(other, fraction):
            return False

        return (self.denominator == other.denominator
                and self.numerator == other.numerator
                and self.sign == other.sign)


    def __add__(self, other):
        if isinstance(self, fraction) and (self.denominator == other.denominator()):
            other_num = other.numerator if (other.sign == self.sign) else -other.numerator
            return fraction(self.numerator+other_num, self.denominator)
        return math_blocks.chain([self, other])
        

    # def __mul__(self, other): need to implement equality operators
