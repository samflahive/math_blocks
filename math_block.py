from copy import deepcopy

class math_block:
         def __init__(self, sign):
                  self.sign = sign

         def __neg__(self):
                  new = deepcopy(self)
                  new.sign = not self.sign
                  return new

         def __radd__(self, other):
                  return self+other

         def __rmul__(self, other):
                  print(self.__class__.__name__, other.__class__.__name__)
                  return self*other
