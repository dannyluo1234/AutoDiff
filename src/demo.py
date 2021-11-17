# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:22:24 2021
@author: Danny Luo
"""

from dual_temp import dual
import ad_operations as ad

# Single dimension input case, x=1
x = dual(1)
f1 = x + 2
# f2 = x + x
# print(f1.val, f1.der)
# print(dir(f1))
# print(f1.__name__)
f1.print_graph()
# f2.print_graph

# # Multiple dimension input case, x=1, y=2
# x = dual(1)
# y = dual(2)
# z = dual(-1)
# f2 = ad.sin(x*y) + x**y -2*x
# # f3 = z ** (0.5)
# print(f2.val, f2.der)
# # print(f3.val, f3.der)
# print(f1)

# # Calculate derivative in a specific direction (gradient dot product with the direction)
# # Same set up as above, but with direction (2, 3)
# x = dual(1,2)
# y = dual(2,3)
# f = ad.sin(x*y) + x**y -2*x
# print(f.val, f.der)

# # Calculating gradient, note that the sin function is the ones we define
# def f(x, y, z):
#     return ad.sin(x) + y**3 + x*z
# # print(get_gradient(f, 3, [1,3,2]))
