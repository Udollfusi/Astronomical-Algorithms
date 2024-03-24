#! /usr/bin/python3

'''Test numerical accuracy, etc.'''

import math
import mpmath.libmp
import numpy as np
import sympy as sp
from sympy import sin, N
from mpmath import pi, radians

# normal Python float, typically 64 bits
BIGANGLE_DEGREES_FLOAT = 36000030.
# this is typically the same as a normal Python float
BIGANGLE_DEGREES_FLOAT64 = np.float64(36000030)
# on x86/amd64, this is likely to be 80 bits instead of 64 bits
BIGANGLE_DEGREES_NPLD = np.longdouble(36000030)
# try us some sympy
BIGANGLE_DEGREES_SPFLOAT = sp.Float('36000030', 30)
# try some better sympy
BIGANGLE_RADIANS_SYM = radians(36000030)
# x ∈ [0..2π)
BIGANGLE_MOD_RADIANS_SYM = radians(36000030 % 360)
# x ∈ [0..2π)
BIGANGLE_RADIANS_SYM_MOD = radians(36000030) % (2 * pi)


print('BIGANGLE_DEGREES_\n')
print(f'float:\t\t{BIGANGLE_DEGREES_FLOAT}')
print(f'float64:\t{BIGANGLE_DEGREES_FLOAT64}')
print(f'longdouble:\t{BIGANGLE_DEGREES_NPLD}')
print(f'Float:\t\t{BIGANGLE_DEGREES_SPFLOAT}')

print('\nBIGANGLE_RADIANS_\n')
print(f'sym/mp:\t{N(BIGANGLE_RADIANS_SYM)}')
print(f'sym/mp (x%360):\t{N(BIGANGLE_MOD_RADIANS_SYM)}')
print(f'(sym/mp)%(2π):\t{N(BIGANGLE_RADIANS_SYM_MOD)}')


math_sin: float = math.sin(BIGANGLE_DEGREES_FLOAT)
numpy_sin_float: float = np.sin(BIGANGLE_DEGREES_FLOAT)
numpy_sin_float64: np.float64 = np.sin(BIGANGLE_DEGREES_FLOAT64)
numpy_sin_npld: np.longdouble = np.sin(BIGANGLE_DEGREES_NPLD)
sympy_sin_Float = sin(BIGANGLE_DEGREES_SPFLOAT)
sympy_sin_mp = sin(BIGANGLE_RADIANS_SYM)
sympy_sin_mp_mod = sin(BIGANGLE_MOD_RADIANS_SYM)


print(f'\nsin({BIGANGLE_DEGREES_FLOAT:.0f})\n')
print(f'math.sin:\t\t{math_sin}')
print(f'numpy.sin (float):\t{numpy_sin_float}')
print(f'numpy.sin (float64):\t{numpy_sin_float64}')
print(f'nympy.sin (longdouble):\t{repr(numpy_sin_npld)}')
print(f'sympy.sin (Float):\t{sympy_sin_Float}')
print(f'sympy.sin (mp):\t\t{N(sympy_sin_mp)}')
print(f'sympy.sin (mp):\t\t{N(sympy_sin_mp_mod)}')


print(f'\n\nmpmath backend ("gmpy" preferred over "python"): {mpmath.libmp.BACKEND}')
