import math_blocks

class polyterm(math_blocks.math_block):

    def __init__(self, coeff, pcomp, sign=True):
        if isinstance(coeff, (int,float)):
            coeff = math_blocks.number(coeff)

        # integrate coeff sign into polyterm parent
        sign = sign and coeff.sign
        coeff.sign = True
        
        math_blocks.math_block.__init__(self, sign=sign)
        self.coeff = coeff
        self.pcomp = pcomp

    def latex(self, explicit=False, show_plus=False):
        if not self.sign:
            return "-%s%s" % (self.coeff.latex(explicit=explicit),
                              self.pcomp.latex(explicit=explicit))
        if show_plus:
            return "+%s%s" % (self.coeff.latex(explicit=explicit),
                              self.pcomp.latex(explicit=explicit))
        
        return "%s%s" % (self.coeff.latex(explicit=explicit),
                         self.pcomp.latex(explicit=explicit))

    def evaluate(self):
        out = self.coeff.evaluate() * self.pcomp.evaluate()
        if self.sign:
            return out
        return -out
