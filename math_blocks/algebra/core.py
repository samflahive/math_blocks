from copy import deepcopy
import functools

# MathBlock, Number, Chain, Fraction, Product, ItemsBlock


# uses Chain, Fraction, Product
class MathBlock:
    def __init__(self, sign, Product_bracket=False,
                  Chain_bracket=False, bracketed=True, block_type="mb"):
        self.sign = sign
        self.Product_bracket = Product_bracket
        self.Chain_bracket = Chain_bracket
        self.bracketed = bracketed
        self.num_collapsable = False
        self.block_type = block_type


    def __add__(self, other):
        return Chain([self, other])

    def __mul__(self, other):
        return Product([self, other])

    def __truediv__(self, other):
        return Fraction(self, other)
              
    def __neg__(self):
        new = deepcopy(self)
        new.sign = not self.sign
        return new

    def __sub__(self, other):
        return self + (-other)

    def __radd__(self, other):
        return self+other

    def __rmul__(self, other):
        return self*other


# uses MathBlock, Number
class Number(MathBlock):
    
    def __init__(self, value, sign=True):
        implied_sign = value > 0
        MathBlock.__init__(self, sign=(implied_sign == sign), block_type="nm")

        value = abs(value)
        self.value = value

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return "-{}".format(self.value)
        if show_plus:
            return "+{}".format(self.value)
        return str(self.value)

    def evaluate(self):
        if self.sign:
            return self.value
        return -self.value




    def __eq__(self, other):
        if not isinstance(other, Number):
            if isinstance(other, (int, float)):
                return other == self.evaluate()
            return False
        return (self.value == other.value and self.sign == other.sign)


# uses MathBlock, Number, Fraction, Product, Chain
class Fraction(MathBlock):
    def __init__(self, numerator, denominator, sign=True):
        MathBlock.__init__(self, sign=sign, block_type="fr")

        if isinstance(numerator, (int, float)):
            numerator = Number(numerator)
        if isinstance(denominator, (int, float)):
            denominator = Number(denominator)

        self.numerator = numerator
        self.denominator = denominator

    def evaluate(self):
        val = self.numerator.evaluate() / self.denominator.evaluate()
        if self.sign:
            return val
        return -val

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return "-\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))
        if show_plus:
            return "+\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))
        return "\\frac{%s}{%s}" % (self.numerator.latex(explicit), self.denominator.latex(explicit))


    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False

        return (self.denominator == other.denominator
                and self.numerator == other.numerator
                and self.sign == other.sign)


    def __add__(self, other):
        if isinstance(other, Fraction) and (self.denominator == other.denominator):
            other_num = other.numerator if (other.sign == self.sign) else -other.numerator
            return Fraction(self.numerator+other_num, self.denominator)
        else:
            return MathBlock.__add__(self, other)
        

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerator*other.numerator,
                            denominator=self.denominator*other.denominator,
                            sign=(self.sign==other.sign))
        else:
            return MathBlock.__mul__(self, other)

    def split(self):
        if self.numerator.block_type in ("pr", "ch", "cx"):
            return self.numerator.fraction_split(denominator=self.denominator, sign=self.sign)
        else:
            raise ValueError("Fractions can only be split when the numerator is a Chain, Product or complex Number")

    def inverse(self):
        return Fraction(numerator=self.denominator, denominator=self.numerator, sign=self.sign)


# uses MathBlock, Number
class ItemsBlock(MathBlock):
    def __init__(self, items, sign=False, block_type="ib"):
        MathBlock.__init__(self, sign=sign, block_type=block_type)
        MathBlock_items = []
        for item in items:
            if isinstance(item, (int, float)):
                MathBlock_items.append(Number(item))
            else:
                MathBlock_items.append(item)
                
        self.items = MathBlock_items

    def evaluate(self):
        block_vals = [item.evaluate() for item in self.items]
        if isinstance(self, Chain):
            total = sum(block_vals)
        elif isinstance(self, Product):
            total = functools.reduce(lambda a,b: a*b, block_vals)

        else:
            raise ValueError("invalid ItemsBlock, must be Chain or Product. Not %s" % self.block_type)

        if self.sign:
            return total
        else:
            return -total

    def ripple_sign(self):
        # make the sign true
        ib = deepcopy(self)
        if not ib.sign:
            for item in ib.items:
                item.sign = not item.sign
            ib.sign = True
        return ib

    def fraction_split(self, denominator, sign):
        Fractions = []
        for item in self.items:
            
            fr = Fraction(item, denominator, sign=self.sign)
            Fractions.append(fr)
            
        if self.block_type == "ch":
            return Chain(items=Fractions, sign=sign)
        else:
            return Product(items=Fractions, sign=sign)

    def __eq__(self, other):
        if not isinstance(other, ItemsBlock):
            return False
        if len(self.items) != len(other.items):
            return False

        for i,c in enumerate(self.items):
            if c != other.items[i]:
                return False

        return self.sign == other.sign

# uses ItemsBlock
class Chain(ItemsBlock):
    # sums of MathBlock objects

    def __init__(self, items, sign=True, block_type="ch"):
        """Chains are simple sums, items refers to a list of operands"""
        ItemsBlock.__init__(self, items=items, sign=sign, block_type=block_type)
        

 
    def latex(self, explicit=False, show_plus=False):
        """
        latex string representing the Chain
        """
        latex_list = []
        
        for index, item in enumerate(self.items):
            #bracketed = isinstance(item, (Chain, complex_Number, MathBlocks.Products.Product))
            
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


# uses MathBlock, Chain, Product
class Product(ItemsBlock):
    
    def __init__(self, items, sign=True, block_type="pr"):
        ItemsBlock.__init__(self, items=items, sign=sign, block_type=block_type)
        

    def latex(self, explicit=False, show_plus=False):
        latex_terms = []
        for i in self.items:
            if i.block_type in ("cx", "ch", "py"):
                item_latex = "(%s)" % i.latex(explicit=explicit)

            else:
                item_latex = i.latex(explicit=explicit)

            latex_terms.append(item_latex)
        core_tex = r" \cdot ".join(latex_terms)
        if show_plus or not self.sign:
            return f"{'+' if self.sign else '-'}({core_tex})"
        else:
            return core_tex
