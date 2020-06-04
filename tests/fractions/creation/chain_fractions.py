import unittest


from math_blocks.fractions import fraction
from math_blocks.chains import chain

class chain_fraction_test(unittest.TestCase):
    def test_chain_latex(self):
        fr = fraction(chain([3,1]),2)
        self.assertEqual(fr.latex(), "\\frac{3+1}{2}")
        fr2 = fraction(1,-chain([-2,2]), sign=False)
        self.assertEqual(fr2.latex(), "-\\frac{1}{-(-2+2)}")

    def test_chain_eval(self):
        fr = fraction(chain([3,1]), 2)
        self.assertEqual(fr.evaluate(), 2)
        fr2 = fraction(1,-chain([-2,3]), sign=False)
        self.assertEqual(fr2.evaluate(), 1)

    



if __name__ == '__main__':
    unittest.main()
