from .math_block import math_block
from .numbers import number
from .complex_numbers import complex_number
# import entire module to avoid circular dependency
#import .fractions.fraction
import math_blocks.chains


class product(math_block):
    # sums of math_block objects

    def __init__(self, items, sign=True):
        math_block.__init__(self, sign=sign)

        math_block_items = []
        for item in items:
            if isinstance(item, (int, float)):
                math_block_items.append(number(item))
            else:
                math_block_items.append(item)

        self.items = math_block_items

    def evaluate(self):
        total = 1
        for i in self.items:
            total *= i.evaluate()
        if self.sign:
            return total
        return -total

    def latex(self, explicit=False, show_plus=False):
        latex_terms = []
        for i in self.items:
            if isinstance(i, (complex_number, math_blocks.chains.chain)): # add chain
                item_latex = "(%s)" % i.latex(explicit=explicit)

            else:
                item_latex = i.latex(explicit=explicit)

            latex_terms.append(item_latex)

        if not self.sign:
            return "-(%s)" % r" \cdot ".join(latex_terms)
        if show_plus:
            return "+(%s)" % r" \cdot ".join(latex_terms)
        return r" \cdot ".join(latex_terms)

    def __eq__(self, other):
        if not isinstance(other, product):
            return False

        for i,p in enumerate(self.items):
            if p != other.items[i]:
                return False

        return self.sign == other.sign
