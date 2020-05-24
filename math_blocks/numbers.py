from .math_block import math_block

class number(math_block):

         def __init__(self, value, sign=True):
                  implied_sign = value > 0
                  math_block.__init__(self, sign=(implied_sign == sign))

                  value = abs(value)
                  self.value = value

         def latex(self, explicit=False):
                  if not self.sign:
                           return "-{}".format(self.value)
                  return str(self.value)

         def evaluate(self):
                  if self.sign:
                           return self.value
                  return -self.value

                  
