# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:47:39 2021

@author: Danny Luo
"""

import math

class dual():
    def __init__(self, value, derivative=1):
        self.val = value
        self.der = derivative
        
    def __add__(self, other):
        if isinstance(other, dual) :
            return dual(self.val + other.val, self.der + other.der)
        elif isinstance(other, float) or isinstance(other, int):
            return dual(self.val + other, self.der)
        else:
            raise TypeError
            
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return dual(self.val * other, self.der * other)
        elif isinstance(other, dual):
            return dual(self.val * other.val, self.der * other.val + self.val * other.der)
        else:
            raise TypeError
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return dual(self.val / other, self.der / other)        
        elif isinstance(other, dual):
            return dual(self.val / other.val, (self.der * other.val - self.val * other.der)/(other.val**2))
        else:
            raise TypeError        
    
    def __rtruediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return dual(other/self.val, -self.der * other /(self.val ** 2))     
        else:
            raise TypeError      
            
    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return dual(self.val - other, self.der)   
        elif isinstance(other, dual):
            return dual(self.val - other.val, self.der - other.der)
        else:
            raise TypeError 
    
    def __rsub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return dual(other-self.val, -self.der )     
        else:
            raise TypeError     
            
    def __pow__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return dual(self.val ** other, other * self.val ** (other-1) * self.der)   
        elif isinstance(other, dual):
            return dual(self.val ** other.val, self.val ** other.val * (other.der * math.log(self.val) + other.val / self.val * self.der))
        else:
            raise TypeError         
    
    def __rpow__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return dual(other ** self.val, self.der * math.log(other) )     
        
def sin(other):
    if isinstance(other, float) or isinstance(other, int):
        return math.sin(other)  
    elif isinstance(other, dual):
        return dual(math.sin(other.val), math.cos(other.val) * other.der)
    else:
        raise TypeError  

def cos(other):
    if isinstance(other, float) or isinstance(other, int):
        return math.cos(other)  
    elif isinstance(other, dual):
        return dual(math.cos(other.val), -math.sin(other.val) * other.der)
    else:
        raise TypeError          

def tan(other):
    if isinstance(other, float) or isinstance(other, int):
        return math.tan(other)  
    elif isinstance(other, dual):
        return dual(math.tan(other.val), 1 / (math.cos(other.val) ** 2) * other.der)
    else:
        raise TypeError  
        
def exp(other):
    if isinstance(other, float) or isinstance(other, int):
        return math.exp(other)  
    elif isinstance(other, dual):
        return dual(math.exp(other.val), math.exp(other.val) * other.der)
    else:
        raise TypeError             
        
def get_gradient(f,dimension,value):
    gradient = []
    for i in range(dimension):
        dual_list = []
        for j in range(dimension):
            if i == j:
                dual_list.append(dual(value[j], 1))
            else:
                dual_list.append(dual(value[j], 0))
        function = f(*dual_list)
        gradient.append(function.der)
    return gradient
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        