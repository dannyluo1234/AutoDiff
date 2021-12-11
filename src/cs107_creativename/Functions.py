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
    >>> print(cos(y)) # -1.0
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
    >>> print(tan(x).val) # 0.0
    >>> print(tan(y).val) # 0.0
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
    >>> print(arcsin(x).val) # 0.0
    >>> print(arcsin(y).val) # 0.0
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
    >>> x = Dual(1)
    >>> y = Node(1)
    >>> print(arccos(x).val) # 0.0
    >>> print(arccos(y).val) # 0.0
    >>> print(arccos(1)) # 0.0
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
    >>> print(arctan(x).val) # 0.0
    >>> print(arctan(y).val) # 0.0
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
    >>> print(sinh(x).val) # 0.0
    >>> print(sinh(y).val) # 0.0
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
    >>> print(cosh(x).val) # 1.0
    >>> print(cosh(y).val) # 1.0
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
    >>> print(tanh(x).val) # 0.0
    >>> print(tanh(y).val) # 0.0
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
    >>> print(arcsinh(x).val) # 0.0
    >>> print(arcsinh(y).val) # 0.0
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
    >>> x = Dual(1)
    >>> y = Node(1)
    >>> print(arccosh(x).val) # 0.0
    >>> print(arccosh(y).val) # 0.0
    >>> print(arccosh(1)) # 0.0
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
    >>> print(arctanh(x).val) # 0.0
    >>> print(arctanh(y).val) # 0.0
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
    >>> print(exp(x).val) # 1.0
    >>> print(exp(y).val) # 1.0
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
    >>> print(exp(x).val) # 2.0
    >>> print(exp(y).val) # 2.0
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
            new_node = Node(math.log(other.val))
            other.children.append((new_node, 1 / other.val / math.log(base)))
            return new_node  
        except ValueError:
            raise ValueError("Attempting to take the square root of negative value.") from None
    else:
        raise TypeError

def logistic(other):
    if isinstance(other, float) or isinstance(other, int) or isinstance(other, Dual) or isinstance(other, Node):
        return 1 / (1 + exp(-other))
    else:
        raise TypeError
