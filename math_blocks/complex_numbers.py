from .math_block import math_block
from .numbers import number
from .variables import variable

class complex_number(math_block):

         def __init__(self, real, imaginary, sign=True):
                  math_block.__init__(self, sign=sign)

                  if isinstance(real, (int, float)):
                           real = number(real)
                  if isinstance(imaginary, (int, float)):
                           imaginary = number(imaginary)

                  self.real = real
                  self.imaginary = imaginary

         def evaluate(self):
                  val = complex(self.real.evaluate(), self.imaginary.evaluate())
                  if self.sign:
                           return val
                  return -val

         def latex(self, explicit=False):
                  bracket_imag = False
                  if isinstance(self.real, (number, variable)):
                           real_latex = self.real.latex()
                  else:
                           real_latex = "(%s)" % self.real.latex()

                  if isinstance(self.imaginary, (number, variable)):
                           imaginary_latex = self.imaginary.latex()
                  else:
                           bracket_imag = True
                           imaginary_latex = "(%s)" % self.imaginary.latex()

                  if self.imaginary.sign or bracket_imag:
                           out = "%s+%si" % (real_latex, imaginary_latex)
                  else:
                           out = "%s%si" % (real_latex, imaginary_latex)

                  if self.sign:
                           return out
                  return "-(%s)" % out
