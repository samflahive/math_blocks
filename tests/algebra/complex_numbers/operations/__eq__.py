import unittest

from math_blocks.algebra.core import Number
from math_blocks.algebra.exponentials import ComplexNumber


class complex_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_cx = ComplexNumber(1,2)
        n = Number(3)
        self.assertEqual(False, main_cx == n)

    def test_complex_eq(self):
        main_cx = ComplexNumber(1,2)
        alt_cx_1 = ComplexNumber(1,2)
        alt_cx_2 = ComplexNumber(1,-2)

        self.assertEqual(True, main_cx == alt_cx_1)
        self.assertEqual(False, main_cx == alt_cx_2)

if __name__ == '__main__':
    unittest.main()
