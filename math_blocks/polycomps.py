from .products import product

class polycomp(product):
    def __init__(self, expos, sign=True):
        # todo: add integrety checks for variable^number
        
        product.__init__(self, items=expos, sign=sign)
        d_var = {}


        # save dict of variables involved
        # useful later for merging terms and calculus
        for i,expo in enumerate(expos):
            target_sym = expo.base.symbol
            if d_var.get(target_sym) == None:
                d_var[target_sym] = [i]
            else:
                d_var[target_sym].append(i)
        self.dependent_variables = d_var

    def latex(self, explicit=False, show_plus=False):
        out = "".join(expo.latex(explicit=explicit,
                                 show_zero_power=False) for expo in self.items)

        if not self.sign:
            return "-%s" % out
        if show_plus:
            return "+%s" % out
        return out

    def __mul__(self, other):
        if isinstance(other, polycomp):
            return polycomp(expos=(self.items+other.items), sign=(self.sign==other.sign))
        return NotImplemented
        
        
        
