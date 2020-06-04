import unittest


from math_blocks.fractions import fraction
from math_blocks.logarithms import logarithm
from math import log

class logarithm_fraction_test(unittest.TestCase):
    def test_logarithm_latex(self):
        # test the latex expression for fractions with numbers only
        fr = fraction(3,logarithm(3,2))
        self.assertEqual(fr.latex(), "\\frac{3}{log_{2}3}")
        fr2 = fraction(-2,-logarithm(3,2), sign=False)
        self.assertEqual(fr2.latex(), "-\\frac{-2}{-log_{2}3}")

    def test_logarithm_eval(self):
        fr = fraction(3,logarithm(3,2))
        self.assertEqual(fr.evaluate(), 3/log(3,2))
        fr2 = fraction(-2,-logarithm(3,2), sign=False)
        self.assertEqual(fr2.evaluate(), -2/log(3,2))

    



if __name__ == '__main__':
    unittest.main()
