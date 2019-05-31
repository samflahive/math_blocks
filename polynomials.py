import copy
from .poly_terms import poly_term
from .exponentials import exponential
from .number_formatting import number_coeff

class polynomial:
   
   # functionality
   # 1) create polynomial from coeffs
   # 2) add and multiply two polynomials
   # 3) evaluate polynomials
   # 4) simplify polynomials
   # 5) latex polynomials in coeffs form
   # 6) latex polynomials in factors form
   # 7) create polynomial from roots

   def __init__(self, coeffs, terms, print_style="coeffs"):
      # coeffs is a list of number and math-block objects
      self.coeffs = coeffs
      # each argument of polynomial is a list or a product
      self.terms = list(map(lambda x : poly_term(*x) if isinstance(x, (list)) else x, terms))
      self.roots_known = False
      self.sign = (coeffs[0] >= 0) if isinstance(coeffs[0], (int, float, complex)) else coeffs[0].sign
      self.print_style = print_style


   def __add__(self, other):
      coeffs = self.coeffs+other.coeffs
      terms = self.terms+other.terms
      return polynomial(coeffs=coeffs, terms=terms)

   def __mul__(self, other):
      # poly * number
      if isinstance(other, (int, float, complex)):
         return polynomial.scale(self, other)
         
      # poly * poly
      # combine the roots
      if self.roots_known and other.roots_known:
         roots = self.roots + other.roots
         return polynomial.from_roots(roots)

      # dont know the roots - have to use the terms
      else:
         new_coeffs = []
         new_terms = []
         # multiply each left hand side (lhs) term by each right hand side term
         for lhs_term_index in range(len(self.terms)):
            
            lhs_term = self.terms[lhs_term_index]
            lhs_coeff = self.coeffs[lhs_term_index]
            for rhs_term_index in range(len(other.terms)):
               rhs_term = other.terms[rhs_term_index]
               rhs_coeff = other.coeffs[rhs_term_index]
               # calculate
               result_coeff = lhs_coeff*rhs_coeff
               result_term = lhs_term*rhs_term
               # fix the order
               result_term.arrange()
               new_coeffs.append(result_coeff)
               new_terms.append(result_term)
         
         return polynomial(coeffs=new_coeffs, terms=new_terms)
               
   def __eq__(self, other):
      # assume that both polynomials have already been reduced

      index_conversion = []
      try:
         # loop through coeffs of self
         for coeff in self.coeffs:
            # try find it in other.coeffs
            try:
               index = other.coeffs.index(coeff)
            except ValueError as valEr:
               # the coeff could not be found in other.coeffs - not a match
               return False
            index_conversion.append(index)
      except AttributeError as AtEr:
         # likely other does not have .coeffs --> not polynomial
         return False
      find_index = 0
      # loop through terms of self
      for term in self.terms:
         if term != other.terms[index_conversion[find_index]]:
            return False
         find_index += 1
      return True         
      
      

   def evaluate(self):
      summing = 0
      for index in range(len(self.coeffs)):
         term_val = self.terms[index].evaluate()
         coeff_val = self.coeffs[index] if isinstance(self.coeffs[index], (int, float, complex)) else self.coeffs[index].evaluate()
         summing += (coeff_val*term_val)
      return summing
	  
   def remove_zeros(self):
      """
      remove coeffs and terms corresponding to zero value coefficients
      """
      index = 0
      while index < len(self.coeffs):
         # remove this coeff and term
         if self.coeffs[index] == 0:
            del self.coeffs[index]
            del self.terms[index]
         else:
            index += 1
      self.sign = (self.coeffs[0] >= 0)

   def replace_coeffs_by_value(self):
      """
      replace all non number coefficients with the number of their current value
      return polynomial
      """
      new_terms = copy.deepcopy(self.terms)
      new_coeffs = list(map(lambda coeff: coeff if isinstance(coeff, (int,float,complex)) else coeff.evaluate(), self.coeffs))

      return polynomial(coeffs=new_coeffs, terms=new_terms)
      
   def reduce(self):
      # 2 steps
      # 1) combine exponentials within a term that have the same base
      # 2) combine terms that have use the same variables (and no others)

      for term in self.terms:
         # 1)
         term.reduce()

   def term_latex(self, index, explicit=False):
      """
      latex for a specifc term in a polynomial, eg. 4*x^2*y^3
      explicit=True should show all coeffs, bases, and powers no matter their value
      explicit=False should show the most natural way it would be written:
         coefficient of 1 should not be shown, unless no variables follow, eg. +1 is ok, +1x^4 should just be +x^4
         coefficient of 0 should mean the enitre term is ignored
         
      """
      
      if self.coeffs[index] == 0:
         return ""

      var_latex = self.terms[index].latex(explicit=explicit)
      # bool to determine explicity
      exp_boo = (explicit or (var_latex == "" and index != 0))
      if isinstance(self.coeffs[index], (int, float, complex)):
         coeff_latex  = number_coeff(self.coeffs[index], index, explicit=exp_boo)
      else:
         coeff_latex = "{0}({1})".format("+" if index != 0 else "", self.coeffs[index].latex())
      
      return "{}{}".format(coeff_latex, var_latex)

   def latex(self, explicit=False):
      # return a string containing a latex expression of this polynomial

      if self.print_style == "coeffs":
         latex = ""
         # loop through coeffs/values
         for index in range(len(self.coeffs)):
            latex += self.term_latex(index, explicit)
         return latex
      else:
         return self.factor_latex()

   def factor_latex(self):
      return "({})".format(")(".join([polynomial.root_to_factor(root).latex() for root in self.roots]))


   @staticmethod
   def from_roots(roots):
      # create a polynomial that represents a factor for the first root
      poly = polynomial.root_to_factor(roots[0])
      
      # create a polynomial factor for each subsequent root and multiply it to the existing one
      for root in roots[1:]:
         poly*=polynomial.root_to_factor(root)
      poly.roots_know = True
      poly.roots = roots
      #poly.reduce()
      return poly

   @staticmethod
   def root_to_factor(root):
      # root is a tuple or list of a variable and value, eg (x, 4)
      # this means x at the value of 4 is a root of some polynomial
      # this function turns the root into a factor and returns it as a polynomial object
      # eg. x - 4
      # 1, -4
      coeffs = [1, -root[1]]
      # x, 1
      terms = [[exponential(root[0], 1)], [exponential(root[0], 0)]]
      
      # 1*x^1 -4*x^0
      return polynomial(coeffs=coeffs, terms=terms)

   @staticmethod
   def scale(poly, number):
      coeffs = list(map(lambda x: x*number, poly.coeffs))
      # clone the terms
      terms = copy.deepcopy(poly.terms)
      return polynomial(coeffs=coeffs, terms=terms)

   def derivative(self, var):
      """
      derivative of polynomial with respect to a variable
      return polynomial
      """
      der_coeffs = []
      der_terms = []
      # loop through the terms
      for index,term in enumerate(self.terms):
         deriv = term.derivative(var)
         # move numbers in the term to their matching coefficient
         scalar = deriv.terms[-1]
         if scalar != 0:
            # remove number from the term
            del deriv.terms[-1]
            # add derivative to new polynomial
            der_coeffs.append(self.coeffs[index]*scalar)
            der_terms.append(deriv)
      return polynomial(der_coeffs, der_terms)
