import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.exponentials import exponential
from math_blocks.complex_numbers import complex_number

class complex_number_exponential_test(unittest.TestCase):
    def test_complex_latex(self):
        exp1 = exponential(2,complex_number(3,2),sign=False)
        exp2 = exponential(-complex_number(-1,1), 2)

        self.assertEqual(exp1.latex(), "-2^{3+2i}")
        self.assertEqual(exp2.latex(), "(-(-1+1i))^{2}")

    def test_complex_evaluation(self):
        exp1 = exponential(2,complex_number(3,2),sign=False)
        exp2 = exponential(-complex_number(-1,1), 2)

        self.assertEqual(exp1.evaluate(), -(2**(3+2j)))
        self.assertEqual(exp2.evaluate(), (-(-1+1j))**2)

if __name__ == "__main__":
    unittest.main()
