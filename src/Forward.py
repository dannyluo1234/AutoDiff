# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:47:39 2021
@author: Danny Luo
"""

import math
from inspect import signature

class Dual():
    """
    A dual class that keeps track of the value and derivative of a function for
    automatic differentiation. It should be initiated by calling the class
    followed by a real number. A direction can also be specified as a second
    argument in order to differentiate towards a specific vector direction.
    For instance,
        x = Dual(3)
        y = Dual(4, 2)
    Parameters
    ----------
    value : real number
            First argument
    direction : real number, optional
            Specifies a vector direction to calculate the gradient. The default
            number is 1
    """
    def __init__(self, value, direction=1):
        if (isinstance(value, int) or isinstance(value, float)) and (isinstance(direction, int) or isinstance(direction, float)):
            self.val = value
            self.der = direction
        else:
            raise TypeError
        
    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val + other, self.der)
        elif isinstance(other, Dual):
            return Dual(self.val + other.val, self.der + other.der)
        else:
            raise TypeError
            
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val * other, self.der * other)
        elif isinstance(other, Dual):
            return Dual(self.val * other.val, self.der * other.val + self.val * other.der)
        else:
            raise TypeError
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val / other, self.der / other)
        elif isinstance(other, Dual):
            return Dual(self.val / other.val, (self.der * other.val - self.val * other.der)/(other.val**2))
        else:
            raise TypeError        
    
    def __rtruediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(other/self.val, -self.der * other /(self.val ** 2))
        else:
            raise TypeError      
            
    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val - other, self.der)
        elif isinstance(other, Dual):
            return Dual(self.val - other.val, self.der - other.der)
        else:
            raise TypeError 
    
    def __rsub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(other-self.val, -self.der )
        else:
            raise TypeError     
            
    def __pow__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val ** other, other * self.val ** (other-1) * self.der)
        elif isinstance(other, Dual):
            return Dual(self.val ** other.val, self.val ** other.val * (other.der * math.log(self.val) + other.val / self.val * self.der))
        else:
            raise TypeError         
    
    def __rpow__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Dual(other ** self.val, other ** self.val * self.der * math.log(other) )
        else:
            raise TypeError

    def __neg__(self):
        return self.__mul__(-1)

    def __lt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.val < other
        elif isinstance(other, Dual):
            return self.val < other.val
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.val > other
        elif isinstance(other, Dual):
            return self.val > other.val
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.val <= other
        elif isinstance(other, Dual):
            return self.val <= other.val
        else:
            raise TypeError    

    def __ge__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.val >= other
        elif isinstance(other, Dual):
            return self.val >= other.val
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Dual):
            return self.val == other.val and self.der == other.der
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)



# To get the gradient, we need to set different seed for different coordinate and calculate the forward mode for n times where n is the dimension
# This is the 1D version that will be called
def AutoDiffF1D(f, val):
    try:
        dimension = len(signature(f).parameters)
    except:
        raise TypeError("the first argument must be a function")

    if dimension != len(val):
        raise Exception("provided value doesn't match the input dimension of f")
        
    gradient = []
    # For loop over dimension, each calculating one coordinate of the gradient
    for i in range(dimension):
        # Initialize the Dual numbers with the specific seed, the seed should have 1 at the current dimension and 0 in other dimension.
        dual_list = []
        # Loop over all the variables to initialize it
        for j in range(dimension):
            # This is the only variable that has 1 as the self.der
            if i == j:
                dual_list.append(Dual(val[j], 1))
            # All other dual variables should have 0 as the self.der as specified by the seed
            else:
                dual_list.append(Dual(val[j], 0))
        # Perform Forward Mode
        function = f(*dual_list)
        # Attach this coordinate to the final result
        gradient.append(function.der)
    return gradient

# General Case, f_list could be a list of functions
def AutoDiffF(f_list, val_list):
    if isinstance(f_list, list):
        results = []
        if len(f_list) != len(val_list):
            raise Exception("function list length doesn't match value list length")
        for f, val in zip(f_list, val_list):
            results.append(AutoDiffF1D(f, val))
        return results
    else:
        return AutoDiffF1D(f_list, val_list)