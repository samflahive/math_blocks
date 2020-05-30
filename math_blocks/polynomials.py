from .chains import chain
from copy import deepcopy

class polynomial(chain):
    def __init__(self, items, sign=True):
        chain.__init__(self, items=items, sign=sign)


    def __add__(self, other):
        if isinstance(other, polynomial):
            if not self.sign:
                self_poly = self.ripple_sign()
            else:
                self_poly = self

            if not other.sign:
                other = other.ripple_sign()
            combined_terms = self_poly.items + other.items
            return polynomial(items=combined_terms)
        return chain([self, other])

    def ripple_sign(self):
        # make the sign true
        poly = deepcopy(self)
        if not poly.sign:
            for item in poly.items:
                item.sign = not item.sign
            poly.sign = True
        return poly
