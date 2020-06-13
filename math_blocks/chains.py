from copy import deepcopy

import math_blocks

class chain(math_blocks.math_block):
    # sums of math_block objects

    def __init__(self, items, sign=True):
        """chains are simple sums, items refers to a list of operands"""
        math_blocks.math_block.__init__(self, sign=sign)
        
        math_block_items = []
        for item in items:
            if isinstance(item, (int, float)):
                math_block_items.append(math_blocks.number(item))
            else:
                math_block_items.append(item)
                
        self.items = math_block_items

    def evaluate(self):
        """
        evaluate this chains
        return number
        """
        total = sum(item.evaluate() for item in self.items)
        if self.sign:
            return total
        return -total
 
    def latex(self, explicit=False, show_plus=False):
        """
        latex string representing the chain
        """
        latex_list = []
        
        for index, item in enumerate(self.items):
            #bracketed = isinstance(item, (chain, complex_number, math_blocks.products.product))
            
            # add sign
            # first item (if positive) should not show a +, unless we are being explicit
            child_show_plus = (not (index == 0 and not explicit))

            latex_list.append(item.latex(explicit=explicit, show_plus=child_show_plus))

        out = "".join(latex_list)
        if not self.sign:
            return "-(%s)" % out
        if show_plus:
            return "+(%s)" % out
        return out

    def ripple_sign(self):
        # make the sign true
        ch = deepcopy(self)
        if not ch.sign:
            for item in ch.items:
                item.sign = not item.sign
            ch.sign = True
        return ch

    def check_num_collapsable(self):
        self.num_collapsable = True
        for i in self.items:
            #  do we already know
            if not i.num_collapsable:
                #  check
                i.check_num_collapsable()
                # result of check
                if not i.num_collapsable:
                    self.num_collapsable = False
                    break
        


    def __eq__(self, other):
        if not isinstance(other, chain):
            return False
        if len(self.items) != len(other.items):
            return False

        for i,c in enumerate(self.items):
            if c != other.items[i]:
                return False

        return self.sign == other.sign
