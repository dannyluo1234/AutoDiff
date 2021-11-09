# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:22:24 2021

@author: Danny Luo
"""

from dual_temp import *

# Single dimension imput case
x = dual(1)
f = sin(x) + x + x**2
print(f.val, f.der)

# Multiple dimension input case
x = dual(1)
y = dual(2)
f = sin(x*y) + x**y -2*x
print(f.val, f.der)

# Calculating gradient
def f(x, y, z):
    return sin(x) + y**3 + x*z
print(get_gradient(f, 3, [1,3,2]))
