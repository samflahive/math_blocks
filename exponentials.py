from .math_block import math_block
from .chains import chain
from .products import product
import math
import copy
from .number_formatting import object_sign

class exponential(math_block):
     
     def __init__(self, base, power):
         print_conditions = "open"
         self.base = base
         self.power = power
         self.print_conditions = print_conditions
         self.sign = True
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
          return chain([self, other])
          
     def __eq__(self, other):
          return isinstance(other, (exponential)) and self.base == other.base and self.power == other.power
     
     def evaluate(self):
         # extract the value of the base whether its a number or variable
         base_value = self.base if isinstance(self.base, (int, float, complex)) else self.base.evaluate()
         power_value = self.power if isinstance(self.power, (int, float, complex)) else self.power.evaluate()
         val = base_value**power_value
         return val if self.sign else -val

     @staticmethod
     def change_base(exp, new_base):

         power_scaler = math.log(exp.base, new_base)
         
         if exp.base % new_base == 0 or new_base % exp.base == 0:
              power_scaler = int(power_scaler)
         new_power = exp.power*power_scaler
         return exponential(new_base, new_power)

     def latex(self, explicit=False, show_plus=False):
          # extract the value of the base whether its a number or variable
          if isinstance(self.base, (int, float)):
               base_symbol = self.base
          else:
               lat = self.base.latex()
               base_symbol = "({})".format(lat) if self.base.bracketed else lat
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
          
          if self.print_conditions == "open":
               return out
          else:
               return "({})".format(out)


               
