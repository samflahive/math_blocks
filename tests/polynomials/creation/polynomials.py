import unittest


from math_blocks.algebra.exponentials import Exponential
from math_blocks.algebra.polynomials import *

class basic_polynomial(unittest.TestCase):
    def test_basic_latex(self):
        #y^2 + 2yz - x^2
        y = Variable("y")
        x = Variable("x")
        p = Polynomial([PolyTerm(coeff=1, pcomp=PolyComp([Exponential(y,2)])),
                    PolyTerm(coeff=2, pcomp=PolyComp([Exponential(y,1),Exponential(x,1)])),
                    PolyTerm(coeff=-1, pcomp=PolyComp([Exponential(x,2)]))])
        
        self.assertEqual(p.latex(), "1y^{2}+2yx-1x^{2}")

        self.assertEqual((-p).latex(), "-(1y^{2}+2yx-1x^{2})")

    def test_basic_eval(self):
        y = Variable("y")
        x = Variable("x")

        p = Polynomial([PolyTerm(coeff=1, pcomp=PolyComp([Exponential(y,2)])),
                    PolyTerm(coeff=2, pcomp=PolyComp([Exponential(y,1),Exponential(x,1)])),
                    PolyTerm(coeff=-1, pcomp=PolyComp([Exponential(x,2)]))])
        
        
        y.value = 1
        x.value = 1
        self.assertEqual(p.evaluate(), 2)

        self.assertEqual((-p).evaluate(), -2)



if __name__ == '__main__':
    unittest.main()
