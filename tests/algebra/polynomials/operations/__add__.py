import unittest

from math_blocks.algebra.polynomials import SimplePoly, Variable
from math_blocks.algebra.core import Chain, Number


class poly_add(unittest.TestCase):

    
    def test_number_add(self):
        x = Variable("x", value=1)
        main_poly = SimplePoly([1,2,3], x)
        
        n = Number(3)

        result = main_poly + n
        
        result_latex = "1x^{2}+2x+3+3"
        result_value = 9
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_poly_eq(self):
        x = Variable("x", value=1)
        main_poly = SimplePoly([1,2,3], x)
        
        a = Variable("a", value=1)
        p = SimplePoly([1,2,3], a)

        result = main_poly + p
        
        result_latex = "1x^{2}+2x+3+1a^{2}+2a+3"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_chain_eq(self):
        x = Variable("x", value=1)
        main_poly = SimplePoly([1,2,3], x)
        
        alt_chain_b = Chain([1,3,2])

        result = main_poly + alt_chain_b
        
        result_latex = "1x^{2}+2x+3+(1+3+2)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)



if __name__ == '__main__':
    unittest.main()
