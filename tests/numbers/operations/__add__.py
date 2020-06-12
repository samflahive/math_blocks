import unittest

import math_blocks


class number_add(unittest.TestCase):

    
    def test_number_add(self):
        main_num = math_blocks.number(9)
        n = math_blocks.number(3)

        result = main_num + n
        
        result_latex = "9+3"
        result_value = 12
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)

    def test_variable_add(self):
        main_num = math_blocks.number(9)
        v = math_blocks.variable("v", value=3)

        result = main_num + v
        
        result_latex = "9+v"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


    def test_product_add(self):
        main_num = math_blocks.number(9)
        p = math_blocks.product([1,2,3])

        result = main_num + p
        
        result_latex = "9+(1 \cdot 2 \cdot 3)"
        result_value = 15
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


    def test_poly_eq(self):
        main_num = math_blocks.number(9)
        a = math_blocks.variable("a", value=1)
        p = math_blocks.simple_poly([1,2,3], a)

        result = main_num + p
        
        result_latex = "9+(1a^{2}+2a+3)"
        result_value = 15
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)

    def test_chain_eq(self):
        main_num = math_blocks.number(9)
        alt_chain_b = math_blocks.chain([1,3,2])

        result = main_num + alt_chain_b
        
        result_latex = "9+(1+3+2)"
        result_value = 15
        
        self.assertEqual(result.latex(), result_latex)
        self.assertAlmostEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
