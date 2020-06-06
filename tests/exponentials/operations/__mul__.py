import unittest

import math_blocks


class exponential_mul(unittest.TestCase):

    
    def test_number_mul(self):
        main_ex = math_blocks.exponential(12,2)
        n = math_blocks.number(3)

        result = main_ex * n
        
        result_latex = "12^{2} \\cdot 3"
        result_value = 432
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_exponential_mul(self):
        main_ex = math_blocks.exponential(12,2)
        alt_ex = math_blocks.exponential(12,1)

        result = main_ex * alt_ex
        
        result_latex = "12^{3}"
        result_value = 1728
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_product_mul(self):
        main_ex = math_blocks.exponential(12,2)
        p = math_blocks.product([1,2,3])

        result = main_ex * p
        
        result_latex = "12^{2} \\cdot 1 \cdot 2 \cdot 3"
        result_value = 864
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)



if __name__ == '__main__':
    unittest.main()
