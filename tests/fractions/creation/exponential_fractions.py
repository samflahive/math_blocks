import unittest


from math_blocks.fractions import fraction
from math_blocks.exponentials import exponential

class exponential_fraction_test(unittest.TestCase):
    def test_fraction_latex(self):

        exp = exponential(3,2)
        fr = fraction(exp,2)
        
        self.assertEqual(fr.latex(), "\\frac{3^{2}}{2}")
        fr3 = - fraction(exp, exponential(2,2))
        self.assertEqual(fr3.latex(), "-\\frac{3^{2}}{2^{2}}")

    def test_fraction_eval(self):
        exp = exponential(3,2)
        fr = fraction(exp,2)
        
        self.assertEqual(fr.evaluate(), (3**2)/2)
        fr3 = - fraction(exp, exponential(2,2))
        self.assertEqual(fr3.evaluate(), -(3**2)/(2**2))
    



if __name__ == '__main__':
    unittest.main()
