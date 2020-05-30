import math_blocks

class complex_number(math_blocks.math_block):

    def __init__(self, real, imaginary, sign=True):
        math_blocks.math_block.__init__(self, sign=sign)

        if isinstance(real, (int, float)):
            real = math_blocks.number(real)
        if isinstance(imaginary, (int, float)):
            imaginary = math_blocks.number(imaginary)

        self.real = real
        self.imaginary = imaginary

    def evaluate(self):
        val = complex(self.real.evaluate(), self.imaginary.evaluate())
        if self.sign:
            return val
        return -val

    def latex(self, explicit=False, show_plus=False):
        bracket_imag = False
        if isinstance(self.real, (math_blocks.number, math_blocks.variable)):
            real_latex = self.real.latex()
        else:
            real_latex = "(%s)" % self.real.latex()

        if isinstance(self.imaginary, (math_blocks.number, math_blocks.variable)):
            imaginary_latex = self.imaginary.latex()
        else:
            bracket_imag = True
            imaginary_latex = "(%s)" % self.imaginary.latex()

        if self.imaginary.sign or bracket_imag:
            out = "%s+%si" % (real_latex, imaginary_latex)
        else:
            out = "%s%si" % (real_latex, imaginary_latex)

        if not self.sign:
            return "-(%s)" % out
        if show_plus:
            return "+(%s)" % out
        return out


