import unittest

import math_blocks


class poly_add(unittest.TestCase):

    
    def test_number_add(self):
        x = math_blocks.variable("x", value=1)
        main_poly = math_blocks.simple_poly([1,2,3], x)
        
        n = math_blocks.number(3)

        result = main_poly + n
        
        result_latex = "1x^{2}+2x+3+3"
        result_value = 9
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_variable_add(self):
        x = math_blocks.variable("x", value=1)
        main_poly = math_blocks.simple_poly([1,2,3], x)
        
        v = math_blocks.variable("v", value=3)

        result = main_poly + v
        
        result_latex = "1x^{2}+2x+3+v"
        result_value = 9
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_product_add(self):
        x = math_blocks.variable("x", value=1)
        main_poly = math_blocks.simple_poly([1,2,3], x)
        
        p = math_blocks.product([1,2,3])

        result = main_poly + p
        
        result_latex = "1x^{2}+2x+3+(1 \cdot 2 \cdot 3)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_poly_eq(self):
        x = math_blocks.variable("x", value=1)
        main_poly = math_blocks.simple_poly([1,2,3], x)
        
        a = math_blocks.variable("a", value=1)
        p = math_blocks.simple_poly([1,2,3], a)

        result = main_poly + p
        
        result_latex = "1x^{2}+2x+3+1a^{2}+2a+3"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_chain_eq(self):
        x = math_blocks.variable("x", value=1)
        main_poly = math_blocks.simple_poly([1,2,3], x)
        
        alt_chain_b = math_blocks.chain([1,3,2])

        result = main_poly + alt_chain_b
        
        result_latex = "1x^{2}+2x+3+(1+3+2)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_complex_eq(self):
        x = math_blocks.variable("x", value=1)
        main_poly = math_blocks.simple_poly([1,2,3], x)
        
        a = math_blocks.complex_number(2,3)

        result = main_poly + a
        
        result_latex = "1x^{2}+2x+3+(2+3i)"
        result_value = complex(8,3)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
