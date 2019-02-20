from math_blocks import *
import random

def algebra_AAA0():
    # a(x+h)^2+c = quadratic, find a, h, c
    x = variables.variable("x")
    a = random.randint(-20,20)
    h = random.randint(-20,20)
    c = random.randint(-20,20)
    
    quad = quadratics.quadratic(coeffs=[a,2*a*h, (h*h)+c], variable=x)

    print("a(x+h)^2 + c = {}\nFind a, h, c".format(quad.latex()))
