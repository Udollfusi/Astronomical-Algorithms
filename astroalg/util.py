'''
Calculations from Astronomical Algorithms by Jean Meeus, second edition

Utility functions
'''

import mpmath.libmp
from mpmath import radians


def degrees_to_radians(deg):
    'Convert deg to radians, first by adjusting deg ∈ [0..360)'
    return radians(deg % 360)


def mpmath_using_python() -> bool:
    'Check whether mpmath is using the python backend'
    return mpmath.libmp.BACKEND == 'python'


def mpmath_using_gmp() -> bool:
    '''
    Check whether mpmath is using the gmpy backend.
    gmpy is the Python wrapper around GMP.
    '''
    return mpmath.libmp.BACKEND == 'gmpy'
