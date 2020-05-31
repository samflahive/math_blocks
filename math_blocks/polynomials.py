import math_blocks
from copy import deepcopy

class polynomial(math_blocks.chain):
    def __init__(self, items, sign=True):
        math_blocks.chain.__init__(self, items=items, sign=sign)


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
        return math_blocks.chain([self, other])

    def ripple_sign(self):
        # make the sign true
        poly = deepcopy(self)
        if not poly.sign:
            for item in poly.items:
                item.sign = not item.sign
            poly.sign = True
        return poly


    def __mul__(self, other):
        if isinstance(other, polynomial):
            items = []
            for self_term in self.items:
                for other_term in other.items:
                    items.append(self_term*other_term)
            return polynomial(items=items, sign=(self.sign == other.sign))
        else:
            return math_blocks.product([self, other])
