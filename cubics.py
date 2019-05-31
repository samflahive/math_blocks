from .polynomials import polynomial
from .exponentials import exponential
from .variables import variable

class cubic(polynomial):
    def __init__(self, coeffs, var):
        if len(coeffs) != 4:
            ValueError("Cubic objects take a list of 3 coefficients")
        if not isinstance(var, variable):
            TypeError("The variable parameter of the cubic class must be a math_blocks variable object")
            
        terms = [[exponential(var, 3)],
                 [exponential(var, 2)],
                 [exponential(var, 1)],
                 [exponential(var, 0)]]
        
        polynomial.__init__(self, coeffs=coeffs, terms=terms)

    @staticmethod
    def from_roots(roots, var):
        # roots = [a,b]
        if len(roots) != 3:
            ValueError("The cubic.from_roots requires the parameter roots is a list of length 3 - not {}".format(len(roots)))
        if not isinstance(var, variable):
            TypeError("The var parameter of the cubic.from_roots method must be a math_blocks variable object")
        # roots = [a,b]
        coeffs = [1, -(roots[0]+roots[1]+roots[2]), (roots[0]*roots[1]+roots[0]*roots[2]+roots[1]*roots[2]), -(roots[0]*roots[1]*roots[2])]
        cube = cubic(coeffs=coeffs, var=var)
        cube.roots_known = True
        cube.roots = [[var, root] for root in roots]
        return cube
