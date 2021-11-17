# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:14 2021
@author: Diana Feng
"""

from dual_temp import dual

# Multiple dimension input case, x=1, y=7
x = dual(1)
y = dual(7)
f1 = 2 * y + x * (y + y) * 3
f2 = 4 * (y + x) * x * (x + 3) + x * y
f1.print_graph()
f2.print_graph()
