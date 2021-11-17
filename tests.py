import pytest
import numpy as np
from src.dual_temp import *

import math
tolerance = 0.000000001


def test_init():
    with pytest.raises(TypeError):
        x = Dual("Here is a string")


def test_add_radd():
# test addition of two Dual numbers
    x = Dual(5, 1)
    y = Dual(8, 3)
    f = x + y
    assert f.val == 13, Exception(f"test_add_radd has error with two Dual numbers")
    assert f.der == 4, Exception(f"test_add_radd has error with two Dual numbers")

# test reverse addition of two Dual numbers
    f_rev = y + x
    assert f_rev.val == 13, Exception(f"test_add_radd has error with reverse")
    assert f_rev.der == 4, Exception(f"test_add_radd has error with reverse")


# test addition of a Dual and non-Dual number
    x = 5
    y = Dual(8, 3)
    f = x + y
    assert f.val == 13, Exception(f"test_add_radd has error with nonDual")
    assert f.der == 3,Exception(f"test_add_radd has error with nonDual")

# test reverse addition of a Dual and non-Dual number
    f_rev = y + x
    assert f_rev.val == 13, Exception(f"test_add_radd has error with reverse and nonDual")
    assert f_rev.der == 3, Exception(f"test_add_radd has error with reverse and nonDual")


# test addition of x and x**2
    x = Dual(5, 1)
    y = x*x
    f = x + y
    assert f.val == 30, Exception(f"test_add_radd has error")
    assert f.der == 11, Exception(f"test_add_radd has error")


def test_mul_rmul():
# test multiplication of two Dual numbers
    x = Dual(5, 1)
    y = Dual(8, 1)
    f = x*y
    assert f.val == 40, Exception(f"test_mul_rmul has error")
    assert f.der == 13, Exception(f"test_mul_rmul has error")

# test reverse multiplication of two Dual numbers
    f_rev = y*x
    assert f_rev.val == 40, Exception(f"test_mul_rmul has error")
    assert f_rev.der == 13, Exception(f"test_mul_rmul has error")


# test multiplication of a Dual and non-Dual number
    x = Dual(5, 1)
    y = 3
    f = x*y
    assert f.val == 15, Exception(f"test_mul_rmul has error")
    assert f.der == 3, Exception(f"test_mul_rmul has error")

# test reverse multiplication of a Dual and non-Dual number
    f_rev = y*x
    assert f_rev.val == 15, Exception(f"test_mul_rmul has error")
    assert f_rev.der == 3, Exception(f"test_mul_rmul has error")

# test multiplication of x and x**2
    x = Dual(5,1)
    y = x*x
    f = x*y
    assert f.val == 125, Exception(f"test_mul_rmul has error")
    assert f.der == 75, Exception(f"test_mul_rmul has error")


def test_sub_rsub():
# test subtraction between two Dual numbers
    x = Dual(5, 1)
    y = Dual(8, 2)
    f = x-y
    assert f.val == -3, Exception(f"test_sub_rsub has error")
    assert f.der == -1, Exception(f"test_sub_rsub has error")

# test reverse subtraction between two Dual numbers
    f_rev = y-x
    assert f_rev.val == 3, Exception(f"test_sub_rsub has error")
    assert f_rev.der == 1, Exception(f"test_sub_rsub has error")

# test subtraction between a Dual and non-Dual number
    x = 7
    y = Dual(5, 1)
    f = x-y
    assert f.val == 2, Exception(f"test_sub_rsub has error")
    assert f.der == -1, Exception(f"test_sub_rsub has error")

# test reverse subtraction between a Dual and non-Dual number
    f_rev = y-x
    assert f_rev.val == -2, Exception(f"test_sub_rsub has error")
    assert f_rev.der == 1, Exception(f"test_sub_rsub has error")

# test subtraction between x and x**2
    x = Dual(5, 1)
    y = x*x
    f = x - y
    assert f.val == -20, Exception(f"test_sub_rsub has error")
    assert f.der == -9, Exception(f"test_sub_rsub has error")


def test_div_rdiv():
# test division between a Dual number and non-Dual number
    x = 2
    y = Dual(1, 1)
    f = x/y
    assert f.val == 2
    assert f.der == -1

# test reverse division between a Dual number and non-Dual number
    f_rev = y/x
    assert f_rev.val == 0.5
    assert f_rev.der == 1

# test division between two Dual numbers
    x = Dual(2, 1)
    y = Dual(1, 1)
    f = x/y
    assert f.val == 2
    assert f.der == -1

    f_rev = y/x
    assert rf.val == 0.5
    assert rf.der == 0.25


def test_pow_rpow():
# test between two Dual numbers 
    x = Dual(2, 1)
    y = Dual(3, 1)
    f = x**y
    assert f.val == 8, Exception(f"test_pow_rpow has error two Dual")
    assert f.der == 12, Exception(f"test_pow_rpow has error two Dual")

# test reverse between two Dual numbers 
    x = Dual(2, 1)
    y = Dual(3, 2)
    f = y**x
    assert f.val == 9, Exception(f"test_pow_rpow has error two Dual")
    assert f.der == 6, Exception(f"test_pow_rpow has error two Dual")

# test one Dual number
    x = Dual(2, 1)
    y = 3
    f = x**y
    assert f.val == 8, Exception(f"test_pow_rpow has error two Dual")
    assert f.der == 12, Exception(f"test_pow_rpow has error two Dual")


#test reverse
    x = Dual(2, 1)
    y = 3
    f = y**x
    assert f.val == 9, Exception(f"test_pow_rpow has error two Dual")
    assert f.der == 6, Exception(f"test_pow_rpow has error two Dual")


def test_sin():
# test sin with a Dual number
    x = Dual(2, 1)
    f = sin(x)
    assert f.val == pytest.approx(math.sin(2), tolerance), Exception(f"test_sin has error")
    assert f.der == pytest.approx(math.cos(2),tolerance), Exception(f"test_sin has error")


# test sin with a non-Dual number
    x = 2
    f = sin(x)
    assert f == pytest.approx(math.sin(2), tolerance), Exception(f"test_sin has error")

def test_cos():
# test cos with a Dual number
    x = Dual(2, 1)
    f = cos(x)
    assert f.val == pytest.approx(math.cos(2), tolerance), Exception(f"test_cos has error")
    assert f.der == pytest.approx(-math.sin(2),tolerance), Exception(f"test_cos has error")

# test cos with a non-Dual number
    x = 2
    f = cos(x)
    assert f == pytest.approx(math.cos(2), tolerance), Exception(f"test_cos has error")

def test_tan():
# test tan with a Dual number
    x = Dual(2, 1)
    f = tan(x)
    assert f.val == pytest.approx(math.tan(2), tolerance), Exception(f"test_tan has error")
    assert f.der == pytest.approx(1/(math.cos(2)**2),tolerance), Exception(f"test_tan has error")

# test tan with a non-Dual number
    x = 2
    f = tan(x)
    assert f == pytest.approx(math.tan(2), tolerance), Exception(f"test_tan has error")

def test_arcsin():
# test arcsin with a Dual number
    x = Dual(0.5, 1)
    f = arcsin(x)
    assert f.val == pytest.approx(np.arcsin(0.5), tolerance), Exception(f"test_arcsin has error")
    assert f.der == pytest.approx(1/(math.sqrt(0.75)),tolerance), Exception(f"test_arcsin has error")

# test arcsin with a non-Dual number
    x = 0.5
    f = arcsin(x)
    assert f == pytest.approx(np.arcsin(0.5), tolerance), Exception(f"test_arcsin has error")

def test_arccos():
# test arccos with a Dual number
    x = Dual(0.5, 1)
    f = arccos(x)
    assert f.val == pytest.approx(np.arccos(0.5), tolerance), Exception(f"test_arccos has error")
    assert f.der == pytest.approx(-1/(math.sqrt(0.75)),tolerance), Exception(f"test_arccos has error")

# test arccos with a non-Dual number
    x = 0.5
    f = arccos(x)
    assert f == pytest.approx(np.arccos(0.5), tolerance), Exception(f"test_arccos has error")

def test_arctan():
# test arctan with a Dual number
    x = Dual(0.5, 1)
    f = arctan(x)
    assert f.val == pytest.approx(np.arctan(0.5), tolerance), Exception(f"test_arctan has error")
    assert f.der == pytest.approx(0.8,tolerance), Exception(f"test_arctan has error")

# test arctan with a non-Dual number
    x = 0.5
    f = arctan(x)
    assert f == pytest.approx(np.arctan(0.5), tolerance), Exception(f"test_arctan has error")


def test_arctanh():
# test arctanh with a Dual number
    x = Dual(0.5, 1)
    f = arctanh(x)
    assert f.val == pytest.approx(np.arctanh(0.5), tolerance), Exception(f"test_arctanh has error")
    assert f.der == pytest.approx(1/0.75,tolerance), Exception(f"test_arctanh has error")


# test arctanh with a non-Dual number
    x = 0.5
    f = arctanh(x)
    assert f == pytest.approx(np.arctanh(0.5), tolerance), Exception(f"test_arctanh has error")


def test_arccosh():
# test arccosh with a Dual number
    x = Dual(2, 1)
    f = arccosh(x)
    assert f.val == pytest.approx(np.arccosh(2), tolerance), Exception(f"test_arccosh has error")
    assert f.der == pytest.approx(1/np.sqrt(3),tolerance), Exception(f"test_arccosh has error")

# test arccosh with a non-Dual number
    x = 2
    f = arccosh(x)
    assert f == pytest.approx(np.arccosh(2), tolerance), Exception(f"test_arccosh has error")


def test_arcsinh():
# test arcsinh with a Dual number
    x = Dual(2, 1)
    f = arcsinh(x)
    assert f.val == pytest.approx(np.arcsinh(2), tolerance), Exception(f"test_arcsinh has error")
    assert f.der == pytest.approx(1/np.sqrt(4),tolerance), Exception(f"test_arcsinh has error")

# test arcsinh with a non-Dual number
    x = 2
    f = arcsinh(x)
    assert f == pytest.approx(np.arcsinh(2), tolerance), Exception(f"test_arcsinh has error")


def test_tanh():
# test tanh with a Dual number
    x = Dual(2, 1)
    f = tanh(x)
    assert f.val == pytest.approx(np.tanh(2), tolerance), Exception(f"test_tanh has error")
    assert f.der == pytest.approx((1/np.cosh(2))**2,tolerance), Exception(f"test_tanh has error")


# test tanh with a non-Dual number
    x = 2
    f = tanh(x)
    assert f == pytest.approx(np.tanh(2), tolerance), Exception(f"test_tanh has error")


def test_cosh():
# test cosh with a Dual number
    x = Dual(2, 1)
    f = cosh(x)
    assert f.val == pytest.approx(np.cosh(2), tolerance), Exception(f"test_cosh has error")
    assert f.der == pytest.approx(np.sinh(2),tolerance), Exception(f"test_cosh has error")


# test cosh with a non-Dual number
    x = 2
    f = cosh(x)
    assert f == pytest.approx(np.cosh(2), tolerance), Exception(f"test_cosh has error")


def test_sinh():
# test sinh with a Dual number
    x = Dual(2, 1)
    f = sinh(x)
    assert f.val == pytest.approx(np.sinh(2), tolerance), Exception(f"test_sinh has error")
    assert f.der == pytest.approx(np.cosh(2),tolerance), Exception(f"test_sinh has error")


# test sinh with a non-Dual number
    x = 2
    f = sinh(x)
    assert f == pytest.approx(np.sinh(2), tolerance), Exception(f"test_sinh has error")


def test_exp():
# test exp with a Dual number
    x = Dual(2, 1)
    f = exp(x)
    assert f.val == pytest.approx(math.exp(2), tolerance), Exception(f"test_exp has error")
    assert f.der == pytest.approx(math.exp(2),tolerance), Exception(f"test_exp has error")

def test_sqrt():
    x = Dual(4, 2)
    y = Dual(-1)
    a = 1.21
    b = (-1)
    f1 = sqrt(x)
    assert f1.val == pytest.approx(np.sqrt(4), tolerance), Exception(f"test_sqrt has error for Dual class")
    assert f1.der == pytest.approx(0.5, tolerance), Exception(f"test_sqrt has error for the derivative for Dual class")
    with pytest.raises(ValueError):
        f2 = sqrt(y)
    f3 = sqrt(a)
    assert f3 == pytest.approx(np.sqrt(1.21), tolerance), Exception(f"test_sqrt has error for real number")
    with pytest.raises(ValueError):
        f4 = sqrt(b)


def func(x, y, z):
        return sin(x) + y**3 + x*z


# test gradient computation
def test_gradient():
    grad1 = get_gradient(func, 3, [1,2,3])
   

