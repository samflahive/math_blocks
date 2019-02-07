import math

class exponential:
         # list of functionality
         
         # 1) multiply exp objects
         # 2) convert bases
         # 3) evaluate
         

         def __init__(self, base, power):
                  self.base = base
                  self.power = power

         def __mul__(self, other):
                  # multiply 2 exponential objects to return an exponential object
                  # returning exponential object will have the same base as the LHS (self) exp

                  # create an exp object equivalent other but with the base of self
                  same_base = exponential.change_base(other, self.base)

                  # create the resulting exponential
                  return exponential(self.base, self.power+same_base.power)

         def evaluate(self):
                  return self.base**self.power


         def change_base(exp, new_base):
                  # return an exponential object with the base of new_base
                  # that is mathematically equivalent to the exponential object exp

                  new_power = exp.power*math.log(exp.base, new_base)
                  return exponential(exp.base, new_power)
