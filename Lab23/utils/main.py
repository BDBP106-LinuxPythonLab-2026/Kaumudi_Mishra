from utils import math_utils
from utils import string_utils

a,b=34,45
print("addition",math_utils.add(a,b))
print("subtraction",math_utils.subtract(a,b))
print("multiplication",math_utils.multiply(a,b))
print("division",math_utils.divide(a,b))
print("remainder",math_utils.remainder(a,b))

text='helLo Bdbh'
s1='BDBH'
s2='101'
print("lower to upper",string_utils.lower_upper(text))
print("upper to lower",string_utils.upper_lower(text))
print("concatenate",string_utils.concatenate(s1,s2))