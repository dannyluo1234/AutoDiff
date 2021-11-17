# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:14 2021
@author: Diana Feng
"""

import math
import numpy as np

class dual():
    def __init__(self, value, direction=1, graph=""):
        if (isinstance(value, int) or isinstance(value, float)) and (isinstance(direction, int) or isinstance(direction, float)):
            self.val = value
            self.der = direction
            self.graph = graph
        else:
            raise TypeError
        
    def __add__(self, other):
        if isinstance(other, dual):
            out = other.graph + self.graph + " Add (" + f'dual({self.val}, {self.der}), ' + f'dual({other.val}, {other.der})) ->'
            return dual(self.val + other.val, self.der + other.der, graph=out)
        elif isinstance(other, float) or isinstance(other, int):
            out = self.graph + " Add (" + f'dual({self.val}, {self.der}), ' + str(other) + ") ->"
            return dual(self.val + other, self.der, graph=out)
        else:
            raise TypeError
            
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, dual):
            out = other.graph + self.graph + " Multiply (" + f'dual({self.val}, {self.der}), ' + f'dual({other.val}, {other.der})) ->'
            return dual(self.val * other.val, self.der * other.val + self.val * other.der, graph=out)
        elif isinstance(other, float) or isinstance(other, int):
            out = self.graph + " Multiply (" + f'dual({self.val}, {self.der}), ' + str(other) + ") ->"
            return dual(self.val * other, self.der * other, graph=out)
        else:
            raise TypeError
    
    def __rmul__(self, other):
        return self.__mul__(other)
    

    def print_graph(self):
        self.graph = self.graph + f' dual({self.val}, {self.der})'
        print(self.graph)
        # pass


