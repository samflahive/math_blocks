import unittest
import math
from math_blocks.complex_numbers import complex_number

class polar_complex_test(unittest.TestCase):
    def test_from_polar(self):
        c1 = complex_number.from_polar(math.pi/4, 10)
        arm = 10/math.sqrt(2)
        result_eval = complex(arm,arm)
        self.assertAlmostEqual(c1.evaluate(), result_eval)


    def test_to_polar(self):
        arm = 10/math.sqrt(2)
        c1 = complex_number(arm, arm).to_polar()
        
        self.assertAlmostEqual(c1.angle, math.pi/4)
        self.assertEqual(c1.radius, 10)


if __name__ == '__main__':
    unittest.main()

