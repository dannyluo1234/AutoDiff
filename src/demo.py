# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:22:24 2021

@author: Danny Luo
"""

from dual_temp import *

# Single dimension input case, x=1
x = dual(1)
f = sin(x) + x + x**2
print(f.val, f.der)

# Multiple dimension input case, x=1, y=2
x = Dual(1)
y = Dual(2)
f = sin(x*y) + x**y -2*x
print(f.val, f.der)

# Calculate derivative in a specific direction (gradient dot product with the direction)
# Same set up as above, but with direction (2, 3)
x = Dual(1,2)
y = Dual(2,3)
f = sin(x*y) + x**y -2*x
print(f.val, f.der)

# Calculating gradient, note that the sin function is the ones we define
def f(x, y, z):
    return sin(x) + y**3 + x*z
print(get_gradient(f, 3, [1,3,2]))

