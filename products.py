from .exponentials import exponential
from .chains import chain

class product:
    # functionality
    # 1) create a product
    # 2) multiply two products
    # 3) evaluate
    # 4) arrange
    # 5) reduce
    # 6) latex

    def __init__(self, *args):
        self.terms = list(args)
        self.sign = True

    def __mul__(self, other):
        if isinstance(other, product):
            return product(*(self.terms+other.terms))
        else:
            return product(*self.terms+[other])

    def __add__(self, other):
        return chain(adders=[self, other])
    
    def scale(self, scalar):
        return product(scalar, *self.terms)
            
    def evaluate(self):
        total = 1
        for term in self.terms:
            total *= term if isinstance(term, (int, float, complex)) else term.evaluate()
        return total
    
    def arrange(self):
        # 1) numbers
        # 2) exponents
        numbers = []
        exps = []
        unwanted = []

        for term in self.terms:
            # number
            if isinstance(term, (int, float, complex)):
                numbers.append(term)
            # exponential
            elif isinstance(term, exponential):
                exps.append(term)
            # should not happen
            else:
                unwanted.append(term)
        self.terms = numbers+exps+unwanted

    def reduce(self):
        # simplify the product
        # combine numbers, combine exponentials
        numbers = []
        exps = []
        others = []
        for term in self.terms:
            # number
            if isinstance(term, (int, float, complex)):
                numbers.append(term)
            # exponential
            elif isinstance(term, exponential):
                exps.append(term)
            # other
            else:
                others.append(term)

        # reduce the numbers list to a single number
        number = product.merge_coeffs(numbers)
        # reduce the exponentials list a (hopefully) smaller list
        exponential.combine_by_base(exps)
        self.terms = [number]+exps+others
        

    def latex(self, explicit=False):
        return "\\cdot".join(map(lambda term: str(term) if isinstance(term, (int, float, complex)) else term.latex(explicit=explicit), self.terms))

    def merge_coeffs(coeffs):
        total = 1
        for coeff in coeffs:
            total *= coeff
        return total

    @staticmethod
    def summable_var_pow(prodA, prodB):
        # checks if two product objects are composed of the same variables ^ powers
        # eg. 4x^2y^3 and 9y^3x^2 should return true
        if len(prodA.terms) != len(prodB.terms):
            return False
        for term in prodA.terms:
            # a coefficient
            if isinstance(term, (int, float, complex)):
                continue
            elif isinstance(term, exponential):
                if term not in prodB.terms:
                    return False
                else:
                    continue
            else:
                # only support numbers and exponenials for now
                return False
        return True
        
            
