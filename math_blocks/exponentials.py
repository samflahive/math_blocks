from .math_block import math_block
from .numbers import number
from .variables import variable
import math
import copy

class exponential(math_block):
     
     def __init__(self, base, power, sign=True):
          math_block.__init__(self, sign=sign)

          # replace python numbers with mathblock numbers
          if isinstance(base, (int, float)):
               base = number(base)
          if isinstance(power, (int, float)):
               power = number(power)
               
          self.base = base
          self.power = power

          
     
     def evaluate(self):
         # extract the value of the base whether its a number or variable
         base_value = self.base.evaluate()
         power_value = self.power.evaluate()
         val = base_value**power_value
         return val if self.sign else -val


     def latex(self, explicit=False, show_zero_power=True):
          base_symbol = self.base.latex(explicit=explicit)
          if not self.base.sign or not isinstance(self.base, (number, variable)):
               base_symbol = "(%s)" % base_symbol
               
          power_symbol = self.power.latex(explicit=explicit)
          
          if explicit:
               out = "{}^{{{}}}".format(base_symbol, power_symbol)
          else:
               if self.power == 0:
                    out = "1" if show_zero_power else ""
               elif self.power == 1:
                    out = "{}".format(base_symbol)
               else:
                    out = "{}^{{{}}}".format(base_symbol, power_symbol)

          return out if self.sign else "-%s" % out


               
