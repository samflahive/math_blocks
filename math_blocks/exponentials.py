from .math_block import math_block
import math
import copy

class exponential(math_block):
     
     def __init__(self, base, power):
         self.base = base
         self.power = power
         math_block.__init__(self, self.sign)
         
     def __mul__(self, other):
          if isinstance(other, exponential):
               if self.base == other.base:
                    return exponential(self.base, self.power+other.power)

               same_base = exponential.change_base(other, self.base)
               return exponential(self.base, self.power+same_base.power)
               
          elif isinstance(other, (int, float)):
               return product([self, other])
          else:
               return NotImplemented
     

     def __add__(self, other):
          pass
          
     
     def evaluate(self):
         # extract the value of the base whether its a number or variable
         base_value = self.base if isinstance(self.base, (int, float, complex)) else self.base.evaluate()
         power_value = self.power if isinstance(self.power, (int, float, complex)) else self.power.evaluate()
         val = base_value**power_value
         return val if self.sign else -val


     def latex(self, explicit=False):
          # extract the value of the base whether its a number or variable
          if isinstance(self.base, (int, float)):
               base_symbol = self.base
          else:
               lat = self.base.latex()
               
          power_symbol = self.power if isinstance(self.power, (int, float)) else self.power.latex()
          
          if explicit:
               out = "{}^{{{}}}".format(base_symbol, power_symbol)
          else:
               if self.power == 0:
                    out = ""
               elif self.power == 1:
                    out = "{}".format(base_symbol)
               else:
                    out = "{}^{{{}}}".format(base_symbol, power_symbol)

          out = object_sign(show_plus=show_plus, sign=self.sign)+out
          
          return out if self.sign else "-%s" % out


               
