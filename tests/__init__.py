import unittest

# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from chains import *
from complex_numbers import *
from exponentials import *
from fractions import *
from logarithms import *
from numbers import *
from polynomials import *
from products import *
from variables import *

if __name__ == '__main__':
    unittest.main()
