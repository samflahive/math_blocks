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
        if isinstance(other, fraction) and (self.denominator == other.denominator):
            other_num = other.numerator if (other.sign == self.sign) else -other.numerator
            return fraction(self.numerator+other_num, self.denominator)
        return math_blocks.chain([self, other])
        

    def __mul__(self, other):
        if isinstance(other, fraction):
            return fraction(numerator=self.numerator*other.numerator,
                            denominator=self.denominator*other.denominator,
                            sign=(self.sign==other.sign))
        return math_blocks.product([self, other])

    def split(self):
        if isinstance(self.numerator, (math_blocks.chain, math_blocks.product)):
            items = [fraction(item,
                              self.denominator,
                              sign=(self.numerator.sign == item.sign)) for item in self.numerator.items]
            
            if isinstance(self.numerator, math_blocks.chain):
                return math_blocks.chain(items=items, sign=self.sign)
            else:
                return math_blocks.product(items=items, sign=self.sign)

        elif isinstance(self.numerator, math_blocks.complex_number):
            real = fraction(self.numerator.real, self.denominator)
            imaginary = fraction(self.numerator.imaginary, self.denominator)
            return math_blocks.complex_number(real=real,  imaginary=imaginary, sign=(self.sign==self.numerator.sign))
        error_message = f"fractionc can only be split when the numerator is type chain (including children), product, or complex_number - not {type(self.numerator)}."
        raise ValueError(error_message)
