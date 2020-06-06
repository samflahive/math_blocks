import unittest

import math_blocks


class chain_add(unittest.TestCase):

    
    def test_number_add(self):
        main_chain = math_blocks.chain([1,2,3])
        n = math_blocks.number(3)

        result = main_chain + n
        
        result_latex = "1+2+3+3"
        result_value = 9
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_variable_add(self):
        main_chain = math_blocks.chain([1,2,3])
        v = math_blocks.variable("v", value=3)

        result = main_chain + v
        
        result_latex = "1+2+3+v"
        result_value = 9
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_product_add(self):
        main_chain = math_blocks.chain([1,2,3])
        p = math_blocks.product([1,2,3])

        result = main_chain + p
        
        result_latex = "1+2+3+(1 \cdot 2 \cdot 3)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_poly_eq(self):
        main_chain = math_blocks.chain([1,2,3])
        a = math_blocks.variable("a", value=1)
        p = math_blocks.simple_poly([1,2,3], a)

        result = main_chain + p
        
        result_latex = "1+2+3+(1a^{2}+2a+3)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_chain_eq(self):
        main_chain = math_blocks.chain([1,2,3])
        alt_chain_b = math_blocks.chain([1,3,2])

        result = main_chain + alt_chain_b
        
        result_latex = "1+2+3+(1+3+2)"
        result_value = 12
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
