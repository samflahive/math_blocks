import math_blocks
import math
import copy

class exponential(math_blocks.math_block):
     
     def __init__(self, base, power, sign=True):
          math_blocks.math_block.__init__(self, sign=sign)

          # replace python numbers with mathblock numbers
          if isinstance(base, (int, float)):
               base = math_blocks.number(base)
          if isinstance(power, (int, float)):
               power = math_blocks.number(power)
               
          self.base = base
          self.power = power

          
     
     def evaluate(self):
         # extract the value of the base whether its a number or variable
         base_value = self.base.evaluate()
         power_value = self.power.evaluate()
         val = base_value**power_value
         return val if self.sign else -val


     def latex(self, explicit=False, show_zero_power=True, show_plus=False):
          base_symbol = self.base.latex(explicit=explicit)
          if not self.base.sign or not isinstance(self.base, (math_blocks.number, math_blocks.variable)):
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

          if not self.sign:
               return "-%s" % out
          if show_plus:
               return "+%s" % out
          return out

     def __eq__(self, other):
          if not isinstance(other, exponential):
               return False
          return (self.base == other.base
                  and self.power == other.power
                  and self.sign == other.sign)

     def __mul__(self, other):
          if isinstance(other, exponential) and self.base == other.base:
               return exponential(self.base, self.power+other.power, sign=(self.sign == other.sign))                    
          return math_blocks.product([self, other])

     def __truediv__(self, other):
          if isinstance(other, exponential) and self.base == other.base:
               return exponential(self.base, self.power-other.power, sign=(self.sign == other.sign))
          return math_blocks.fraction(self, other)
               
