import unittest

from math_blocks.algebra.core import Number, Fraction


class fraction_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_fr = Fraction(1,2)
        n = Number(3)
        self.assertEqual(False, main_fr == n)

    

    def test_fraction_eq(self):
        main_fr = Fraction(1,2)
        alt_fr = Fraction(1,2, sign=False)

        self.assertEqual(False, main_fr == alt_fr)
        self.assertEqual(True, main_fr == -alt_fr)
        
if __name__ == '__main__':
    unittest.main()
