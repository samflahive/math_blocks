import products
import exponentials

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
