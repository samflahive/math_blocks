import math

import math_blocks

class complex_number(math_blocks.math_block):

    def __init__(self, real, imaginary, sign=True):
        math_blocks.math_block.__init__(self, sign=sign)

        if isinstance(real, (int, float)):
            real = math_blocks.number(real)
        if isinstance(imaginary, (int, float)):
            imaginary = math_blocks.number(imaginary)

        self.real = real
        self.imaginary = imaginary
        self.form = "rect"
        self.radius = None
        self.angle = None

    def evaluate(self):
        r_val, i_val = self.real.evaluate(), self.imaginary.evaluate()
        if i_val == 0:
            val = r_val
        else:
            val = complex(r_val, i_val)
        if self.sign:
            return val
        return -val

    def latex(self, explicit=False, show_plus=False):
        bracket_imag = False
        if isinstance(self.real, (math_blocks.number, math_blocks.variable)):
            real_latex = self.real.latex()
        else:
            real_latex = "(%s)" % self.real.latex()

        if isinstance(self.imaginary, (math_blocks.number, math_blocks.variable)):
            imaginary_latex = self.imaginary.latex()
        else:
            bracket_imag = True
            imaginary_latex = "(%s)" % self.imaginary.latex()

        if self.imaginary.sign or bracket_imag:
            out = "%s+%si" % (real_latex, imaginary_latex)
        else:
            out = "%s%si" % (real_latex, imaginary_latex)

        if not self.sign:
            return "-(%s)" % out
        if show_plus:
            return "+(%s)" % out
        return out

    def check_num_collapsable(self):
        self.num_collapsable = True
        if not self.real.num_collapsable:
            self.real.check_num_collapsable()
            if not self.real.num_collapsable:
                self.num_collapsable = False
                return
        if not self.imaginary.num_collapsable:
            self.imaginary.check_num_collapsable()
            if not self.imaginary.num_collapsable or self.imaginary.evaluate() != 0:
                self.num_collapsable = False

    def __add__(self, other):
        if isinstance(other, complex_number):
            left_real, left_imag = (self.real, self.imaginary) if self.sign else (-self.real, -self.imaginary)
            right_real, right_imag = (other.real, other.imaginary) if other.sign else (-other.real, -other.imaginary)
            return complex_number(left_real+right_real, left_imag+right_imag)
        return math_blocks.chain([self, other])

    def conjugate(self):
        return complex_number(real=self.real, imaginary=-self.imaginary, sign=self.sign)

    def conjugate_product(self):
        return math_blocks.exponential(self.real,2) + math_blocks.exponential(self.imaginary,2)

    def __mul__(self, other):
        if isinstance(other, complex_number):
            real = self.real*other.real - self.imaginary*other.imaginary
            imaginary = self.real*other.imaginary + self.imaginary*other.real
            return complex_number(real=real,  imaginary=imaginary, sign=(self.sign==other.sign))
        
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, complex_number):
            return False
        return (self.real == other.real
                and self.imaginary == other.imaginary
                and self.sign == other.sign)

    @staticmethod
    def from_polar(angle, radius, sign=True):
        real = radius * math.cos(angle)
        imaginary = radius * math.sin(angle)
        cx = math_blocks.complex_number(real, imaginary, sign=sign)

        cx.form = "polar"
        if isinstance(radius, (int, float)):
            radius = math_blocks.number(radius)
        if isinstance(angle, (int, float)):
            angle = math_blocks.number(angle)
            
        cx.radius = radius
        cx.angle = angle
        return cx

    def to_polar(self):
        radius = math.sqrt(self.real.evaluate()**2 + self.imaginary.evaluate()**2)
        angle = math.atan2(self.imaginary.evaluate(), self.real.evaluate())

        return complex_number.from_polar(angle, radius, sign=self.sign)
        
