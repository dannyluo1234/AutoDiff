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

    Parameters
    ----------
    value : real number
            First argument, a value at which the function should be evaluated.
    direction : real number, optional
            Specifies a vector direction to calculate the gradient. The default
            number is 1

    Returns
    ----------
    Dual
        Returns a Dual class object with a value (val) and a derivative (der).

    Examples
    ----------
    >>> x = Dual(3)
    >>> y = Dual(4, 2)
    """
    def __init__(self, value, direction=1):
        """
        Intialize a Dual class object
        """

        if (isinstance(value, int) or isinstance(value, float)) and (isinstance(direction, int) or isinstance(direction, float)):
            self.val = value
            self.der = direction
        else:
            raise TypeError
        
    def __add__(self, other):
        """
        Add a Dual class object with a real number or another Dual class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the addition result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x + y
        >>> print(f) # Value:7, Derivative: 2
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val + other, self.der)
        elif isinstance(other, Dual):
            return Dual(self.val + other.val, self.der + other.der)
        else:
            raise TypeError
            
    def __radd__(self, other):
        """
        Add a real number or another Dual class object with a Dual class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the addition result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x + y
        >>> print(f) # Value:7, Derivative: 2
        """
        return self.__add__(other)
    
    def __mul__(self, other):
        """
        Multiply a Dual class object with a real number or another Dual class
        object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the multiplication result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x * y
        >>> print(f) # Value:12, Derivative: 7
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val * other, self.der * other)
        elif isinstance(other, Dual):
            return Dual(self.val * other.val, self.der * other.val + self.val * other.der)
        else:
            raise TypeError
    
    def __rmul__(self, other):
        """
        Multiply a real number or another Dual class object with a Dual class
        object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the multiplication result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x * y
        >>> print(f) # Value:12, Derivative: 7
        """
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """
        Divide a Dual class object by a real number or another Dual class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the division result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x / y
        >>> print(f) # Value:0.75, Derivative: 0.0625
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val / other, self.der / other)
        elif isinstance(other, Dual):
            return Dual(self.val / other.val, (self.der * other.val - self.val * other.der)/(other.val**2))
        else:
            raise TypeError        
    
    def __rtruediv__(self, other):
        """
        Divide a real number or another Dual class object by a Dual class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the division result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x / y
        >>> print(f) # Value:0.75, Derivative: 0.0625
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(other/self.val, -self.der * other /(self.val ** 2))
        else:
            raise TypeError      
            
    def __sub__(self, other):
        """
        Subtract a real number or another Dual class object from a Dual class
        object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the subtraction result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x / y
        >>> print(f) # Value:0.75, Derivative: 0.0625
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val - other, self.der)
        elif isinstance(other, Dual):
            return Dual(self.val - other.val, self.der - other.der)
        else:
            raise TypeError 
    
    def __rsub__(self, other):
        """
        Subtract a Dual class object from a real number or another Dual class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the subtraction result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x / y
        >>> print(f) # Value:0.75, Derivative: 0.0625
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(other-self.val, -self.der )
        else:
            raise TypeError     
            
    def __pow__(self, other):
        """
        Raise a Dual class object to the power of a real number or another Dual
        class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x ** y
        >>> print(f) # Value: 81, Derivative: 196.9875953821169
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(self.val ** other, other * self.val ** (other-1) * self.der)
        elif isinstance(other, Dual):
            return Dual(self.val ** other.val, self.val ** other.val * (other.der * math.log(self.val) + other.val / self.val * self.der))
        else:
            raise TypeError         
    
    def __rpow__(self, other):
        """
        Raise a Dual class object or a real number to the power of another Dual
        class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = x ** y
        >>> print(f) # Value: 81, Derivative: 196.9875953821169
        """
        if isinstance(other, float) or isinstance(other, int):
            return Dual(other ** self.val, other ** self.val * self.der * math.log(other) )
        else:
            raise TypeError

    def __neg__(self):
        """
        Negate a dual class object

        Returns
        ----------
        Dual
            Returns a Dual class object representating the negation result

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> f = -x
        >>> print(f) # Value: -3, Derivative: -1
        """
        return self.__mul__(-1)

    def __lt__(self, other):
        """
        Determine whether a Dual class is less than a real number or another
        Dual class

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> x < y # True
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val < other
        elif isinstance(other, Dual):
            return self.val < other.val
        else:
            raise TypeError

    def __gt__(self, other):
        """
        Determine whether a Dual class is greater than a real number or another
        Dual class

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> x > y # False
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val > other
        elif isinstance(other, Dual):
            return self.val > other.val
        else:
            raise TypeError

    def __le__(self, other):
        """
        Determine whether a Dual class is less than or equal to a real number or
        another Dual class

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> x <= y # True
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val <= other
        elif isinstance(other, Dual):
            return self.val <= other.val
        else:
            raise TypeError    

    def __ge__(self, other):
        """
        Determine whether a Dual class is greater than or equal to a real number
        or another Dual class

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> x >= y # False
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val >= other
        elif isinstance(other, Dual):
            return self.val >= other.val
        else:
            raise TypeError

    def __eq__(self, other):
        """
        Determine whether a Dual class has the same val and der to another Dual
        class object

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> x == y # False
        """
        if isinstance(other, Dual):
            return self.val == other.val and self.der == other.der
        else:
            return False

    def __ne__(self, other):
        """
        Determine whether a Dual class does not have the same val and der to
        another Dual class object

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> x != y # True
        """
        return not self.__eq__(other)

    def __str__(self):
        """
        Print out the value and derivative of a Dual class

        Returns
        ----------
        String

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> str(x)
        >>> Value: 3, Derivative: 1
        """
        return (f'Dual({self.val}, {self.der})')

    def __repr__(self):
        """
        Print out the value and derivative of a Dual class in the format of
        Dual(val, der)

        Returns
        ----------
        String

        Examples
        ----------
        >>> x = Dual(3)
        >>> y = Dual(4)
        >>> repr(x)
        >>> Dual(3, 1)
        """
        return (f'Dual({self.val}, {self.der})')



# To get the gradient, we need to set different seed for different coordinate and calculate the forward mode for n times where n is the dimension
# This is the 1D version that will be called
def AutoDiffF1D(f, val):
    """
    For a one-dimensional function, f, and a list of values at which to evaluate
    f, val, return the derivative(s) of the function in a list

    Parameters
    ----------
    f : a lambda function or a user-defined function
        First argument, the one-dimensional function to be evaluated
    val : a list of real number(s)
        Second argument, the value(s) at which the function should be evaluated

    Returns
    ----------
    List
        A list with the same size as val, representing the partial derivatives
        of each variable

    Examples
    ----------
    >>> AutoDiffF1D(lambda x, y : x + y ** 2, [3, 5])
    >>> [1, 10]
    >>> AutoDiffF1D(lambda x : x * 2, [3])
    >>> [6]
    """
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
    """
    For a multi-dimensional function set, f_list, and a list of list of values
    at which to evaluate the function set, val_list, return the derivative(s) of
    the function in a list

    Parameters
    ----------
    f_list : a list of lambda functions or user defined functions
             First argument, a list of functions to be evaluated. Size of
             val_list and f_list must match.
    val_list : a list of list of real number(s)
               Second argument, each list within the list represents a set of
               values at which to evaluate the corresponding function within the
               function set, f_list. Size of val_list and f_list must match.

    Returns
    ----------
    List
        A list of list with the same size as f_list and val_list, representing
        the partial derivatives of each variable in each function

    Examples
    ----------
    >>> AutoDiffF([lambda x: 2*x, lambda y: sin(y), lambda x, y: x+y],
                  [[2],[5],[2,5]])
    >>> [[2], [0.2836621854632263], [1, 1]]
    >>> def f(x, y, z):
            return x + y ** 2 / z
    >>> AutoDiffF([lambda x: cos(x), f], [[np.pi], [np.pi, 3, 5]])
    >>> [[-1.2246467991473532e-16], [1.0, 1.2, -0.36]]
    """
    if isinstance(f_list, list):
        results = []
        if len(f_list) != len(val_list):
            raise Exception("function list length doesn't match value list length")
        for f, val in zip(f_list, val_list):
            results.append(AutoDiffF1D(f, val))
        return results
    else:
        return AutoDiffF1D(f_list, val_list)
