import unittest

from math_blocks.algebra.core import Number, Fraction


class fraction_mul(unittest.TestCase):

    
    def test_number_mul(self):
        main_fr = Fraction(12,2)
        n = Number(3)

        result = main_fr * n
        
        result_latex = "\\frac{12}{2} \\cdot 3"
        result_value = 18
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_fraction_mul(self):
        main_fr = Fraction(12,2)
        alt_fr = Fraction(12,2)

        result = main_fr * alt_fr
        
        result_latex = "\\frac{12 \\cdot 12}{2 \\cdot 2}"
        result_value = 36
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

        result = main_fr * -alt_fr
        
        result_latex = "-\\frac{12 \\cdot 12}{2 \\cdot 2}"
        result_value = -36
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
