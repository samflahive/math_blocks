import unittest

from math_blocks.numbers import number
from math_blocks.variables import variable
from math_blocks.exponentials import exponential
from math_blocks.polycomps import polycomp
from math_blocks.polyterms import polyterm
from math_blocks.polynomials import polynomial

class basic_polynomial(unittest.TestCase):
    def test_basic_latex(self):
        #y^2 + 2yz - x^2
        y = variable("y")
        x = variable("x")
        p = polynomial([polyterm(coeff=1, pcomp=polycomp([exponential(y,2)])),
                    polyterm(coeff=2, pcomp=polycomp([exponential(y,1),exponential(x,1)])),
                    polyterm(coeff=-1, pcomp=polycomp([exponential(x,2)]))])
        
        self.assertEqual(p.latex(), "1y^{2}+2yx-1x^{2}")

        self.assertEqual((-p).latex(), "-(1y^{2}+2yx-1x^{2})")

    def test_basic_eval(self):
        y = variable("y")
        x = variable("x")

        p = polynomial([polyterm(coeff=1, pcomp=polycomp([exponential(y,2)])),
                    polyterm(coeff=2, pcomp=polycomp([exponential(y,1),exponential(x,1)])),
                    polyterm(coeff=-1, pcomp=polycomp([exponential(x,2)]))])
        
        
        y.value = 1
        x.value = 1
        self.assertEqual(p.evaluate(), 2)

        self.assertEqual((-p).evaluate(), -2)



if __name__ == '__main__':
    unittest.main()
