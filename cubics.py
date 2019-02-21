import polynomials
import exponentials

class cubic(polynomials.polynomial):
    def __init__(self, coeffs, variable):
        terms = [[exponentials.exponential(variable, 3)],
                 [exponentials.exponential(variable, 2)],
                 [exponentials.exponential(variable, 1)],
                 [exponentials.exponential(variable, 0)]]
        
        polynomials.polynomial.__init__(self, coeffs=coeffs, terms=terms)

    def from_roots(roots, var):
        if len(roots) != 3:
            ValueError("The cubic.from_roots requires the parameter roots is a list of length 3 - not {}".format(len(roots)))
        # roots = [a,b]
        coeffs = [1, -2*(roots[0]*roots[1]+roots[2]), 2*roots[0]*roots[1]*(1-roots[2]), -(roots[0]*roots[1]*roots[2])]
        return cubic(coeffs=coeffs, variable=var)
