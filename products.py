from .math_block import math_block
from .chains import chain
from .number_formatting import object_sign

class product(math_block):

    def __init__(self, terms, sign=True):
        self.terms = terms
        self.sign = sign
        math_block.__init__(self, sign=sign, chain_bracket=True)

        
    def __mul__(self, other):
        if isinstance(other, product):
            return product(terms=self.terms+other.terms,
                           sign=(self.sign==other.sign))
        else:
            return product(self.terms+[other])

    def __add__(self, other):
        # UPDATE - signs
        return chain([self, other])
    
    def scale(self, scalar):
        return product([scalar, *self.terms])
            
    def evaluate(self):
        total = 1
        for term in self.terms:
            total *= term if isinstance(term, (int, float)) else term.evaluate()
        return total if self.sign else -total
        

    def latex(self, explicit=False, show_plus=False, show_neg=False):
        latex_terms = []
        for term in self.terms:
            if isinstance(term, (int, float)):
                term_latex = str(term)
            elif term.product_bracket:
                term_latex = "({})".format(term.latex(explicit=explicit))
            else:
                term_latex = term.latex(explicit=explicit)
            latex_terms.append(term_latex)
        out = " \\cdot ".join(latex_terms)
        if show_plus or not self.sign:
            out = "{}({})".format(object_sign(show_plus=show_plus, sign=self.sign),out)
        return out
    
    def merge_coeffs(coeffs):
        total = 1
        for coeff in coeffs:
            total *= coeff
        return total
        
            
