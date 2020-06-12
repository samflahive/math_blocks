import unittest

import math_blocks


class fraction_add(unittest.TestCase):

    
    def test_number_add(self):
        main_fr = math_blocks.fraction(12,2)
        n = math_blocks.number(3)

        result = main_fr + n
        
        result_latex = "\\frac{12}{2}+3"
        result_value = 9
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_variable_add(self):
        main_fr = math_blocks.fraction(12,2)
        v = math_blocks.variable("v", value=3)

        result = main_fr + v
        
        result_latex = "\\frac{12}{2}+v"
        result_value = 9
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_product_add(self):
        main_fr = math_blocks.fraction(12,2)
        p = math_blocks.product([1,2,3])

        result = main_fr + p
        
        result_latex = "\\frac{12}{2}+(1 \cdot 2 \cdot 3)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_poly_add(self):
        main_fr = math_blocks.fraction(12,2)
        a = math_blocks.variable("a", value=1)
        p = math_blocks.simple_poly([1,2,3], a)

        result = main_fr + p
        
        result_latex = "\\frac{12}{2}+(1a^{2}+2a+3)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_chain_add(self):
        main_fr = math_blocks.fraction(12,2)
        alt_chain_b = math_blocks.chain([1,3,2])

        result = main_fr + alt_chain_b
        
        result_latex = "\\frac{12}{2}+(1+3+2)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_fraction_add(self):
        main_fr = math_blocks.fraction(12,2)
        alt_fr = math_blocks.fraction(12,2)

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
