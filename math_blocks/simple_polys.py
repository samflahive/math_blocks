from .polynomials import polynomial
from .polyterms import polyterm
from .polycomps import polycomp
from .exponentials import exponential

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
        
