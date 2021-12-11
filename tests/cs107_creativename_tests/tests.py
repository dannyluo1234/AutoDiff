import pytest
import numpy as np
import sys

from cs107_creativename import *

import math
tolerance = 0.000000001


#####################################################################################
# Tests for Forward.py, Functions with Dual & init file using Forward
def test_Forward_init():
    with pytest.raises(TypeError):
        x = Dual("Here is a string")
    
    x = Dual(3, 4)
    assert x.val == 3
    assert x.der == 4


def test_Forward_add_radd():
    # test addition of two Dual numbers
    x = Dual(5, 1)
    y = Dual(8, 3)
    f = x + y
    assert f.val == 13, Exception(f"test_Forward_add_radd has error with two Dual numbers")
    assert f.der == 4, Exception(f"test_Forward_add_radd has error with two Dual numbers")

    # test reverse addition of two Dual numbers
    f_rev = y + x
    assert f_rev.val == 13, Exception(f"test_Forward_add_radd has error with reverse")
    assert f_rev.der == 4, Exception(f"test_Forward_add_radd has error with reverse")


    # test addition of a Dual and non-Dual number
    x = 5
    y = Dual(8, 3)
    f = x + y
    assert f.val == 13, Exception(f"test_Forward_add_radd has error with nonDual")
    assert f.der == 3,Exception(f"test_Forward_add_radd has error with nonDual")

    # test reverse addition of a Dual and non-Dual number
    f_rev = y + x
    assert f_rev.val == 13, Exception(f"test_Forward_add_radd has error with reverse and nonDual")
    assert f_rev.der == 3, Exception(f"test_Forward_add_radd has error with reverse and nonDual")


    # test addition of x and x**2
    x = Dual(5, 1)
    y = x*x
    f = x + y
    assert f.val == 30, Exception(f"test_Forward_add_radd has error")
    assert f.der == 11, Exception(f"test_Forward_add_radd has error")

    # test invalid type addition
    with pytest.raises(TypeError):
        f = x + np.array([0, 4, 9])


def test_Forward_mul_rmul():
    # test multiplication of two Dual numbers
    x = Dual(5, 1)
    y = Dual(8, 1)
    f = x*y
    assert f.val == 40, Exception(f"test_Forward_mul_rmul has error")
    assert f.der == 13, Exception(f"test_Forward_mul_rmul has error")

    # test reverse multiplication of two Dual numbers
    f_rev = y*x
    assert f_rev.val == 40, Exception(f"test_Forward_mul_rmul has error")
    assert f_rev.der == 13, Exception(f"test_Forward_mul_rmul has error")


    # test multiplication of a Dual and non-Dual number
    x = Dual(5, 1)
    y = 3
    f = x*y
    assert f.val == 15, Exception(f"test_Forward_mul_rmul has error")
    assert f.der == 3, Exception(f"test_Forward_mul_rmul has error")

    # test reverse multiplication of a Dual and non-Dual number
    f_rev = y*x
    assert f_rev.val == 15, Exception(f"test_Forward_mul_rmul has error")
    assert f_rev.der == 3, Exception(f"test_Forward_mul_rmul has error")

    # test multiplication of x and x**2
    x = Dual(5,1)
    y = x*x
    f = x*y
    assert f.val == 125, Exception(f"test_Forward_mul_rmul has error")
    assert f.der == 75, Exception(f"test_Forward_mul_rmul has error")

    # test invalid type multiplication
    with pytest.raises(TypeError):
        f = x * np.array([0, 4, 9])


def test_Forward_sub_rsub():
    # test subtraction between two Dual numbers
    x = Dual(5, 1)
    y = Dual(8, 2)
    f = x-y
    assert f.val == -3, Exception(f"test_Forward_sub_rsub has error")
    assert f.der == -1, Exception(f"test_Forward_sub_rsub has error")

    # test reverse subtraction between two Dual numbers
    f_rev = y-x
    assert f_rev.val == 3, Exception(f"test_Forward_sub_rsub has error")
    assert f_rev.der == 1, Exception(f"test_Forward_sub_rsub has error")

    # test subtraction between a Dual and non-Dual number
    x = 7
    y = Dual(5, 1)
    f = x-y
    assert f.val == 2, Exception(f"test_Forward_sub_rsub has error")
    assert f.der == -1, Exception(f"test_Forward_sub_rsub has error")

    # test reverse subtraction between a Dual and non-Dual number
    f_rev = y-x
    assert f_rev.val == -2, Exception(f"test_Forward_sub_rsub has error")
    assert f_rev.der == 1, Exception(f"test_Forward_sub_rsub has error")

    # test subtraction between x and x**2
    x = Dual(5, 1)
    y = x*x
    f = x - y
    assert f.val == -20, Exception(f"test_Forward_sub_rsub has error")
    assert f.der == -9, Exception(f"test_Forward_sub_rsub has error")

    # test invalid type subtraction
    with pytest.raises(TypeError):
        f = x - np.array([0, 4, 9])

    # test invalid type rsubtraction
    with pytest.raises(TypeError):
        f = "3" - x


def test_Forward_div_rdiv():
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

def test_Forward_neg():
    # test between two Dual numbers
    x = Dual(2, 1)
    f = -x
    assert f.val == -2, Exception(f"test_Forward_neg has wrong value")
    assert f.der == -1, Exception(f"test_Forward_neg has wrong value")


def test_Forward_pow_rpow():
    # test between two Dual numbers
    x = Dual(2, 1)
    y = Dual(3, 1)
    f = x**y
    assert f.val == 8, Exception(f"test_Forward_pow_rpow has error two Dual")
    assert f.der == pytest.approx(2**3*(np.log(2)+3/2), tolerance), Exception(f"test_Forward_pow_rpow has error two Dual")

    # test reverse between two Dual numbers
    x = Dual(2, 1)
    y = Dual(3, 2)
    f = y**x
    assert f.val == 9, Exception(f"test_Forward_pow_rpow has error two Dual")
    assert f.der == pytest.approx(3**2*(np.log(3)+2/3*2), tolerance), Exception(f"test_Forward_pow_rpow has error two Dual")

    # test one Dual number
    x = Dual(2, 1)
    y = 3
    f = x**y
    assert f.val == 8, Exception(f"test_Forward_pow_rpow has error two Dual")
    assert f.der == 12, Exception(f"test_Forward_pow_rpow has error two Dual")


    #test reverse
    x = Dual(2, 1)
    y = 3
    f = y**x
    assert f.val == 9, Exception(f"test_Forward_pow_rpow has error two Dual")
    assert f.der == pytest.approx(3**2*(np.log(3)*1), tolerance), Exception(f"test_Forward_pow_rpow has error two Dual")

    # test invalid type power
    with pytest.raises(TypeError):
        f = x ** np.array([0, 4, 9])
        
    # test invalid type for rpow
    with pytest.raises(TypeError):
        f = "3" ** x


def test_Forward_sin():
    # test sin with a Dual number
    x = Dual(2, 1)
    f = sin(x)
    assert f.val == pytest.approx(math.sin(2), tolerance), Exception(f"test_Forward_sin has error")
    assert f.der == pytest.approx(math.cos(2),tolerance), Exception(f"test_Forward_sin has error")

    # test sin with a non-Dual number
    x = 2
    f = sin(x)
    assert f == pytest.approx(math.sin(2), tolerance), Exception(f"test_Forward_sin has error")

    # test invalid type sin
    with pytest.raises(TypeError):
        f = sin(np.array([0, 4, 9]))

def test_Forward_cos():
    # test cos with a Dual number
    x = Dual(2, 1)
    f = cos(x)
    assert f.val == pytest.approx(math.cos(2), tolerance), Exception(f"test_Forward_cos has error")
    assert f.der == pytest.approx(-math.sin(2),tolerance), Exception(f"test_Forward_cos has error")

    # test cos with a non-Dual number
    x = 2
    f = cos(x)
    assert f == pytest.approx(math.cos(2), tolerance), Exception(f"test_Forward_cos has error")

    # test invalid type cos
    with pytest.raises(TypeError):
        f = cos(np.array([0, 4, 9]))

def test_Forward_tan():
    # test tan with a Dual number
    x = Dual(2, 1)
    f = tan(x)
    assert f.val == pytest.approx(math.tan(2), tolerance), Exception(f"test_Forward_tan has error")
    assert f.der == pytest.approx(1/(math.cos(2)**2),tolerance), Exception(f"test_Forward_tan has error")

    # test tan with a non-Dual number
    x = 2
    f = tan(x)
    assert f == pytest.approx(math.tan(2), tolerance), Exception(f"test_Forward_tan has error")

    # test invalid type tan
    with pytest.raises(TypeError):
        f = tan(np.array([0, 4, 9]))

def test_Forward_arcsin():
    # test arcsin with a Dual number
    x = Dual(0.5, 1)
    f = arcsin(x)
    assert f.val == pytest.approx(np.arcsin(0.5), tolerance), Exception(f"test_Forward_arcsin has error")
    assert f.der == pytest.approx(1/(math.sqrt(0.75)),tolerance), Exception(f"test_Forward_arcsin has error")

    # test arcsin with a non-Dual number
    x = 0.5
    f = arcsin(x)
    assert f == pytest.approx(np.arcsin(0.5), tolerance), Exception(f"test_Forward_arcsin has error")

    # test invalid type arcsin
    with pytest.raises(TypeError):
        f = arcsin(np.array([0, 4, 9]))

def test_Forward_arccos():
    # test arccos with a Dual number
    x = Dual(0.5, 1)
    f = arccos(x)
    assert f.val == pytest.approx(np.arccos(0.5), tolerance), Exception(f"test_Forward_arccos has error")
    assert f.der == pytest.approx(-1/(math.sqrt(0.75)),tolerance), Exception(f"test_Forward_arccos has error")

    # test arccos with a non-Dual number
    x = 0.5
    f = arccos(x)
    assert f == pytest.approx(np.arccos(0.5), tolerance), Exception(f"test_Forward_arccos has error")

    # test invalid type arccos
    with pytest.raises(TypeError):
        f = arccos(np.array([0, 4, 9]))

def test_Forward_arctan():
    # test arctan with a Dual number
    x = Dual(0.5, 1)
    f = arctan(x)
    assert f.val == pytest.approx(np.arctan(0.5), tolerance), Exception(f"test_Forward_arctan has error")
    assert f.der == pytest.approx(0.8,tolerance), Exception(f"test_Forward_arctan has error")

    # test arctan with a non-Dual number
    x = 0.5
    f = arctan(x)
    assert f == pytest.approx(np.arctan(0.5), tolerance), Exception(f"test_Forward_arctan has error")

    # test invalid type arctan
    with pytest.raises(TypeError):
        f = arctan(np.array([0, 4, 9]))

def test_Forward_arctanh():
    # test arctanh with a Dual number
    x = Dual(0.5, 1)
    f = arctanh(x)
    assert f.val == pytest.approx(np.arctanh(0.5), tolerance), Exception(f"test_Forward_arctanh has error")
    assert f.der == pytest.approx(1/0.75,tolerance), Exception(f"test_Forward_arctanh has error")

    # test arctanh with a non-Dual number
    x = 0.5
    f = arctanh(x)
    assert f == pytest.approx(np.arctanh(0.5), tolerance), Exception(f"test_Forward_arctanh has error")

    # test invalid type arctanh
    with pytest.raises(TypeError):
        f = arctanh(np.array([0, 4, 9]))


def test_Forward_arccosh():
    # test arccosh with a Dual number
    x = Dual(2, 1)
    f = arccosh(x)
    assert f.val == pytest.approx(np.arccosh(2), tolerance), Exception(f"test_Forward_arccosh has error")
    assert f.der == pytest.approx(1/np.sqrt(3),tolerance), Exception(f"test_Forward_arccosh has error")

    # test arccosh with a non-Dual number
    x = 2
    f = arccosh(x)
    assert f == pytest.approx(np.arccosh(2), tolerance), Exception(f"test_Forward_arccosh has error")

    # test invalid type arccosh
    with pytest.raises(TypeError):
        f = arccosh(np.array([0, 4, 9]))

def test_Forward_arcsinh():
    # test arcsinh with a Dual number
    x = Dual(2, 1)
    f = arcsinh(x)
    assert f.val == pytest.approx(np.arcsinh(2), tolerance), Exception(f"test_Forward_arcsinh has error")
    assert f.der == pytest.approx(1/np.sqrt(5),tolerance), Exception(f"test_Forward_arcsinh has error")

    # test arcsinh with a non-Dual number
    x = 2
    f = arcsinh(x)
    assert f == pytest.approx(np.arcsinh(2), tolerance), Exception(f"test_Forward_arcsinh has error")

    # test invalid type arcsinh
    with pytest.raises(TypeError):
        f = arcsinh(np.array([0, 4, 9]))


def test_Forward_tanh():
# test tanh with a Dual number
    x = Dual(2, 1)
    f = tanh(x)
    assert f.val == pytest.approx(np.tanh(2), tolerance), Exception(f"test_Forward_tanh has error")
    assert f.der == pytest.approx((1/np.cosh(2))**2,tolerance), Exception(f"test_Forward_tanh has error")

    # test tanh with a non-Dual number
    x = 2
    f = tanh(x)
    assert f == pytest.approx(np.tanh(2), tolerance), Exception(f"test_Forward_tanh has error")

    # test invalid type tanh
    with pytest.raises(TypeError):
        f = tanh(np.array([0, 4, 9]))

def test_Forward_cosh():
    # test cosh with a Dual number
    x = Dual(2, 1)
    f = cosh(x)
    assert f.val == pytest.approx(np.cosh(2), tolerance), Exception(f"test_Forward_cosh has error")
    assert f.der == pytest.approx(np.sinh(2),tolerance), Exception(f"test_Forward_cosh has error")

    # test cosh with a non-Dual number
    x = 2
    f = cosh(x)
    assert f == pytest.approx(np.cosh(2), tolerance), Exception(f"test_Forward_cosh has error")

    # test invalid type cosh
    with pytest.raises(TypeError):
        f = cosh(np.array([0, 4, 9]))

def test_Forward_sinh():
    # test sinh with a Dual number
    x = Dual(2, 1)
    f = sinh(x)
    assert f.val == pytest.approx(np.sinh(2), tolerance), Exception(f"test_Forward_sinh has error")
    assert f.der == pytest.approx(np.cosh(2),tolerance), Exception(f"test_Forward_sinh has error")

    # test sinh with a non-Dual number
    x = 2
    f = sinh(x)
    assert f == pytest.approx(np.sinh(2), tolerance), Exception(f"test_Forward_sinh has error")

    # test invalid type sinh
    with pytest.raises(TypeError):
        f = sinh(np.array([0, 4, 9]))


def test_Forward_exp():
    # test exp with a Dual number
    x = Dual(2, 1)
    a = 2
    f1 = exp(x)
    assert f1.val == pytest.approx(math.exp(2), tolerance), Exception(f"test_Forward_exp has error")
    assert f1.der == pytest.approx(math.exp(2),tolerance), Exception(f"test_Forward_exp has error")
    f2 = exp(a)
    assert f2 == pytest.approx(math.exp(2), tolerance), Exception(f"test_Forward_exp has error for real number")

    # test invalid type exponential
    with pytest.raises(TypeError):
        f = exp(np.array([0, 4, 9]))
        
        
def test_Forward_lt():
    # test between a Dual number and a non-Dual number
    x = 2
    y = Dual(3)
    f = x < y.val
    f1 = x > y.val
    assert f == True , Exception(f"test_Forward_lt has wrong value")
    assert f1 == False , Exception(f"test_Forward_lt has wrong value")
    
       
    # test between two Dual numbers
    x = Dual(2)
    y = Dual(3)
    f = x.val < y.val
    f1 = y.val < x.val
    assert f == True, Exception(f"test_Forward_lt has wrong value")
    assert f1 == False, Exception(f"test_Forward_lt has wrong value")
    
    #test invalid type
    x = Dual(2)
    y = 'string'
    with pytest.raises(TypeError):
        x.val < y
    
    
def test_Forward_le():
    # test between a Dual number and a non-Dual number
    x = 2
    y = Dual(3)
    f = x <= y.val
    f1 = y.val <= x
    assert f == True, Exception(f"test_Forward_le has wrong value")
    assert f1 == False, Exception(f"test_Forward_le has wrong value")
       
    # test between two Dual numbers
    x = Dual(2)
    y = Dual(3)
    f = x.val <= y.val
    f1 = y.val <= x.val
    assert f == True, Exception(f"test_Forward_le has wrong value")
    assert f1 == False, Exception(f"test_Forward_le has wrong value")
    
    
    #test invalid type
    x = Dual(2)
    y = 'string'
    with pytest.raises(TypeError):
        x.val < y
    
    
def test_Forward_gt():
    # test between a Dual number and a non-Dual number
    x = 3
    y = Dual(1)
    f = x > y.val
    f1 = y.val > x
    assert f == True, Exception(f"test_Forward_gt has wrong value")
    assert f1 == False, Exception(f"test_Forward_gt has wrong value")
    
    # test between two Dual numbers
    x = Dual(3)
    y = Dual(1)
    f = x.val > y.val
    f1 = y.val > x.val
    assert f == True, Exception(f"test_Forward_gt has wrong value")
    assert f1 == False, Exception(f"test_Forward_gt has wrong value")
    
    #test invalid type
    x = Dual(2)
    y = 'string'
    with pytest.raises(TypeError):
        x.val > y
    
    
    
def test_Forward_ge():
    # test between a Dual number and a non-Dual number
    x = 3
    y = Dual(1)
    f = x >= y.val
    f1 = y.val >= x
    assert f == True, Exception(f"test_Forward_ge has wrong value")
    assert f1 == False, Exception(f"test_Forward_ge has wrong value")
       
    # test between two Dual numbers
    x = Dual(3)
    y = Dual(1)
    f = x.val >= y.val
    f1 = y.val >= x.val
    assert f == True, Exception(f"test_Forward_ge has wrong value")
    assert f1 == False, Exception(f"test_Forward_ge has wrong value")

    
    #test invalid type
    x = Dual(2)
    y = 'string'
    with pytest.raises(TypeError):
        x.val >= y
    
    
def test_Forward_eq():
    # test between two Dual numbers
    x = Dual(2)
    y = Dual(2)
    assert x.val == y.val, Exception(f"test_Forward_eq has wrong value")
    assert x.der == y.der, Exception(f"test_Forward_eq has wrong derivative")
    
    


def test_Forward_ne():
    # test between two Dual numbers
    x = Dual(2)
    y = Dual(3)
    assert x.val is not y.val, Exception(f"test_Forward_ne has wrong value")

def test_Forward_sqrt():
    x = Dual(4, 2)
    y = Dual(-1)
    a = 1.21
    b = (-1)
    c = np.array([0, 4, 9])

    # test sqrt on a simple Dual number
    f1 = sqrt(x)
    assert f1.val == pytest.approx(np.sqrt(4), tolerance), Exception(f"test_Forward_sqrt has error for Dual class")
    assert f1.der == pytest.approx(0.5, tolerance), Exception(f"test_Forward_sqrt has error for the derivative for Dual class")

    # test sqrt on negative Dual number
    with pytest.raises(ValueError):
        f2 = sqrt(y)

    # test sqrt on a float
    f3 = sqrt(a)
    assert f3 == pytest.approx(np.sqrt(1.21), tolerance), Exception(f"test_Forward_sqrt has error for real number")

    # test sqrt on a negative real number
    with pytest.raises(ValueError):
        f4 = sqrt(b)

    # test invalid type for sqrt
    with pytest.raises(TypeError):
        f = sqrt(np.array([0, 4, 9]))


# test AutoDiffF1D
def test_AutoDiffF1D():
    # test one dimensional function
    func = lambda x,y,z: x**2 + 2*y + sin(z)
    grad1 = AutoDiffF1D(func, [1,2,3])
    assert grad1 == pytest.approx([2, 2, np.cos(3)], tolerance), Exception(f"test_AutoDiffF1D has error")
   
    # test mismatch input dimension
    with pytest.raises(Exception):
        grad1 = AutoDiffF1D(func, [1,2,3,4])
    
    # test invalid input (non-function input)
    with pytest.raises(TypeError):
        grad1 = AutoDiffF1D("3", [1,2,3,4])    

# test AutoDiff
def test_AutoDiff():
    # test one dimensional function
    func = lambda x,y,z: x**2 + 2*y + sin(z)
    grad1 = AutoDiffF(func, [1,2,3])
    assert grad1 == pytest.approx([2, 2, np.cos(3)], tolerance), Exception(f"test_AutoDiffF1D has error")
   
    # test mismatch function length and value length
    func2 = lambda x,y,z: x**y + 4*(x-y) + tan(z)
    with pytest.raises(Exception):
        grad1 = AutoDiffF([func, func2], [[1,2,3],[1,2,4],[3]])    
    
    # test AutoDiff with multiple function
    grad1 = AutoDiffF([func, func2], [[1,2,3],[1,2,4]])  
    assert grad1[0] == pytest.approx([2, 2, np.cos(3)], tolerance), Exception(f"test_AutoDiffF has error")
    assert grad1[1] == pytest.approx([2 * 1+4, 1*np.log(1)-4, 1/np.cos(4)**2], tolerance), Exception(f"test_AutoDiffF has error")
    
    
 #####################################################################################
# Tests for Reverse.py, Functions with Node & init file using Reverse
    
def test_Reverse_init():
    with pytest.raises(TypeError):
        x = Node("Here is a string")
    
    x = Node(3)
    assert x.val == 3
    assert x.children == []
    assert x.der == None

def test_Reverse_add_radd():
   # test addition of two Nodes
   x = Node(5)
   y = Node(8)
   f = x + y
   assert f.val == 13, Exception(f"test_Reverse_add_radd has error in value with two Nodes")
   assert x.children == [(f,1)], Exception(f"test_Reverse_add_radd has error in first node's children")
   assert y.children == [(f,1)], Exception(f"test_Reverse_add_radd has error in second node's children")
   

   # test addition of a Node and non-Node number
   x = 5
   y = Node(8)
   f = y+x
   assert f.val == 13, Exception(f"test_Reverse_add_radd has error in value with Node and non-node")
   assert y.children == [(f,1)], Exception(f"test_Reverse_add_radd has error in second node's children")


   # test reverse addition of a Node and non-Node number
   x = 5
   y = Node(8)
   f = x+y
   assert f.val == 13, Exception(f"test_Reverse_add_radd has error in value with Node and non-node")
   assert y.children == [(f,1)], Exception(f"test_Reverse_add_radd has error in second node's children")


   # test invalid type addition
   with pytest.raises(TypeError):
       x = Node(5)
       f = x + np.array([0, 4, 9])
       
       
def test_Reverse_sub_rsub():
   # test subtraction of two Nodes
   x = Node(5)
   y = Node(3)
   f = x - y
   assert f.val == 2, Exception(f"test_Reverse_sub_rsub has error in value with two Nodes")
   assert x.children == [(f,1)], Exception(f"test_Reverse_add_radd has error in first node's children")
   assert y.children == [(f,-1)], Exception(f"test_Reverse_add_radd has error in second node's children")
   

   # test reverse subtraction of a Node and non-Node number
   x = 5
   y = Node(3)
   f = y-x
   assert f.val == -2, Exception(f"test_Reverse_sub_rsub has error in value with Node and non-node")
   assert y.children == [(f,1)], Exception(f"test_Reverse_sub_rsub has error in second node's children")


   # test subtraction of a Node and non-Node number
   x = 5
   y = Node(3)
   f = x-y
   assert f.val == 2, Exception(f"test_Reverse_sub_rsub has error in value with Node and non-node")
   assert y.children == [(f,-1)], Exception(f"test_Reverse_sub_rsub has error in second node's children")


   # test invalid type addition
   with pytest.raises(TypeError):
       x = Node(5)
       f = x - np.array([0, 4, 9])
       
       
def test_Reverse_mul_rmul():
   # test subtraction of two Nodes
   x = Node(5)
   y = Node(3)
   f = x * y
   assert f.val == 15, Exception(f"test_Reverse_mul_rmul has error in value with two Nodes")
   assert x.children == [(f,3)], Exception(f"test_Reverse_mul_rmul has error in first node's children")
   assert y.children == [(f,5)], Exception(f"test_Reverse_mul_rmul has error in second node's children")
   

   # test reverse multiplication of a Node and non-Node number
   x = 5
   y = Node(3)
   f = y*x
   assert f.val == 15, Exception(f"test_Reverse_mul_rmul has error in value with Node and non-node")
   assert y.children == [(f,5)], Exception(f"test_Reverse_mul_rmul has error in second node's children")


   # test multiplication of a Node and non-Node number
   x = 5
   y = Node(3)
   f = x*y
   assert f.val == 15, Exception(f"test_Reverse_mul_rmul has error in value with Node and non-node")
   assert y.children == [(f,5)], Exception(f"test_Reverse_mul_rmul has error in second node's children")


   # test invalid type multiplication
   with pytest.raises(TypeError):
       x = Node(5)
       f = x*np.array([0, 4, 9])
       
       
def test_Reverse_truediv_rtruediv():
   # test subtraction of two Nodes
   x = Node(6)
   y = Node(3)
   f = x/y
   assert f.val == 2, Exception(f"test_Reverse_truediv_rtruediv has error in value with two Nodes")
   assert x.children == [(f,1/3)], Exception(f"test_Reverse_truediv_rtruediv has error in first node's children")
   assert y.children == [(f,-6/9)], Exception(f"test_Reverse_truediv_rtruediv has error in second node's children")
   

   # test reverse division of a Node and non-Node number
   x = 6
   y = Node(3)
   f = y/x
   assert f.val == 0.5, Exception(f"test_Reverse_truediv_rtruediv has error in value with Node and non-node")
   assert y.children == [(f,1/6)], Exception(f"test_Reverse_truediv_rtruediv has error in second node's children")

   # test division of a Node and non-Node number
   x = 6
   y = Node(3)
   f = x/y
   assert f.val == 2, Exception(f"test_Reverse_truediv_rtruediv has error in value with Node and non-node")
   assert y.children == [(f,-6/9)], Exception(f"test_Reverse_truediv_rtruediv has error in second node's children")


   # test invalid type division
   with pytest.raises(TypeError):
       x = Node(5)
       f = x/np.array([0, 4, 9])
       
       
def test_Reverse_pow_rpow():
   # test power of two Nodes
   x = Node(2)
   y = Node(3)
   f = x**y
   assert f.val == 8, Exception(f"test_Reverse_pow_rpow has error in value with two Nodes")
   assert x.children == [(f,12)], Exception(f"test_Reverse_pow_rpow has error in first node's children")
   assert y.children == [(f,2**3*math.log(3))], Exception(f"test_Reverse_pow_rpow has error in second node's children")
   

   # test reverse power of a Node and non-Node number
   x = 2
   y = Node(3)
   f = y**x
   assert f.val == 9, Exception(f"test_Reverse_pow_rpow has error in value with Node and non-node")
   assert y.children == [(f,6)], Exception(f"test_Reverse_pow_rpow has error in second node's children")


   # test power of a Node and non-Node number
   x = 2
   y = Node(3)
   f = x**y
   assert f.val == 8, Exception(f"test_Reverse_pow_rpow has error in value with Node and non-node")
   assert y.children == [(f,2**3*np.log(2))], Exception(f"test_Reverse_pow_rpow has error in second node's children")


   # test invalid type addition
   with pytest.raises(TypeError):
       x = Node(5)
       f = x**np.array([0, 4, 9])
       
       
def test_Reverse_neg():
    # test negative for a Node number
    x = Node(2)
    f = -x
    assert f.val == -2, Exception(f"test_Reverse_neg has wrong value")


def test_Reverse_lt():
    # test between a Node number and a non-Node number
    x = 2
    y = Node(3)
    assert x < y.val, Exception(f"test_Reverse_lt has wrong value")
       
    # test between two Node numbers 
    x = Node(2)
    y = Node(3)
    assert x.val < y.val, Exception(f"test_Reverse_lt has wrong value")

def test_Reverse_gt():
    # test between a Node number and a non-Node number
    x = 5
    y = Node(3)
    assert x > y.val, Exception(f"test_Reverse_gt has wrong value")
       
    # test between two Node numbers 
    x = Node(5)
    y = Node(3)
    assert x.val > y.val, Exception(f"test_Reverse_gt has wrong value")   
       

def test_Reverse_ge():
    # test between a Node number and a non-Node number
    x = 5
    y = Node(5)
    assert x >= y.val, Exception(f"test_Reverse_ge has wrong value")
       
    # test between two Node numbers 
    x = Node(5)
    y = Node(5)
    assert x.val >= y.val, Exception(f"test_Reverse_ge has wrong value") 


def test_Reverse_eq():
    # test between two Node numbers
    x = Node(2)
    y = Node(2)
    assert x.val == y.val, Exception(f"test_Reverse_eq has wrong value")
    assert x.der == y.der, Exception(f"test_Reverse_eq has wrong derivative")
    assert x.children == y.children, Exception(f"test_Reverse_eq has wrong children")

def test_Reverse_ne():
    # test between two Node numbers
    x = Node(2)
    y = Node(3)
    assert x.val is not y.val, Exception(f"test_Reverse_ne has wrong value")
    
def test_Reverse_sin():
    # test sin with a Node 
    x = Node(2)
    f = sin(x)
    assert f.val == pytest.approx(math.sin(2), tolerance), Exception(f"test_Reverse_sin has error")
    assert x.children == pytest.approx([(f,math.cos(2))],tolerance), Exception(f"test_Reverse_sin has error")

def test_Reverse_cos():
    # test cos with a Node
    x = Node(2)
    f = cos(x)
    assert f.val == pytest.approx(math.cos(2), tolerance), Exception(f"test_Reverse_cos has error")
    assert x.children == pytest.approx([(f,-math.sin(2))],tolerance), Exception(f"test_Reverse_cos has error")


def test_Reverse_tan():
    # test tan with a Node number
    x = Node(2)
    f = tan(x)
    assert f.val == pytest.approx(math.tan(2), tolerance), Exception(f"test_Reverse_tan has error")
    assert x.children == pytest.approx([(f,1/(math.cos(2)**2))],tolerance), Exception(f"test_Reverse_tan has error")


def test_Reverse_arcsin():
    # test arcsin with a Node number
    x = Node(0.5)
    f = arcsin(x)
    assert f.val == pytest.approx(np.arcsin(0.5), tolerance), Exception(f"test_Reverse_arcsin has error")
    assert x.children == pytest.approx([(f, 1/(math.sqrt(0.75)))],tolerance), Exception(f"test_Reverse_arcsin has error in children")


def test_Reverse_arccos():
    # test arccos with a Node number
    x = Node(0.5)
    f = arccos(x)
    assert f.val == pytest.approx(np.arccos(0.5), tolerance), Exception(f"test_Reverse_arccos has error")
    assert x.children == pytest.approx([(f, -1/(math.sqrt(0.75)))],tolerance), Exception(f"test_Reverse_arccos has error in children")


def test_Reverse_arctan():
    # test arctan with a Node number
    x = Node(0.5)
    f = arctan(x)
    assert f.val == pytest.approx(np.arctan(0.5), tolerance), Exception(f"test_Reverse_arctan has error")
    assert x.children == pytest.approx([(f, 0.8)], tolerance), Exception(f"test_Reverse_arctan has error")



def test_Reverse_arctanh():
    # test arctanh with a Node number
    x = Node(0.5)
    f = arctanh(x)
    assert f.val == pytest.approx(np.arctanh(0.5), tolerance), Exception(f"test_Reverse_arctanh has error")
    assert x.children == pytest.approx([(f, 1/0.75)],tolerance), Exception(f"test_Reverse_arctanh has error")



def test_Reverse_arccosh():
    # test arccosh with a Node number
    x = Node(2)
    f = arccosh(x)
    assert f.val == pytest.approx(np.arccosh(2), tolerance), Exception(f"test_Reverse_arccosh has error")
    assert x.children == pytest.approx([(f, 1/np.sqrt(3))],tolerance), Exception(f"test_Reverse_arccosh has error")


def test_Reverse_arcsinh():
    # test arcsinh with a Node number
    x = Node(2)
    f = arcsinh(x)
    assert f.val == pytest.approx(np.arcsinh(2), tolerance), Exception(f"test_Reverse_arcsinh has error")
    assert x.children == pytest.approx([(f, 1/np.sqrt(5))], tolerance), Exception(f"test_Reverse_arcsinh has error")
