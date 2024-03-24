'''
Calculations from Astronomical Algorithms by Jean Meeus, second edition

Utility functions
'''

import mpmath.libmp
from mpmath import radians


def degrees_to_radians(d):
    'Convert deg to radians, first by adjusting deg ∈ [0..360)'
    return radians(d % 360)


def dms_to_degrees(d, m, s):
    'Convert degrees, minutes, seconds to decimal degrees'
    return (s / 3600) + (m / 60) + d


def mpmath_using_gmp() -> bool:
    '''
    Check whether mpmath is using the gmpy backend.
    gmpy is the Python wrapper around GMP.
    '''
    return mpmath.libmp.BACKEND == 'gmpy'


def mpmath_using_python() -> bool:
    'Check whether mpmath is using the python backend'
    return mpmath.libmp.BACKEND == 'python'
