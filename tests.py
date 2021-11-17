import pytest
import numpy as np
from src.dual_temp import *



def test_init():
    with pytest.raises(TypeError):
        x = dual("Here is a string")


def test_add_radd():

# test addition of two dual numbers
    x = dual(5, 1)
    y = dual(8, 3)
    f = x + y
    assert f.val == 13, Exception(f"test_add_radd has error with two dual numbers")
    assert f.der == 4, Exception(f"test_add_radd has error with two dual numbers")

# test reverse addition of two dual numbers
    f_rev = y + x
    assert f_rev.val == 13, Exception(f"test_add_radd has error with reverse")
    assert f_rev.der == 4, Exception(f"test_add_radd has error with reverse")


# test addition of a dual and non-dual number
    x = 5
    y = dual(8, 3)
    f = x + y
    assert f.val == 13, Exception(f"test_add_radd has error with nondual")
    assert f.der == 3,Exception(f"test_add_radd has error with nondual")

# test reverse addition of a dual and non-dual number
    f_rev = y + x
    assert f_rev.val == 13, Exception(f"test_add_radd has error with reverse and nondual")
    assert f_rev.der == 3, Exception(f"test_add_radd has error with reverse and nondual")


# test addition of x and x**2
    x = dual(5, 1)
    y = x*x
    f = x + y
    assert f.val == 30, Exception(f"test_add_radd has error")
    assert f.der == 11, Exception(f"test_add_radd has error")


def test_mul_rmul():
# test multiplication of two dual numbers
    x = dual(5, 1)
    y = dual(8, 1)
    f = x*y
    assert f.val == 40, Exception(f"test_mul_rmul has error")
    assert f.der == 13, Exception(f"test_mul_rmul has error")

# test reverse multiplication of two dual numbers
    f_rev = y*x
    assert f_rev.val == 40, Exception(f"test_mul_rmul has error")
    assert f_rev.der == 13, Exception(f"test_mul_rmul has error")


# test multiplication of a dual and non-dual number
    x = dual(5, 1)
    y = 3
    f = x*y
    assert f.val == 15, Exception(f"test_mul_rmul has error")
    assert f.der == 3, Exception(f"test_mul_rmul has error")

# test reverse multiplication of a dual and non-dual number
    f_rev = y*x
    assert f_rev.val == 15, Exception(f"test_mul_rmul has error")
    assert f_rev.der == 3, Exception(f"test_mul_rmul has error")

# test multiplication of x and x**2
    x = dual(5,1)
    y = x*x
    f = x*y
    assert f.val == 125, Exception(f"test_mul_rmul has error")
    assert f.der == 75, Exception(f"test_mul_rmul has error")


def test_sub_rsub():
# test subtraction between two dual numbers
    x = dual(5, 1)
    y = dual(8, 2)
    f = x-y
    assert f.val == -3, Exception(f"test_sub_rsub has error")
    assert f.der == -1, Exception(f"test_sub_rsub has error")

# test reverse subtraction between two dual numbers
    f_rev = y-x
    assert f_rev.val == 3, Exception(f"test_sub_rsub has error")
    assert f_rev.der == 1, Exception(f"test_sub_rsub has error")

# test subtraction between a dual and non-dual number
    x = 7
    y = dual(5, 1)
    f = x-y
    assert f.val == 2, Exception(f"test_sub_rsub has error")
    assert f.der == -1, Exception(f"test_sub_rsub has error")

# test reverse subtraction between a dual and non-dual number
    f_rev = y-x
    assert f_rev.val == -2, Exception(f"test_sub_rsub has error")
    assert f_rev.der == 1, Exception(f"test_sub_rsub has error")

# test subtraction between x and x**2
    x = dual(5, 1)
    y = x*x
    f = x - y
    assert f.val == -20, Exception(f"test_sub_rsub has error")
    assert f.der == -9, Exception(f"test_sub_rsub has error")


# test division between a dual number and non-dual number
#     def test_div_rdiv(self):
#     x = 2
#     y = dual(1, 1)
#     f = x/y
#     assert f.val == 2
#     assert f.der ==

#     # test reverse division between a dual number and non-dual number
#     f_rev = y/x
#     assert f_rev.val = 0.5
#     assert f_rev.der =

#     # test division between two dual numbers
#     x = dual(2, 2)
#     y = dual(1, 2)
#     f = x/y
#     assert f.val = 2
#     assert f.der =

#     f_rev = y/x
#     assert rf.val = 0.5
#     assert rf.der =


