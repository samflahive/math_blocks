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


    def __mul__(self, other):
        if isinstance(other, polynomial):
            items = []
            for self_term in self.items:
                for other_term in other.items:
                    items.append(self_term*other_term)
            return polynomial(items=items, sign=(self.sign == other.sign))
        else:
            return math_blocks.product([self, other])

    @staticmethod
    def root_to_factor(var, val):
        return math_blocks.simple_poly([1,-val], var)

    @staticmethod
    def from_roots(root_pairs):
        # root_pairs is a list of tuples (variable, root), eg. (x, 3)
        poly = polynomial.root_to_factor(*root_pairs[0])
        for root_pair in root_pairs[1:]:
            poly *= polynomial.root_to_factor(*root_pair)

        return poly
        
