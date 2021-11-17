# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:47:39 2021
@author: Danny Luo
"""

import math
import numpy as np

class dual():
    def __init__(self, value, direction=1, graph=""):
        if (isinstance(value, int) or isinstance(value, float)) and (isinstance(direction, int) or isinstance(direction, float)):
            self.val = value
            self.der = direction
            self.graph = graph
            # print(self.val, self.der)
            # print(self.graph)
        else:
            raise TypeError
        
    def __add__(self, other):
        if isinstance(other, dual) :
            self.graph = self.graph + "Add (" + str(self)
            return dual(self.val + other.val, self.der + other.der, graph=self.graph)
        elif isinstance(other, float) or isinstance(other, int):
            self.graph = self.graph + "Add (" + str(other) + str(self)
            return dual(self.val + other, self.der, graph=self.graph)
        else:
            raise TypeError
            
    def __radd__(self, other):
        print("radd")
        return self.__add__(other)
    
    # def __mul__(self, other):
    #     if isinstance(other, float) or isinstance(other, int):
    #         self.graph = self.graph + "Multiply ( "
    #         # print(self.graph)
    #         return dual(self.val * other, self.der * other, graph=self.graph + "Multiply ( ")
    #     elif isinstance(other, dual):
    #         other.graph = other.graph + "Multiply ( "
    #         # print(other.graph)
    #         return dual(self.val * other.val, self.der * other.val + self.val * other.der, graph=other.graph + "Multiply ( ")
    #     else:
    #         raise TypeError
    
    # def __rmul__(self, other):
    #     print("rmul")
    #     return self.__mul__(other)
    

    def print_graph(self):
        print(self.graph)


