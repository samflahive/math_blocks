import unittest

from math_blocks.algebra.exponentials import Exponential


class exponential_div(unittest.TestCase):

    
    def test_number_div(self):
        main_ex = Exponential(12,2)
        n = 3

        result = main_ex / n
        
        result_latex = "\\frac{12^{2}}{3}"
        result_value = 48
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_exponential_div(self):
        main_ex = Exponential(12,2)
        alt_ex = Exponential(12,1)

        result = main_ex / alt_ex
        
        result_latex = "12^{2-1}"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)




if __name__ == '__main__':
    unittest.main()
