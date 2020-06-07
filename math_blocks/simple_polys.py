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

"""
    @staticmethod
    def root_product_sum(roots, size):
        if size == 1:
            return sum(roots)
        size -= 1
        total = 0
        for i in range(len(roots)-size):
            base = list_product(roots[i:i+size])
            for j in range(i+size, len(roots)):
                total += base * roots[j]
        return total

    
    @staticmethod
    def from_roots(var, roots):
        coeffs = [1]
        for i in range(len(roots)):
            coeff  = simple_poly.root_product_sum(roots, i+1)
            if i % 2 == 0:
                coeffs.append(-coeff)
            else:
                coeffs.append(coeff)

        return simple_poly(coeffs, var)
        
def list_product(ls):
    total = 1
    for i in ls:
        total *= i
    return total

"""
