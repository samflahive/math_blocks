from .number_formatting import number_coeff
import copy

class chain:
    # sums of math_block objects

    def __init__(self, adders):
        # adders are objects to be added in the chain: list of math_blocks objects
        self.adders = adders

    def evaluate(self):
        """
        evaluate this chains
        return number
        """
        return sum(list(map(lambda x: x if isinstance(x,(int,float,complex)) else x.evaluate(), self.adders)))

    def __add__(self, other):
        """
        addition operator for chain objects - supports all non-chain objects
        return chain object
        """
        # clone chain
        new_chain = copy.deepcopy(self)
        # add object to adders
        new_chain.adders.append(other)
        return new_chain

        

    def latex(self, explicit=False):
        """
        latex string representing the chain
        """
        latex = ""
        
        for index,term in enumerate(self.adders):
            sign = (term >= 0) if isinstance(term, (int, float, complex)) else term.sign
            if sign:
                latex += "{}{}".format("" if index == 0 else "+", str(term) if isinstance(term, (int, float, complex)) else term.latex(explicit=explicit))
            else:
                latex += "{}".format(number_coeff(term, index=index, explicit=explicit) if isinstance(term, (int, float, complex)) else term.latex(explicit=explicit))
        return latex
