import unittest
from math import log


from math_blocks.logarithms import logarithm
from math_blocks.complex_numbers import complex_number


class complex_logarithm_test(unittest.TestCase):
    def test_complex_latex(self):
        c1 = complex_number(3, 2)
        loga = logarithm(c1, 3)
        self.assertEqual(loga.latex(), "log_{3}3+2i")

    def test_complex_eval(self):
        c1 = complex_number(3, 2)
        loga = logarithm(c1, 3)
        self.assertRaises(ValueError, loga.evaluate)

if __name__ == '__main__':
    unittest.main()
