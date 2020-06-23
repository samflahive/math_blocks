import unittest


from math_blocks.algebra.exponentials import Exponential


class exponential_mul(unittest.TestCase):

    
    def test_number_mul(self):
        main_ex = Exponential(12,2)
        n = 3

        result = main_ex * n
        
        result_latex = "12^{2} \\cdot 3"
        result_value = 432
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_exponential_mul(self):
        main_ex = Exponential(12,2)
        alt_ex = Exponential(12,1)

        result = main_ex * alt_ex
        
        result_latex = "12^{2+1}"
        result_value = 1728
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)



if __name__ == '__main__':
    unittest.main()
