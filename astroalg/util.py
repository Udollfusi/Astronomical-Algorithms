'''
Calculations from Astronomical Algorithms by Jean Meeus, second edition

Utility functions
'''

from mpmath import radians

def degrees_to_radians(deg):
    'Convert deg to radians, first by adjusting deg ∈ [0..360)'
    return radians(deg % 360)
