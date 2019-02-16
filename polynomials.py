from products import product

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
      self.terms = list(map(lambda x : product(*x) if isinstance(x, list) else x, terms))
      self.roots_known = False


   def __add__(self, other):
      coeffs = self.coeffs+other.coeffs
      terms = self.terms+other.terms
      return polynomial(coeffs=coeffs, terms=terms)

   def __mult__(self, other):
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
               new_coeffs.append(result_term)
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
         term.reduce();
      # 2)
      self.combine_variable_powers()

   def combine_variable_powers(self):
      # if variables and powers match perfectly between 2 terms - merge them
      target_index = 0
      length = len(self.terms)
      while target_index < length:
         length = self.combine_variable_powers_from_index(target_index)
         target_index += 1
         
   def combine_variable_powers_from_index(self, const_index):
      moving_index = const_index+1
      length = len(self.coeffs)
      while moving_index < length:
         # same variable powers
         if product.summable_var_pow(self.terms[const_index], self.terms[moving_index]):
            print("same", self.terms[const_index].latex(), self.terms[moving_index].latex())
            # merge
            self.coeffs[const_index]+=self.coeffs[moving_index]
            # delete
            del self.terms[moving_index]
            del self.coeffs[moving_index]
            # reduce length to avoid index out of range
            length -= 1
         else:
            print("different", const_index, moving_index)
            moving_index += 1
      return length
         
         
