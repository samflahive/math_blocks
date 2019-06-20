from .math_block import math_block
from .number_formatting import number_coeff
import math

class complex_number(math_block):
         def __init__(self, real, imag):
                  self.real = real
                  self.imag = imag
                  self.form = "rect"
                  self.sign = True
                  self.angle = None
                  self.modulus = None
                  math_block.__init__(self, sign=self.sign)

         def __mul__(self, other):
                  if isinstance(other, complex_number):
                           if self.form == "rect":
                                    real = self.real*other.real - self.imag*other.imag
                                    imag = self.real*other.imag + self.imag*other.real
                                    return complex_number(real, imag)
                           else:
                                    modulus = self.modulus*other.modulus
                                    angle = self.angle+other.angle
                                    return complex_number.from_polar(modulus, angle)
                           
                  elif isinstance(other, (int, float)):
                                  return complex_number(self.real*other, self.imag*other) if self.form == "rect" else complex_number.from_polar(self.modulus*other, self.angle)

                  raise Exception("Complex numbers can currently only be multiplied by other complex numbers or numbers")

         def __rmul__(self, other):
                  return self*other

         def __add__(self, other):
                  if isinstance(other, (int, float)):
                           o_real = other
                           o_imag = 0
                  elif isinstance(other, complex_number):
                           o_real = other.real
                           o_imag = other.imag

                  else:
                           raise Exception("Complex numbers can currently only be added to other complex numbers or numbers")
                           
                  if self.form == "rect":
                           s_real = self.real
                           s_imag = self.imag
                  

                  return complex_number(s_real+o_real, s_imag+o_imag)

         def __radd__(self, other):
                  return self+other
         
         def polar_form(self):
                  if self.form == "polar":
                           return self
                  return complex_number.from_polar(math.hypot(self.real, self.imag), math.atan2(self.imag, self.real))

         def latex(self, explicit=False, show_plus=False):
                  if self.form == "rect":
                           real_latex = number_coeff(self.real, index=0, one_special=False) if isinstance(self.real, (int, float)) else self.real.latex(explicit=explicit)
                           imag_latex = number_coeff(self.imag, index=0, explicit=True) if isinstance(self.imag, (int, float)) else self.imag.latex(explicit=explicit, show_plus=real_latex!="")
                           return "{}{}i".format(real_latex, imag_latex)
                  else:
                           return "{0}(\cos{1}+i\sin{1})".format(self.modulus, self.angle)


         def evaluate(self):
                  real_val = self.real if isinstance(self.real, (int, float)) else self.real.evaluate()
                  imag_val = self.imag if isinstance(self.real, (int, float)) else self.real.evaluate()
                  return complex(real_val, imag_val)

         @staticmethod
         def from_polar(modulus, angle):
                  ans = complex_number(modulus*math.cos(angle), modulus*math.sin(angle))
                  ans.angle = angle
                  ans.modulus = modulus
                  ans.form = "polar"
                  return ans
