import unittest

from math_blocks.algebra.core import Number
from math_blocks.algebra.exponentials import Logarithm


class log_add(unittest.TestCase):

    
    def test_number_add(self):
        main_log = Logarithm(9,3)
        n = Number(3)

        result = main_log + n
        
        result_latex = "log_{3}9+3"
        result_value = 5
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


    def test_log_add(self):
        main_log = Logarithm(9,3)
        alt_log = Logarithm(27, 3)

        result = main_log + alt_log
        
        result_latex = "log_{3}9 \\cdot 27"
        result_value = 5
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)

        result = main_log - alt_log
        
        #result_latex = "log_{3}0.3333"
        result_value = -1
        
        #self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
