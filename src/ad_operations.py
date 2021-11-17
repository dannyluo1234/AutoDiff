import math
import numpy as np
from dual_temp import dual

class ad_operations:
    def sin(other):
        if isinstance(other, float) or isinstance(other, int):
            return math.sin(other)
        elif isinstance(other, dual):
            return dual(math.sin(other.val), math.cos(other.val) * other.der)
        else:
            raise TypeError

    def cos(other):
        if isinstance(other, float) or isinstance(other, int):
            return math.cos(other)
        elif isinstance(other, dual):
            return dual(math.cos(other.val), -math.sin(other.val) * other.der)
        else:
            raise TypeError

    def tan(other):
        if isinstance(other, float) or isinstance(other, int):
            return math.tan(other)
        elif isinstance(other, dual):
            return dual(math.tan(other.val), 1 / (math.cos(other.val) ** 2) * other.der)
        else:
            raise TypeError

    def arcsin(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.arcsin(other)
        elif isinstance(other, dual):
            return dual(np.arcsin(other.val), (1 / (1-other.val**2)**0.5) * other.der)
        else:
            raise TypeError

    def arccos(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.arccos(other)
        elif isinstance(other, dual):
            return dual(np.arccos(other.val), -(1 / (1-other.val**2)**0.5) * other.der)
        else:
            raise TypeError

    def arctan(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.arctan(other)
        elif isinstance(other, dual):
            return dual(np.arctan(other.val), (1 / (1+other.val**2)) * other.der)
        else:
            raise TypeError

    def sinh(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.sinh(other)
        elif isinstance(other, dual):
            return dual(np.sinh(other.val), np.cosh(other.val) * other.der)
        else:
            raise TypeError

    def cosh(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.cosh(other)
        elif isinstance(other, dual):
            return dual(np.cosh(other.val), np.sinh(other.val) * other.der)
        else:
            raise TypeError

    def tanh(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.tanh(other)
        elif isinstance(other, dual):
            return dual(np.tanh(other.val), (1 / np.cosh(other.val)**2) * other.der)
        else:
            raise TypeError

    def arcsinh(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.arcsinh(other)
        elif isinstance(other, dual):
            return dual(np.arcsinh(other.val), (1 / (other.val**2 + 1)**0.5) * other.der)
        else:
            raise TypeError

    def arccosh(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.arccosh(other)
        elif isinstance(other, dual):
            return dual(np.arccosh(other.val), (1 / (other.val**2 - 1)**0.5) * other.der)
        else:
            raise TypeError

    def arctanh(other):
        if isinstance(other, float) or isinstance(other, int):
            return np.arctanh(other)
        elif isinstance(other, dual):
            return dual(np.arctanh(other.val), (1 / (1-other.val**2)) * other.der)
        else:
            raise TypeError

    def exp(other):
        if isinstance(other, float) or isinstance(other, int):
            return math.exp(other)
        elif isinstance(other, dual):
            return dual(math.exp(other.val), math.exp(other.val) * other.der)
        else:
            raise TypeError
