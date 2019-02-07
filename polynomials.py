"""
   The polynomial class is not intended to solve polynomial operations. Though it does offer limited functionality in that department.
   The purpose of this class is to organise the concept of a polynomial in a way that makes question development easier.
   
   The addition and multiplication operators do work (at least for simple polynomials) however they are not efficiently implemented.
   If a question involves subtracting one polynomial from another, add two polynomials and use the answer in the question.
   
   This is a trend throughout both this class and other math_blocks classes. If a question involves dividing, you should multiply and
   then reverse engineer the question. If you want a question to ask about the roots of a polynomial, create roots first, then construct
   your polynomial around them.

   The proper use of the functionality is generally to generate an answer and then reverse engineer the question.
   
   This is a simple learning tool - any other expectations will lead to unholy rage.

   - Sam Flahive 02/02/2019
   
"""




class polynomial:
   # coeffs is a list of numbers representing the coefficients of a polynomial: 1 number = 1 coefficient
   # variables (when in use) is a list of lists representing all the variables in the polynomial
   # powers is a list of lists representing all the powers of the polynomials variables

   # each of these lists must be the same length - the indices of each match the coeffs with its variables and variables with their powers
   
   # eg. coeffs = [1,2,3], variables = [["x"], ["x","y"], ["y"]], powers = [[2], [1,1], [2]]
   # = 1x^2 + 2x^1y^1 + 3y^2

   
   def __init__(self, coeffs=None, variables="x", powers=None):
      self.coeffs = coeffs
      self.variables = variables
      self.powers = powers
      self.roots_known = False
      self.roots_partial = False

   def __mul__(self, other):
      # multiply 2 polynomials
      
      # calculate the resulting coeffs
      coeffs = []
      # multiply each of the LHS coeffs by each of the RHS coeffs
      for coeff in other.coeffs:
         coeffs.extend(list(map(lambda x: x*coeff, self.coeffs)))

      # calculate the resulting variables
      variables = []
      for variable in other.variables:
         variables.extend(list(map(lambda x: copy_extend(x, variable), self.variables)))
      

      # calculate the resulting powers
      powers = []
      for power in other.powers:
         powers.extend(list(map(lambda x: copy_extend(x, power), self.powers)))
      poly = polynomial(coeffs=coeffs, variables=variables, powers=powers)
      poly.reduce()

      if self.roots_known and other.roots_known:
         poly.roots_known = True
         poly.roots = [self.roots[0]+other.roots[0], self.roots[1]+other.roots[1]]
      elif self.roots_known and other.roots_known:
         poly.roots_known = False
         poly.roots_partial = True
         poly.roots = self.roots if self.roots_known else other.roots_known
      else:
         poly.roots_known = False
         poly.roots_partial = False
      return poly    
      

   def __add__(self, other):
      # sum 2 polynomials

      coeffs = self.coeffs + other.coeffs
      variables = self.variables + other.variables
      powers = self.powers + other.powers

      poly = polynomial(coeffs=coeffs, variables=variables, powers=powers)
      poly.reduce()
      
      return poly

   def latex_coeffs(self):
      # returns a string that is the latex representation of this polynomial

      # the first term is handled seperately
      latex = str(self.coeffs[0]) if abs(self.coeffs[0]) != 1 else "" if self.coeffs[0] == 1 else "-"

      for index in range(len(self.variables[0])):
         latex += variable_format(self.variables[0][index], self.coeffs[0], self.powers[0][index])+power_format(self.powers[0][index], self.coeffs[0])

      # all other terms can be handled in a loop
      # loop through the terms of the polynomial
      for term_index in range(1,len(self.coeffs)):
         coeff = self.coeffs[term_index]
         latex += coeff_format(coeff)

         # loop through the variable/power pairs of the term
         for variable_index in range(len(self.variables[term_index])):
            
            variable = self.variables[term_index][variable_index]
            power = self.powers[term_index][variable_index]

            latex += variable_format(variable, coeff, power) + power_format(power, coeff)
            

      return latex
     

   def simplify_powers(self):
      # if a variable appears more than once with a coefficient
      # combine them to one variable - sum their powers
      new_powers = []
      # loop through each coefficient looking at their variables
      for outer_index in range(len(self.variables)):
         sub_variables = self.variables[outer_index]
         sub_powers = self.powers[outer_index]

         new_sub_variables = []
         new_sub_powers = []
         for inner_index in range(len(sub_variables)):
            target_variable = sub_variables[inner_index]
            target_power = sub_powers[inner_index]
            
            # not the first occurence of this variable at this coefficient
            if target_variable in new_sub_variables:
               # the index of this variable in the new variables list
               target_index = new_sub_variables.index(target_variable)
               # add to the power of this variable
               new_sub_powers[target_index]+=target_power

            else:
               new_sub_variables.append(target_variable)
               new_sub_powers.append(target_power)
               
         # replace the old variables and powers with the new
         self.variables[outer_index] = new_sub_variables
         self.powers[outer_index] = new_sub_powers


   def combine_coefficients(self):
      # if coefficients have the same variables with the same powers
      # they should be combined to a single coefficient - the sum
      delete_these = []
      # loop through each coeff
      for current_index in range(len(self.coeffs)):
         # loop through all coeffs after the current one
         for later_index in range(current_index+1,len(self.coeffs)):
            # compare the current coeff variables to the ones after it
            if equivalent_variables(self.variables[current_index],
                                    self.variables[later_index],
                                    self.powers[current_index],
                                    self.powers[later_index]):
               # merge the later term into the first occurence (current)
               self.coeffs[current_index]+=self.coeffs[later_index]
               # delete the term that has been merged into the first occurence
               # TO DO
               delete_these.append(later_index)
      # delete all merged terms - DOING THIS IN THE LOOP WOULD BE BETTER - REMOVE THIS LATER
      # TO DO
      index_update = 0
      for delete in delete_these:
         del self.coeffs[delete-index_update]
         del self.variables[delete-index_update]
         del self.powers[delete-index_update]
         index_update+=1


   def reduce(self):
      # eliminate repetitve terms
      # for example 4x^2x^1 - 3x^3 becomes 1x^3

      # 4x^2x^1 - 3x^3 becomes 4x^3 - 3x^3
      self.simplify_powers()
      # 4x^3 - 3x^3 becomes 1x^3
      self.combine_coefficients()
      

   def poly_roots(self):
      # return the roots of a polynomial
      # format [[variable, value], [variable, value]]
      # eg. [["x", 3], ["x", 2], ["y", -6]]

      # the roots are already known
      if self.roots_known:
         return poly_root_restructure(self.roots)
      # the roots are not known
      else:
         # THIS CASE SHOULD NEVER OCCUR
         return [1,2,3,4]
      
      
   def evaluate(self, values):
      # values is a dictionary holding the values of each variable
      # eg. values = {"x":2, "y":4.5}
      # evaluate the polynomials at the given variable values

      running_total = 0

      # go through all the terms of the poly
      for term_index in range(len(self.coeffs)):
         term_total = self.coeffs[term_index]

         # multiply the coefficient of the term by the variables (evaluated) at their given power
         for variable_index in range(len(self.variables[term_index])):
            term_total *= values[self.variables[term_index][variable_index]]**self.powers[term_index][variable_index]

         # sum all the term values
         running_total += term_total

      return running_total
         


   def from_roots(roots, variables="x"):
      # calculate the coefficients of a polynomial based on its roots
      # convert each root into a factor (a polynomial)
      # multuply all these factors together
      
      if type(variables) is str:
        variables = [variables for _ in roots]

      poly = polynomial.root_to_factor(roots[0], variables[0])
      for i in range(1, len(roots)):
         poly = poly*polynomial.root_to_factor(roots[i], variables[i])
      
      # save the roots as an object attribute for easy access later
      poly.roots_known = True
      poly.roots_data = [roots, variables]

      return poly
   
   def root_to_factor(root, variable):
      # root is a number 4
      # variable is a string eg. "x"
      # want to create a polynomial object representing x-4
      coeffs = [1, -root]
      powers = [[1], [0]]
      variables = [[variable], [variable]]
      return polynomial(coeffs=coeffs, variables=variables, powers=powers)
      
def coeff_format(number, explicit=False):
   # returns a string representation of a polynomial's coefficient
   
   # explicit means that 1s are shown
   if number > 0:
      if number != 1 or explicit:
         return "+{}".format(number)
      else:
         return "+"
   elif number < 0:
      if number != -1 or explicit:
         return str(number)
      else:
         return "-"
   else:
      return ""
      
def power_format(power, coeff, explicit=False):
   # returns a string representation of a polynomial's variable's power
   if (power !=1 and power !=0 and coeff != 0) or explicit:
      return "^{}".format(power)
   else:
      return ""


def variable_format(variable, coeff, power, explicit=False):
   # returns a string representation of a polynomial's variable's

   if (coeff != 0 and power != 0) or explicit:
      return variable
   else:
      return ""

def copy_extend(copy, extend):
   copied = list(copy)
   copied.extend(extend)
   return copied

def equivalent_variables(varA, varB, powA, powB):
   # returns true if the variables are equivalent - same values in varA and varB aswell as the same corresponding powers
   # otherwise false
   multi_array_order(varA, powA)
   multi_array_order(varB, powB)

   return (varA == varB and powA == powB)
   
def multi_array_order(A,B):
   # order the list A usinf bubblesort
   # rearrange the list B in the same way as A
   # ie. if the value at A[3] has been moved to A[7] then B[3] should be moved to B[7]

   # Swap the elements to arrange in order
   for iter_num in range(len(A)-1,0,-1):
      for idx in range(iter_num):
         if A[idx]>A[idx+1]:
            
            tempA = A[idx]
            tempB = B[idx]
            
            A[idx] = A[idx+1]
            B[idx] = B[idx+1]
            
            A[idx+1] = tempA
            B[idx+1] = tempB

test_poly = polynomial(coeffs=[1, -1, 2, 3, 0, 4],
                       variables=[["x","y"], ["x"], ["y","x"], ["y"], ["x"], ["y"]],
                       powers=[[2,3],[1], [0,1], [3], [2], [4]])
