import products
import exponentials
import copy
# this is a child of the product class
# it is designed for use by the polynomial class
# it is a product class which has terms that are exclusively exponential objects
# if a polynomial were to respresent x^2y^3 + 4xy^2 - 8x
# poly_term objects would be used to represent [x^2, y^3], [x^1, y^2], [x^1]

class poly_term(products.product):
    def __init__(self, *args):
        # make sure that the arguments are entirely exponential objects
        for term in args:
            if not isinstance(term, (exponentials.exponential)):
                error = """The poly_term class only accepts as arguments, any number of exponential objects"""
                raise ValueError(error)
        # valid input
        products.product.__init__(self, *args)

    def reduce(self):
        # merge terms of the same base
        # overriding the product method
        current_index = 0
        terms_length = len(self.terms)

        # move through the terms of the product
        while current_index < terms_length:
            # collapse as many terms into following the current one, into the current one
            # in case a term is collapsed, the terms_length needs to be updated
            terms_length = self.reduce_after_index(current_index)
            current_index += 1

    def reduce_after_index(self, current_index):
        moving_index = current_index+1
        terms_length = len(self.terms)

        # move through the terms after the current one
        while moving_index < terms_length:
            # compare bases
            if self.terms[current_index].base == self.terms[moving_index].base:
                # collapse the moving into the current
                self.terms[current_index].power += self.terms[moving_index].power
                del self.terms[moving_index]
                
                # update terms_length to reflect this deletion
                terms_length -= 1
            else:
                moving_index += 1
        return terms_length

    def latex(self, explicit=False):
        return "".join(map(lambda x: x.latex(explicit), self.terms))

    def derivative(self, var):
        """
        derivative of x^n*y^m*z^k with respect to x, y, or z
        assume that each term appear once eg. x^3*x^2 does not occur, it has been reduced to x^5
        return product object
        """
        
        for index,term in enumerate(self.terms):
            # this is the term with the derivative variable
            if term.base == var:
                # reduces to nothing
                if term.power == 0:
                    return products.product(0)
                else:
                    # create a copy of the term
                    der_term = copy.deepcopy(self)
                    # replace the target term with its derivative
                    der_term.terms.append(der_term.terms[index].power)
                    der_term.terms[index].power -= 1
                    return der_term
                
        # no matching variable found
        return products.product(0)
