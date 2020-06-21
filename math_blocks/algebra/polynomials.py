from . import core
from . import exponentials
from copy import deepcopy


# uses Product, PolyComp
class PolyComp(core.Product):
    def __init__(self, expos, sign=True, block_type="pc"):
        # todo: add integrety checks for Variable^Number
        # add option to avoid integrity check - eg for math_board exps not MathBlock exps
        
        core.Product.__init__(self, items=expos, sign=sign, block_type=block_type)
        d_var = {}

        # save dict of Variables involved
        # useful later for merging terms and calculus
        for i,expo in enumerate(expos):
            target_sym = expo.base.symbol
            if d_var.get(target_sym) == None:
                d_var[target_sym] = [i]
            else:
                d_var[target_sym].append(i)
        self.dependent_Variables = d_var

    def latex(self, explicit=False, show_plus=False):
        out = "".join(expo.latex(explicit=explicit,
                                 show_zero_power=False) for expo in self.items)

        if not self.sign:
            return "-%s" % out
        if show_plus:
            return "+%s" % out
        return out

    def __mul__(self, other):
        if isinstance(other, PolyComp):
            return PolyComp(expos=(self.items+other.items), sign=(self.sign==other.sign))
        return NotImplemented
        

# uses MathBlock, Number, PolyTerm
class PolyTerm(core.MathBlock):

    def __init__(self, coeff, pcomp, sign=True, block_type="pt"):
        if isinstance(coeff, (int,float)):
            coeff = core.Number(coeff)
        # integrate coeff sign into PolyTerm parent
        sign = sign and coeff.sign
        coeff.sign = True
        
        core.MathBlock.__init__(self, sign=sign, block_type=block_type)
        self.coeff = coeff
        self.pcomp = pcomp

    def latex(self, explicit=False, show_plus=False):
        if isinstance(self.coeff, (core.ItemsBlock, exponentials.ComplexNumber)):
            coeff_latex = "(%s)" % self.coeff.latex(explicit=explicit)
        else:
            coeff_latex = self.coeff.latex(explicit=explicit)
        if not self.sign:
            return "-%s%s" % (coeff_latex,
                              self.pcomp.latex(explicit=explicit))
        if show_plus:
            return "+%s%s" % (coeff_latex,
                              self.pcomp.latex(explicit=explicit))
        
        return "%s%s" % (coeff_latex,
                         self.pcomp.latex(explicit=explicit))

    def evaluate(self):
        out = self.coeff.evaluate() * self.pcomp.evaluate()
        if self.sign:
            return out
        return -out

    def __mul__(self, other):
        if isinstance(other, PolyTerm):
            return PolyTerm(coeff=(self.coeff*other.coeff),
                            pcomp=(self.pcomp*other.pcomp),
                            sign=(self.sign == other.sign))
        else:
            return core.MathBlock.__mul__(self, other)

    def __eq__(self, other):
        if not isinstance(other, PolyTerm):
            return False

        return (self.coeff == other.coeff
                and self.pcomp == other.pcomp
                and self.sign == other.sign)


# uses Chain, Polynomial, SimplePoly
class Polynomial(core.Chain):
    def __init__(self, items, sign=True, block_type="py"):
        core.Chain.__init__(self, items=items, sign=sign, block_type=block_type)


    def __add__(self, other):
        if isinstance(other, Polynomial):
            if not self.sign:
                self_poly = self.ripple_sign()
            else:
                self_poly = self

            if not other.sign:
                other = other.ripple_sign()
            combined_terms = self_poly.items + other.items
            return Polynomial(items=combined_terms)
        return core.MathBlock.__add__(self, other)


    def __mul__(self, other):
        if isinstance(other, Polynomial):
            items = []
            for self_term in self.items:
                for other_term in other.items:
                    items.append(self_term*other_term)
            return Polynomial(items=items, sign=(self.sign == other.sign))
        else:
            return core.MathBlock.__mul__(self, other)

    @staticmethod
    def root_to_factor(var, val):
        return SimplePoly([1,-val], var)
    
    @staticmethod
    def from_roots(root_pairs):
        # root_pairs is a list of tuples (Variable, root), eg. (x, 3)
        poly = Polynomial.root_to_factor(*root_pairs[0])
        for root_pair in root_pairs[1:]:
            poly *= Polynomial.root_to_factor(*root_pair)

        return poly
        
# uses Polynomial, PolyComp, PolyTerm, Number, SimplePoly
class SimplePoly(Polynomial):
    def __init__(self, coeffs, var, start_power=None, sign=True, block_type="sp"):
        if start_power == None:
            start_power = len(coeffs) - 1

        items = []
        for coeff in coeffs:
            items.append(PolyTerm(coeff=coeff,
                                  pcomp=PolyComp([exponentials.Exponential(var, start_power)])))
            start_power -= 1

        Polynomial.__init__(self, items=items, sign=sign, block_type=block_type)
        self.var_sym = var.symbol


    @staticmethod
    def from_roots(var, roots):
        roots = list(map(lambda r: (core.Number(r) if isinstance(r, (int, float)) else r), roots))
        # quadratic
        if len(roots) == 2:
            #(x-a)(x-b) = x^2 - (a+b)x + a*b 
            return SimplePoly(coeffs=[1, -(roots[0]+roots[1]), roots[0]*roots[1]], var=var)
        # cubic
        elif len(roots) == 3:
            # (x-a)(x-b)(x-c) = x^3 - (a+b+c)x^2 + (a*b + a*c + b*c)x - a*b*c
            a,b,c = roots
            return SimplePoly(coeffs=[1, -(a+b+c), (a*b + a*c + b*c), -(a*b*c)], var=var)

        else:
            raise NotImplementedError("SimplePoly can only handle quadratic or cubic roots for now")
            

# uses MathBlock, Number, Polynomial, ComplexNumber
class Variable(core.MathBlock):
    def __init__(self, symbol, value=None, sign=True, block_type="vr"):
        core.MathBlock.__init__(self, sign=sign, block_type=block_type)
        self.symbol = symbol
        self.sign = sign
        if isinstance(value, (int, float)):
            value = core.Number(value)
        self.value = value

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return "-%s" % self.symbol
        if show_plus:
            return "+%s" % self.symbol
        return self.symbol
    
    def evaluate(self):
        if self.value != None:
            if isinstance(self.value, (int, float)):
                self.value = core.Number(self.value)
            val = self.value.evaluate()
            if self.sign:
                return val
            return -val
        else:
            raise ValueError("Variable (symbol=%s) does not have a value" % self.symbol)


    def __mul__(self, other):
        if isinstance(other, exponential.ComplexNumber):
            return exponential.ComplexNumber(real=(self*other.real), imaginary=(self*other.imaginary), sign=other.sign)
        elif isinstance(other, core.polynomial):
            return Polynomial(items=[self*term for term in other.items], sign=other.sign)
        elif isinstance(other, PolyTerm):
            return PolyTerm(coeff=self*other.coeff, pcomp=other.pcomp, sign=other.sign)
        else:
            return core.MathBlock(self, other)

    def __eq__(self, other):
        if not isinstance(other, Variable):
            return False
        return (self.symbol == other.symbol and self.sign == other.sign)
            