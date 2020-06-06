import unittest

import math_blocks


class complex_add(unittest.TestCase):

    
    def test_number_add(self):
        main_cx = math_blocks.complex(2,3)
        n = math_blocks.number(3)

        result = main_cx + n
        
        result_latex = "(2+3j)+3"
        result_value = complex(5,3)
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_variable_add(self):
        main_cx = math_blocks.complex(2,3)
        v = math_blocks.variable("v", value=3)

        result = main_cx + v
        
        result_latex = "(2+3j)+v"
        result_value = complex(5,3)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_product_add(self):
        main_cx = math_blocks.complex(2,3)
        p = math_blocks.product([1,2,3])

        result = main_cx + p
        
        result_latex = "(2+3j)+(1 \cdot 2 \cdot 3)"
        result_value = complex(8,3)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


    def test_poly_eq(self):
        main_cx = math_blocks.complex(2,3)
        a = math_blocks.variable("a", value=1)
        p = math_blocks.simple_poly([1,2,3], a)

        result = main_cx + p
        
        result_latex = "(2+3j)+(1a^{2}+2a+3)"
        result_value = complex(8,3)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_chain_eq(self):
        main_cx = math_blocks.complex(2,3)
        alt_chain_b = math_blocks.chain([1,3,2])

        result = main_cx + alt_chain_b
        
        result_latex = "(2+3j)+(1+3+2)"
        result_value = complex(8,3)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

    def test_complex_eq(self):
        main_cx = math_blocks.complex(2,3)
        a = math_blocks.complex(2,3)

        result = main_cx + a
        
        result_latex = "4+6j"
        result_value = complex(4,6)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)

        result = main_cx - a
        
        result_latex = "0+0j"
        result_value = complex(0,0)
        
        self.assertEqual(result.latex(), result_latex)
        self.assertEqual(result.evaluate(), result_value)


if __name__ == '__main__':
    unittest.main()
