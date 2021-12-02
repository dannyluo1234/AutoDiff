# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:22:24 2021

@author: Danny Luo
"""

from Forward import *
from Reverse import *
from Functions import *

# Single dimension input case, x=1
x = Dual(1)
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

# Calculating gradient using forward mode
print(AutoDiffF(f, [1,3,2]))

# Calculating gradient using reverse mode
print(AutoDiffR(f, [1,3,2]))

# Define a new function to illustrate multiple functions
def g(x, y, z):
    return logistic(x) + arctan(y*sin(x)) + x*tan(z)

# Calculating gradient using forward mode
print(AutoDiffF([f,g], [[1,3,2],[5,0,-2]]))

# Calculating gradient using reverse mode
print(AutoDiffR([f,g], [[1,3,2],[5,0,-2]]))    
