import copy
import variables
from poly_terms import poly_term
import exponentials
import number_formatting

class polynomial:
   # functionality
   # 1) create polynomial from coeffs
   # 2) add and multiply two polynomials
   # 3) evaluate polynomials
   # 4) simplify polynomials
   # 5) latex polynomials in coeffs form
   # 6) latex polynomials in factors form
   # 7) create polynomial from roots

   def __init__(self, coeffs, terms):
      # coeffs is a list of number and math-block objects
      self.coeffs = coeffs
      # each argument of polynomial is a list or a product
      self.terms = list(map(lambda x : poly_term(*x) if isinstance(x, (list)) else x, terms))
      self.roots_known = False


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
               
         

   def evaluate(self):
      summing = 0
      for index in range(len(self.coeffs)):
         term_val = self.terms[index].evaluate()
         coeff_val = self.coeffs[index] if isinstance(self.coeffs[index], (int, float, complex)) else self.coeffs[index].evaluate()
         summing += (coeff_val*term_val)
      return summing

   def reduce(self):
      # 2 steps
      # 1) combine exponentials within a term that have the same base
      # 2) combine terms that have use the same variables (and no others)

      for term in self.terms:
         # 1)
         term.reduce()

   def latex(self):
      # return a string containing a latex expression of this polynomial

      latex = ""
      # loop through coeffs/values
      for index in range(len(self.coeffs)):
         term_latex = "{}{}".format(number_formatting.number_coeff(self.coeffs[index], index), self.terms[index].latex())
         latex += term_latex
      return latex
   
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

   def root_to_factor(root):
      # root is a tuple or list of a variable and value, eg (x, 4)
      # this means x at the value of 4 is a root of some polynomial
      # this function turns the root into a factor and returns it as a polynomial object
      # eg. x - 4
      # 1, -4
      coeffs = [1, -root[1]]
      # x, 1
      terms = [[exponentials.exponential(root[0], 1)], [exponentials.exponential(root[0], 0)]]
      # 1*x^1 -4*x^0
      return polynomial(coeffs=coeffs, terms=terms)

   def scale(poly, number):
      coeffs = list(map(lambda x: x*number, poly.coeffs))
      # clone the terms
      terms = copy.deepcopy(poly.terms)
      return polynomial(coeffs=coeffs, terms=terms)

x = variables.variable("x")
y = variables.variable("y")

term1 = [exponentials.exponential(x, 4),exponentials.exponential(y, 4)]
term2 = [exponentials.exponential(y, 3),exponentials.exponential(x, 4)]
term3 = [exponentials.exponential(x, 1),exponentials.exponential(y, 2)]
term4 = [exponentials.exponential(x, 2),exponentials.exponential(y, 1)]

poly_test = polynomial([1,2,3,4], [term1, term2, term3, term4])
