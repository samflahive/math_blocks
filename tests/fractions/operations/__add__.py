import unittest

from math_blocks.algebra.core import Fraction, Number


class fraction_add(unittest.TestCase):

    
    def test_number_add(self):
        main_fr = Fraction(12,2)
        n = Number(3)

        result = main_fr + n
        
        result_latex = "\\frac{12}{2}+3"
        result_value = 9
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_fraction_add(self):
        main_fr = Fraction(12,2)
        alt_fr = Fraction(12,2)

        result = main_fr + alt_fr
        
        result_latex = "\\frac{12+12}{2}"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

        result = main_fr - alt_fr
        
        result_latex = "\\frac{12-12}{2}"
        result_value = 0
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
