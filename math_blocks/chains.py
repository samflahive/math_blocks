from .math_block import math_block
from .number_formatting import number_coeff, object_sign
import copy

class chain(math_block):
    # sums of math_block objects

    def __init__(self, items, sign=True):
        """chains or simple sums, items refers to a list of tuples.
            The first value in each tuple is a number or math_block object,
            the second value is a sign, True=+ and False=- """
        math_block.__init__(self, sign=sign)
        self.items = items

    def evaluate(self):
        """
        evaluate this chains
        return number
        """
        total = 0
        for (item, sign) in self.items:
            item_value = item if isinstance((int, float)) else item.evaluate()
            if not sign:
                total -= item_value
            else:
                total += item_value
        return total

    def __add__(self, other):
        """
        addition operator for chain objects - supports all non-chain objects
        return chain object
        """
        return chain(items=[*self.items, (other, True)], sign=self.sign)


    def __sub__(self, other):
        other = -other
        return self + other

        

    def latex(self, explicit=False, show_plus=False):
        """
        latex string representing the chain
        """
        latex_list = []
        
        for index, (item, sign) in enumerate(self.items):
            if isinstance(item, (int, float)):
                    item_latex = item
                    
            else:
<<<<<<< HEAD
                item_latex = item.latex(explicit=explicit)
                if not (index == 0 and not explicit and sign):
                    sign_sym = "+" if sign else "-"
                    if not item.sign:
                        item_latex = "%s(%s)" % (item_latex, sign_sym)
                    else:
                        item_latex = "%s%s" % (item_latex, sign_sym)
            latex_list.append(item_latex)
        out = "".join(latex_list)
        return out if self.sign else "-({})".format(out)
=======
                latex = term.latex(show_plus=(index != 0))

            latex_list.append(latex)
                
            out = "".join(latex_list)
        if show_plus or not self.sign:
            return "{}({})".format(object_sign(show_plus,self.sign),out)
        return out
>>>>>>> 5961f465424fb6d8574ef03fadc31e702186ebda
