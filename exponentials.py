import math

class exponential:
     # list of functionality
     
     # 1) multiply exp objects
     # 2) convert bases
     # 3) evaluate
     # 4) print latex
     

     def __init__(self, base, power):
         self.base = base
         self.power = power

     def __mul__(self, other):
         # multiply 2 exponential objects to return an exponential object
         # returning exponential object will have the same base as the LHS (self) exp

         # if bases are the same - just add the bases
         if self.base == other.base:
              return exponential(self.base, self.power+other.power)
          
         # create an exp object equivalent other but with the base of self
         same_base = exponential.change_base(other, self.base)

         # create the resulting exponential
         return exponential(self.base, self.power+same_base.power)
          
     def __eq__(self, other):
          # equality operator ==
          if not isinstance(other, (exponential)):
               return False
          return self.base == other.base and self.power == other.power
     
     def evaluate(self):
         # extract the value of the base whether its a number or variable
         base_value = self.base if isinstance(self.base, (int, float, complex)) else self.base.evaluate()
         power_value = self.power if isinstance(self.power, (int, float, complex)) else self.power.evaluate()
         return base_value**power_value


     def change_base(exp, new_base):
         # return an exponential object with the base of new_base
         # that is mathematically equivalent to the exponential object exp

         power_scaler = math.log(exp.base, new_base)
         
         # new power might be slightly off - even when exact value is calculatable
         # eg 2.0000000002 should be 2

         # log(exp.base, new_base) should return a clean int
         if exp.base % new_base == 0 or new_base % exp.base == 0:
              power_scaler = int(power_scaler)
         new_power = exp.power*power_scaler
         return exponential(new_base, new_power)

     def latex(self, explicit=False):
          # extract the value of the base whether its a number or variable
          base_symbol = self.base if isinstance(self.base, (int, float, complex)) else self.base.latex()
          power_symbol = self.power if isinstance(self.power, (int, float, complex)) else self.power.latex()
          if explicit:
               return "{}^{}".format(base_symbol, power_symbol)
          else:
               if self.power == 0:
                    return ""
               elif self.power == 1:
                    return "{}".format(base_symbol)
               else:
                    return "{}^{}".format(base_symbol, power_symbol)


               
