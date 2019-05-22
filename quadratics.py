import math_blocks.polynomials
import math_blocks.exponentials
import math_blocks.variables

class quadratic(math_blocks.polynomials.polynomial):
    def __init__(self, coeffs, variable):
        if len(coeffs) != 3:
            ValueError("quadratic objects take a list of 3 coefficients")
        if not isinstance(variable, (math_blocks.variables.variable)):
            TypeError("The variable parameter of the quadratic class must be a math_blocks variable object")
        terms = [[math_blocks.exponentials.exponential(variable, 2)], [math_blocks.exponentials.exponential(variable, 1)], [math_blocks.exponentials.exponential(variable, 0)]]
        math_blocks.polynomials.polynomial.__init__(self, coeffs=coeffs, terms=terms)

    def from_roots(roots, var):
        # roots = [a,b]
        if len(roots) != 2:
            ValueError("The quadratic.from_roots requires the parameter roots is a list of length 2 - not {}".format(len(roots)))
        if not isinstance(var, (math_blocks.variables.variable)):
            TypeError("The var parameter of the quadratic.from_roots method must be a math_blocks variable object")
        coeffs = [1, -(roots[0]+roots[1]), roots[0]*roots[1]]
        return math_blocks.quadratic(coeffs=coeffs, variable=var)
        
