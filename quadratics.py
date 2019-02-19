import polynomials
import exponentials

class quadratic(polynomials.polynomial):
    def __init__(self, coeffs, variable):
        terms = [[exponentials.exponential(variable, 2)], [exponentials.exponential(variable, 1)], [exponentials.exponential(variable, 0)]]
        polynomials.polynomial.__init__(self, coeffs=coeffs, terms=terms)

    def from_roots(roots, var):
        # roots = [a,b]
        coeffs = [1, -(roots[0]+roots[1]), roots[0]*roots[1]]
        return quadratic(coeffs=coeffs, variable=var)
        
