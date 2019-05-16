import number_formatting
import copy

class chain:
    # sums of math_block objects

    def __init__(self, adders, subbers, order):
        # adders are objects to be added in the chain: list of math_blocks objects
        self.adders = adders
        # subbers are objects to be subtracted in the chain: list of math_blocks objects
        self.subbers = subbers
        # order is the order in which the adders and subbers should be mixed when displayed: [[adders indices],[subbers indices]]
        self.order = order

    def evaluate(self):
        """
        evaluate this chains
        return number
        """
        return sum(item.evaluate() for item in self.adders) - sum(item.evaluate() for item in self.subbers)

    def __add__(self, other):
        """
        addition operator for chain objects - supports all non-chain objects
        return chain object
        """
        # clone chain
        new_chain = copy.deepcopy(self)
        # add object to adders
        new_chain.adders.append(other)
        # update order - this item will be shown last
        new_chain.order[0].append(max(new_chain.order[0][-1], new_chain.order[1][-1])+1)

        return new_chain

    def __sub__(self, other):
        """
        subtraction operator for chain objects - supports all non-chain objects
        return chain object
        """
        # clone chain
        new_chain = copy.deepcopy(self)
        # add object to subbers
        new_chain.subbers.append(other)
        # update order - this item will be shown last
        new_chain.order[1].append(max(new_chain.order[0][-1], new_chain.order[1][-1])+1)

        return new_chain
        

    def latex(self, explicit=False):
        """
        latex string representing the chain
        """
        latex = ""
        
        adder_order_index = 0
        subber_order_index = 0

        # loop through the order until the final one of each is reached
        while adder_order_index < len(self.order[0]) or subber_order_index < len(self.order[1]):
            # might have to block some functionality if the adders are finished before the subbers or vice versa
            adder_finished = (adder_order_index >= len(self.order[0]))
            subber_finished = (subber_order_index >= len(self.order[1]))
            print(adder_order_index, subber_order_index)
            
            
            # the print order of the current adder and subber - if not finished
            adder_index = self.order[1][subber_order_index]+1 if adder_finished else self.order[0][adder_order_index]
            subber_index = self.order[0][adder_order_index]+1 if subber_finished else self.order[1][subber_order_index]

            # the current adder is before the current subber
            if adder_index < subber_index:
                adder = self.adders[adder_order_index]
                if isinstance(adder, (int, float, complex)):
                    latex += number_formatting.number_coeff(adder, adder_order_index, explicit=explicit, one_special=False)
                else:
                    latex += "{}{}".format("+" if adder_order_index != 0 else "",adder.latex(explicit=explicit))

                adder_order_index += 1

            # the current subber is before the current adder
            else:
                subber = self.subbers[subber_order_index]
                if isinstance(adder, (int, float, complex)):
                    latex += number_formatting.number_coeff(-subber, subber_order_index, explicit=explicit, one_special=False)
                else:
                    latex += "{}{}".format("-" if subber_order_index != 0 else "",subber.latex(explicit=explicit))

                subber_order_index += 1

        return latex

                
        
