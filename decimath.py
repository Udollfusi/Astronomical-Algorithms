#! /usr/bin/python3

'''
Decimal math

Some functions based on examples in the Python 3.11 library reference.
'''

from decimal import Decimal, getcontext, localcontext

_ZERO: Decimal = Decimal(0)
_ONE: Decimal = Decimal(1)
_TWO: Decimal = Decimal(2)
_THREE: Decimal = Decimal(3)


def pi() -> Decimal:
    'Compute π to the current precision'
    prec: int = getcontext().prec
    with localcontext() as ctx:
        ctx.prec = prec + 2  # increase precision for intermediate steps
        lasts: Decimal = _ZERO
        t: Decimal = _THREE
        s: Decimal = _THREE
        n = 1
        na = 0
        d = 0
        da = 24
        while s != lasts:
            lasts = s
            n: int = n + na
            na: int = na + 8
            d: int = d + da
            da: int = da + 32
            t = (t * n) / d
            s += t
    return +s  # round back to the default precision


def cos(x: Decimal) -> Decimal:
    'Return the cosine of x as measured in radians'
    prec: int = getcontext().prec
    with localcontext() as ctx:
        ctx.prec = prec + 2  # increase precision for intermediate steps
        
        # x ∈ [0..2π) --- improve Taylor series accuracy
        twopi: Decimal = _TWO * pi()
        if x >= twopi or x < _ZERO:
            x = x % twopi

        i: Decimal = _ZERO
        lasts: Decimal = _ZERO
        s: Decimal = _ONE
        fact: Decimal = _ONE
        num: Decimal = _ONE
        while s != lasts:
            lasts = s
            i += 1
            fact *= i
            num *= x
            s += num / fact
    return +s  # round back to the default precision


def exp(x: Decimal) -> Decimal:
    'Return e raised to the power of x'
    prec: int = getcontext().prec
    with localcontext() as ctx:
        ctx.prec = prec + 2  # increase precision for intermediate steps
        i: Decimal = _ZERO
        lasts: Decimal = _ZERO
        s: Decimal = _ONE
        fact: Decimal = _ONE
        num: Decimal = _ONE
        while s != lasts:
            lasts = s
            i += 1
            fact *= i
            num *= x
            s += num / fact
    return +s  # round back to the default precision


def sin(x: Decimal) -> Decimal:
    'Return the sine of x as measured in radians'
    prec: int = getcontext().prec
    with localcontext() as ctx:
        ctx.prec = prec + 2  # increase precision for intermediate steps

        # x ∈ [0..2π) --- improve Taylor series accuracy
        twopi: Decimal = _TWO * pi()
        if x >= twopi or x < _ZERO:
            x = x % twopi

        i: Decimal = _ONE
        lasts: Decimal = _ZERO
        s: Decimal = x
        fact: Decimal = _ONE
        num: Decimal = x
        sign: Decimal = _ONE
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i-1)
            num *= x * x
            sign *= -1
            s += num / fact * sign
    return +s  # round back to the default precision
