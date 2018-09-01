from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise ZeroDivisionError("Denominator may not be zero.")
        divisor = self.greatest_common_divisor(numer, denom)
        self.numer = numer / divisor
        self.denom = denom / divisor

    def greatest_common_divisor(self, a, b):
        if b == 0:
            return a
        else:
            return self.greatest_common_divisor(b, a % b)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = (self.numer * other.denom) - (other.numer * self.denom)
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if other.numer * self.denom == 0:
            raise ZeroDivisionError("Denominator may not be zero.")
        return Rational(self.numer * other.denom, other.numer * self.denom)

    def __abs__(self):
        return(Rational(abs(self.numer), abs(self.denom)))

    def __pow__(self, power):
        return(Rational(self.numer ** power, self.denom ** power))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
