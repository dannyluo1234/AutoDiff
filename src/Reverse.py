# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:04:57 2021

@author: Danny Luo
"""

import math

class Node:
    def __init__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.value = value
            # children will store tuples of form (a,b) where a is a child and b is  
            # this child's partial derivative
            self.children = []
            self.der = None
        else:
            raise TypeError
    
    def get_gradient(self):
        if self.der is not None:
            return self.der
        else:
            self.der = sum([child.get_gradient() * partial for child, partial in self.children])
            return self.der

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.value + other)
            self.children.append((new_node, 1))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.value + other.value)
            self.children.append((new_node, 1))
            other.children.append((new_node, 1))
            return new_node
        else:
            raise TypeError
            
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.value * other)
            self.children.append((new_node, other))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.value * other.value)
            self.children.append((new_node, other.value))
            other.children.append((new_node, self.value))
            return new_node
        else:
            raise TypeError
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.value / other)
            self.children.append((new_node, 1/other))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.value / other.value)
            self.children.append((new_node, 1 / other.value))
            other.children.append((new_node, - self.value / (other.value ** 2)))
            return new_node
        else:
            raise TypeError       

    def __rtruediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(other / self.value)
            self.children.append((new_node, - other / (self.value ** 2)))
            return new_node
        else:
            raise TypeError  

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.value - other)
            self.children.append((new_node, 1))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.value - other.value)
            self.children.append((new_node, 1))
            other.children.append((new_node, -1))
            return new_node
        else:
            raise TypeError
    
    def __rsub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(other - self.value)
            self.children.append((new_node, -1))
            return new_node
        else:
            raise TypeError  
            
    def __pow__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.value ** other)
            self.children.append((new_node, other * self.value ** (other-1)))
            return new_node        
        elif isinstance(other, Node):
            new_node = Node(self.value ** other.value)
            self.children.append((new_node, other.value * self.value ** (other.value-1)))
            other.children.append((new_node, self.value ** other.value * math.log(other.value)))
            return new_node       
        else:
            raise TypeError         
    
    def __rpow__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(other ** self.value)
            self.children.append((new_node, other ** self.value * math.log(other)))
            return new_node 
        else:
            raise TypeError
    
    def __neg__(self):
        return self.__mul__(-1)

    def __lt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.value < other
        elif isinstance(other, Node):
            return self.value < other.value
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.value > other
        elif isinstance(other, Node):
            return self.value > other.value
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.value <= other
        elif isinstance(other, Node):
            return self.value <= other.value
        else:
            raise TypeError    

    def __ge__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.value >= other
        elif isinstance(other, Node):
            return self.value >= other.value
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value and self.der == other.der and self.children == other.children
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)            
            

    # using reverse pass to calculate the gradient of specific variables
    def AutoDiffR(self, variables):
        self.der = 1
        result = []
        for var in variables:
            '''
            try:
                var_grad = var.get_gradient()
                result.append(var_grad)
            except:
                print("Variable Not specified")
                return
            '''
            var_grad = var.get_gradient()
            result.append(var_grad)
        return result
        

















