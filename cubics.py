import polynomials
import exponentials

class cubic(polynomials.polynomial):
    def __init__(self, coeffs, variable):
        if len(coeffs) != 4:
            ValueError("Cubic objects take a list of 3 coefficients")
        if not isinstance(variable, (variables.variable)):
            TypeError("The variable parameter of the cubic class must be a math_blocks variable object")
            
        terms = [[exponentials.exponential(variable, 3)],
                 [exponentials.exponential(variable, 2)],
                 [exponentials.exponential(variable, 1)],
                 [exponentials.exponential(variable, 0)]]
        
        polynomials.polynomial.__init__(self, coeffs=coeffs, terms=terms)

    def from_roots(roots, var):
        # roots = [a,b]
        if len(roots) != 3:
            ValueError("The cubic.from_roots requires the parameter roots is a list of length 3 - not {}".format(len(roots)))
         if not isinstance(var, (variables.variable)):
            TypeError("The var parameter of the cubic.from_roots method must be a math_blocks variable object")
        # roots = [a,b]
        coeffs = [1, -2*(roots[0]*roots[1]+roots[2]), 2*roots[0]*roots[1]*(1-roots[2]), -(roots[0]*roots[1]*roots[2])]
        return cubic(coeffs=coeffs, variable=var)
