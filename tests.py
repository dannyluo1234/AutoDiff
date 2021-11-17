# Start writing code here...
import pytest
import numpy as np
from ../dual_temp import *

tolerance = 0.000000001

class TestForward:

    def test_init(self):
        with pytest.raises(TypeError):
            x = dual("Here is a string")


    def test_add_radd(self)

    # test addition of two dual numbers
        x = dual(5, 1)
        y = dual(8, 3)
        f = x + y
        assert f.val == 13
        assert f.der == 4

    # test reverse addition of two dual numbers
        f_rev = y + x
        assert f_rev.val == 13
        assert f_rev.der == 4


    # test addition of a dual and non-dual number
        x = 5
        y = dual(8, 3)
        f = x + y
        assert f.val == 13
        assert f.der == 3

    # test reverse addition of a dual and non-dual number
        f_rev = y + x
        assert f_rev.val == 13
        assert f_rev.der == 3


    # test addition of x and x**2
        x = dual(5, 1)
        y = x*x
        f = x + y
        assert f.val == 30
        assert f.der == 11


    def test_mul_rmul(self)
    # test multiplication of two dual numbers
        x = dual(5, 1)
        y = dual(8, 1)
        f = x*y
        assert f.val == 40
        assert f.der == 1

    # test reverse multiplication of two dual numbers
        f_rev = y*x
        assert f_rev.val == 40
        assert f_rev.der == 1


    # test multiplication of a dual and non-dual number
        x = dual(5, 1)
        y = 3
        f = x*y
        assert f.val == 15
        assert f.der == 1

    # test reverse multiplication of a dual and non-dual number
        f_rev = y*x
        assert f_rev.val == 15
        assert f_rev.der == 1

    # test multiplication of x and x**2
        x = dual(5,1)
        y = x*x
        f = x*y
        assert f.val == 125
        assert f.der == 75


    def test_sub_rsub(self):
    # test subtraction between two dual numbers
        x = dual(5, 1)
        y = dual(8, 2)
        f = x-y
        assert f.val = -3
        assert f.der = -1

    # test reverse subtraction between two dual numbers
        f_rev = y-x
        assert f_rev.val = 3
        assert f_rev.der = 1

    # test subtraction between a dual and non-dual number
        x = 7
        y = dual(5, 1)
        f = x-y
        assert f.val = 2
        assert f.der = -1

    # test reverse subtraction between a dual and non-dual number
        f_rev = y-x
        assert f_rev.val = 2
        assert f_rev.der = 1

    # test subtraction between x and x**2
        x = dual(5, 1)
        y = x*x
        f = x - y
        assert f.val == -20
        assert f.der == -9

    
    # test division between a dual number and non-dual number
    def test_div_rdiv(self):
    x = 2
    y = dual(1, 1)
    f = x/y
    assert f.val == 2
    assert f.der ==

    # test reverse division between a dual number and non-dual number
    f_rev = y/x
    assert f_rev.val = 0.5
    assert f_rev.der =

    # test division between two dual numbers
    x = dual(2, 2)
    y = dual(1, 2)
    f = x/y
    assert f.val = 2
    assert f.der =

    f_rev = y/x
    assert rf.val = 0.5
    assert rf.der =

    
