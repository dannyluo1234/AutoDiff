# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:22:24 2021

@author: Danny Luo
"""

import dual

# Single dimension imput case
x = dual(1)
f = sin(x) + x + x**2
print(f.val, f.der)

# Multiple dimension input case
x = dual(1)
y = dual(2)
f = sin(x*y) + x**y -2*x
print(f.val, f.der)
