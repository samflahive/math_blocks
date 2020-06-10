from .polynomials import polynomial
from .polyterms import polyterm
from .polycomps import polycomp
from .exponentials import exponential
import math_blocks

class simple_poly(polynomial):
    def __init__(self, coeffs, var, start_power=None, sign=True):
        
        if start_power == None:
            start_power = len(coeffs) - 1

        items = []
        for coeff in coeffs:
            items.append(polyterm(coeff=coeff,
                                  pcomp=polycomp([exponential(var, start_power)])))
            start_power -= 1

        polynomial.__init__(self, items=items, sign=sign)
        self.var_sym = var.symbol


    @staticmethod
    def from_roots(var, roots):
        roots = list(map(lambda r: math_blocks.number(r), roots))
        # quadratic
        if len(roots) == 2:
            #(x-a)(x-b) = x^2 - (a+b)x + a*b 
            return simple_poly(coeffs=[1, -(roots[0]+roots[1]), roots[0]*roots[1]], var=var)
        # cubic
        elif len(roots) == 3:
            # (x-a)(x-b)(x-c) = x^3 - (a+b+c)x^2 + (a*b + a*c + b*c)x - a*b*c
            a,b,c = roots
            return simple_poly(coeffs=[1, -(a+b+c), (a*b + a*c + b*c), -(a*b*c)], var=var)

        else:
            raise NotImplementedError("simple_poly can only handle quadratic or cubic roots for now")
            
