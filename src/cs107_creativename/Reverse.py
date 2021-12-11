# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:04:57 2021

@author: Danny Luo
"""

import math
from inspect import signature

class Node():
    """
    A Node class that keeps track of the current value and derivative of a
    variable in a function or function set, as well as the pointers to all of
    the Nodes that depend on it (i.e. its "children").
    It should be initiated by calling the class followed by a real number.

    Parameters
    ----------
    val : real number
          The current value of the Node. Has to be defined at instantiation.
    der : real number
          The current derivative of the Node
    children : a list of tuples, each tuple representing a child
               The first value in the tuple is a pointer to the child node, and
               the second value in the pointer is its current partial derivative

    Returns
    ----------
    Node
        Returns a Node class object

    Examples
    ----------
    >>> x = Node(3)
    """
    def __init__(self, val):
        """
        Intialize a Node class object with an empty list of children and
        no derivative value.
        """
        if isinstance(val, int) or isinstance(val, float):
            self.val = val
            # children will store tuples of form (a,b) where a is a child and b is  
            # this child's partial derivative
            self.children = []
            self.der = None
        else:
            raise TypeError
    
    def get_gradient(self):
        """
        Returns the current derivative of a node. If the dertivative is None,
        update the derivative to a sum of all of its children's partial
        derivatives and return that value.
        """
        if self.der is not None:
            return self.der
        else:
            self.der = sum([child.get_gradient() * partial for child, partial in self.children])
            return self.der

    def __add__(self, other):
        """
        Add a Node class object with a real number or another Node class object
        by creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x + y
        >>> x.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, 1)]
        >>> x.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.val + other)
            self.children.append((new_node, 1))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.val + other.val)
            self.children.append((new_node, 1))
            other.children.append((new_node, 1))
            return new_node
        else:
            raise TypeError
            
    def __radd__(self, other):
        """
        Add a real number or another Node class object with a Node class object
        by creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x + y
        >>> y.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, 1)]
        >>> y.children[0][0] == f # True
        """
        return self.__add__(other)
    
    def __mul__(self, other):
        """
        Mutiply a Node class object with a real number or another Node class
        object by creating a new Node and appending it to the original Node's
        children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x * y
        >>> x.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, 4)]
        >>> x.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.val * other)
            self.children.append((new_node, other))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.val * other.val)
            self.children.append((new_node, other.val))
            other.children.append((new_node, self.val))
            return new_node
        else:
            raise TypeError
    
    def __rmul__(self, other):
        """
        Mutiply a real number or another Node class by a Node class object by
        creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x * y
        >>> y.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, 3)]
        >>> y.children[0][0] == f # True
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Divide a Node class object by a real number or another Node class by
        creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x / y
        >>> x.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, 0.25)]
        >>> x.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.val / other)
            self.children.append((new_node, 1/other))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.val / other.val)
            self.children.append((new_node, 1 / other.val))
            other.children.append((new_node, - self.val / (other.val ** 2)))
            return new_node
        else:
            raise TypeError       

    def __rtruediv__(self, other):
        """
        Divide a real number or another Node class by a Node class object by
        creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x / y
        >>> y.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>,
            -0.1875)]
        >>> y.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(other / self.val)
            self.children.append((new_node, - other / (self.val ** 2)))
            return new_node
        else:
            raise TypeError  

    def __sub__(self, other):
        """
        Subtract a Node class object by a real number or another Node class by
        creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x - y
        >>> x.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, 1)]
        >>> x.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.val - other)
            self.children.append((new_node, 1))
            return new_node
        elif isinstance(other, Node):
            new_node = Node(self.val - other.val)
            self.children.append((new_node, 1))
            other.children.append((new_node, -1))
            return new_node
        else:
            raise TypeError
    
    def __rsub__(self, other):
        """
        Subtract a real number or another Node class by a Node class object by
        creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x - y
        >>> y.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, -1)]
        >>> y.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(other - self.val)
            self.children.append((new_node, -1))
            return new_node
        else:
            raise TypeError  
            
    def __pow__(self, other):
        """
        Raise a Node class object by a real number or another Node class by
        creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x ** y
        >>> x.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, 108)]
        >>> x.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(self.val ** other)
            self.children.append((new_node, other * self.val ** (other-1)))
            return new_node        
        elif isinstance(other, Node):
            new_node = Node(self.val ** other.val)
            self.children.append((new_node, other.val * self.val ** (other.val-1)))
            other.children.append((new_node, self.val ** other.val * math.log(self.val)))
            return new_node       
        else:
            raise TypeError         
    
    def __rpow__(self, other):
        """
        Raise a real number or another Node class by a Node class object by
        creating a new Node and appending it to the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x ** y
        >>> y.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>,
            112.28984325071113)]
        >>> y.children[0][0] == f # True
        """
        if isinstance(other, float) or isinstance(other, int):
            new_node = Node(other ** self.val)
            self.children.append((new_node, other ** self.val * math.log(other)))
            return new_node 
        else:
            raise TypeError
    
    def __neg__(self):
        """
        Negate a Node class object by multiplying the Node by -1, thus creating
        a new Node and updating the original Node's children

        Returns
        ----------
        Node
            Returns a Node class object representating the new Node

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = -x
        >>> x.children
        >>> [(<cs107_creativename.Reverse.Node object at 0x7fab33718670>, -1)]
        >>> x.children[0][0] == f # True
        """
        return self.__mul__(-1)

    def __lt__(self, other):
        """
        Determine whether a Node class is less than a real number or another
        Node class by compare their values

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> x < y # True
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val < other
        elif isinstance(other, Node):
            return self.val < other.val
        else:
            raise TypeError

    def __gt__(self, other):
        """
        Determine whether a Node class is greater than a real number or another
        Node class by compare their values

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> x > y # False
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val > other
        elif isinstance(other, Node):
            return self.val > other.val
        else:
            raise TypeError

    def __le__(self, other):
        """
        Determine whether a Node class is less than or equal to a real number or
        another Node class by compare their values

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> x <= y # True
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val <= other
        elif isinstance(other, Node):
            return self.val <= other.val
        else:
            raise TypeError    

    def __ge__(self, other):
        """
        Determine whether a Node class is greater than or equal to a real number
        or another Node class by compare their values

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> x >= y # False
        """
        if isinstance(other, float) or isinstance(other, int):
            return self.val >= other
        elif isinstance(other, Node):
            return self.val >= other.val
        else:
            raise TypeError

    def __eq__(self, other):
        """
        Determine whether a Node class is equal to a real number or another Node
        class by compare their value, derivative, and children

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> x == y # False
        """
        if isinstance(other, Node):
            return self.val == other.val and self.der == other.der and self.children == other.children
        else:
            return False

    def __ne__(self, other):
        """
        Determine whether a Node class is equal to a real number or another Node
        class by compare their value, derivative, and children

        Returns
        ----------
        bool

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> x != y # True
        """
        return not self.__eq__(other)

    def __repr__(self):
        """
        Print out the value, derivative, and a list of children recursively for
        a Node class object in a simplified form

        Returns
        ----------
        String

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x ** y
        >>> g = x + 7
        >>> repr(x)
        >>> 'Node(3, None, [(Node(81, None, []), 108), (Node(10, None, []), 1)])'
        """
        return(f'Node({self.val}, {self.der}, {self.children})')

    def __str__(self):
        """
        Print out the value, derivative, and a list of children recursively for
        a Node class object

        Returns
        ----------
        String

        Examples
        ----------
        >>> x = Node(3)
        >>> y = Node(4)
        >>> f = x ** y
        >>> g = x + 7
        >>> str(x)
        >>> 'Node(3, None, [(Node(81, None, []), 108), (Node(10, None, []), 1)])'
        """
        return self.__repr__


    # using reverse pass to calculate the gradient of specific variables
    def _AutoDiffR(self, variables):
        """
        Calculate the result gradient in reverse mode AD

        Returns
        ----------
        List
            A list of gradient, each element representing the gradient for one
            variable
        """
        self.der = 1
        result = []
        for var in variables:
            var_grad = var.get_gradient()
            result.append(var_grad)
        return result

# One dimensional case wher f: R^n to R
def AutoDiffR1D(f, val):
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
    >>> AutoDiffR1D(lambda x, y : x + y ** 2, [3, 5])
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
    
    variables = [Node(val[i]) for i in range(dimension)]
    result = f(*variables)        
    return result._AutoDiffR(variables)

# General Case, f_list could be a list of functions
def AutoDiffR(f_list, val_list):
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
            results.append(AutoDiffR1D(f, val))
        return results
    else:
        return AutoDiffR1D(f_list, val_list)
