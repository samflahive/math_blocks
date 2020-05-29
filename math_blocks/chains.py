from .math_block import math_block
from .numbers import number
from .complex_numbers import complex_number
import math_blocks.products

#import math_blocks.products


class chain(math_block):
    # sums of math_block objects

    def __init__(self, items, sign=True):
        """chains or simple sums, items refers to a list of tuples.
            The first value in each tuple is a number or math_block object,
            the second value is a sign, True=+ and False=- """
        math_block.__init__(self, sign=sign)
        
        math_block_items = []
        for item in items:
            if not isinstance(item, (list, tuple)):
                item = (item, True)
            if isinstance(item[0], (int, float)):
                math_block_items.append((number(item[0]), item[1]))
            else:
                math_block_items.append(item)
                
        self.items = math_block_items

    def evaluate(self):
        """
        evaluate this chains
        return number
        """
        total = 0
        for (item, sign) in self.items:
            item_value = item.evaluate()
            if not sign:
                total -= item_value
            else:
                total += item_value
        if self.sign:
            return total
        return -total
 
    def latex(self, explicit=False, show_plus=False):
        """
        latex string representing the chain
        """
        latex_list = []
        
        for index, (item, sign) in enumerate(self.items):

            sign_sym = "+" if sign else "-"

            bracketed = isinstance(item, (chain, complex_number, math_blocks.products.product))
            if not bracketed:
                item_latex = item.latex(explicit=explicit) # does not show '+' but does show '-'
            else:
                item_latex = "(%s)" % item.latex(explicit=explicit)

            # add sign
            if not (index == 0 and not explicit and sign):
                if item.sign or bracketed: # no sign inherent to the item
                    item_latex = "%s%s" % (sign_sym, item_latex)
                else: # already a "-" before the item
                    item_latex = "%s(%s)" % (sign_sym, item_latex)
                    

            latex_list.append(item_latex)

        out = "".join(latex_list)
        return out if self.sign else "-({})".format(out)

