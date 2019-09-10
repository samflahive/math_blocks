from random import randint
class numberGenerator:
         def __init__(self, low, high, avoid, unique=False):
                  self.low = low
                  self.high = high
                  self.avoid = avoid
                  self.unique = unique
                  
         def create(self, max_attempts=20):
                  for i in range(max_attempts):
                           num = randint(self.low,  self.high)
                           if not num in self.avoid:
                                    if self.unique:
                                             self.avoid.append(num)
                                    
                                    return num
                  raise Exception("this number could not be generated in {} attempts".format(max_attempts))

         def create_many(self, many, max_attempts=20):
                  return [self.create(max_attempts) for i in range(many)]
