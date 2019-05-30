from .polynomials import polynomial
from .exponentials import exponential
from .variables import variable

class quadratic(polynomial):
    def __init__(self, coeffs, var):
        if len(coeffs) != 3:
            ValueError("quadratic objects take a list of 3 coefficients")
        if not isinstance(var, variable):
            TypeError("The variable parameter of the quadratic class must be a math_blocks variable object")
        terms = [[exponential(var, 2)], [exponential(var, 1)], [exponential(var, 0)]]
        polynomial.__init__(self, coeffs=coeffs, terms=terms)

    @staticmethod
    def from_roots(roots, var):
        # roots = [a,b]
        if len(roots) != 2:
            ValueError("The quadratic.from_roots requires the parameter roots is a list of length 2 - not {}".format(len(roots)))
        if not isinstance(var, variable):
            TypeError("The var parameter of the quadratic.from_roots method must be a math_blocks variable object")
        coeffs = [1, -(roots[0]+roots[1]), roots[0]*roots[1]]
        return quadratic(coeffs=coeffs, var=var)
        
