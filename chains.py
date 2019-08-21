from .math_block import math_block
from .number_formatting import number_coeff
import copy

class chain(math_block):
    # sums of math_block objects

    def __init__(self, items, sign=True):
        # adders are objects to be added in the chain: list of math_blocks objects
        math_block.__init__(self, sign=sign)
        self.items = items

    def evaluate(self):
        """
        evaluate this chains
        return number
        """
        return sum(list(map(lambda x: x if isinstance(x,(int,float,complex)) else x.evaluate(), self.items)))

    def __add__(self, other):
        """
        addition operator for chain objects - supports all non-chain objects
        return chain object
        """
        return chain(items=[*self.items, other], sign=self.sign)

    def __sub__(self, other):
        other = -other
        return self + other

        

    def latex(self, explicit=False):
        """
        latex string representing the chain
        """
        latex_list = []
        
        for index,term in enumerate(self.items):
            if isinstance(term, (int, float)):
                latex = number_coeff(term, index=index)

            else:
                latex = term.latex(show_plus=(index != 0))

            latex_list.append(latex)
                
            out = "".join(latex_list)
        return out if self.sign else "-({})".format(out)
