from . import core
import math_blocks.constants
import math
import copy

# uses MathBlock, Number, Exponential
class Exponential(core.MathBlock):
     
    def __init__(self, base, power, sign=True, block_type="ex", num_collapsable=False):
          core.MathBlock.__init__(self, sign=sign, block_type=block_type, num_collapsable=num_collapsable)

          # replace python Numbers with mathblock Numbers
          if isinstance(base, (int, float)):
               base = core.Number(base)
          if isinstance(power, (int, float)):
               power = core.Number(power)
               
          self.base = base
          self.power = power

    def evaluate(self):
        # extract the value of the base whether its a Number or variable
        base_value = self.base.evaluate()
        power_value = self.power.evaluate()
        val = base_value**power_value
        return val if self.sign else -val

    def latex(self, explicit=False, show_zero_power=True, show_plus=False):
        base_symbol = self.base.latex(explicit=explicit)
        if not self.base.sign or not self.base.block_type in ("nm", "vr"):
            base_symbol = "(%s)" % base_symbol
               
        power_symbol = self.power.latex(explicit=explicit)
          
        if explicit:
            out = "{}^{{{}}}".format(base_symbol, power_symbol)
        else:
            if self.power == 0:
                out = "1" if show_zero_power else ""
            elif self.power == 1:
                out = "{}".format(base_symbol)
            else:
                out = "{}^{{{}}}".format(base_symbol, power_symbol)

        if not self.sign:
            return "-%s" % out
        if show_plus:
            return "+%s" % out
        return out

    def __eq__(self, other):
        if not isinstance(other, Exponential):
            return False
        return (self.base == other.base
                and self.power == other.power
                and self.sign == other.sign)

    def __mul__(self, other):
        if isinstance(other, Exponential) and self.base == other.base:
            return Exponential(self.base, self.power+other.power, sign=(self.sign == other.sign))                    
        return core.MathBlock.__mul__(self, other)

    def __truediv__(self, other):
        if isinstance(other, Exponential) and self.base == other.base:
            return Exponential(self.base, self.power-other.power, sign=(self.sign == other.sign))
        return core.MathBlock.__truediv__(self, other)

    def rebase(self, base):
        power = self.power * Logarithm(self.base, base)
        return Exponential(base=base, power=power, sign=self.sign)

    def equiv_num(self):
        num = core.combine_to_num(self.base, self.power)
        if not num:
            num = self.base.equiv_num() and self.power.equiv_num()
        self.num_collapsable = num
        return num
               

# uses Number, ComplexNumber, Logarithm
class Logarithm(core.MathBlock):
    
    def __init__(self, exponent, base, sign=True, block_type="lg", num_collapsable=False):
        core.MathBlock.__init__(self, sign=sign, block_type=block_type)

        self.eval_complex_flag = False
        
        if isinstance(base, (int, float)):
            base = core.Number(base)
        elif isinstance(base, ComplexNumber):
            self.eval_complex_flag = True
            
        if isinstance(exponent, (int, float)):
            exponent = core.Number(exponent)
        elif isinstance(exponent, ComplexNumber):
            self.eval_complex_flag = True
            
        self.exponent = exponent
        self.base = base

    def evaluate(self):
        if self.eval_complex_flag:
            raise ValueError("evaluated Logarithms cannot contain complex Numbers")
        
        exponent_value = self.exponent.evaluate()
        base_value = self.base.evaluate()
        value_out =  math.log(exponent_value, base_value)

        # correct value out for machine artifacts
        if exponent_value**round(value_out) == base_value:
            value_out = round(value_out)
        
        return value_out if self.sign else -value_out
    
    def latex(self, explicit=False, show_plus=False):
        if isinstance(self.base, math_blocks.constants.Constant) and self.base.symbol == "e":
            return self.ln_latex(explicit=explicit, show_plus=show_plus)
        else:
            return self.log_latex(explicit=explicit, show_plus=show_plus)

    def ln_latex(self, explicit=False, show_plus=False):
        exponent_symbol = self.exponent.latex()
        if explicit:
            out = "ln(%s)" % exponent_symbol
        else:
            out = "ln%s" % exponent_symbol
        if not self.sign:
            return "-%s" % out
        if show_plus:
            return "+%s" % out
        return out

    def log_latex(self, explicit=False, show_plus=False):
        exponent_symbol = self.exponent.latex()
        base_symbol = self.base.latex()
        if explicit:
            out = "log_{%s}(%s)" % (base_symbol, exponent_symbol)
        else:
            out = "log_{%s}%s" % (base_symbol, exponent_symbol)
        if not self.sign:
            return "-%s" % out
        if show_plus:
            return "+%s" % out
        return out

    def __eq__(self, other):
        if not isinstance(other, Logarithm):
            return False

        return (self.base == other.base
                and self.exponent == other.exponent
                and self.sign == other.sign)

    def __add__(self, other):
        if isinstance(other, Logarithm) and other.base == self.base:
            if other.sign == self.sign:
                return Logarithm(base=self.base, exponent=self.exponent*other.exponent, sign=self.sign)
            elif not self.sign:
                return Logarithm(base=self.base, exponent=other.exponent/self.exponent)
            else:
                return Logarithm(base=self.base, exponent=self.exponent/other.exponent)
        return core.MathBlock.__add__(self, other)


    def equiv_num(self):
        num = core.combine_to_num(self.base, self.exponent)
        if not num:
            num = self.base.equiv_num() and self.exponent.equiv_num()
        self.num_collapsable = num
        return num
        
        

#  uses MathBlocks, Number, ComplexNumber, Exponential
class ComplexNumber(core.MathBlock):

    def __init__(self, real, imaginary, sign=True, block_type="cx", num_collapsable=False):
        core.MathBlock.__init__(self, sign=sign, block_type=block_type, num_collapsable=num_collapsable)

        if isinstance(real, (int, float)):
            real = core.Number(real)
        if isinstance(imaginary, (int, float)):
            imaginary = core.Number(imaginary)

        self.real = real
        self.imaginary = imaginary
        self.form = "rect"
        self.radius = None
        self.angle = None

    def evaluate(self):
        val = complex(self.real.evaluate(), self.imaginary.evaluate())
        if self.sign:
            return val
        return -val

    def latex(self, explicit=False, show_plus=False):
        bracket_imag = False
        if self.real.block_type in ("nm", "vr"):
            real_latex = self.real.latex()
        else:
            real_latex = "(%s)" % self.real.latex()

        if self.imaginary.block_type in ("nm", "vr"):
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

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            left_real, left_imag = (self.real, self.imaginary) if self.sign else (-self.real, -self.imaginary)
            right_real, right_imag = (other.real, other.imaginary) if other.sign else (-other.real, -other.imaginary)
            return ComplexNumber(left_real+right_real, left_imag+right_imag)
        return core.MathBlock.__add__(self, other)

    def conjugate(self):
        return ComplexNumber(real=self.real, imaginary=-self.imaginary, sign=self.sign)

    def conjugate_product(self):
        return Exponential(self.real,2) + Exponential(self.imaginary,2)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real*other.real - self.imaginary*other.imaginary
            imaginary = self.real*other.imaginary + self.imaginary*other.real
            return ComplexNumber(real=real,  imaginary=imaginary, sign=(self.sign==other.sign))
        
        return core.MathBlock.__mul__(self, other)

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            return False
        return (self.real == other.real
                and self.imaginary == other.imaginary
                and self.sign == other.sign)

    def fraction_split(self, denominator, sign):
        # -(-(3+2i)/2) --> -(-(3/2)-(2/2)i)
        real = core.Fraction(self.real, denominator, sign=self.sign)
        imaginary = core.Fraction(self.imaginary, denominator, sign=self.sign)
        return ComplexNumber(real=real, imaginary=imaginary, sign=sign)


    @staticmethod
    def from_polar(angle, radius, sign=True):
        real = radius * math.cos(angle)
        imaginary = radius * math.sin(angle)
        cx = ComplexNumber(real, imaginary, sign=sign)

        cx.form = "polar"
        if isinstance(radius, (int, float)):
            radius = core.Number(radius)
        if isinstance(angle, (int, float)):
            angle = core.Number(angle)
            
        cx.radius = radius
        cx.angle = angle
        return cx

    def to_polar(self):
        radius = math.sqrt(self.real.evaluate()**2 + self.imaginary.evaluate()**2)
        angle = math.atan2(self.imaginary.evaluate(), self.real.evaluate())

        return ComplexNumber.from_polar(angle, radius, sign=self.sign)
        
    def equiv_num(self):
        num = core.combine_to_num(self.real, self.imaginary)
        if not num:
            num = self.real.equiv_num() and self.imaginary.equiv_num()
        self.num_collapsable = num
        return num