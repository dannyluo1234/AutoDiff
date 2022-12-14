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

    # test invalid type addition
    with pytest.raises(TypeError):
        f = x + np.array([0, 4, 9])


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

    # test invalid type multiplication
    with pytest.raises(TypeError):
        f = x * np.array([0, 4, 9])


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

    # test invalid type subtraction
    with pytest.raises(TypeError):
        f = x - np.array([0, 4, 9])

    # test invalid type rsubtraction
    with pytest.raises(TypeError):
        f = "3" - x


def test_div_rdiv():
    # test division between a Dual number and non-Dual number
    x = 2
    y = Dual(1, 1)
    f = x/y
    assert f.val == 2
    assert f.der == -2

    # test reverse division between a Dual number and non-Dual number
    f_rev = y/x
    assert f_rev.val == 0.5
    assert f_rev.der == 0.5

    # test division between two Dual numbers
    x = Dual(2, 1)
    y = Dual(1, 1)
    f = x/y
    assert f.val == 2
    assert f.der == -1

    f_rev = y/x
    assert f_rev.val == 0.5
    assert f_rev.der == 0.25

    # test invalid type division
    with pytest.raises(TypeError):
        f = x / np.array([0, 4, 9])

    # test invalid type rdivision
    with pytest.raises(TypeError):
        f = "3" / y

def test_neg():
    # test between two Dual numbers
    x = Dual(2, 1)
    f = -x
    assert f.val == -2, Exception(f"test_neg has wrong value")
    assert f.der == -1, Exception(f"test_neg has wrong value")


def test_pow_rpow():
    # test between two Dual numbers
    x = Dual(2, 1)
    y = Dual(3, 1)
    f = x**y
    assert f.val == 8, Exception(f"test_pow_rpow has error two Dual")
    assert f.der == pytest.approx(2**3*(np.log(2)+3/2), tolerance), Exception(f"test_pow_rpow has error two Dual")

    # test reverse between two Dual numbers
    x = Dual(2, 1)
    y = Dual(3, 2)
    f = y**x
    assert f.val == 9, Exception(f"test_pow_rpow has error two Dual")
    assert f.der == pytest.approx(3**2*(np.log(3)+2/3*2), tolerance), Exception(f"test_pow_rpow has error two Dual")

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
    assert f.der == pytest.approx(3**2*(np.log(3)*1), tolerance), Exception(f"test_pow_rpow has error two Dual")

    # test invalid type power
    with pytest.raises(TypeError):
        f = x ** np.array([0, 4, 9])


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

    # test invalid type sin
    with pytest.raises(TypeError):
        f = sin(np.array([0, 4, 9]))

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

    # test invalid type cos
    with pytest.raises(TypeError):
        f = cos(np.array([0, 4, 9]))

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

    # test invalid type tan
    with pytest.raises(TypeError):
        f = tan(np.array([0, 4, 9]))

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

    # test invalid type arcsin
    with pytest.raises(TypeError):
        f = arcsin(np.array([0, 4, 9]))

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

    # test invalid type arccos
    with pytest.raises(TypeError):
        f = arccos(np.array([0, 4, 9]))

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

    # test invalid type arctan
    with pytest.raises(TypeError):
        f = arctan(np.array([0, 4, 9]))

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

    # test invalid type arctanh
    with pytest.raises(TypeError):
        f = arctanh(np.array([0, 4, 9]))


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

    # test invalid type arccosh
    with pytest.raises(TypeError):
        f = arccosh(np.array([0, 4, 9]))

def test_arcsinh():
    # test arcsinh with a Dual number
    x = Dual(2, 1)
    f = arcsinh(x)
    assert f.val == pytest.approx(np.arcsinh(2), tolerance), Exception(f"test_arcsinh has error")
    assert f.der == pytest.approx(1/np.sqrt(5),tolerance), Exception(f"test_arcsinh has error")

    # test arcsinh with a non-Dual number
    x = 2
    f = arcsinh(x)
    assert f == pytest.approx(np.arcsinh(2), tolerance), Exception(f"test_arcsinh has error")

    # test invalid type arcsinh
    with pytest.raises(TypeError):
        f = arcsinh(np.array([0, 4, 9]))


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

    # test invalid type tanh
    with pytest.raises(TypeError):
        f = tanh(np.array([0, 4, 9]))

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

    # test invalid type cosh
    with pytest.raises(TypeError):
        f = cosh(np.array([0, 4, 9]))

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

    # test invalid type sinh
    with pytest.raises(TypeError):
        f = sinh(np.array([0, 4, 9]))


def test_exp():
    # test exp with a Dual number
    x = Dual(2, 1)
    a = 2
    f1 = exp(x)
    assert f1.val == pytest.approx(math.exp(2), tolerance), Exception(f"test_exp has error")
    assert f1.der == pytest.approx(math.exp(2),tolerance), Exception(f"test_exp has error")
    f2 = exp(a)
    assert f2 == pytest.approx(math.exp(2), tolerance), Exception(f"test_exp has error for real number")

    # test invalid type exponential
    with pytest.raises(TypeError):
        f = exp(np.array([0, 4, 9]))

def test_sqrt():
    x = Dual(4, 2)
    y = Dual(-1)
    a = 1.21
    b = (-1)
    c = np.array([0, 4, 9])

    # test sqrt on a simple Dual number
    f1 = sqrt(x)
    assert f1.val == pytest.approx(np.sqrt(4), tolerance), Exception(f"test_sqrt has error for Dual class")
    assert f1.der == pytest.approx(0.5, tolerance), Exception(f"test_sqrt has error for the derivative for Dual class")

    # test sqrt on negative Dual number
    with pytest.raises(ValueError):
        f2 = sqrt(y)

    # test sqrt on a float
    f3 = sqrt(a)
    assert f3 == pytest.approx(np.sqrt(1.21), tolerance), Exception(f"test_sqrt has error for real number")

    # test sqrt on a negative real number
    with pytest.raises(ValueError):
        f4 = sqrt(b)

    # test invalid type for sqrt
    with pytest.raises(TypeError):
        f = sqrt(np.array([0, 4, 9]))


def func(x, y, z):
        return sin(x) + y**3 + x*z


# test gradient computation
def test_gradient():
    grad1 = get_gradient(func, 3, [1,2,3])
   

