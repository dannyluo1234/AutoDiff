# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:19:36 2021

@author: Danny Luo
"""

from .Forward import Dual as Dual
from .Reverse import Node as Node
import math
import numpy as np

def sin(other):
    """
    Calculate the sin of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(sin(x)) # Dual(0.0, 1.0)
    >>> print(sin(y)) # Node(1.0, None, [])
    >>> print(sin(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return math.sin(other)  
    elif isinstance(other, Dual):
        return Dual(math.sin(other.val), math.cos(other.val) * other.der)
    elif isinstance(other, Node):
        new_node = Node(math.sin(other.val))
        other.children.append((new_node, math.cos(other.val)))
        return new_node        
    else:
        raise TypeError  
def cos(other):
    """
    Calculate the cos of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(np.pi)
    >>> y = Node(np.pi)
    >>> print(cos(x)) # Dual(-1.0, -1.2246467991473532e-16)
    >>> print(cos(y)) # Node(-1.0, None, [])
    >>> print(cos(np.pi)) # -1.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return math.cos(other)  
    elif isinstance(other, Dual):
        return Dual(math.cos(other.val), -math.sin(other.val) * other.der)
    elif isinstance(other, Node):
        new_node = Node(math.cos(other.val))
        other.children.append((new_node, -math.sin(other.val)))
        return new_node  
    else:
        raise TypeError          
def tan(other):
    """
    Calculate the tan of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(tan(x)) # Dual(0.0, 1.0)
    >>> print(tan(y)) # Node(0.0, None, [])
    >>> print(tan(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return math.tan(other)  
    elif isinstance(other, Dual):
        return Dual(math.tan(other.val), 1 / (math.cos(other.val) ** 2) * other.der)
    elif isinstance(other, Node):
        new_node = Node(math.tan(other.val))
        other.children.append((new_node, 1 / (math.cos(other.val) ** 2)))
        return new_node  
    else:
        raise TypeError  
        
def arcsin(other):
    """
    Calculate the arcsin of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(arcsin(x)) # Dual(0.0, 1.0)
    >>> print(arcsin(y)) # Node(0.0, None, [])
    >>> print(arcsin(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.arcsin(other)  
    elif isinstance(other, Dual):
        return Dual(np.arcsin(other.val), (1 / (1-other.val**2)**0.5) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.arcsin(other.val))
        other.children.append((new_node, (1 / (1-other.val**2)**0.5)))
        return new_node      
    else:
        raise TypeError  
        
def arccos(other):
    """
    Calculate the arccos of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(arccos(x)) # Dual(1.5707963267948966, -1.0)
    >>> print(arccos(y)) # Node(1.5707963267948966, None, [])
    >>> print(arccos(0)) # 1.5707963267948966
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.arccos(other)  
    elif isinstance(other, Dual):
        return Dual(np.arccos(other.val), -(1 / (1-other.val**2)**0.5) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.arccos(other.val))
        other.children.append((new_node, -(1 / (1-other.val**2)**0.5)))
        return new_node  
    else:
        raise TypeError  
        
def arctan(other):
    """
    Calculate the arctan of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(arctan(x)) # Dual(0.0, 1.0)
    >>> print(arctan(y)) # Node(0.0, None, [])
    >>> print(arctan(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.arctan(other)  
    elif isinstance(other, Dual):
        return Dual(np.arctan(other.val), (1 / (1+other.val**2)) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.arctan(other.val))
        other.children.append((new_node, (1 / (1+other.val**2))))
        return new_node  
    else:
        raise TypeError  
        
def sinh(other):
    """
    Calculate the sinh of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(sinh(x)) # Dual(0.0, 1.0)
    >>> print(sinh(y)) # Node(0.0, None, [])
    >>> print(sinh(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.sinh(other)  
    elif isinstance(other, Dual):
        return Dual(np.sinh(other.val), np.cosh(other.val) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.sinh(other.val))
        other.children.append((new_node, np.cosh(other.val)))
        return new_node  
    else:
        raise TypeError
        
def cosh(other):
    """
    Calculate the cosh of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(cosh(x)) # Dual(1.0, 0.0)
    >>> print(cosh(y)) # Node(1.0, None, [])
    >>> print(cosh(0)) # 1.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.cosh(other)  
    elif isinstance(other, Dual):
        return Dual(np.cosh(other.val), np.sinh(other.val) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.cosh(other.val))
        other.children.append((new_node, np.sinh(other.val)))
        return new_node  
    else:
        raise TypeError
        
def tanh(other):
    """
    Calculate the tanh of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(tanh(x)) # Dual(0.0, 1.0)
    >>> print(tanh(y)) # Node(0.0, None, [])
    >>> print(tanh(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.tanh(other)  
    elif isinstance(other, Dual):
        return Dual(np.tanh(other.val), (1 / np.cosh(other.val)**2) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.tanh(other.val))
        other.children.append((new_node, (1 / np.cosh(other.val)**2)))
        return new_node  
    else:
        raise TypeError
    
def arcsinh(other):
    """
    Calculate the arcsinh of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(arcsinh(x)) # Dual(0.0, 1.0)
    >>> print(arcsinh(y)) # Node(0.0, None, [])
    >>> print(arcsinh(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.arcsinh(other)  
    elif isinstance(other, Dual):
        return Dual(np.arcsinh(other.val), (1 / (other.val**2 + 1)**0.5) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.arcsinh(other.val))
        other.children.append((new_node, (1 / (other.val**2 + 1)**0.5)))
        return new_node  
    else:
        raise TypeError
        
def arccosh(other):
    """
    Calculate the arccosh of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(2)
    >>> y = Node(2)
    >>> print(arccosh(x)) # Dual(1.3169578969248166, 0.5773502691896258)
    >>> print(arccosh(y)) # Node(1.3169578969248166, None, [])
    >>> print(arccosh(0.5)) # 1.3169578969248166
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.arccosh(other)  
    elif isinstance(other, Dual):
        return Dual(np.arccosh(other.val), (1 / (other.val**2 - 1)**0.5) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.arccosh(other.val))
        other.children.append((new_node, (1 / (other.val**2 - 1)**0.5)))
        return new_node  
    else:
        raise TypeError
    
def arctanh(other):
    """
    Calculate the arctanh of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(arctanh(x)) # Dual(0.0, 1.0)
    >>> print(arctanh(y)) # Node(0.0, None, [])
    >>> print(arctanh(0)) # 0.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return np.arctanh(other)  
    elif isinstance(other, Dual):
        return Dual(np.arctanh(other.val), (1 / (1-other.val**2)) * other.der)
    elif isinstance(other, Node):
        new_node = Node(np.arctanh(other.val))
        other.children.append((new_node, (1 / (1-other.val**2))))
        return new_node  
    else:
        raise TypeError
        
def exp(other):
    """
    Calculate the exponential of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(exp(x)) # Dual(1.0, 1.0)
    >>> print(exp(y)) # Node(1.0, None, [])
    >>> print(exp(0)) # 1.0
    """
    if isinstance(other, float) or isinstance(other, int):
        return math.exp(other)  
    elif isinstance(other, Dual):
        return Dual(math.exp(other.val), math.exp(other.val) * other.der)
    elif isinstance(other, Node):
        new_node = Node(math.exp(other.val))
        other.children.append((new_node, math.exp(other.val)))
        return new_node  
    else:
        raise TypeError
        
def sqrt(other):
    """
    Calculate the square root of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(4)
    >>> y = Node(4)
    >>> print(exp(x)) # Dual(2.0, 0.25)
    >>> print(exp(y)) # Node(2.0, None, [])
    >>> print(exp(4)) # 2.0
    """
    if isinstance(other, float) or isinstance(other, int):
        try:
            return math.sqrt(other)
        except ValueError:
            raise ValueError("Attempting to take the square root of negative value.") from None
    elif isinstance(other, Dual):
        try:
            return Dual(math.sqrt(other.val), 1/2 * other.val ** (-1/2) * other.der)
        except ValueError:
            raise ValueError("Attempting to take the square root of negative value.") from None
    elif isinstance(other, Node):
        try:
            new_node = Node(math.sqrt(other.val))
            other.children.append((new_node, 1/2 * other.val ** (-1/2)))
            return new_node  
        except ValueError:
            raise ValueError("Attempting to take the square root of negative value.") from None
    else:
        raise TypeError

def log(other, base):
    """
    Calculate the square root of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(8)
    >>> y = Node(8)
    >>> print(log(x, 2)) # Dual(3.0, 0.18033688011112042)
    >>> print(log(y, 2)) # Node(2.0794415416798357, None, [])
    >>> print(log(8, 2)) # 3.0
    """
    if not (isinstance(base, float) or isinstance(base, int)):
        raise TypeError
    if isinstance(other, float) or isinstance(other, int):
        try:
            return math.log(other,base)
        except ValueError:
            raise ValueError("Attempting to take log with negative value.") from None
    elif isinstance(other, Dual):
        try:
            return Dual(math.log(other.val,base), 1 / other.val / math.log(base) * other.der)
        except ValueError:
            raise ValueError("Attempting to take log with negative value.") from None
    elif isinstance(other, Node):
        try:
            new_node = Node(math.log(other.val, base))
            other.children.append((new_node, 1 / other.val / math.log(base)))
            return new_node  
        except ValueError:
            raise ValueError("Attempting to take the square root of negative value.") from None
    else:
        raise TypeError

def logistic(other):
    """
    Calculate the square root of a real number, Dual class, or Node class

    Returns
    ----------
    Real number, Dual class, or Node class
        Returns the output in the same type as the input

    Examples
    ----------
    >>> x = Dual(0)
    >>> y = Node(0)
    >>> print(logistic(x)) # Dual(0.5, 0.25)
    >>> print(logistic(y)) # Node(0.5, None, [])
    >>> print(0) # 0.5
    """
    if isinstance(other, float) or isinstance(other, int) or isinstance(other, Dual):
        return 1 / (1 + exp(-other))
    if isinstance(other, Node):
        new_node = Node(1 / (1 + math.exp(-other.val)))
        other.children.append((new_node, math.exp(-other.val)/((1+math.exp(-other.val))**2)))
        return new_node  
    else:
        raise TypeError
