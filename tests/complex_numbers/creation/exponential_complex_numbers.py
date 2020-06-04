import unittest

from math_blocks.complex_numbers import complex_number
from math_blocks.exponentials import exponential


class exponential_complex_test(unittest.TestCase):
    def test_exponential_latex(self):
        exp1 = exponential(3,2)
        c1 = complex_number(exp1,exp1)
        self.assertEqual(c1.latex(), "(3^{2})+(3^{2})i")

        exp2 = exponential(-3,2, sign=False)
        c1 = complex_number(exp2, exp2)
        self.assertEqual(c1.latex(), "(-(-3)^{2})+(-(-3)^{2})i")

    def test_exponential_eval(self):
        exp1 = exponential(3,2)
        c1 = complex_number(exp1,exp1)
        self.assertEqual(c1.evaluate(), complex((3**2),(3**2)))

        exp2 = exponential(-3,2, sign=False)
        c1 = complex_number(exp2, exp2)
        self.assertEqual(c1.evaluate(), complex(-((-3)**2),-((-3)**2)))


if __name__ == '__main__':
    unittest.main()
