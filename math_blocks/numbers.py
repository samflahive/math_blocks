from .math_block import math_block

class number(math_block):

         def __init__(value, sign=True):
                  implied_sign = value > 0
                  math_block.__init__(self, sign=(implied_sign and sign))

                  value = abs(value)
                  self.value = value

         def latex(self, explicit=False):
                  sign = "+" if self.sign else "-"
                  return "{}{}".format(sign, self.value)

         def evaluate(self):
                  if self.sign:
                           return self.value
                  return -self.value

                  
